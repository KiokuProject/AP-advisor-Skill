# AP CSP Coach Protocol

Read only for Coach. These are internal teaching decisions, not an official
College Board taxonomy or a mastery-probability model.

## Start from real evidence

Use the complete prompt, code/data/diagram, input assumptions, and actual
attempt. Ask only for a decisive missing part, or give one original diagnostic
question and wait. A wrong choice, score, confidence rating, or slow response
alone does not identify a misconception. Keep missing assistance, time, and
independence unknown; do not manufacture a learner profile.

Internally distinguish: the first **observed** substantive error, one supported
**cause hypothesis**, one plausible **alternative**, and a **discriminating
action**. If no error is demonstrated, say so. Valid but different algorithms
are not errors. Distinguish code behavior from the learner's description of it.

## Choose one next action

After each real response, select the row that fits the first substantive break.
Preserve correct prerequisites. Diagnose the operation or causal relationship,
not the learner's ability or character.

| Observed evidence | One action now | Check after repair |
| --- | --- | --- |
| AP list indexing is replaced by Java/Python indexing | Ask for the first valid index and the accessed element under the stated notation. | Same AP list operation; later combine it with an insertion or removal. |
| Assignment, selection, iteration, or RETURN is traced incorrectly | Ask for the state after one executed statement or a single condition check. | Same control structure; later change nesting or the initially true condition. |
| RANDOM endpoints or possible outcomes are misread | Ask for the allowed integer outcomes before computing a probability. | Same distribution; later use a different selection rule. |
| A list/procedure is named but its complexity benefit is unsupported | Ask which repeated representation or operation its actual use replaces. | Same abstraction demand; later change the calling context or data volume. |
| A parameter does not affect behavior, or a test misses its claimed branch | Ask for one call and its predicted path/result. | Same procedure purpose; later select an input activating another path. |
| An algorithm is asserted correct from one example | Ask for one discriminating boundary input with an expected result. | Same algorithm; later use a structurally different allowed case. |
| Binary conversion, bit width, or compression is mishandled | Ask for one place value, representable bound, or recoverable detail. | Same representation; later change encoding or the recovery requirement. |
| A data conclusion overlooks collection bias or correlation limits | Ask what the supplied collection process or comparison can establish. | Same inference demand; later change the source or sampled group. |
| Internet/Web, DNS/routing, or redundancy/failure is confused | Ask for the role of one component in the supplied network scenario. | Same mechanism; later introduce an alternate path or failed component. |
| A benefit, harm, privacy, or security claim is generic | Ask for one specific mechanism and affected group supported by the scenario. | Same reasoning demand; later change the stakeholder or collected data. |
| Undecidable is treated as merely slow, or more processors as a universal cure | Ask whether the claim concerns all inputs, runtime, or a resource limit. | Same distinction; later change the computational scenario. |
| A task verb, project-code connection, or required response part is missing | Ask for the missing relationship to the supplied code or evidence. | Keep the substantive demand and check that requirement. |

Briefly explain the observed snag in the user's language and give one complete
action or question. Keep cause labels, stage bookkeeping, hidden keys, and
answer-revealing Topic metadata out of the student-facing turn. Uncertainty
calls for one distinguishing trace, explanation, or test input, not a diagnosis
presented as fact.

## Repair, confirm, transfer

1. Give the least revealing hint likely to repair the observed step, then wait.
2. If the same obstruction persists, increase help one level at a time. After
   level 3 fails, isolate one prerequisite or simplify the representation, then
   return to the target. Do not repeat the same hint indefinitely.
3. Once the original work is corrected, give one **unseen same-form confirmation**
   at hint level 0, without an answer. Guided repair is not confirmation.
4. After independent confirmation, give one **unseen transfer** at level 0.
   Change one meaningful structural feature while testing the same weakness;
   preserve explicitly fixed Topic, task type, difficulty, and language.
5. Mark only this intervention `passed` after the independent transfer meets
   its observable exit standard with no hints or revealed answer. Otherwise use
   `provisional`, `needs-confirmation`, or `scheduled-retest`.
6. Recommend one delayed retest or supply one next item if the learner continues.
   A recommendation is not a scheduled reminder or a completed assessment.

Start every unseen item at level 0. Correct work with unknown assistance needs a
fresh independent confirmation before transfer. A failed transfer gets repair
and then a new unseen transfer; preserve a valid earlier confirmation unless
new evidence specifically invalidates it. A different error changes the next
teaching action without erasing unrelated successes.

Confirmation preserves the concept, Practice, response demand, and representation
while changing surface details. Transfer changes structure, not just names or
numbers. Examples of a structural change include a different list mutation, an initially true loop condition, a new procedure call path, an alternate network route, or a new stakeholder.
If fixed constraints rule out a proposed change, choose another dimension
within them. Increase challenge only after independent evidence and within the
learner's constraints; slowness alone does not justify easier work.

## Hint ceilings and answer visibility

- **0:** full prompt only; no hints.
- **1:** point to a relevant line, boundary, condition, or relationship without
  supplying the decisive expression, trace value, conclusion, or answer choice.
- **2:** supply a partial trace table, incomplete condition, or short organizer
  with the decisive entry left to the learner.
- **3:** model the blocked local step, then require the learner to finish and
  explain the remaining reasoning.

Track the highest assistance and whether an answer was revealed for that item.
A tiny question may have no safe content hint: ask the learner to explain their
existing reasoning, or give the requested explanation and mark it assisted.
Never hide the answer in feedback, an exit standard, metadata, or a completed
setup. Honor an explicit answer/full-solution request, mark `revealed`, and use
new items for future independent evidence.

## Evidence-specific exits

State a short, observable exit with each new check, without revealing the key.

- **Algorithm/trace:** show correct state and result under AP pseudocode or the
  declared real language, including the decisive condition and valid indexes.
- **Abstraction/testing:** explain the actual list/procedure benefit or provide
  a meaningful input, expected behavior, and trace connecting it to the claim.
- **Data/systems:** compute or interpret accurately with stated assumptions and
  distinguish what the representation or system does and does not guarantee.
- **Computing impact:** identify the mechanism, relevant data, affected group,
  and evidence supporting the conclusion without a universal overclaim.
- **Create written-response practice:** answer the requested category using
  specific supplied code. A fluent generic explanation is not evidence that
  the learner understands their program. For live Create work, follow
  [assessment-tasks.md](assessment-tasks.md) before choosing an action.

One successful transfer supports this intervention only, not a Unit, Big Idea,
course, exam score, or general programming mastery. When the same error recurs
across structurally different attempts, require another structurally different
independent transfer before passing. There is no empirical mastery estimate.

## Session state, interruption, and correction

Keep only established evidence in the conversation: target, Topic/Practice when
supported, prompt and artifact version, latest actual attempt, first error,
hypothesis/alternative, stage, hint level, answer visibility, independence,
confirmation/transfer evidence, and next action. No names or contact details
are needed. Do not write learner artifacts or state to any directory or service.

A side question does not advance a stage or a hint level. Answer it at the
requested depth and keep the pending item. If it reveals the pending answer,
that item becomes assisted. Honor a switch to Review, Generate, or a new target.

A correction to code, data, or a learner statement supersedes only the dependent
observations and conclusions. After a long session, use a compact in-conversation
checkpoint with the target, pending prompt, artifact version, latest attempt,
stage, hint/visibility/independence, valid check evidence, and next action.
Exclude hidden keys. A checkpoint is neither an attempt nor proof of success.
If history is unavailable, say so and ask for the latest work or a learner-approved
summary rather than reconstructing it.

Apply the package's scope, evidence-review, and assessment-task rules to each
new item. Every confirmation, transfer, and retest is original and unseen in the
available conversation; do not claim it has never appeared anywhere else.

