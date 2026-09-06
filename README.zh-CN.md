[English](./README.md) | **简体中文** | [繁體中文](./README.zh-TW.md)

# AP Advisor Skills

把题目和你的解题过程发给它。它会帮你找出哪里出了错，带你改好这一步，
再根据你的表现安排下一题。

这是三套给 Codex 用的 AP 学习技能，支持英文、简体中文和繁体中文。

| 安装哪个技能 | 可以学什么 |
| --- | --- |
| [ap-calculus-advisor](./ap-calculus-advisor/) | AP Precalculus、AP Calculus AB、AP Calculus BC |
| [ap-psychology-advisor](./ap-psychology-advisor/) | AP 心理学 |
| [ap-biology-advisor](./ap-biology-advisor/) | AP 生物学 |

## 先用起来

在 Codex 中发送对应科目的安装指令，需要哪科就装哪科：

```text
$skill-installer Install the skill at path ap-calculus-advisor from iyorixy/AP-advisor-Skill as ap-calculus-advisor.
$skill-installer Install the skill at path ap-psychology-advisor from iyorixy/AP-advisor-Skill as ap-psychology-advisor.
$skill-installer Install the skill at path ap-biology-advisor from iyorixy/AP-advisor-Skill as ap-biology-advisor.
```

安装的是这三个科目文件夹，不是整个仓库。装好后如果没显示，可以重启 Codex。
本地检查脚本需要 Python 3.10+，不需要额外安装 Python 库。

然后贴上题目、必要的图表或材料，以及你已经写出的步骤，比如：

```text
$ap-calculus-advisor 我在学 AP Calculus AB。请根据我的错误调整下一题，每次只给一个提示，先让我自己做，不要直接公布答案。
```

还没做题也没关系。告诉它你学哪门课、想练什么，它会先出一题，等你作答。
不需要先查好知识点编号。

## 它能帮你做什么

| 你想做什么 | 可以这样说 |
| --- | --- |
| 学概念、要练习（Generate） | “讲讲这个概念，再出一道类似题，先不要答案。” |
| 检查作答（Review） | “看看我的过程，指出最先出错的那一步。” |
| 决定先学什么（Advisor） | “根据这些错题，帮我选接下来最该练的 1–3 件事。” |
| 边做边调整（Coach） | “一步步带我练，根据我怎么错来决定下一题。” |

不用记这些模式名。练到一半想看完整讲解、换知识点或者结束，直接说就行。

## Coach 怎么根据错误调整

五门课都支持。核心很简单：**错在哪里，就先练哪里。**
它会看你的实际步骤；只有一个低分或错误选项，还不能确定原因。

| 你的作答出了什么问题 | 它接下来怎么带你练 |
| --- | --- |
| 概念混了、规则用错了 | 先做一个小对比，或检查这条规则的适用条件。 |
| 方法对了，只是算错 | 先修正那一步，下一题保持相近难度。 |
| 图表或示意图读错了 | 先读出一个关键信息，再解释它的意思。 |
| 定义背对了，却不会用在题目里 | 先把定义和情境中的一个具体细节联系起来。 |
| 建模、实验设计或论证缺了一环 | 只补那个关系、对照或理由。 |
| 漏看条件、漏答一部分 | 先补上遗漏的要求。 |

拿一道原创求导练习来说：

> **你：** f(x) = x³ − 2x，我算出 f′(x) = 3x² + 2。
>
> **Coach：** 第一项求导没问题。先检查 −2x 这一项的符号，单独写出它的导数。

说完就等你做，不会替你编出“我懂了”，也不会马上塞来一整套题。

这一步改对后，它会给**一道同类新题，先不给提示**。你能独立做对，
再换一个情境或表达方式，看看你还能不能用出来。卡住时，提示会逐步增加；
到了第三级还不会，就拆出一个更小的基础步骤。

换个情境也能做对，说明这个具体问题有进展。后面再出错，不会抹掉之前已经
做对的其他部分；答对一题也不等于整章都会了。你明确指定的课程、知识点、
题型和难度都不会被擅自更改。

## 各科可以这样开始

```text
$ap-calculus-advisor 我在学 AP Precalculus。根据这份函数图像作答，带我练下一步。
$ap-calculus-advisor 我在学 AP Calculus AB。检查我的求导过程，从第一个错误开始带我改。
$ap-calculus-advisor 我在学 AP Calculus BC。根据这道级数收敛题的作答，决定我下一步该练什么。
$ap-psychology-advisor 这个概念的定义我会背，但不会用。请根据我的回答，每次带我练一题。
$ap-biology-advisor 请看我的图表解读和解释，判断是读数据出了错还是生物学机制没讲清，每次只带我做一步。
```

记得一起附上原题和你的作答。

## 用之前知道这几件事就够了

- **练习题是原创的。** 数学已有 96 道题，覆盖 32 类错误；没覆盖的地方可以
  另外出题。生物和心理学按需要出题。这不是完整题库，也不提供 AP Classroom 保密题。
- **答案什么时候看，由你决定。** Coach 默认先让你试；看过提示或答案后做对，
  不会算成“已经能独立完成”。
- **默认只记住当前对话。** 数学可以保存本地学习记录，但需要你明确提出，并指定
  仓库外的文件夹。生物和心理学只使用对话里的记录。
- **它是学习助手，也可能出错。** 技能包含适用于 GPT-6 Astra 等模型的指导。
  知识点编号检查通过，不代表讲解或评分一定正确。要按官方标准打分，
  还需要对应的原题和评分指南。

课程范围见上方各科的技能文件。想了解本地存档、运行检查或修改项目，
看[开发说明](./docs/development.md)。

## 许可证

[MIT](./LICENSE)。AP 是 College Board 的商标，本项目未获 College Board 认可。
