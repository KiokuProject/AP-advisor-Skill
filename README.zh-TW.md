[English](./README.md) | [日本語](./README.ja.md) | [简体中文](./README.zh-CN.md) | **繁體中文** | [한국어](./README.ko.md) | [Deutsch](./README.de.md)

# AP Advisor Skills

把題目和你的解題過程傳給它。它會幫你找出哪裡出了錯，帶你改好這一步，
再根據你的表現安排下一題。

這是五套給 Codex 用的 AP 學習技能，涵蓋七門課，支援英文、日語、簡體中文、
繁體中文、韓語和德語。

| 安裝哪個技能 | 可以學什麼 |
| --- | --- |
| [ap-calculus-advisor](./ap-calculus-advisor/) | AP Precalculus、AP Calculus AB、AP Calculus BC |
| [ap-psychology-advisor](./ap-psychology-advisor/) | AP 心理學 |
| [ap-biology-advisor](./ap-biology-advisor/) | AP 生物學 |
| [ap-csa-advisor](./ap-csa-advisor/) | AP Computer Science A (CSA) |
| [ap-csp-advisor](./ap-csp-advisor/) | AP Computer Science Principles (CSP) |

## 先用起來

在 Codex 中傳送對應科目的安裝指令，需要哪科就裝哪科：

```text
$skill-installer Install the skill at path ap-calculus-advisor from iyorixy/AP-advisor-Skill as ap-calculus-advisor.
$skill-installer Install the skill at path ap-psychology-advisor from iyorixy/AP-advisor-Skill as ap-psychology-advisor.
$skill-installer Install the skill at path ap-biology-advisor from iyorixy/AP-advisor-Skill as ap-biology-advisor.
$skill-installer Install the skill at path ap-csa-advisor from iyorixy/AP-advisor-Skill as ap-csa-advisor.
$skill-installer Install the skill at path ap-csp-advisor from iyorixy/AP-advisor-Skill as ap-csp-advisor.
```

安裝的是這些科目資料夾，不是整個儲存庫。裝好後如果沒顯示，可以重新啟動 Codex。
本機檢查指令碼需要 Python 3.10+，不需要額外安裝 Python 套件。

然後貼上題目、必要的圖表或材料，以及你已經寫出的步驟，例如：

```text
$ap-calculus-advisor 我在學 AP Calculus AB。請根據我的錯誤調整下一題，每次只給一個提示，先讓我自己做，不要直接公布答案。
```

還沒做題也沒關係。告訴它你學哪門課、想練什麼，它會先出一題，等你作答。
不需要先查好知識點編號。

## 它能幫你做什麼

| 你想做什麼 | 可以這樣說 |
| --- | --- |
| 學概念、要練習（Generate） | 「講講這個概念，再出一道類似題，先不要答案。」 |
| 檢查作答（Review） | 「看看我的過程，指出最先出錯的那一步。」 |
| 決定先學什麼（Advisor） | 「根據這些錯題，幫我選接下來最該練的 1–3 件事。」 |
| 邊做邊調整（Coach） | 「一步步帶我練，根據我怎麼錯來決定下一題。」 |

不用記這些模式名稱。練到一半想看完整講解、換知識點或者結束，直接說就行。

## Coach 怎麼根據錯誤調整

七門課都支援。核心很簡單：**錯在哪裡，就先練哪裡。**
它會看你的實際步驟；只有一個低分或錯誤選項，還不能確定原因。

| 你的作答出了什麼問題 | 它接下來怎麼帶你練 |
| --- | --- |
| 概念混了、規則用錯了 | 先做一個小對比，或檢查這條規則的適用條件。 |
| 方法對了，只是算錯 | 先修正那一步，下一題保持相近難度。 |
| 圖表或示意圖讀錯了 | 先讀出一個關鍵資訊，再解釋它的意思。 |
| 定義背對了，卻不會用在題目裡 | 先把定義和情境中的一個具體細節連起來。 |
| 建模、實驗設計或論證缺了一環 | 只補那個關係、對照或理由。 |
| 程式的索引、迴圈邊界或物件狀態出錯 | 先追蹤一步執行，或用一個輸入檢查錯誤。 |
| 漏看條件、漏答一部分 | 先補上遺漏的要求。 |

拿一道原創求導練習來說：

> **你：** f(x) = x³ − 2x，我算出 f′(x) = 3x² + 2。
>
> **Coach：** 第一項求導沒問題。先檢查 −2x 這一項的符號，單獨寫出它的導數。

說完就等你做，不會替你編出「我懂了」，也不會馬上塞來一整套題。

這一步改對後，它會給**一道同類新題，先不給提示**。你能獨立做對，
再換一個情境或表達方式，看看你還能不能用出來。卡住時，提示會逐步增加；
到了第三級還不會，就拆出一個更小的基礎步驟。

換個情境也能做對，說明這個具體問題有進展。後面再出錯，不會抹掉之前已經
做對的其他部分；答對一題也不等於整章都會了。你明確指定的課程、知識點、
題型和難度都不會被擅自更改。

## 各科可以這樣開始

```text
$ap-calculus-advisor 我在學 AP Precalculus。根據這份函數圖像作答，帶我練下一步。
$ap-calculus-advisor 我在學 AP Calculus AB。檢查我的求導過程，從第一個錯誤開始帶我改。
$ap-calculus-advisor 我在學 AP Calculus BC。根據這道級數收斂題的作答，決定我下一步該練什麼。
$ap-psychology-advisor 這個概念的定義我會背，但不會用。請根據我的回答，每次帶我練一題。
$ap-biology-advisor 請看我的圖表解讀和解釋，判斷是讀資料出了錯還是生物學機制沒講清，每次只帶我做一步。
$ap-csa-advisor 我的 Java ArrayList 迴圈刪除元素後漏掉了相鄰項。請看程式碼，每次給一個提示，再用新題檢查。
$ap-csp-advisor 根據我的 AP 偽程式碼追蹤安排下一步，再帶我練習用自己的程式碼解釋程序。
```

記得一起附上原題和你的作答。

## 用之前知道這幾件事就夠了

- **練習題是原創的。** 數學已有 96 道題，涵蓋 32 類錯誤；沒涵蓋的地方可以
  另外出題。生物、心理學、CSA 和 CSP 按需要出題。這不是完整題庫，也不提供 AP Classroom 保密題。
- **答案什麼時候看，由你決定。** Coach 預設先讓你試；看過提示或答案後做對，
  不會算成「已經能獨立完成」。
- **預設只記住目前對話。** 數學可以儲存本機學習紀錄，但需要你明確提出，並指定
  儲存庫外的資料夾。生物、心理學、CSA 和 CSP 只使用對話裡的紀錄。
- **CSA、CSP 分別按各自框架教學。** CSA 使用 Fall 2025 Java 框架；CSP 在
  2026–27 學年使用 Fall 2023 框架。CSP 支援 Create 練習與規則允許的程式協助，
  影片、PPR 和考場作答的獨立完成要求見其測評指南。
- **它是學習助手，也可能出錯。** 技能包含適用於 GPT-6 Astra 等模型的指引。
  知識點編號檢查通過，不代表講解或評分一定正確。要按官方標準評分，
  還需要對應的原題和評分指南。

課程範圍見上方各科的技能檔案。想了解本機存檔、執行檢查或修改專案，
看[開發說明](./docs/development.md)。

## 授權條款

[MIT](./LICENSE)。AP 是 College Board 的商標，本專案未獲 College Board 認可。
