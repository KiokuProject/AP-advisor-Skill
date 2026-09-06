# Adaptive Coach behavior checks

These are original, synthetic test scenarios for reviewing the Coach
instructions. They are not student records, scored runs, or evidence of learning
gains. Use the named subject Skill with its local references. Give the tester the
request and supplied work, then evaluate the response against the expected
behavior. For multi-turn cases, submit a real tester response each turn; do not
ask the Coach to invent the learner's replies.

## 1. Precalculus: concept versus algebra

**Request:** “我在学 AP Precalculus。函数 f(x)=x²，定义域是全体实数。
我写 f⁻¹(x)=√x，因为反函数就是开平方。根据我的错误带我练下一步，
先不要完整答案。”

**Expected:** Focus on whether an inverse function exists on the stated domain,
using one one-to-one/domain check. Do not silently restrict the domain or assign
another algebra drill. Ask one concrete action and wait.

## 2. Calculus AB: local sign slip

**Request:** “AP Calculus AB，先保持普通难度，每次只带我做一步。
题目是求 f(x)=x³−2x 的导数。我写了 f′(x)=3x²+2。”

**Expected:** Preserve the correct first term and focus on differentiating the
negative linear term. Give one local cue or action, not a whole derivative
lesson, a full solution, or a new confirmation before repair.

**Next input:** The tester independently writes “−2x 的导数是 −2，所以应是
3x²−2。”

**Expected next turn:** Give one unseen same-form question without hints or its
answer, preserving the difficulty and response structure. The guided repair
does not justify transfer or a pass yet.

## 3. Calculus BC: missing convergence condition

**Request:** “我在学 AP Calculus BC。判断 ∑从 n=1 到无穷的
(−1)^(n+1)n/(n+1) 是否收敛。我写：正负交替，所以根据交错级数判别法收敛。
根据这个错误决定下一步，只给一个提示。”

**Expected:** Target the missing conditions for the claimed test, with one
non-revealing condition check. Do not jump to a harder series, switch to AB, or
give the convergence verdict in the same turn.

## 4. Biology: mechanism versus arithmetic

**Request A:** “AP Biology，带我练这一步。原创情境：在细菌种群中，施加抗生素后，
抗性细菌的比例上升。我解释：每个细菌因为需要生存，所以产生了抗性。”

**Expected A:** Target the unsupported individual/need-based explanation and
elicit one population-level causal link. Do not invent observed mutations,
experimental procedures, or data.

**Request B, separate session:** “AP Biology，带我改错。合成数据：对照组平均生物量
12 g，处理组平均生物量 9 g。求处理组相对对照组减少百分比。
我的式子是 (12−9)/12×100%，算得 20%。”

**Expected B:** Preserve the correct setup and ask for local calculation repair
with the appropriate units/percentage. Do not reteach the biological mechanism
or infer statistical significance.

## 5. Psychology: definition versus application

**Request:** “AP Psychology，逐题带我练。原创情境：系好安全带后，提醒音停止，
司机后来更常系安全带。题目要求用负强化解释这个变化。
我答：负强化是移除厌恶刺激，使行为更常发生。”

**Expected:** Acknowledge the valid definition and ask for its connection to the
specific stimulus and behavior. Do not ask another definition quiz, supply the
completed application, or infer that the concept itself is unknown.

## 6. Psychology: sampling versus assignment

**Request:** “AP Psychology，根据这份作答安排下一步。合成研究：从一所学校随机抽取
100 人，记录他们自报的睡眠时间和当天测验分数，发现两者正相关。我答：
随机抽样证明增加睡眠会提高测验分数。先让我自己改。”

**Expected:** Ask one concrete design/inference question distinguishing sampling
from an intervention or assignment. Do not fabricate random assignment, label
the study an experiment, or replace it with a calculation drill.

## 7. All courses: no evidence and unknown independence

Run separately with each of Precalculus, Calculus AB, Calculus BC, Biology, and
Psychology.

**Request A:** “我这门课最近只考了 50%，根据我的错误给我下一步。”

**Expected A:** Ask for one missed prompt and actual work, or give one bounded
diagnostic prompt when a target is known. Do not diagnose a concept from the
score, pick an unsupported Topic, or start a full diagnostic set.

**Request B:** “上次我做对了，帮我升级。现在没有上次的过程，也不确定有没有看提示。”

**Expected B:** Keep prior independence unknown. Collect one independent
same-form response after establishing the target; do not count the report as
confirmed transfer or a reason to increase difficulty.

## 8. All courses: help reaches its limit

For a concrete pending question, supply actual unsuccessful attempts through
hint levels 1, 2, and 3.

**Expected:** At each turn, give only one useful action. After level 3 fails,
isolate one prerequisite step or use a simpler representation of the same
target. Do not create level 4, repeat the same hint indefinitely, reveal an
unrequested complete answer, or advance to confirmation without correction.

## 9. All courses: failed transfer preserves earlier evidence

First complete an unseen same-form item independently at level 0. On the
following transfer, deliberately make a new local error while retaining the
previously demonstrated reasoning.

**Expected:** Repair the new first error without erasing the earlier valid
confirmation or silently lowering a fixed difficulty. After repair, use a new
unseen transfer; redoing the exposed item is not an independent transfer pass.

## 10. All courses: answer request and mode switch

While a Coach question is pending, ask “这题请直接给我完整讲解”, then after the
explanation say “先不练了，只帮我检查这份新作答” and provide a new attempt.

**Expected:** Honor both requests. The revealed answer is assisted evidence,
not a pass. Review only the newly supplied work without forcing another Coach
question or creating a local learning record.
