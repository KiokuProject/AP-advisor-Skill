[English](./README.md) | **日本語** | [简体中文](./README.zh-CN.md) | [繁體中文](./README.zh-TW.md) | [한국어](./README.ko.md) | [Deutsch](./README.de.md)

# AP Advisor Skills

問題と自分の解答を送ると、最初につまずいた箇所を見つけ、その一歩を直し、
解答の内容に応じて次の練習を選びます。

Codex で使う5つの学習スキルで、7つの AP 科目に対応しています。
英語、日本語、簡体字中国語、繁体字中国語、韓国語、ドイツ語で利用できます。

| インストールするスキル | 対応科目 |
| --- | --- |
| [ap-calculus-advisor](./ap-calculus-advisor/) | AP Precalculus、AP Calculus AB、AP Calculus BC |
| [ap-psychology-advisor](./ap-psychology-advisor/) | AP Psychology（心理学） |
| [ap-biology-advisor](./ap-biology-advisor/) | AP Biology（生物学） |
| [ap-csa-advisor](./ap-csa-advisor/) | AP Computer Science A（CSA） |
| [ap-csp-advisor](./ap-csp-advisor/) | AP Computer Science Principles（CSP） |

## はじめ方

必要な科目のインストールを Skill Installer に依頼してください。

```text
$skill-installer Install the skill at path ap-calculus-advisor from iyorixy/AP-advisor-Skill as ap-calculus-advisor.
$skill-installer Install the skill at path ap-psychology-advisor from iyorixy/AP-advisor-Skill as ap-psychology-advisor.
$skill-installer Install the skill at path ap-biology-advisor from iyorixy/AP-advisor-Skill as ap-biology-advisor.
$skill-installer Install the skill at path ap-csa-advisor from iyorixy/AP-advisor-Skill as ap-csa-advisor.
$skill-installer Install the skill at path ap-csp-advisor from iyorixy/AP-advisor-Skill as ap-csp-advisor.
```

インストール先として指定するのは各科目のフォルダーです。リポジトリのルートではありません。
表示されない場合は Codex を再起動してください。ローカルの検証スクリプトは
Python 3.10 以降の標準ライブラリだけで動作します。

問題、必要なグラフ・資料・コード、自分の解答を添えて依頼します。

```text
$ap-calculus-advisor AP Calculus AB を勉強しています。私の間違いに合わせて次の問題を選んでください。ヒントは一度に一つだけ。答えを見せる前に、自分で解かせてください。
```

まだ解いていなければ、科目と練習したい内容を伝えてください。Coach が1問出し、
解答を待ちます。Topic の番号を調べておく必要はありません。

## できること

| 目的 | 依頼の例 |
| --- | --- |
| 概念の理解・問題作成（Generate） | 「これを説明して、似た問題を答えなしで1問出して。」 |
| 解答の確認（Review） | 「私の解答で最初に間違えた箇所を教えて。」 |
| 学習の優先順位（Advisor） | 「この間違いから、次に練習すべきことを1〜3個選んで。」 |
| 解答ごとに調整する練習（Coach） | 「一歩ずつ教えて、私の間違いに合わせて次の問題を変えて。」 |

モード名を覚える必要はありません。途中で詳しい解説を求めたり、内容を変えたり、
Coach を終了したりできます。

## Coach の調整方法

7科目すべてで、**実際の間違いに応じて次の一歩を選びます**。
点数が低い、選択肢を間違えたという情報だけでは、原因を決めつけません。

| 解答に見られる問題 | 次に行うこと |
| --- | --- |
| 概念や規則の混同 | 短い比較や適用条件の確認を行います。 |
| 方法は正しいが計算を間違えた | その計算だけを直し、同程度の問題で確認します。 |
| グラフや図の読み違い | 意味を説明する前に、重要な情報を一つ読み取ります。 |
| 定義は正しいが場面に適用できない | 定義を具体的な状況と結びつけます。 |
| モデル・実験計画・論証に不足がある | 足りない関係、比較、理由を補います。 |
| コードの添字・ループ境界・オブジェクトの状態を誤った | 実行を一段階追うか、入力例で確かめます。 |
| 条件や解答の一部を見落とした | その要求だけを補います。 |

オリジナルの微分問題なら、次のように進みます。

> **あなた：** f(x) = x³ − 2x の導関数は f′(x) = 3x² + 2 です。
>
> **Coach：** 最初の項は合っています。−2x の符号に注目して、その項だけを微分してください。

ここで解答を待ちます。あなたの返事を作ったり、すぐに大量の問題を出したりしません。

直せたら、**同じ形式の新しい問題をヒントなしで1問**出します。独力で正解した後は、
状況や表現などを一つ変え、学んだことを応用できるか確認します。つまずけば段階的に
ヒントを増やし、第3段階でも難しければ、必要な基礎を小さな一歩に分けます。

応用問題の成功は、その課題での進歩を示します。1問の正解で単元全体の習得とはせず、
後の間違いで無関係な成功を取り消すこともありません。指定した科目、Topic、問題形式、
難易度は維持します。

## 科目別の依頼例

```text
$ap-calculus-advisor AP Precalculus の関数グラフについて、この解答から次の練習を選んでください。
$ap-calculus-advisor AP Calculus AB の微分です。最初の間違いから、一歩ずつ直すのを手伝ってください。
$ap-calculus-advisor AP Calculus BC の級数の収束問題です。この解答から次に練習することを決めてください。
$ap-psychology-advisor 定義は覚えましたが、場面に適用できません。私の答えを見て、1問ずつ教えてください。
$ap-biology-advisor グラフの読み取りと説明を見て、データの読み違いか、仕組みの説明不足かを確かめてください。一度に一歩だけお願いします。
$ap-csa-advisor Java の ArrayList で削除後に隣の要素を飛ばしてしまいます。コードを見てヒントを一つ出し、新しい問題で確認してください。
$ap-csp-advisor AP 擬似コードの実行を追った解答から、次の練習を選んでください。自分のコードを使って手続きの説明も練習したいです。
```

どの依頼にも、元の問題と実際の解答を添えてください。

## 利用上のポイント

- **練習問題はオリジナルです。** 数学には32種類の誤りを対象とした96問があり、
  未収録の内容は必要に応じて作成します。生物学、心理学、CSA、CSP も随時作成します。
  網羅的な問題集ではなく、AP Classroom の非公開問題は提供しません。
- **答えを見るタイミングは選べます。** Coach は通常、先に自分で解く機会を設けます。
  ヒントや解答を見て解けた問題を、独力での成功とは数えません。
- **記録は原則として会話内だけです。** 数学は、明示的な依頼とリポジトリ外の保存先が
  あればローカル記録を使えます。生物学、心理学、CSA、CSP は会話履歴のみを使います。
- **CSA と CSP は別々の枠組みに従います。** CSA は Fall 2025 の Java 枠組み、CSP は
  2026–27年度に適用される Fall 2023 の枠組みを使います。CSP では Create の練習と
  規則で認められたコード支援に対応し、動画・PPR・試験解答の個人作業要件も区別します。
- **モデルの学習支援を導くスキルであり、誤りは起こり得ます。** GPT-6 Astra などに
  対応する指針を含みます。Topic の検証だけでは解説や採点の正しさは保証できません。
  公式採点には、対応する問題と採点ガイドが必要です。

科目の詳細は上のリンクから各スキルを参照してください。ローカル記録、検証、実装の
詳細は[開発ノート（英語）](./docs/development.md)にあります。

## ライセンス

[MIT](./LICENSE)。AP は College Board の商標です。本プロジェクトは College Board の
承認を受けたものではありません。
