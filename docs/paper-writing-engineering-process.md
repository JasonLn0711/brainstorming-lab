# Paper Writing Engineering Process

這份規則適用於未來所有論文撰寫，不只適用於單一手稿。

核心原則：

```text
一篇論文只能保護一個主問題、一個主方法、一組主證據、一句主貢獻。
```

論文不是把做過的事情全部寫出來。論文的任務是讓陌生 reviewer 在有限時間內相信：問題重要、現有方法不足、方法合理、證據支撐主張、限制被誠實處理。

## First Principle

開始寫全文前，先回答一題：

```text
哪一個主張最值得被國際期刊保存？
```

其他材料都要服務這一句主張。若一段文字沒有讓主張更可信，就移到 appendix、supplement、future work，或刪掉。

以 cybercrime triage `v3.11` 類型手稿為例，主張可以壓成：

```text
Cybercrime triage 的 action plausibility 與 forensic reconstructability 是兩個不同性質；只看 action correctness 會高估後續可重建性。
```

所有材料都要回到這條線：

- synthetic dataset
- artifact packet
- graph inspection
- claim boundary
- restricted data protocol
- governance table
- source manifest
- public-safe design

## Evidence Chain

每篇 paper 都要形成一條證據鏈：

```text
Problem -> Gap -> Proposed idea -> Method -> Evidence -> Boundary -> Contribution
```

每一節只回答一個主要問題：

| Section | 必須回答的問題 |
| --- | --- |
| Abstract | 這篇 paper 一句話在做什麼？ |
| Introduction | 為什麼這個問題重要？ |
| Related Work | 現有研究漏掉什麼？ |
| Method | 你提出什麼可檢查的方法？ |
| Evaluation | 你如何驗證這方法？ |
| Results | 數據顯示什麼？ |
| Discussion | 這些結果代表什麼？ |
| Limitation | 什麼還不能宣稱？ |
| Conclusion | 讀者該記住哪一句話？ |

## Step 1: One-Sentence Claim

沒有這一句，不要開始寫全文。

格式：

```text
This paper shows that [main phenomenon] by proposing [main method] and validating it through [main evidence].
```

範例：

```text
This paper shows that cybercrime-triage action plausibility can diverge from forensic reconstructability by proposing bridge-constrained inspection and validating it through public-safe synthetic and artifact-packet stress tests.
```

這句會強迫你分清楚：

- 主現象是什麼
- 主方法是什麼
- 主證據是哪一組
- 哪些東西只是支援材料

## Step 2: Reviewer Question List

每篇 paper 先列 5 個 reviewer 會問的問題。

範例：

```text
1. What is reconstructability?
2. Why is action correctness insufficient?
3. How does bridge-constrained inspection work?
4. What public evidence supports the claim?
5. What claims are excluded?
```

全文的任務是回答這五題。若某節無法回答其中任何一題，它大概率不是 main text。

## Step 3: Contribution-to-Evidence Map

每個 contribution 都要能接到 method 與 evidence。

| Contribution | Method section | Evidence section | Claim boundary |
| --- | --- | --- | --- |
| Formalize reconstructability | Definitions | Trace-field examples | Not legal truth |
| Introduce bridge-constrained inspection | Algorithm / schema | Packet comparison | Not algorithmic superiority claim |
| Design public-safe evidence architecture | Evidence tiers | Synthetic + packet layers | Not field performance |
| Provide stress tests | Evaluation protocol | Result tables | Internal diagnostics only |
| Define claim-boundary controls | Claim ledger | Boundary table | No deployment / fraud-status claim |

沒有 evidence 的 contribution 必須降級成 discussion 或 future work。

## Step 4: Figure 1 First

先畫 Figure 1，再寫全文。

Figure 1 必須讓 reviewer 在 10 秒內知道 paper 做什麼：

```text
Problem
  -> Method object
  -> Inspection / evaluation process
  -> Evidence stack
  -> Boundary-controlled contribution
```

如果 Figure 1 畫不出來，代表主線還不清楚。

## Abstract Rule

Abstract 必須依序包含五個元素：

```text
1. problem
2. gap
3. proposed method
4. main result
5. contribution and boundary
```

第一句直接講現象，不要從大背景開始。

弱寫法：

```text
Digital forensics is important in modern cybercrime investigation.
```

強寫法：

```text
Cybercrime triage may produce plausible actions while preserving weak traces for later forensic reconstruction.
```

Abstract 裡最多保留三個主概念。其他術語放 Method 或 Definition section。

## Introduction Rule

Introduction 用六段模型：

| Paragraph | 功能 |
| --- | --- |
| 1 | 現實問題 |
| 2 | 現有方法不足 |
| 3 | 核心區分或新視角 |
| 4 | 本文方法 |
| 5 | 本文證據 |
| 6 | 貢獻列表 |

貢獻列表必須用動詞開頭：

- We formalize ...
- We introduce ...
- We design ...
- We provide ...
- We define ...

不要讓 reviewer 自己推理 novelty。要明講：

```text
The novelty is not [old technical component]. The novelty is [new scientific use, diagnostic framing, or evidence chain].
```

## Contribution Rule

Contribution 不是「我做了很多事」。

每個 contribution 必須同時滿足：

```text
1. 以前沒有被清楚處理
2. 本文提出可檢查的新東西
3. 後面有 evidence 支撐
```

弱寫法：

```text
A public-safe reconstructability diagnostic framework.
```

強寫法：

```text
We define a public-safe reconstructability diagnostic framework that evaluates whether evidence, provenance, authority, review, decision-hinge, and claim-boundary fields remain connected to the selected action.
```

強寫法比較好，因為它說清楚 scientific object、檢查對象、可驗證的欄位。

## Related Work Rule

Related Work 不是資料庫整理。它的任務是建立精準落差：

```text
別人解決了什麼 -> 還缺什麼 -> 本文補上什麼
```

建議用四類文獻加一張 gap closure table：

| Prior work family | What it solves | Remaining gap | This paper | Claim boundary |
| --- | --- | --- | --- | --- |
| Digital forensics traceability | Evidence handling and provenance | Action reconstructability | Trace-field inspection | Not legal sufficiency |
| AI-assisted triage | Classification / ranking / routing | Later inspection | Reconstructability diagnostic | Not operational deployment |
| Graph-based investigation modeling | Relation and path representation | Bridge sufficiency | Bridge-constrained graph inspection | Not algorithmic novelty |
| Public-safe restricted-data research | Reproducible public layers | Field-data release limits | Synthetic + artifact-packet architecture | Not field performance |

## Method Rule

Method section 要像工具，不要像理念。

建議順序：

```text
1. Trace-field schema
2. Diagnostic definitions
3. Algorithm or procedure
4. Labels / outputs
5. Failure modes
6. Reproducibility path
```

先給 schema，再給 definition，再給 algorithm。

錯誤順序：

```text
definition -> governance -> graph math -> evidence tier -> result
```

正確順序：

```text
what fields exist -> what the method checks -> how labels are assigned -> what failure looks like
```

每個新術語都要回答四題：

```text
What is it?
How is it checked?
When does it fail?
Where is it used in results?
```

## Algorithm Rule

若方法可以程序化，就寫成 Algorithm。

範例：

```text
Algorithm 1: Bridge-Constrained Reconstructability Inspection

Input:
- released trace fields
- evidence-side nodes
- action-side nodes
- required bridge fields
- unsupported-claim flags

Steps:
1. Build a trace graph from released fields.
2. Identify evidence-side nodes and selected-action nodes.
3. Search for paths connecting evidence-side nodes to action-side nodes.
4. Require the path to pass through at least one sufficient bridge.
5. Check required support fields:
   provenance, authority, review, decision hinge, evidence-to-action map, claim boundary.
6. Downgrade the trace if required support is missing or unsupported claims are present.
7. Assign a diagnostic state:
   reconstructable, partially reconstructable, insufficient, or unsafe gap.
```

這會讓 reviewer 知道 paper 不是只在談 philosophy。

## Evidence Architecture Rule

Evidence section 要回答：

```text
哪一層 evidence 支撐哪一種 claim？
哪一層 evidence 不能支撐哪一種 claim？
```

範例：

| Layer | Can support | Cannot support |
| --- | --- | --- |
| Restricted operational records | Future authorized aggregate diagnostics | Current public result |
| Public synthetic layer | Mechanism stress test | Field performance |
| Public artifact packets | Schema transfer behavior | Raw image measurement |
| Claim ledger | Boundary discipline | Empirical validation |

Data governance 放在方法後面。Reviewer 先需要知道你做什麼，再判斷你是否越界。

## Evaluation Rule

Evaluation 不要展示所有表格。它要回答：

```text
哪個實驗測試哪個 claim？
```

每個 experiment 都要有一個明確問題。

範例：

```text
Experiment 1:
Can action agreement remain high when audit or provenance support is weakened?

Experiment 2:
Does action-only inspection over-credit traces with missing bridge support?
```

每個 Result 用三層寫：

```text
1. What happened?
2. Why does it matter?
3. Which claim does it support?
```

弱寫法：

```text
The action-only method has reconstructability 1.000 and false reconstructable rate 0.250.
```

強寫法：

```text
The action-only baseline marks all packets as reconstructable, including negative-control packets with missing bridge elements. This produces a false reconstructable rate of 0.250. Strict bridge-constrained inspection lowers reconstructability to 0.750 and removes false reconstructable cases. This supports the paper's main claim: an action string alone can overstate forensic trace sufficiency.
```

## Discussion Rule

Discussion 不要重複結果。它要回答：

```text
這些結果改變了我們怎麼理解這個領域？
```

建議三段：

| Paragraph | 功能 |
| --- | --- |
| Scientific implication | action-level correctness 是否足夠？ |
| Investigative / practical implication | 實務使用者會承擔什麼風險？ |
| Methodological implication | 以後 evaluation 應該多檢查什麼？ |

## Limitation Rule

Limitation 要誠實，但不要自我削弱。

弱寫法：

```text
This study has many limitations and does not prove operational validity.
```

強寫法：

```text
The study is bounded by design. The public evidence layers test mechanism behavior and schema transfer under public-safe constraints. They do not estimate operational field performance, practitioner agreement, legal sufficiency, or fraud-status truth.
```

每個 limitation 都要接 future validation path：

| Limitation | Future validation |
| --- | --- |
| Synthetic labels | Authorized restricted aggregate diagnostic |
| Author-defined bridge rules | Practitioner trace-readability study |
| Public packet summaries | Broader public forensic corpus mapping |
| No operational evaluation | Controlled field-facing aggregate study |

## Conclusion Rule

Conclusion 不只是摘要。它要讓 reader 帶走一句話。

格式：

```text
This paper shows that [main distinction]. By [method] and [evidence], it provides [contribution] under [boundary].
```

最後一句可以回到核心問題：

```text
The central question is not only whether the action can be selected, but whether the remaining trace can still be reconstructed.
```

## Sentence-Level Rules

每段第一句要有主張。

弱寫法：

```text
There are many issues in cybercrime triage. Some systems use AI. Some systems use rule-based methods. In many cases, data are restricted.
```

強寫法：

```text
Restricted-data settings create a reproducibility problem for cybercrime-triage research.
```

每段只處理一個功能：

- 定義問題
- 說明缺口
- 說明方法
- 報告結果
- 解釋意義
- 說明限制

避免連續抽象名詞。

弱寫法：

```text
The framework provides governance-supported reconstructability-aware diagnostic evaluation for public-safe forensic research constraints.
```

強寫法：

```text
The framework checks whether a selected action can still be traced back to evidence, provenance, authority, review, and claim-boundary fields.
```

## Figure And Table Rules

第一張圖一定要是 paper overview：

```text
problem -> method -> evaluation -> evidence -> boundary-controlled contribution
```

Method figure 呈現 input、process、output。

Result table 要小而有力。每張 table 只回答一個問題。

每個 table 前後都要有 take-away sentence：

```text
Table X shows that [result]. This supports [claim] because [reason].
```

## Boundary Rule

Claim boundary 很重要，但不能主導 main text。

建議比例：

```text
70% method + evidence
20% interpretation
10% boundary
```

詳細 claim ledger、role table、defense table、exclusion list 放 appendix，除非它們是理解 method 的必要條件。

## Reviewer Simulation

投稿前，逐一回答：

| Reviewer question | Manuscript must answer |
| --- | --- |
| 這篇到底解決什麼問題？ | 第一頁出現 one-sentence problem |
| 和一般 classification / detection 有什麼不同？ | Introduction 定義核心區分 |
| 你有什麼 evidence？ | Contribution-to-evidence map 可追 |
| 方法怎麼重現？ | Method 有 schema、algorithm、input/output |
| 你不能宣稱什麼？ | Limitation 與 claim boundary 清楚 |

## Final Checklist

### First Page

| Check | Pass |
| --- | --- |
| 第一段直接講核心問題 |  |
| 第一頁出現 main gap |  |
| 第一頁出現 proposed method |  |
| 第一頁出現 contribution list |  |
| reviewer 能在 90 秒內知道本文價值 |  |

### Contribution

| Check | Pass |
| --- | --- |
| 每個 contribution 用動詞開頭 |  |
| 每個 contribution 可驗證 |  |
| 每個 contribution 有對應結果 |  |
| 沒有把 future work 寫成 contribution |  |
| 沒有把 engineering cleanup 寫成 scientific novelty |  |

### Method

| Check | Pass |
| --- | --- |
| method 能被陌生人重現 |  |
| 有 schema |  |
| 有 algorithm 或 procedure |  |
| 有 clear input/output |  |
| 有 failure rule |  |

### Results

| Check | Pass |
| --- | --- |
| 每個 table 有 take-away sentence |  |
| 每個 result 支撐 main claim |  |
| 沒有展示和主張無關的表格 |  |
| 數字被解釋成 scientific / forensic implication |  |
| 沒有 overclaim |  |

### Claim Boundary

| Check | Pass |
| --- | --- |
| synthetic result 的性質清楚 |  |
| restricted data 未公開的邊界清楚 |  |
| 避免 legal / fraud / deployment claim |  |
| boundary 放在適當位置 |  |
| main text 沒有被防衛文字壓過 |  |

## Default Revision Order

當一篇草稿材料太多、主線不夠集中時，依序處理：

1. 重寫 one-sentence claim。
2. 重寫 Abstract 成 problem-gap-method-result-boundary。
3. 重寫 Introduction 前兩頁成六段模型。
4. 把 contribution list 改成動詞句。
5. 新增 Figure 1 overview。
6. 把 definitions 集中到 Method。
7. 把核心方法寫成 Algorithm 1。
8. 建立 evidence architecture table。
9. 把 Results 壓成三個 main findings。
10. 把 claim ledger、role table、defense table 後移到 Appendix。
11. 把 Conclusion 收束成一句核心觀點。

## Main Text vs Appendix

Main text 是刀，appendix 是倉庫。

Main text 只保留：

- 讓 reviewer 理解主問題的內容
- 讓 reviewer 檢查主方法的內容
- 直接支撐主 claim 的 evidence
- 必要 claim boundary

Appendix 放：

- 詳細 claim ledger
- long role table
- supplementary examples
- robustness table
- implementation detail
- defensive boundary catalog

## Submission Engineering / PaperOps

Manuscript repo 的 `npm run ready` 應該被視為本機 release gate，不是投稿動作。

`npm` 在這裡的角色是讀取 `package.json` 裡的 `scripts`，把 LaTeX build、claim check、voice check、portal packet check、artifact check、whitespace check 等流程串成可重跑的本機檢查。

`portal` 指期刊投稿網站；`portal:check` 或 `portal:dryrun` 只應檢查本機為投稿網站準備的 mapping、runbook、declaration、file list、deviation log，不應登入外部系統或送出投稿。

一個 PaperOps-ready repo 應該至少保護：

- submission state：`draft -> internal-review -> pre-submission -> portal-ready -> submitted -> revision -> camera-ready`
- artifact manifest：記錄 manuscript、title page、figures、supplementary、cover letter、declarations 的 hash、大小、來源命令與時間
- portal dry run：檢查 title、abstract、keywords、author metadata、funding、COI、AI-use declaration、PDF size、supplementary list
- reviewer redteam：找 overclaim、unsupported causal language、missing baseline、ethical ambiguity、synthetic/public boundary confusion
- deviation log：記錄每個刻意例外與不一致為什麼被接受

Boundary：本機 automation 可以準備、檢查、稽核 submission packet；最後登入 portal、預覽、按 submit 必須是人類明確確認。

## Reusable Prompt For Future Drafting

```text
Please rewrite this manuscript as a one-claim journal paper.

Use this structure:
1. one main problem
2. one main gap
3. one main method
4. one main evidence stack
5. one contribution statement

Before revising, produce:
- one-sentence claim
- reviewer question list
- contribution-to-evidence map
- main-text vs appendix split

Then revise:
- Abstract: problem-gap-method-result-boundary
- Introduction: six paragraphs
- Method: schema, definitions, algorithm, labels, failure modes
- Results: result -> interpretation -> supported claim
- Limitation: limitation -> future validation
- Conclusion: one remembered sentence
```
