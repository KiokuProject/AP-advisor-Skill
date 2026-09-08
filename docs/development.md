# Development notes

For installation and everyday use, start with the [README](../README.md),
[日本語](../README.ja.md), [简体中文](../README.zh-CN.md),
[繁體中文](../README.zh-TW.md), [한국어](../README.ko.md), or [Deutsch](../README.de.md).
Commands below run from the repository root.

## Where to make changes

| Change | File |
| --- | --- |
| When a subject Skill should activate | Its `SKILL.md` |
| Error type → teaching action, hint levels, confirmation, and transfer | Its `references/session-protocol.md` |
| How to choose a short study plan | Its `references/advisor.md` |
| Course scope, Topic names, and assessment requirements | Its framework, boundary, and assessment-task references |
| Maintained mathematics questions and selection | Mathematics misconception/item files and `scripts/select_next_task.py` |

Each subject folder must work when installed alone. Coach uses the host model
to read the student's work and follow the subject's error-to-action table; it
doesn't run a separate classifier or estimate a mastery probability. Mathematics
also has a deterministic selector for maintained items. Its output must fit the
current teaching stage and user constraints before being shown.

The student-facing response should briefly explain the observed snag and give
one complete action or question. Internal cause hypotheses, labels, and hidden
answers stay out of that response. All seven courses support this flow:

- [Precalculus / Calculus AB / Calculus BC](../ap-calculus-advisor/references/session-protocol.md)
- [Biology](../ap-biology-advisor/references/session-protocol.md)
- [Psychology](../ap-psychology-advisor/references/session-protocol.md)
- [Computer Science A](../ap-csa-advisor/references/session-protocol.md)
- [Computer Science Principles](../ap-csp-advisor/references/session-protocol.md)

Use the [adaptive Coach scenarios](../evals/adaptive-coach-cases.md) to review
error routing and multi-turn behavior after changing these instructions.
They are manual behavioral cases, not executed model results. Keep historical
review records intact; a local release check doesn't create fresh model evidence.
The [CSA/CSP scenarios](../evals/cs-adaptive-coach-cases.md) additionally cover
Java/AP pseudocode semantics, Create assistance boundaries, and multi-turn
confirmation/transfer. These new scenarios have no recorded model-run results.

## Course baselines

The recorded baselines are Fall 2026 for Precalculus; Fall 2020 plus Fall 2026
clarifications for Calculus AB/BC; Fall 2025 plus October 2025 clarifications for
Psychology; and Fall 2025 plus June 2025/June 2026 clarifications for Biology.
Precalculus Unit 4 is instructional only. Source dates, scope, and corrections
are maintained in the subject packages:

- [Mathematics boundaries](../ap-calculus-advisor/references/ap-content-boundaries.json)
- [Psychology boundaries](../ap-psychology-advisor/references/ap-psychology-boundaries.json)
- [Biology boundaries](../ap-biology-advisor/references/ap-biology-boundaries.json)
- [CSA boundaries](../ap-csa-advisor/references/ap-csa-boundaries.json)
- [CSP boundaries](../ap-csp-advisor/references/ap-csp-boundaries.json)

CSA uses the Fall 2025 four-unit framework (53 Topics, 12 Practice skills).
CSP uses the Fall 2023 five-Big-Idea framework (35 Topics, 20 Practice skills)
for 2026–27. These baselines were checked on 2026-09-08 against the
[official course changes table](https://apcentral.collegeboard.org/courses/how-ap-develops-courses-and-exams/course-changes-overview)
and the CED sources recorded in each package. Recheck the announced CSP 2027–28
revision before changing that baseline. Older CSA ten-unit citations and CSP
Explore/pre-2024 Create formats require explicit historical handling.

The two CS packages keep their catalog and declared task/exclusion rules in one
boundary JSON each. Their small, identical standard-library validators are
bundled in both packages so either folder installs alone; keep both copies in
sync. They check exact citations, Practice compatibility, and declared scope
flags, not code semantics or full-task completeness. `--practice-only` deliberately
cannot certify an exam task or content scope. New practice is generated and
reviewed by the host; these packages do not include a maintained item bank,
automatic mastery estimator, or persistent learner-state engine.

A Topic check validates the citation and declared scope, not the reasoning,
question quality, or an official score. Review the subject matter separately.
Recheck time-sensitive exam information against current official sources.

## Privacy and optional local state

Every Coach is session-only by default and writes no local files. The Biology,
Psychology, CSA, and CSP Coaches remain session-only. For the three mathematics courses,
local persistence requires both explicit authorization and a caller-supplied
data directory outside this repository. The state stores a pseudonymous profile
ID, course, attempts, evidence, hint/independence fields, and a review queue; it
does not request names or email addresses.

Use an explicit external directory (replace the examples below with paths
chosen by the caller). Replace `calc-ab` with `precalculus` or `calc-bc` when
initializing another mathematics course:

```powershell
python ap-calculus-advisor/scripts/update_learner_state.py --data-dir "D:\learner-data\calc-ab-demo" `
  --as-of "2026-08-31T12:00:00Z" --evidence-json init --profile-id demo_profile --course calc-ab
python ap-calculus-advisor/scripts/update_learner_state.py --data-dir "D:\learner-data\calc-ab-demo" `
  --as-of "2026-08-31T12:10:00Z" --evidence-json record --attempt-file attempt.json
python ap-calculus-advisor/scripts/update_learner_state.py --data-dir "D:\learner-data\calc-ab-demo" `
  --as-of "2026-08-31T12:10:00Z" --evidence-json queue
```

`clear-test-profile` works only for a directory initialized with `--test-data`
and removes only the recognized files for the exact profile. It is not a
general data-deletion command. Keep real learner data outside the repository
and do not commit it.

```powershell
python ap-calculus-advisor/scripts/update_learner_state.py --data-dir "D:\learner-data\calc-ab-test" `
  --evidence-json init --profile-id test_profile --course calc-ab --test-data
python ap-calculus-advisor/scripts/update_learner_state.py --data-dir "D:\learner-data\calc-ab-test" `
  --evidence-json clear-test-profile --profile-id test_profile
```

## Verify a checkout

Run from the repository root (`python3` may replace `python`):

```bash
python ap-calculus-advisor/scripts/validate_topic_code.py --self-check --evidence-json
python ap-psychology-advisor/scripts/validate_topic_code.py --self-check --evidence-json
python ap-biology-advisor/scripts/validate_topic_code.py --self-check --evidence-json
python ap-csa-advisor/scripts/validate_topic_code.py --self-check --evidence-json
python ap-csp-advisor/scripts/validate_topic_code.py --self-check --evidence-json
python scripts/run_evals.py --self-check --evidence-json
python -m unittest discover -s tests -v
python scripts/check_release.py --evidence-json
```

The five validator self-checks cover each Skill's mapping and boundary package.
The release gate additionally validates all Coach protocol artifacts, the
mathematics assessment contract, misconception/item cross-references, math
audit hashes, learner-state safety, selector determinism, behavioral review
thresholds, Python compilation and standard-library imports, unit tests, and
the installed skill-creator validator. Treat the checkout as verified only when
every command exits `0` and the last command emits lower-case
`"overall_status":"pass"`.

These are local checks, including consistency checks on recorded behavioral
reviews; they do not run a fresh Astra evaluation or measure learning gains.
Historical review records remain historical evidence; Astra-specific behavior
has not yet been evaluated with fresh model outputs.
CSA/CSP unit tests include isolated package copies, rejection of legacy citations,
invalid task/Practice combinations, explicit scope exclusions, and malformed
boundary data. Passing them does not turn the manual Coach scenarios into
behavioral evidence or extend the historical mathematics reviews to CS.

The mathematics selector deliberately uses transparent rules rather than BKT,
IRT, vector retrieval, or empirical mastery probabilities. Aggregate
calibration exports remain descriptive and report `insufficient_data` below
their sample minimum; future calibration requires real, consented,
de-identified response data and a separate review.
