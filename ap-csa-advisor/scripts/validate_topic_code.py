#!/usr/bin/env python3
"""Validate the installed CS Skill's declared Topic, Practice, and task scope."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
import unicodedata


ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT.name.removeprefix("ap-").removesuffix("-advisor")
BOUNDARIES = ROOT / "references" / f"ap-{COURSE}-boundaries.json"


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_boundaries(path=BOUNDARIES):
    data = json.loads(Path(path).read_text(encoding="utf-8"), object_pairs_hook=_unique_object)
    if not isinstance(data, dict) or data.get("schema_version") != 1 or data.get("course") != COURSE:
        raise ValueError("boundary version/course mismatch")
    expected_label = {"csa": "Unit", "csp": "Big Idea"}[COURSE]
    if data.get("group_label") != expected_label:
        raise ValueError("wrong course grouping label")
    for field in ("groups", "topics", "practices", "exam_tasks", "scope_flags"):
        if not isinstance(data.get(field), dict) or not data[field]:
            raise ValueError(f"{field} must be a nonempty object")
    for field in ("groups", "topics", "practices"):
        if any(not isinstance(v, str) or not v.strip() for v in data[field].values()):
            raise ValueError(f"invalid {field} label")
    for code in data["topics"]:
        if not re.fullmatch(r"[1-9]\d*\.[1-9]\d*", code) or code.split(".")[0] not in data["groups"]:
            raise ValueError(f"invalid Topic grouping: {code}")
    if any(not re.fullmatch(r"[1-6]\.[A-Z]", p) for p in data["practices"]):
        raise ValueError("invalid Practice code")
    sources = data.get("sources")
    if not isinstance(sources, list) or not sources or any(
        not isinstance(s, dict) or not isinstance(s.get("id"), str)
        or not isinstance(s.get("url"), str) or not s["url"].startswith("https://")
        for s in sources
    ):
        raise ValueError("invalid source records")
    source_ids = {s["id"] for s in sources}
    if len(source_ids) != len(sources):
        raise ValueError("duplicate source id")
    for name, task in data["exam_tasks"].items():
        if not isinstance(task, dict) or task.get("source") not in source_ids:
            raise ValueError(f"invalid task source: {name}")
        allowed, prefixes = task.get("allowed_practices"), task.get("required_topic_prefixes")
        if not isinstance(allowed, list) or not allowed or any(p not in data["practices"] for p in allowed):
            raise ValueError(f"invalid task Practices: {name}")
        if not isinstance(prefixes, list) or any(
            not isinstance(prefix, str) or not any(_topic_matches(code, prefix) for code in data["topics"])
            for prefix in prefixes
        ):
            raise ValueError(f"invalid task Topics: {name}")
    for name, flag in data["scope_flags"].items():
        if not isinstance(flag, dict) or flag.get("source") not in source_ids:
            raise ValueError(f"invalid exclusion source: {name}")
        if not isinstance(flag.get("reason"), str) or not flag["reason"].strip():
            raise ValueError(f"missing exclusion reason: {name}")
        codes = flag.get("topics")
        if not isinstance(codes, list) or not codes or any(c not in data["topics"] for c in codes):
            raise ValueError(f"invalid exclusion Topics: {name}")
    return data


def _topic_matches(code, prefix):
    return code.startswith(prefix) if prefix.endswith(".") else code == prefix


def citation(data, code):
    return f"{data['group_label']} {code.split('.')[0]}, Topic {code} — {data['topics'][code]}"


def validate_request(data, citations=(), *, practices=(), exam_task=None,
                     scope_flags=(), assessed_topic=False, practice_only=False):
    citations, practices, scope_flags = list(citations), list(practices), list(scope_flags)
    payload = {"schema_version": 1, "validator": f"ap-{COURSE}-topic-v1",
               "course": COURSE, "overall_status": "pass", "results": [], "failures": [],
               "validation_limit": data["validation_limit"]}
    if practice_only and (citations or assessed_topic or scope_flags or exam_task):
        payload.update(overall_status="error", error="--practice-only accepts only Practices, not Topic/task/scope claims")
        return 2, payload
    if (practice_only and not practices) or (not practice_only and not citations):
        payload.update(overall_status="error", error="supply a full Topic citation, or --practice-only with --practice")
        return 2, payload
    normalize = lambda s: unicodedata.normalize("NFKC", s)
    by_citation = {normalize(citation(data, code)): code for code in data["topics"]}
    matched = set()
    for query in citations:
        code = by_citation.get(normalize(query))
        payload["results"].append({"input": query, "status": "pass" if code else "fail", "topic_code": code})
        if code:
            matched.add(code)
        else:
            payload["failures"].append(f"no exact current-framework citation: {query}")
    for practice in practices:
        if practice not in data["practices"]:
            payload["failures"].append(f"unknown Practice: {practice}")
    if exam_task is not None:
        task = data["exam_tasks"].get(exam_task)
        if task is None:
            payload["failures"].append(f"unknown exam task: {exam_task}")
        else:
            if not practices:
                payload["failures"].append("an exam task needs at least one Practice")
            if any(p not in task["allowed_practices"] for p in practices):
                payload["failures"].append(f"Practice is not assessed by task: {exam_task}")
            prefixes = task["required_topic_prefixes"]
            if prefixes and not any(_topic_matches(code, prefix) for code in matched for prefix in prefixes):
                payload["failures"].append(f"task needs a relevant content Topic: {exam_task}")
    for name in scope_flags:
        flag = data["scope_flags"].get(name)
        if flag is None:
            payload["failures"].append(f"unknown scope flag: {name}")
        else:
            if matched.isdisjoint(flag["topics"]):
                payload["failures"].append(f"scope flag does not apply to the mapped Topics: {name}")
            if assessed_topic or exam_task:
                payload["failures"].append(flag["reason"])
    payload["claim"] = "practice-only" if practice_only else "exam-oriented" if exam_task else "assessed-topic" if assessed_topic else "instructional"
    payload["topic_status"] = "not-established" if practice_only else "validated" if matched and not payload["failures"] else "not-validated"
    payload["practices"], payload["exam_task"], payload["scope_flags"] = practices, exam_task, scope_flags
    if payload["failures"]:
        payload["overall_status"] = "fail"
    return (1 if payload["failures"] else 0), payload


def self_check(data):
    checks = 0

    def expect(expected, *args, **kwargs):
        nonlocal checks
        code, result = validate_request(data, *args, **kwargs)
        checks += 1
        if code != expected:
            raise ValueError(f"self-check expected exit {expected}, got {code}: {result}")

    for code in data["topics"]:
        expect(0, [citation(data, code)], assessed_topic=True)
    for practice in data["practices"]:
        expect(0, practices=[practice], practice_only=True)
    for name, flag in data["scope_flags"].items():
        queries = [citation(data, flag["topics"][0])]
        expect(0, queries, scope_flags=[name])
        expect(1, queries, scope_flags=[name], assessed_topic=True)
    for name, task in data["exam_tasks"].items():
        prefixes = task["required_topic_prefixes"]
        code = next(c for c in data["topics"] if not prefixes or any(_topic_matches(c, p) for p in prefixes))
        expect(0, [citation(data, code)], practices=[task["allowed_practices"][0]], exam_task=name)
        expect(1, [citation(data, code)], exam_task=name)
    first = citation(data, next(iter(data["topics"])))
    expect(1, [first + " (old title)"])
    expect(1, [first], practices=["9.Z"])
    expect(1, [first], exam_task="unknown")
    expect(1, [first], scope_flags=["unknown"])
    expect(2)
    expect(2, practice_only=True)
    expect(2, [first], practices=["1.A"], practice_only=True)
    return {"schema_version": 1, "validator": f"ap-{COURSE}-topic-v1", "course": COURSE,
            "overall_status": "pass", "check_count": checks, "topic_count": len(data["topics"]),
            "practice_count": len(data["practices"])}


class Parser(argparse.ArgumentParser):
    def error(self, message):
        raise ValueError(message)


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    parser = Parser(description=__doc__)
    parser.add_argument("citations", nargs="*")
    parser.add_argument("--practice", action="append", default=[])
    parser.add_argument("--exam-task")
    parser.add_argument("--scope-flag", action="append", default=[])
    parser.add_argument("--assessed-topic", action="store_true")
    parser.add_argument("--practice-only", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    parser.add_argument("--evidence-json", action="store_true")
    try:
        args = parser.parse_args(argv)
        data = load_boundaries()
        if args.self_check:
            if args.citations or args.practice or args.exam_task or args.scope_flag or args.assessed_topic or args.practice_only:
                raise ValueError("--self-check cannot be combined with a validation request")
            result, code = self_check(data), 0
        else:
            code, result = validate_request(data, args.citations, practices=args.practice,
                exam_task=args.exam_task, scope_flags=args.scope_flag,
                assessed_topic=args.assessed_topic, practice_only=args.practice_only)
    except (OSError, UnicodeError, ValueError, TypeError, KeyError) as exc:
        code, result = 2, {"schema_version": 1, "validator": f"ap-{COURSE}-topic-v1",
                           "course": COURSE, "overall_status": "error", "error": str(exc)}
    if "--evidence-json" in argv:
        print(json.dumps(result, ensure_ascii=False, separators=(",", ":")))
    else:
        print(result["overall_status"].upper())
        for message in result.get("failures", []):
            print(message)
        if "error" in result:
            print(result["error"])
    return code


if __name__ == "__main__":
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    raise SystemExit(main())
