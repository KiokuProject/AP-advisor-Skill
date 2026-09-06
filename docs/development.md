# Development notes

For installation and everyday use, start with the [README](../README.md),
[简体中文说明](../README.zh-CN.md), or [繁體中文說明](../README.zh-TW.md).
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
answers stay out of that response. All five courses support this flow:

- [Precalculus / Calculus AB / Calculus BC](../ap-calculus-advisor/references/session-protocol.md)
- [Biology](../ap-biology-advisor/references/session-protocol.md)
- [Psychology](../ap-psychology-advisor/references/session-protocol.md)

Use the [adaptive Coach scenarios](../evals/adaptive-coach-cases.md) to review
error routing and multi-turn behavior after changing these instructions.
They are manual behavioral cases, not executed model results. Keep historical
review records intact; a local release check doesn't create fresh model evidence.

## Course baselines

The recorded baselines are Fall 2026 for Precalculus; Fall 2020 plus Fall 2026
clarifications for Calculus AB/BC; Fall 2025 plus October 2025 clarifications for
Psychology; and Fall 2025 plus June 2025/June 2026 clarifications for Biology.
Precalculus Unit 4 is instructional only. Source dates, scope, and corrections
are maintained in the subject packages:

- [Mathematics boundaries](../ap-calculus-advisor/references/ap-content-boundaries.json)
- [Psychology boundaries](../ap-psychology-advisor/references/ap-psychology-boundaries.json)
- [Biology boundaries](../ap-biology-advisor/references/ap-biology-boundaries.json)

A Topic check validates the citation and declared scope, not the reasoning,
question quality, or an official score. Review the subject matter separately.
Recheck time-sensitive exam information against current official sources.

## Privacy and optional local state

Every Coach is session-only by default and writes no local files. The Biology
and Psychology Coaches remain session-only. For the three mathematics courses,
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
python scripts/run_evals.py --self-check --evidence-json
python -m unittest discover -s tests -v
python scripts/check_release.py --evidence-json
```

The three validator self-checks cover each Skill's mapping and boundary package.
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

The mathematics selector deliberately uses transparent rules rather than BKT,
IRT, vector retrieval, or empirical mastery probabilities. Aggregate
calibration exports remain descriptive and report `insufficient_data` below
their sample minimum; future calibration requires real, consented,
de-identified response data and a separate review.
