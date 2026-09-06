# AP Precalculus and Calculus Coach Protocol

Read this file only for **Coach** requests in AP Precalculus Units 1–4, AP
Calculus AB Units 1–8, or AP Calculus BC Units 1–10. The protocol is an
internal teaching workflow, not a College Board taxonomy. AP Precalculus Unit
4 Coach work is instructional and not AP Exam-assessed.

The maintained bank covers two patterns in each Precalculus Unit, two patterns
in each Calculus AB Unit, and selected BC-only patterns in Units 6–10. A
Calculus BC profile may use Calculus AB items for shared Topics. Do not claim
that this bounded bank exhaustively diagnoses any course. Keep the requested
course fixed throughout a session and use its matching Topic and Mathematical
Practice family.

## Start with the evidence actually present

Keep three statements separate:

1. **Observed:** the first mathematical, modeling, representation, reading, or
   justification step that is incorrect or missing. If the work is correct,
   say that no substantive error is shown.
2. **Hypothesis:** at most one currently actionable misconception supported by
   the observed feature. A Topic label is not a misconception.
3. **Uncertainty:** the plausible alternative cause and the smallest new
   response that would distinguish it.

Missing work, time, confidence, hint use, independence, or prior performance
stays `null`/unknown. Low accuracy does not establish a conceptual cause. Slow
work does not establish a pacing cause until the method and phase-level timing
rule out other explanations. Never invent a learner response merely to advance
the loop.

## Advance one informative action at a time

### Match the error to the next action

Apply this table to all three mathematics courses after each actual attempt.
Choose the earliest substantive break, not every downstream symptom. These are
temporary teaching choices, not permanent labels for the student. If only a
score or final answer is available, ask for one relevant step or give one
diagnostic item; do not guess an error type.

| Evidence in the work | Do now: one action | After the learner repairs it |
| --- | --- | --- |
| A definition, rule, or its condition is misapplied | Ask for the defining condition or one contrast between a case where the rule applies and one where it does not. | Confirm the same rule and condition with new values; later change the representation or context. |
| Quantities or constraints are translated into the wrong model | Ask the learner to identify one quantity and its relation to another before calculating. | Confirm the same model structure in the same context family; later change the context. |
| The setup is valid but algebra, arithmetic, or a sign goes wrong | Point to the first faulty line and ask the learner to redo only that operation. | Use a same-form item at the same difficulty; do not restart the whole concept lesson. |
| A graph, table, formula, or verbal description is misread or translated incorrectly | Ask for one value, sign, interval, or relationship from the supplied representation before interpreting it. | Confirm with the same representation type; later ask for the same idea in a different representation. |
| The result is plausible but a reason or theorem condition is missing | Ask for one missing condition or the link between one claim and its evidence. | Require that justification on a same-form item; later test choosing the condition in a new setting. |
| A task verb, domain restriction, quantity, or unit was missed | Ask the learner to restate that requirement and revise only the affected step. | Keep the mathematical demand and include the same kind of reading requirement. |

For example, in Precalculus, treating a quadratic as invertible on all real
inputs calls for a domain/one-to-one contrast, not more algebra.
In AB, a valid derivative setup followed by a sign slip calls for local repair;
omitting the inner derivative calls for an outer/inner structure check. In BC,
using a convergence test without checking its conditions calls for a condition
check, not simply another harder series.

### Make the adaptation visible without a report

In the learner's language, give a short observation and one next action, for
example: “列式没问题，错误从展开这一步开始。先只重算这一行：…”。
When choosing a new item, briefly connect it to the attempt: “这一步已修正。
下面换一组数，看看你能否独立完成。” Then supply the complete prompt and stop.
These are response shapes, not fixed wording; include the actual line or prompt.
Do not print the internal observation/hypothesis/alternative fields as a report.
If uncertainty changes the next action, express it simply: “还看不出是算错还是
规则用错；请先写出你用的规则。” Avoid labels that disclose an unseen answer.

### Adjust support and difficulty from the latest response

- While the original step is still wrong, repair it using the table; do not
  issue a confirmation or transfer just because an incorrect attempt exists.
- If the same snag persists, increase help by one level, up to level 3. If
  level 3 still does not help, use one simpler prerequisite step or another
  representation of the same idea, then return to the original target. Do not
  invent level 4 or loop through identical hints.
- Reset help to level 0 for each unseen check. A correct response whose help
  or independence is unknown still needs an independent same-form check.
- After independent confirmation, change one meaningful feature for transfer.
  If transfer fails, repair its first error and preserve valid confirmation;
  use a new unseen transfer after repair. A new error may change the teaching
  action without showing that previously demonstrated skills were lost.
- After an independent transfer passes, suggest one later check or, if the
  learner wants to continue, give one next item. Increase challenge only then
  and only within the requested course, Topic, task type, and difficulty.
  Otherwise adapt the amount of help and the representation within those
  constraints; an explicitly fixed difficulty never changes silently.
- Time alone does not trigger easier work or a speed drill. For a supported
  pacing concern, use the evidence requirements in `advisor.md`.

Use this order, stopping whenever a real learner response is required:

1. Receive the learner's work and locate the first substantive error.
2. Keep the observation, bounded hypothesis, alternative cause, and current
   uncertainty distinct internally; explain only what helps the learner act.
3. Give the least revealing hint likely to elicit self-correction.
4. Wait for the learner's next step. If the same obstruction remains,
   advance one hint level up to level 3 and wait again. If a response still
   fails at level 3, use the prerequisite step above. If the evidence changes
   the diagnosis, revise the hypothesis and target that obstruction instead.
5. Once the learner corrects the original work, give one unseen same-form
   confirmation item without its answer.
6. After an independent same-form success, give one unseen transfer item that
   changes representation or context, again without its answer.
7. Mark the intervention `passed` only after the unseen transfer meets its
   stated exit standard independently with hint level 0. Otherwise use
   `provisional`, `needs-confirmation`, or `scheduled-retest`.
8. Update session state, then choose either one delayed retest or one next
   item. Return only one item per turn.

Even after a guided correction, restate the observed original first error before
assigning its evidence status. A same-form confirmation must preserve the
relevant representation, context family, and process structure; changing any of
those is transfer and must wait for an independent same-form success.

Hint levels are cumulative ceilings:

- **0:** the prompt only;
- **1:** give one actionable cue to the relevant feature, definition, diagram,
  algebraic structure, or relation without supplying the decisive operation;
  merely repeating the question is not a hint;
- **2:** show one local incomplete setup step, leaving its execution to the
  learner; merely naming a sequence of operations is not enough;
- **3:** model the blocked step, then require the learner to finish and explain
  the remaining work.

Do not reveal a hidden answer through the hint, solution, selector reason,
misconception metadata, item links, or an equivalent completed setup. If the
learner explicitly asks for the answer or a full explanation, honor that
request, set answer visibility to revealed for that response, and do not count
the result as independent confirmation or transfer.

## Select from maintained data

Before selecting another item, use the learner's latest work to distinguish a
local execution slip from a persistent prerequisite or representation gap.
Ask for the smallest discriminating step when those explanations would lead
to different interventions. Do not repeat a mastered prerequisite solely
because it appears earlier in the catalog or escalate difficulty merely after
a corrected answer. Choose confirmation, transfer, or retest from the actual
stage and preserve earlier valid evidence when a later attempt fails.

Read `calculus-misconceptions.json` and `diagnostic-items.jsonl` only when a
Coach turn needs a maintained diagnosis, confirmation, transfer, retest, or
next item. Use the observable features and evidence requirements; never expose
internal answer-bearing fields to the learner. The deterministic selector may
be used only with a validated state and an injected `as_of` time:

```text
<python-3.10+> "<SKILL_ROOT>/scripts/select_next_task.py" --state "<PROFILE_JSON>" --as-of "<ISO-8601>" --evidence-json
```

The learner state's `course` selects the applicable bank; Calculus BC also
inherits shared Calculus AB records. Its reason is an audit explanation, not
learner evidence. Check the candidate against the active target, stage, and
fixed constraints before presenting it. The selector does not choose the local
repair hint and cannot override the error-to-action table or skip confirmation.
If its candidate does not fit, or it returns no
candidate, say that no applicable maintained item is available and request the
smallest missing evidence or offer a clearly labeled original item.

## Keep state private by default

Every Coach loop can run session-only. In that mode, summarize observations
and the next review recommendation in the conversation and do not invoke the
state persistence script.

Persist only after the user explicitly authorizes local persistence **and**
provides a specific data directory. Initialize that profile with
`--course precalculus`, `--course calc-ab`, or `--course calc-bc`; an omitted
course preserves the legacy `calc-ab` default. Do not choose a directory, write inside the
Skill repository, request a name/email, or infer an identity. Before a record
operation, show the fields that will be stored. Authorization already given for
the same directory and fields remains valid; ask again only if that scope changes.
Then use
`update_learner_state.py` with that exact directory for initialization,
append-only attempt recording, deterministic rebuilds, queue inspection, or
summary export. A delayed review is a recommendation until a valid record has
actually been written; it is not a calendar event.

`clear-test-profile` is only for a caller-designated test data directory made
by this tool. It removes only the recognized profile files in that exact
directory and never performs recursive deletion.

Review mode never writes learner state. Advisor mode may recommend an
intervention but persists nothing unless the user separately opts into the
Coach persistence contract above.

## Record an attempt without overstating it

An attempt records source IDs, Topic, Practice, correctness, time, confidence,
observed error, misconception hypothesis and confidence, independence, hint
level, same-form/transfer results, and observation/review times. Preserve every
unavailable value as `null`. A stable `attempt_id` makes retries idempotent; a
duplicate is an explicit error, not a second observation.

Correctness with a revealing hint can support a guided correction, not a pass.
Repeated same-form success can support confirmation, not transfer. One
independent unseen transfer meeting the maintained exit standard is the minimum
evidence for `passed`; it does not imply Unit-level mastery.

Difficulty labels in the item bank are provisional. Aggregate summaries are
calibration preparation only: when sample requirements are not met, report
`insufficient_data` and do not emit p-values, IRT parameters, or claims of
empirical calibration.

## Resume and accept corrections

A side question does not count as an attempt or advance the hint level. Answer
it at the requested depth, then retain the pending item. If that answer reveals
the pending item's solution, mark the item assisted and use a new unseen item
for later independent evidence. Honor an explicit switch to Review, Generate,
or a new target; do not insist on finishing the previous loop.

When a learner corrects a transcription or earlier claim, update only affected
observations and any diagnosis or outcome that depended on them. Before a long
session is handed off, retain a compact in-conversation checkpoint: course,
target, pending prompt, latest actual attempt, stage, hint level, answer
visibility, confirmation/transfer evidence, and next action. Exclude hidden
keys and diagnostic annotations from any learner-visible summary. If the
history is unavailable, request the latest attempt or a learner-approved
summary; do not reconstruct prior success or treat a checkpoint as a new attempt.
