[English](./README.md) | [日本語](./README.ja.md) | [简体中文](./README.zh-CN.md) | [繁體中文](./README.zh-TW.md) | **한국어** | [Deutsch](./README.de.md)

# AP Advisor Skills

문제와 풀이를 보내면 처음 틀린 부분을 찾고, 그 단계를 고친 뒤 실제 답변에 맞춰
다음 연습을 선택하도록 도와줍니다.

Codex에서 사용하는 5개 학습 스킬로 AP 7개 과목을 지원합니다.
영어, 일본어, 중국어 간체·번체, 한국어, 독일어로 사용할 수 있습니다.

| 설치할 스킬 | 지원 과목 |
| --- | --- |
| [ap-calculus-advisor](./ap-calculus-advisor/) | AP Precalculus, AP Calculus AB, AP Calculus BC |
| [ap-psychology-advisor](./ap-psychology-advisor/) | AP Psychology(심리학) |
| [ap-biology-advisor](./ap-biology-advisor/) | AP Biology(생물학) |
| [ap-csa-advisor](./ap-csa-advisor/) | AP Computer Science A(CSA) |
| [ap-csp-advisor](./ap-csp-advisor/) | AP Computer Science Principles(CSP) |

## 시작하기

필요한 과목을 Skill Installer에 설치해 달라고 요청하세요.

```text
$skill-installer Install the skill at path ap-calculus-advisor from iyorixy/AP-advisor-Skill as ap-calculus-advisor.
$skill-installer Install the skill at path ap-psychology-advisor from iyorixy/AP-advisor-Skill as ap-psychology-advisor.
$skill-installer Install the skill at path ap-biology-advisor from iyorixy/AP-advisor-Skill as ap-biology-advisor.
$skill-installer Install the skill at path ap-csa-advisor from iyorixy/AP-advisor-Skill as ap-csa-advisor.
$skill-installer Install the skill at path ap-csp-advisor from iyorixy/AP-advisor-Skill as ap-csp-advisor.
```

저장소 루트가 아닌 과목별 폴더를 설치합니다. 설치한 스킬이 보이지 않으면 Codex를
다시 시작하세요. 로컬 검증 스크립트는 Python 3.10 이상에서 표준 라이브러리만 사용합니다.

문제, 필요한 그래프·자료·코드, 본인의 풀이를 함께 보내세요.

```text
$ap-calculus-advisor AP Calculus AB를 공부하고 있어요. 제 실수에 맞춰 다음 문제를 골라 주세요. 힌트는 한 번에 하나씩 주고, 답을 보여 주기 전에 제가 풀게 해 주세요.
```

아직 풀지 않았다면 과목과 연습할 내용을 알려 주세요. Coach가 한 문제를 내고 답변을
기다립니다. Topic 번호를 미리 찾을 필요는 없습니다.

## 요청할 수 있는 도움

| 하고 싶은 일 | 요청 예시 |
| --- | --- |
| 개념 이해·연습 문제 만들기(Generate) | “이 개념을 설명하고 비슷한 문제를 답 없이 하나 내 주세요.” |
| 풀이 검토(Review) | “제 풀이에서 처음 틀린 단계를 찾아 주세요.” |
| 학습 우선순위 정하기(Advisor) | “이 오답들을 보고 다음에 연습할 것 1~3개를 골라 주세요.” |
| 답변에 맞춰 조정하며 연습하기(Coach) | “한 단계씩 도와주고, 제가 틀린 이유에 맞춰 다음 문제를 골라 주세요.” |

모드 이름을 외울 필요는 없습니다. 언제든 전체 해설을 요청하거나, 주제를 바꾸거나,
코칭을 끝낼 수 있습니다.

## Coach가 조정하는 방법

7개 과목 모두 **실제 풀이에서 드러난 오류에 따라 다음 행동을 선택합니다**.
낮은 점수나 틀린 선택지만으로 원인을 단정하지 않습니다.

| 풀이에서 드러난 문제 | 다음에 하는 일 |
| --- | --- |
| 개념이나 규칙을 혼동함 | 짧은 비교나 적용 조건을 확인합니다. |
| 방법은 맞지만 계산이 틀림 | 해당 계산을 고치고 비슷한 난이도를 유지합니다. |
| 그래프나 도표를 잘못 읽음 | 의미를 해석하기 전에 정보 하나를 정확히 읽습니다. |
| 정의는 알지만 상황에 적용하지 못함 | 정의를 상황의 구체적인 요소와 연결합니다. |
| 모델·실험 설계·논증에 빠진 부분이 있음 | 필요한 관계, 비교, 이유를 보완합니다. |
| 코드의 인덱스·반복문 경계·객체 상태를 잘못 판단함 | 실행 한 단계를 추적하거나 입력 하나로 확인합니다. |
| 조건이나 답변 항목을 빠뜨림 | 빠진 요구 사항만 먼저 완성합니다. |

직접 만든 미분 문제에서는 이렇게 진행할 수 있습니다.

> **학습자:** f(x) = x³ − 2x의 도함수를 f′(x) = 3x² + 2로 구했어요.
>
> **Coach:** 첫 항은 맞아요. −2x 항의 부호를 확인하고, 그 항만 미분해 보세요.

그다음 실제 답변을 기다립니다. 학습자의 답을 지어내거나 곧바로 문제 묶음을 주지 않습니다.

오류를 고치면 **같은 유형의 새 문제 한 개를 힌트 없이** 제시합니다. 독립적으로 맞히면
상황이나 표현 방식처럼 의미 있는 요소 하나를 바꿔 응용을 확인합니다. 막히면 힌트를
단계적으로 늘리고, 3단계 후에도 어렵다면 필요한 기초를 더 작은 단계로 나눕니다.

응용 문제의 성공은 해당 과제에서의 진전을 뜻합니다. 한 문제를 맞혔다고 단원 전체를
익혔다고 판단하지 않으며, 나중의 오류로 관련 없는 이전 성과를 지우지도 않습니다.
명시한 과목, Topic, 문제 유형, 난이도는 유지합니다.

## 과목별 요청 예시

```text
$ap-calculus-advisor AP Precalculus 함수 그래프 풀이를 보고 다음 연습을 골라 주세요.
$ap-calculus-advisor AP Calculus AB 미분 풀이에서 첫 오류부터 한 단계씩 고치도록 도와주세요.
$ap-calculus-advisor AP Calculus BC 급수 수렴 문제의 답변을 보고 다음 학습 내용을 정해 주세요.
$ap-psychology-advisor 정의는 외웠지만 적용이 어려워요. 제 답변을 보고 한 문제씩 도와주세요.
$ap-biology-advisor 그래프 해석과 설명을 보고 데이터 읽기 오류인지 생물학적 기작 설명의 문제인지 확인해 주세요. 한 번에 한 단계만 부탁해요.
$ap-csa-advisor Java ArrayList에서 삭제 후 인접한 항목을 건너뛰어요. 코드를 보고 힌트를 하나씩 준 뒤 새 문제로 확인해 주세요.
$ap-csp-advisor AP 의사 코드 실행을 추적한 답변에 맞춰 다음 연습을 골라 주세요. 제 코드로 프로시저를 설명하는 연습도 하고 싶어요.
```

각 요청에 원래 문제와 실제 풀이를 함께 첨부하세요.

## 알아둘 점

- **연습 문제는 직접 만듭니다.** 수학에는 32가지 오류 유형을 다루는 96개 문제가 있고,
  빈 부분은 필요에 따라 생성합니다. 생물학, 심리학, CSA, CSP도 필요할 때 문제를 만듭니다.
  전체 범위를 망라한 문제 은행이 아니며 AP Classroom 비공개 문제를 제공하지 않습니다.
- **답을 볼 시점은 직접 정합니다.** Coach는 보통 먼저 풀 기회를 줍니다. 힌트나 답을 보고
  맞힌 문제는 독립적인 성공으로 기록하지 않습니다.
- **기록은 기본적으로 대화 안에만 남습니다.** 수학은 명시적으로 요청하고 저장소 외부
  폴더를 지정하면 로컬 기록을 사용할 수 있습니다. 생물학, 심리학, CSA, CSP는 대화만 사용합니다.
- **CSA와 CSP는 각자의 교육과정 기준을 따릅니다.** CSA는 Fall 2025 Java 기준,
  CSP는 2026–27학년도에 적용되는 Fall 2023 기준을 사용합니다. CSP는 Create 연습과
  규정상 허용되는 코드 지원을 제공하며, 영상·PPR·시험 답변의 개별 작성 요건을 구분합니다.
- **모델의 학습 지원을 안내하는 스킬이며 틀릴 수 있습니다.** GPT-6 Astra 등에서 사용할
  지침이 포함되어 있습니다. Topic 검증만으로 설명이나 점수의 정확성을 보장하지 않습니다.
  공식 채점에는 해당 문제와 일치하는 채점 지침이 필요합니다.

과목별 범위는 위에 연결된 스킬에서 확인하세요. 로컬 기록, 검증, 구현에 관한 내용은
[개발 문서(영어)](./docs/development.md)에 있습니다.

## 라이선스

[MIT](./LICENSE). AP는 College Board의 상표입니다. 이 프로젝트는 College Board의
공인을 받지 않았습니다.
