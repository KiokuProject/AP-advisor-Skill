**English** | [简体中文](./README.zh-CN.md) | [繁體中文](./README.zh-TW.md)

# AP Advisor Skills

Send a question and your attempt. Get help finding where you went wrong,
fixing that step, and choosing what to try next.

These three Skills add AP study guidance to Codex. They support English,
Simplified Chinese, and Traditional Chinese.

| Install this Skill | For these courses |
| --- | --- |
| [ap-calculus-advisor](./ap-calculus-advisor/) | AP Precalculus, AP Calculus AB, AP Calculus BC |
| [ap-psychology-advisor](./ap-psychology-advisor/) | AP Psychology |
| [ap-biology-advisor](./ap-biology-advisor/) | AP Biology |

## Start here

Ask Skill Installer to install the subjects you need:

```text
$skill-installer Install the skill at path ap-calculus-advisor from iyorixy/AP-advisor-Skill as ap-calculus-advisor.
$skill-installer Install the skill at path ap-psychology-advisor from iyorixy/AP-advisor-Skill as ap-psychology-advisor.
$skill-installer Install the skill at path ap-biology-advisor from iyorixy/AP-advisor-Skill as ap-biology-advisor.
```

Install the subject folders, not the repository root. If an installed Skill
doesn't appear, try restarting Codex. Local checking scripts need Python 3.10+
and use only its standard library.

Then attach or paste the question, any needed graph/data/source, and your work:

```text
$ap-calculus-advisor I'm studying AP Calculus AB. Use my mistakes to choose the next question. One hint at a time; let me try before showing the answer.
```

No attempt yet? Name your course and what you want to practice. Coach starts
with one question and waits for your answer. You don't need to know a Topic code.

## What you can ask for

| You want to… | Say something like… |
| --- | --- |
| Understand an idea or get practice (Generate) | “Explain this, then give me a similar question without the answer.” |
| Check your work (Review) | “Find the first error in my solution.” |
| Decide what to study (Advisor) | “Based on these mistakes, pick the next 1–3 things to practice.” |
| Practice with feedback after each attempt (Coach) | “Guide me one step at a time and adjust the next question from my mistakes.” |

You don't need to memorize the mode names. You can ask for a full explanation,
switch topics, or stop coaching at any time.

## How Coach adapts

All five courses use the same idea: **your actual mistake determines the next
action**. A low score alone isn't enough to tell what went wrong.

| What your work shows | What Coach does next |
| --- | --- |
| A concept or rule is mixed up | Gives a short contrast or checks the missing condition. |
| The method is right, but a calculation goes wrong | Helps fix that step, then keeps the next question at a similar level. |
| A graph, table, or diagram is misread | Asks you to read one feature before interpreting it. |
| A definition is correct but doesn't explain the scenario | Asks you to connect it to one specific detail. |
| A model, experiment, or evidence-based argument has a gap | Focuses on the missing relationship, comparison, or reason. |
| A condition or required answer part was missed | Asks you to complete that part. |

For example, on an original derivative exercise:

> **You:** For f(x) = x³ − 2x, I got f′(x) = 3x² + 2.
>
> **Coach:** The first term is correct. Check the sign in the −2x term: write just its derivative.

Coach then waits. It doesn't invent your correction or give you a whole worksheet.

Once you fix the step, you get **one new question of the same kind, without
hints**. If you solve it independently, the next question changes one meaningful
feature, such as the context or representation. If you get stuck, help increases
gradually; after three hint levels, Coach breaks out a smaller prerequisite step.

Passing that changed question shows progress on this specific skill. A later
mistake doesn't erase unrelated successes, and one success doesn't mean you've
mastered the entire unit. The course, Topic, task type, and difficulty you
explicitly requested stay fixed.

## Try it in your subject

```text
$ap-calculus-advisor I'm studying AP Precalculus. Use this function-graph attempt to choose my next step.
$ap-calculus-advisor I'm studying AP Calculus AB. Check my derivative work and guide me through the first error.
$ap-calculus-advisor I'm studying AP Calculus BC. Use this series-convergence attempt to choose what I should practice next.
$ap-psychology-advisor I know this concept's definition but can't apply it. Use my answer to guide me one question at a time.
$ap-biology-advisor Use my graph and explanation to decide whether I need help reading the data or explaining the mechanism. Give me one step.
```

Include the actual question and attempt with each request.

## A few things to know

- **Practice questions are original.** Mathematics includes 96 maintained
  questions covering 32 error patterns, with generated practice for gaps.
  Biology and Psychology generate questions as needed. This isn't a complete
  question bank or a source of secure AP Classroom material.
- **You choose when to see the answer.** Coach normally lets you try first.
  A solution completed with help doesn't count as independent success.
- **Memory stays in the conversation by default.** Mathematics can save a local
  learning record when you explicitly request it and provide a folder outside
  this repository. Biology and Psychology use conversation history only.
- **These Skills guide the model; they can still make mistakes.** They include
  instructions for GPT-6 Astra and other capable hosts. Topic checks don't
  prove that an explanation or score is correct. Official scoring needs the
  matching question and scoring guide.

For course details, read the subject's Skill linked above. For local records,
checks, and implementation details, see [development notes](./docs/development.md).

## License

[MIT](./LICENSE). AP is a College Board trademark. This project is not endorsed
by College Board.
