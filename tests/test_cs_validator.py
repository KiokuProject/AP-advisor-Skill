from __future__ import annotations

import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


def load(course):
    path = ROOT / f"ap-{course}-advisor" / "scripts" / "validate_topic_code.py"
    spec = importlib.util.spec_from_file_location(f"{course}_validator", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ComputerScienceValidatorTests(unittest.TestCase):
    def test_complete_current_catalogs_and_self_checks(self):
        for course, topics, practices in (("csa", 53, 12), ("csp", 35, 20)):
            with self.subTest(course=course):
                module = load(course)
                data = module.load_boundaries()
                result = module.self_check(data)
                self.assertEqual(result["overall_status"], "pass")
                self.assertEqual(result["topic_count"], topics)
                self.assertEqual(result["practice_count"], practices)

    def test_legacy_and_cross_course_citations_are_not_silently_remapped(self):
        for course, citation in (
            ("csa", "Unit 8, Topic 8.1 — 2D Arrays"),
            ("csa", "Unit 1, Topic 1.1 — Why Programming? Why Java?"),
            ("csp", "Unit 3, Topic 3.10 — Lists"),
            ("csp", "Big Idea 3, Topic 3.10 — ArrayList Methods"),
        ):
            with self.subTest(course=course, citation=citation):
                module = load(course)
                code, _ = module.validate_request(module.load_boundaries(), [citation])
                self.assertEqual(code, 1)

    def test_exclusions_do_not_erase_positive_scope(self):
        for course, topic, flag in (
            ("csa", "4.16", "write-recursive-code"),
            ("csa", "4.6", "mixed-scanner-modes"),
            ("csa", "1.12", "inheritance-implementation"),
            ("csp", "3.11", "binary-search-implementation"),
            ("csp", "3.17", "formal-big-o"),
            ("csp", "3.18", "prove-undecidability"),
        ):
            with self.subTest(course=course, flag=flag):
                module = load(course)
                data = module.load_boundaries()
                query = [module.citation(data, topic)]
                self.assertEqual(module.validate_request(data, query, assessed_topic=True)[0], 0)
                self.assertEqual(module.validate_request(data, query, scope_flags=[flag])[0], 0)
                self.assertEqual(module.validate_request(data, query, scope_flags=[flag], assessed_topic=True)[0], 1)

    def test_task_claims_require_the_right_practice_and_content(self):
        csa = load("csa")
        a = csa.load_boundaries()
        arraylist = [csa.citation(a, "4.8")]
        self.assertEqual(csa.validate_request(a, arraylist, practices=["2.B"], exam_task="frq-data")[0], 0)
        self.assertEqual(csa.validate_request(a, arraylist, practices=["3.B"], exam_task="frq-data")[0], 1)
        self.assertEqual(csa.validate_request(a, [csa.citation(a, "4.3")], practices=["2.B"], exam_task="frq-data")[0], 1)
        self.assertEqual(csa.validate_request(a, [csa.citation(a, "4.1")], practices=["5.A"], exam_task="mcq")[0], 0)
        csp = load("csp")
        p = csp.load_boundaries()
        ethics = [csp.citation(p, "5.5")]
        self.assertEqual(csp.validate_request(p, ethics, practices=["6.C"], exam_task="mcq-single")[0], 1)
        self.assertEqual(csp.validate_request(p, ethics, practices=["5.E"], exam_task="mcq-single")[0], 0)
        self.assertEqual(csp.validate_request(p, ethics, practices=["4.A"], exam_task="written-response")[0], 1)
        self.assertEqual(csp.validate_request(p, ethics, practices=["5.E"], exam_task="explore")[0], 1)

    def test_practice_only_and_unknown_flags_cannot_certify_scope(self):
        for course in ("csa", "csp"):
            module = load(course)
            data = module.load_boundaries()
            code, result = module.validate_request(data, practices=["1.A"], practice_only=True)
            self.assertEqual(code, 0)
            self.assertEqual(result["topic_status"], "not-established")
            for claim in ({"assessed_topic": True}, {"exam_task": "mcq"}, {"scope_flags": ["unknown"]}):
                self.assertEqual(module.validate_request(data, practices=["1.A"], practice_only=True, **claim)[0], 2)
            query = [module.citation(data, "1.1")]
            self.assertEqual(module.validate_request(data, query, scope_flags=["unknown"])[0], 1)

    def test_malformed_boundary_data_is_rejected(self):
        for course in ("csa", "csp"):
            module = load(course)
            original = module.load_boundaries()
            with tempfile.TemporaryDirectory(prefix="ap-cs-boundary-") as tmp:
                path = Path(tmp) / "boundary.json"
                for mutate in (
                    lambda d: d.update(course="other"),
                    lambda d: d["topics"].update({"99.1": "Bad group"}),
                    lambda d: d["exam_tasks"].update({"bad": {"source": "missing"}}),
                    lambda d: d["scope_flags"].update({"bad": {"source": "ced", "reason": "Bad", "topics": ["99.1"]}}),
                ):
                    data = json.loads(json.dumps(original))
                    mutate(data)
                    path.write_text(json.dumps(data), encoding="utf-8")
                    with self.assertRaises(ValueError):
                        module.load_boundaries(path)
                path.write_text('{"schema_version":1,"schema_version":1}', encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "duplicate JSON key"):
                    module.load_boundaries(path)

    def test_each_package_runs_alone_and_emits_machine_errors(self):
        for course in ("csa", "csp"):
            with self.subTest(course=course), tempfile.TemporaryDirectory(prefix="ap-cs-standalone-") as tmp:
                name = f"ap-{course}-advisor"
                package = Path(tmp) / name
                shutil.copytree(ROOT / name, package)
                script = package / "scripts" / "validate_topic_code.py"
                import sys
                env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONUTF8="1")
                for args, expected, status in (
                    (["--self-check"], 0, "pass"),
                    (["--unknown-option"], 2, "error"),
                    (["--self-check", "invalid citation"], 2, "error"),
                ):
                    result = subprocess.run([sys.executable, "-B", str(script), *args, "--evidence-json"],
                        cwd=tmp, env=env, capture_output=True, text=True, encoding="utf-8", timeout=20)
                    self.assertEqual(result.returncode, expected, result.stderr)
                    self.assertEqual(json.loads(result.stdout)["overall_status"], status)
                    self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
