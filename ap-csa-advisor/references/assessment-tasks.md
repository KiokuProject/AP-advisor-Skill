# AP CSA assessment tasks

Read before generating or reviewing an exam task. Baseline checked 2026-09-08;
recheck the [official exam page](https://apcentral.collegeboard.org/courses/ap-computer-science-a/exam)
before quoting changeable exam facts. The recorded format is 42 MCQs in 90
minutes (55%) and four FRQs in 90 minutes (45%), with digital responses in
Bluebook. The linked Java Quick Reference defines the supplied library surface.

## Match the actual task

| Validator task | Original practice must supply |
| --- | --- |
| `mcq` | A complete stem and any code/input/class context; four choices with one defensible key. Include the needed API contract. |
| `frq-methods` | A supplied class and specifications for two methods, or a constructor and method. Part A uses selection/iteration and calls in the specified class; Part B uses String methods. |
| `frq-class` | A scenario and interaction/result table sufficient to implement the class header, fields, constructor, and required method. |
| `frq-data` | A supplied scenario/class and one method using, analyzing, and manipulating an ArrayList. A plain-array-only exercise is not a full current Question 3. |
| `frq-2d` | A supplied scenario/class and one method using, analyzing, and manipulating a rectangular 2D array. |

All current FRQs assess Practice 2. A trace-only question can be useful practice,
but is not a full code-writing FRQ. An excerpt, one part of Question 1, or a
single constructor exercise must be labeled partial. Validate every materially
used Topic and Practice; the script's task check cannot certify full coverage.
The table is paraphrased from the official exam task descriptions above.

## Review before showing an item

Solve the final prompt independently. Check signatures, visibility, return
types, permitted operations, preconditions, and the examples against the code.
Use at least the normal input and the case that discriminates the targeted
error. Do not reject a valid alternative algorithm merely because it differs
from the private key. Do not add requirements absent from the prompt.

Check four choices for unique correctness, including aliases, order of
evaluation, index bounds, and integer division. Keep the private answer,
distractor diagnoses, and filled trace tables out of hidden-answer output.
Label generated questions original and generated data synthetic.

## Scoring and legacy material

Only give an official numeric score when the released prompt and official
scoring guide match the year, form, and question. Read the guide's treatment of
minor syntax errors and alternative solutions; successful compilation is
neither necessary nor sufficient evidence of an official score. Without the
matching guide, give explicitly unscored feedback, or a requested instructional
score using a disclosed original checklist.

May 2025 and earlier questions retain their original rubric and ten-unit
mapping. Explain any current-scope differences, particularly inheritance
implementation, the new text-file content, and changed FRQ structures. Never
relabel an old question's original title or rubric as a current one.

For scope details and source versions, consult
[ap-csa-boundaries.json](ap-csa-boundaries.json). Exclusion flags are not a
complete Java parser or an exhaustive description of every CED exclusion.
