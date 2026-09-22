# Expert Review: Data, Benchmark, And Experiment Design

Date recorded: 2026-06-01

Status: expert methodology guidance recorded verbatim from user-provided review.

## Full Expert Review

如果我們要做這樣的研究，我們要使用什麼樣的資料來做研究，是使用公開資料集嗎？還是使用自己的資料比較好呢？而我們的摘要的效果以及能力，是否要使用某些以及被公認可以作為評分標準的 benchmark 呢？我們在實驗以及研究的設計上，該如何設計呢？請詳細且具體的說明，並且完整給我們答覆與分析。

專家建議：
我的建議：**第一篇主實驗用公開資料集；自有資料只做 case study。**

原因很硬：公開資料集讓 reviewer 可以重現、比較、質疑；自有資料雖然更貼近真實會議與決策場景，但容易被卡在隱私、標註偏差、資料不可公開、倫理審查、不可比較。第一篇若主張方法學創新，核心證據要站在公開 benchmark 上。自有資料適合第二階段，證明這套 schema 和 compression objective 能轉移到真實工作流。

你們目前的研究題目也不該被設計成「摘要 benchmark」。更精準是：

```text
在固定 token budget 下，provenance-preserving compressed evidence graph packet
是否能讓 <10B 小模型產生更少 unsupported claims、
保留更多 evidence lineage、
並維持更穩定的 decision label？
```

這個問題不能只用 ROUGE、BERTScore 之類摘要指標回答。那些可以放 secondary。主指標必須是 evidence discipline、provenance retention、unsupported-claim rate、decision stability。

---

## 一、資料策略：三層資料，不要只選一種

最好的設計是三層：

```text
Layer 1: 公開資料集
→ 主實驗、主要量化證據、可重現性

Layer 2: controlled synthetic / semi-synthetic stress set
→ 測壓縮機制、反證保留、干擾節點、label flip

Layer 3: 自有資料
→ 外部效度、真實場景展示、case study
```

第一篇 paper 的主結論應該只靠 Layer 1 + Layer 2。Layer 3 可以放在 appendix 或 pilot case，除非你們願意公開資料或公開足夠完整的匿名化標註。

---

## 二、公開資料集 vs 自有資料

| 資料來源 | 優點 | 風險 | 建議用途 |
| --- | --- | --- | --- |
| 公開 claim / evidence 資料集 | 可重現、已有 gold label、已有 evidence span 或 rationale | 不一定像會議紀錄；資料形態較乾淨 | 第一篇主實驗 |
| 公開 meeting summarization 資料集 | 貼近長會議紀錄，有 transcript / minutes / query-summary | provenance、decision boundary、uncertainty 通常不足，需要自己補標註 | 第二實驗或外部 domain |
| 自有會議 / 醫療 / 詐騙資料 | 最貼近你們真正應用；決策、風險、責任歸屬明確 | 隱私、IRB、不可公開、標註偏差、reviewer 難重現 | case study 或第二篇 |
| synthetic graph benchmark | 可控變因，能測壓縮比、反證、干擾、路徑長度 | reviewer 可能嫌 toy | ablation / stress test |

我會這樣切：

```text
第一篇：
public scientific claim audit + small controlled stress set

第二篇：
public meeting / public cyber evidence + stronger graph schema

第三篇：
自有資料或 high-stakes workflow external validation
```

不要一開始就用自己的會議紀錄當主資料。那會讓研究看起來像產品內部評估，而不是可被國際期刊或會議審查的科學實驗。

---

## 三、第一篇最適合的公開資料集

### 1. SciFact：第一候選

SciFact 很適合你們的第一篇，因為它本來就是 scientific claim verification：claim、evidence-containing abstracts、support/refute labels、rationales。這正好可以轉成 claim-centered evidence graph。資料規模約 1.4K expert-written scientific claims，且有 evidence/rationale 標註，足以做 pilot 與主實驗。([ACL Anthology][1])

適合用途：

```text
claim → source abstract → evidence span → support/refute decision
```

你們可以把每筆資料轉成：

```text
Claim node
Evidence-span node
Source-paper node
Concept node
Method/result node
Lineage edge
Evidence relation edge
Uncertainty / limitation node
```

優點：乾淨、公開、審稿人容易理解。

缺點：它不像會議紀錄，少了 speaker、action item、decision owner、deadline。這沒關係。第一篇先證明核心機制。

---

### 2. FEVEROUS：第二候選，適合測 text + table provenance

FEVEROUS 有 87,026 verified claims，每個 claim 都有 sentence 或 table cell 作為 evidence，並標註 support / refute / not enough information。它比 SciFact 更適合測 structured evidence、table provenance、mixed evidence。([ACL Anthology][2])

適合用途：

```text
claim → text evidence / table-cell evidence → verdict
```

如果你們想證明「knowledge graph packet 不只是 text chunk」，FEVEROUS 很好。因為 table cell、sentence、page、section 本來就可以形成 graph。

缺點：Wikipedia domain 比 scientific decision support 弱一點。它比較像 factual verification，不像 expert decision support。

---

### 3. Qasper：適合 full-paper evidence QA

Qasper 是 research paper QA dataset，包含 5,049 questions over 1,585 NLP papers，而且答案有 supporting evidence。這很適合你們第二階段，因為它比 SciFact 更接近「長文件內找 evidence，產生 bounded answer」。([ACL Anthology][3])

適合用途：

```text
question → full paper sections → supporting evidence → answer
```

它可以測：

```text
long-document evidence preservation
citation lineage
answer grounding
small-model context construction
```

缺點：比 SciFact 複雜。第一個 2–4 週 pilot 不要直接從 Qasper 開始。

---

### 4. PubMedQA：適合 decision label，但 provenance 較弱

PubMedQA 是 biomedical research QA，任務是根據 PubMed abstract 回答 yes / no / maybe。它有 1K expert-annotated examples，另有 unlabeled 和 artificially generated instances。([ACL Anthology][4])

適合用途：

```text
question → abstract → yes / no / maybe
```

它對 decision stability 很好，因為 label 空間清楚。但它的 evidence span / provenance 結構不如 SciFact、FEVEROUS、Qasper 直接。

建議：當作第二資料源，不要當第一主資料。

---

## 四、如果一定要貼近「會議紀錄摘要」

可以用 QMSum 或 MeetingBank，但我不建議第一篇就把它當主實驗。

QMSum 是 query-based multi-domain meeting summarization benchmark，有 1,808 query-summary pairs over 232 meetings，涵蓋 academic meetings、product meetings、committee meetings。它很適合測「針對會議問題產生摘要」，也比一般 generic summarization 更接近 decision support。([ACL Anthology][5])

MeetingBank 是 city council meeting summarization benchmark，包含 1,366 meetings、3,579 小時以上影片、transcripts、meeting minutes、agenda、metadata；平均 transcript 超過 28K tokens。它非常適合長會議紀錄，但它不是天然的 provenance-preserving decision benchmark。你們需要自己補標註 decision、action item、evidence span、speaker role、agenda linkage。([MeetingBank][6])

所以我會這樣安排：

```text
第一篇：
SciFact / FEVEROUS
→ 證明 evidence graph packet 的方法學

第二實驗：
QMSum / MeetingBank
→ 證明方法可轉移到長會議紀錄

自有會議資料：
→ 最後做 case study
```

會議資料的問題不是沒有資料，而是 benchmark 指標不夠對應你們的研究物件。QMSum / MeetingBank 的 reference summary 可以評摘要相似度，但不能直接評「壓縮後是否保留 provenance、uncertainty、反證、decision boundary」。

---

## 五、是否要使用公認 benchmark？

要。但不能只用單一 benchmark。

這個方向目前沒有一個完全對應的標準 benchmark。你們要做的是：

```text
使用公認公開資料集作為底座
+
建立你們自己的 derived benchmark / evaluation protocol
+
用既有 metric 支撐部分面向
+
新增專屬 metric 評估 provenance 與 decision stability
```

也就是：

```text
不是發明一個完全自說自話的 benchmark。
也不是硬套 ROUGE / BERTScore。
```

正確做法是建立一個 derived benchmark，例如：

```text
PB-EGP-50 pilot
Provenance-Bounded Evidence Graph Packet Benchmark

資料來源：
SciFact / FEVEROUS / Qasper

每筆資料：
claim / question
source document
gold evidence span
gold decision label
candidate evidence graph
compressed packet
model output
audit annotation
```

這樣 reviewer 可以接受，因為原始資料來自公認資料集，新增的 graph packet schema 和 metric 是你們的 contribution。

---

## 六、哪些 benchmark / metric 可以用？

### 1. 摘要相似度：只能當 secondary

ROUGE 是傳統摘要自動評估方法，主要看 n-gram overlap。它可以報，但不能作為你們主指標。([ACL Anthology][7])

BERTScore 用 contextual embeddings 評估生成文字與 reference 的語意相似度，比 ROUGE 對 paraphrase 友善，但它仍然不能保證 evidence support。([arXiv][8])

SummEval 重新評估多種 summarization metrics，並把 human judgments 放入一致的比較框架；如果你們要寫 meeting summarization extension，可以引用它作為摘要評估背景。([ACL Anthology][9])

結論：

```text
ROUGE / BERTScore / summary relevance
可以報
不能當主結論
```

---

### 2. Factual consistency：可以作為輔助主軸

QAFactEval 是 QA-based factual consistency metric，用問題生成與回答比對來評摘要是否忠實於來源。([ACL Anthology][10])

SummaC 是 NLI-based factual consistency benchmark / method，專門處理 summary 是否和 source document 一致。([ACL Anthology][11])

AlignScore 用 unified alignment function 評估不同任務中的 factual consistency。([ACL Anthology][12])

FActScore 把長生成拆成 atomic facts，再計算有多少 atomic facts 被可靠來源支持。這個特別適合你們，因為 unsupported-claim rate 可以參考 FActScore 的 atomic-fact 概念。([ACL Anthology][13])

結論：

```text
FActScore-style atomic claim audit
+
QAFactEval / SummaC / AlignScore
```

可以支撐你們的 factuality 評估。

---

### 3. Attribution / citation：很重要

AIS，也就是 Attributable to Identified Sources，是評估 NLG output 是否能被指定來源驗證的框架。這和你們的 provenance-preserving 方向高度相關。([ACL Anthology][14])

ALCE 是 citation evaluation benchmark，要求系統檢索 supporting evidence 並產生帶 citation 的答案，評估 fluency、correctness、citation quality。([ACL Anthology][15])

Ref-Long 是 2025 ACL 的 long-context referencing benchmark，專門測 long-context model 是否能正確引用長文本中的特定位置。這對你們很有參考價值，因為你們的主張是「小模型在壓縮 graph packet 上也能維持 referencing discipline」。([ACL Anthology][16])

結論：

```text
citation precision
citation recall
source-lineage preservation
long-context referencing accuracy
```

這些要比 ROUGE 更核心。

---

### 4. RAG faithfulness：可以當輔助比較

RAGAS 是 RAG pipeline 的 reference-free evaluation framework，評估 retrieval augmented generation 的多個面向。([ACL Anthology][17])

ARES 針對 RAG 系統評估 context relevance、answer faithfulness、answer relevance，並用 synthetic training data 訓練 lightweight LM judges。([ACL Anthology][18])

RAGTruth 是 RAG hallucination corpus，有約 18,000 naturally generated responses，並有人工作 word-level hallucination annotation。([ACL Anthology][19])

這些可以用來對照你們和一般 RAG / GraphRAG 的差異，但不能取代你們自己的 provenance retention metric。

---

### 5. Long-context benchmark：只能當背景，不是主實驗

LongBench 是 bilingual multi-task long-context benchmark，涵蓋 single-doc QA、multi-doc QA、summarization、few-shot、synthetic tasks、code completion。([ACL Anthology][20])

LongBench v2 更強調深層 long-context reasoning，contexts ranging from 8K to 2M words，包含 503 challenging multiple-choice questions。([ACL Anthology][21])

SummHay 是針對 long-context LLMs 和 RAG systems 的挑戰式 summarization benchmark，要求系統從 haystack documents 中找出 repeated insights 並引用來源。([arXiv][22])

這些可以拿來說明「長 context 不等於理解」，也可做 later benchmark。但你們第一篇不是 long-context leaderboard paper。

---

## 七、你們應該建立的核心評分指標

第一篇的 primary metrics 應該是這些。

### 1. Decision correctness

模型輸出是否符合 gold label。

例如：

```text
supported / refuted / insufficient / mixed
yes / no / maybe
escalate / monitor / insufficient evidence
```

對 SciFact / FEVEROUS，可以用 label accuracy、macro-F1。對 PubMedQA，可以用 yes/no/maybe accuracy。

---

### 2. Unsupported-claim rate

這是最重要指標之一。

做法：

```text
把模型回答拆成 atomic claims。
每個 atomic claim 判斷是否被 packet 或 source evidence 支持。
```

公式：

```text
Unsupported-claim rate =
unsupported atomic claims / total atomic claims
```

例子：

```text
模型回答：
“Study A proves that treatment X reduces mortality in elderly patients.”

atomic claims:
1. Study A studied treatment X.
2. Study A measured mortality.
3. Study A proves reduction.
4. Population was elderly patients.

如果來源只支持 1 和 2，不支持 3 和 4，
unsupported-claim rate = 2 / 4
```

這比「整段回答對不對」細很多。

---

### 3. Provenance retention

壓縮後是否保留 gold evidence 的 source lineage。

公式：

```text
Provenance retention =
retained gold evidence lineage items / total gold evidence lineage items
```

可以拆成：

```text
source_id retention
span_id retention
section / table / paragraph retention
citation-chain retention
primary-vs-secondary-source retention
```

最低限度要保留：

```text
source_id
span_id
source type
supporting text
lineage path
```

---

### 4. Citation lineage preservation

這和 provenance retention 類似，但更偏輸出端。

模型引用的來源是否真的支持它的 claim？

```text
Citation precision =
valid supporting citations / all cited sources

Citation recall =
answer claims with valid citations / answer claims requiring citations
```

你們可以參考 ALCE / AIS 的思路，但要加上 graph lineage。

---

### 5. Uncertainty preservation

壓縮後是否仍然保留不確定性。

例如：

```text
source says “may reduce”
packet says “reduces”
→ uncertainty lost

source says “association, not causation”
packet says “causes”
→ risk boundary lost
```

可以標註：

```text
low uncertainty
medium uncertainty
high uncertainty
conflicting evidence
insufficient evidence
temporal uncertainty
population mismatch
```

評分：

```text
uncertainty label macro-F1
ordinal agreement
human audit score 1–5
```

---

### 6. Decision stability

你們的核心題目叫 small-model decision stability，這個一定要測。

對同一筆資料做 perturbation：

```text
改變 evidence order
加入 irrelevant distractor nodes
刪除 redundant background nodes
改變 packet token budget
換一個等價 prompt
加入低權威來源
加入 counterevidence
```

看模型 label 是否翻轉。

公式：

```text
Label flip rate =
number of changed labels across perturbations / number of perturbation trials
```

或：

```text
Decision stability =
1 - label flip rate
```

這可以直接支撐你們的主 claim。

---

### 7. Counterevidence retention

如果原始 evidence graph 有反證，壓縮後是否保留？

公式：

```text
Counterevidence retention =
retained counterevidence nodes / total gold counterevidence nodes
```

這很重要。很多壓縮方法會留下支持路徑，把反對路徑刪掉，最後模型變得更自信、更危險。

---

### 8. Human audit time

請人類 reviewer 判斷模型答案是否有根據，需要多久？

```text
audit time = seconds needed to verify answer against source
```

這個指標很適合你們的 expert-support framing。好的 packet 不只是讓模型答對，也要讓人類更快查核。

---

### 9. Compression ratio / token budget

公式：

```text
Compression ratio =
original context tokens / packet tokens
```

但 compression ratio 不能單獨報。高壓縮率如果帶來 evidence loss，沒有意義。

主張應該是：

```text
在相同或更小 token budget 下，
保留更多 provenance，
減少 unsupported claims，
並維持 decision correctness。
```

---

## 八、第一個實驗：最小但有說服力的設計

我會設計成：

```text
Experiment 1:
Provenance-bounded evidence graph packets for scientific claim audit
```

### Domain

```text
scientific-paper claim audit
```

第一階段用 SciFact。第二階段補 FEVEROUS 或 Qasper。

---

### Data unit

每一筆 record 長這樣：

```json
{
  "record_id": "R001",
  "claim": "Claim text",
  "decision_question": "Is this claim supported by the evidence?",
  "allowed_labels": ["supported", "refuted", "insufficient", "mixed"],
  "source_documents": [
    {
      "source_id": "S001",
      "title": "...",
      "abstract_or_text": "...",
      "source_type": "primary_paper",
      "year": 2020
    }
  ],
  "gold_evidence_spans": [
    {
      "span_id": "S001_SENT_03",
      "text": "...",
      "relation_to_claim": "supports",
      "evidence_force": "direct",
      "uncertainty": "low"
    }
  ],
  "gold_label": "supported"
}
```

注意一點：**不要把 gold_label 直接放進模型輸入。**

這是很常見的實驗漏洞。你可以用 gold evidence 建 oracle upper bound，但主實驗不能讓 packet 直接洩漏答案。

---

### Graph schema

最小 graph schema：

```text
Node types:
- Claim
- EvidenceSpan
- SourceDocument
- Entity / Concept
- Method
- Result
- Limitation
- Uncertainty
- CounterEvidence

Edge types:
- mentions
- reports
- measures
- compares
- derived_from
- cites
- qualifies
- contradicts
- supports_candidate
- refutes_candidate
- source_lineage
```

第一篇不要把 schema 做太大。越大越像系統工程。

必備欄位：

```text
claim_id
source_id
span_id
span_text
source_type
source_date
lineage_path
candidate_relation
uncertainty_tag
counterevidence_flag
compression_reason
```

---

### Compression method

第一篇不要用複雜 RL 或 pheromone。用一個 reviewer 看得懂的 constrained budgeted compression。

輸入：

```text
candidate evidence graph G
task question q
token budget B
```

輸出：

```text
compressed evidence graph packet P_B
```

壓縮原則：

```text
Hard constraints:
- retain at least one source lineage path for each retained claim
- retain direct evidence spans before background nodes
- retain counterevidence if present
- retain uncertainty and limitation nodes
- retain source type and span id
- do not merge claims with different evidence force

Soft objectives:
- maximize task relevance
- maximize evidence coverage
- maximize source diversity
- minimize redundant background
- minimize token length
```

可以寫成簡單目標：

```text
maximize:
evidence_coverage
+ provenance_coverage
+ counterevidence_coverage
+ uncertainty_coverage
+ task_relevance
- redundancy

subject to:
packet_tokens <= B
```

實作可以先用 greedy selection。之後再做 ILP 或 learned compressor。

---

### Context conditions / baselines

Reviewer 會期待看到這些 baseline。

Must-have：

```text
B1. Raw text + SLM
原始 source text，直接給小模型。

B2. Equal-budget raw text + SLM
把 raw text 截到和 packet 同樣 token budget。

B3. Top-k retrieved text + SLM
用 BM25 或 embedding retrieval 取 top-k evidence snippets。

B4. Generic summary + SLM
先做一般摘要，再給小模型回答。

B5. Uncompressed graph neighborhood + SLM
把 claim 周圍 k-hop graph 全部轉成文字或 JSON。

B6. Random graph pruning + SLM
隨機刪 node/edge 到同樣 token budget。

B7. Centrality-based graph pruning + SLM
用 degree / PageRank / betweenness 取重要節點。

B8. Provenance-bounded compressed graph packet + SLM
你們的方法。
```

Strong baseline：

```text
B9. GraphRAG-style subgraph retrieval + SLM
```

GraphRAG 已經是成熟對照。Microsoft GraphRAG 的代表性工作是 query-focused summarization，用 graph 結構從 local 到 global 組織 retrieval / summarization；你們若不和 GraphRAG-style baseline 比，reviewer 會覺得差異不夠。([arXiv][23])

Upper bound：

```text
B10. Oracle evidence packet + SLM
只給 gold evidence spans + provenance。
```

Reference ceiling：

```text
B11. Larger LLM + same context
```

這不是 gold truth，只是能力上限參考。

---

### SLM task

每個模型必須輸出固定格式：

```json
{
  "decision_label": "supported/refuted/insufficient/mixed",
  "answer": "one short paragraph",
  "evidence_used": ["source_id:span_id"],
  "uncertainty_note": "...",
  "unsupported_or_unverified_parts": ["..."],
  "abstention": true
}
```

Prompt 必須強制 evidence boundary：

```text
You may only answer using the provided evidence packet.
If the evidence does not support the claim, answer insufficient.
Every factual claim must cite source_id:span_id.
Do not infer beyond the provided evidence.
```

小模型常常會忽略指令，所以這本身就是研究重點。

---

## 九、2–4 週 pilot 設計

這是最小可行版本。

```text
資料：
40 records

來源：
SciFact 為主
必要時補少量 FEVEROUS 作 insufficient / mixed cases

模型：
1–2 個 <10B SLM
1 個 larger LLM reference

context conditions：
raw text
top-k retrieved text
generic summary
uncompressed graph neighborhood
centrality-pruned graph
provenance-bounded packet

token budget：
1024 或 2048 tokens 固定

perturbation：
原始順序
evidence order shuffled
加入 distractor evidence

評估：
decision correctness
unsupported-claim rate
provenance retention
citation precision
uncertainty preservation
label flip rate
audit time
```

Pilot 的目標不是發 paper，而是回答三個問題：

```text
1. packet 是否真的降低 unsupported claims？
2. provenance 欄位是否真的被小模型使用？
3. 壓縮是否造成反證或 uncertainty 流失？
```

如果這三個答案不漂亮，不要急著擴大資料集。先修 schema。

---

## 十、正式第一篇 paper 的設計

### Dataset size

最低可投 workshop / short paper：

```text
50–100 records
```

比較像正式 NLP / IR / KG paper：

```text
200–500 records
```

我建議：

```text
Main:
300 SciFact / FEVEROUS records

External:
50 Qasper records

Optional:
30 QMSum / MeetingBank meeting records with manual provenance annotation
```

---

### Balanced sampling

不要隨機抽。要 stratified sample。

```text
supported: 25%
refuted: 25%
insufficient: 25%
mixed / uncertain / weak support: 25%
```

如果資料集原本沒有 mixed label，就自己建立 controlled mixed cases：

```text
supporting evidence + counterevidence
strong evidence + limitation
direct evidence + population mismatch
correlation evidence + causal claim
```

這些 mixed cases 很重要，因為它們最能測小模型是否 overclaim。

---

### Graph construction：兩條軌道

你們要避免 reviewer 說：

```text
你們只是把 gold evidence 包裝成 graph，然後模型照抄答案。
```

所以要做兩條軌道。

#### Track A: Oracle graph compression

用 gold evidence spans 建圖。

用途：

```text
測壓縮與 packet schema 的上限。
```

不能用來主張 end-to-end system 已經可部署。

#### Track B: Predicted graph compression

用 retrieval + extractor 建 candidate graph。

例如：

```text
BM25 / dense retrieval 找 candidate spans
NLI model 或小 LLM 判斷 candidate relation
entity / concept extraction 建輔助節點
compression method 選 packet
```

用途：

```text
測真實可用性。
```

第一篇至少要有 Track A。最好也有 Track B 的小規模結果。

---

### Ablation study

這是你們證明「不是 JSON prompt trick」的關鍵。

做這些 ablation：

```text
Full packet
完整 packet。

- provenance
移除 source_id / span_id / lineage。

- uncertainty
移除 uncertainty / limitation。

- counterevidence
移除反證。

- compression log
移除 retained_reason / dropped_reason。

- graph relation labels
只留文字，不留 edge type。

- source type
移除 primary / secondary / synthesis 標記。

- equal-token summary
同樣 token 數的普通摘要。
```

如果 Full packet 沒有明顯贏過 ablation，研究主張會變弱。

---

### Perturbation tests

每筆 record 做小型 stress test：

```text
P0: 原始 packet
P1: evidence order shuffled
P2: 加入 irrelevant distractor nodes
P3: 加入 low-authority related source
P4: 壓縮 budget 減半
P5: 移除 redundant background nodes
P6: prompt paraphrase
```

觀察：

```text
decision label 是否翻轉
citation 是否亂掉
unsupported claims 是否增加
uncertainty 是否消失
```

這就是 decision stability。

---

## 十一、評分流程

我建議用「自動 + 人工」混合。

### Automatic evaluation

可以自動計算：

```text
decision accuracy
macro-F1
token count
compression ratio
citation ID match
gold evidence span retention
label flip rate
```

可半自動計算：

```text
atomic claim extraction
FActScore-style support checking
QAFactEval / AlignScore factual consistency
RAGAS / ARES faithfulness
```

但 automatic metric 不可完全取代人工。

---

### Human audit

至少要做 blinded human audit。

每個輸出由兩位 annotator 評：

```text
1. decision label 是否正確
2. 每個 atomic claim 是否被 evidence 支持
3. citation 是否真的支持該句
4. uncertainty 是否被保留
5. 是否有 overclaim
6. 是否有 missed counterevidence
7. audit time
```

要報：

```text
inter-annotator agreement
Cohen's kappa 或 Krippendorff's alpha
adjudication procedure
```

如果沒有一致性，metric 本身站不住。

---

## 十二、最重要的 reviewer 風險與解法

### 風險 1：被說成普通 GraphRAG

解法：

```text
不要只報 answer accuracy。
一定要報 provenance retention、unsupported-claim rate、uncertainty preservation、decision stability。
```

GraphRAG survey 已經把 graph-based indexing、graph-guided retrieval、graph-enhanced generation 描述成成熟範圍；你們要避開「又一個 graph retrieval pipeline」。([arXiv][24])

---

### 風險 2：被說成 graph summary

解法：

```text
compression objective 不以節點數最小為主。
compression objective 以 evidence boundary preservation 為主。
```

你們不是在做：

```text
更短的 graph
```

你們在做：

```text
小模型可用的 bounded evidence substrate
```

---

### 風險 3：gold evidence 洩漏答案

解法：

```text
分 Oracle track 和 Predicted track。
清楚說 Oracle track 只測 compression upper bound。
主 claim 不建立在 oracle-only 結果上。
```

---

### 風險 4：LLM judge 不可信

解法：

```text
LLM judge 只能輔助。
主結果要有人類 audit subset。
```

至少人工審 20–30% outputs。Pilot 可以人工全審。

---

### 風險 5：自有資料不可公開

解法：

```text
自有資料只做 external validation。
公開主資料 + 公開 code + 公開 derived graph schema。
```

如果自有資料要變成主實驗，就要準備：

```text
de-identification protocol
ethics review / IRB statement
data access statement
annotation guideline
可公開的匿名樣本
```

---

## 十三、自有資料應該怎麼用？

自有資料很有價值，但不要第一篇主打。

你們可以把自有資料設計成：

```text
External Validity Case Study:
Long meeting / scam / medical-intake transcript decision packet
```

資料單位：

```json
{
  "meeting_id": "...",
  "transcript_segment": "...",
  "decision_question": "What decision was made about X?",
  "gold_decision": "...",
  "evidence_spans": [
    {
      "speaker": "A",
      "timestamp": "...",
      "text": "...",
      "role": "proposal/support/objection/decision"
    }
  ],
  "action_items": [
    {
      "owner": "...",
      "deadline": "...",
      "evidence_span": "..."
    }
  ],
  "risk_boundaries": ["..."],
  "uncertainty": ["..."]
}
```

這種資料可以展示你們的真正應用：

```text
會議逐字稿
→ decision / action / risk graph
→ compressed evidence packet
→ SLM decision memo
```

但它的 paper role 是：

```text
public benchmark 證明方法有效
private case study 證明場景重要
```

不要反過來。

---

## 十四、如果研究重心仍是「會議摘要」，該怎麼改？

如果你們最後想明確寫成 meeting summarization paper，那設計要改成：

```text
task:
query-based meeting decision summarization

input:
long transcript

output:
decision memo with cited transcript spans

primary metrics:
decision coverage
action-item correctness
speaker attribution accuracy
evidence-span recall
unsupported-claim rate
audit time
```

可用資料：

```text
QMSum:
query-based meeting summarization

MeetingBank:
long public city council meetings, transcripts, minutes, agenda
```

但你們需要自己加標註：

```text
decision span
speaker
agenda item
action item
owner
deadline
risk / objection
evidence support
```

這是一篇很好的第二篇 paper。第一篇不建議走這條，因為標註成本高，method proof 會被資料工程拖慢。

---

## 十五、建議的正式實驗矩陣

### Factors

```text
Data:
SciFact / FEVEROUS / Qasper

Model:
SLM-1
SLM-2
Larger reference model

Context condition:
raw text
equal-budget raw text
top-k text
generic summary
uncompressed graph
centrality-pruned graph
GraphRAG-style subgraph
provenance-bounded packet

Budget:
512
1024
2048 tokens

Perturbation:
none
shuffle
distractor
reduced budget
counterevidence stress
```

### Main comparison

最重要比較不是全部 pairwise，而是這三個：

```text
provenance-bounded packet
vs
generic summary

provenance-bounded packet
vs
top-k retrieved text

provenance-bounded packet
vs
uncompressed graph neighborhood under same token budget
```

如果你們贏不了 generic summary 和 top-k retrieved text，這個方向會很危險。

---

## 十六、統計分析

因為每個 record 都跑多個方法，這是 paired design。

建議：

```text
decision correctness:
McNemar test 或 paired bootstrap

unsupported-claim rate:
Wilcoxon signed-rank test / paired bootstrap

provenance retention:
paired bootstrap confidence interval

label flip rate:
paired comparison across perturbations

audit time:
Wilcoxon signed-rank test

effect size:
報 absolute difference，不只報 p-value
```

不要只報平均分數。要報 confidence interval。

例如：

```text
Unsupported-claim rate:
generic summary: 0.31
top-k text: 0.24
compressed packet: 0.14
paired bootstrap 95% CI: [-0.15, -0.05]
```

這樣 reviewer 比較容易信。

---

## 十七、第一篇 paper 的最低成功條件

最低限度，你們要證明：

```text
在相同 token budget 下，
provenance-bounded compressed graph packet
比 generic summary、top-k text、centrality-pruned graph
產生更低 unsupported-claim rate，
更高 provenance retention，
且 decision correctness 不下降。
```

更強的成功條件：

```text
在 perturbation 下，
packet 的 label flip rate 更低。
```

最強的成功條件：

```text
packet 讓人類 audit time 降低，
且仍保留 counterevidence 與 uncertainty。
```

---

## 十八、最小 pilot 的具體執行清單

### Week 1：資料與 schema

```text
選 40–50 records
建立 graph schema v0
寫 annotation guideline
定義 allowed labels
定義 unsupported claim rubric
```

資料建議：

```text
30 SciFact support/refute
10–20 FEVEROUS insufficient / mixed / table evidence
```

---

### Week 2：建 graph 與 packet

```text
把 source documents 切 evidence spans
建立 source_id / span_id
建立 claim-evidence graph
實作 greedy packet compressor
產生 512 / 1024 / 2048 token packets
產生 baselines
```

---

### Week 3：跑模型

```text
跑 1–2 個 <10B SLM
跑 1 個 larger reference model
固定 temperature = 0
每筆 record 跑 5–6 context conditions
輸出 JSON 格式
```

---

### Week 4：評估與錯誤分析

```text
人工審 output
拆 atomic claims
標 unsupported claims
算 provenance retention
算 citation precision / recall
算 label flip rate
整理 failure cases
```

Pilot 結束要做一個 go / no-go decision：

```text
Go:
packet 明顯降低 unsupported claims
且 provenance retention 明顯提升

Revise:
packet 有用，但模型不穩定或 uncertainty 不見

Stop / reframe:
top-k text + prompt 已經同樣好
或 generic summary 已經同樣好
```

---

## 十九、正式 paper 的建議結構

```text
Title:
Provenance-Bounded Evidence Graph Packets for Stable Small-Model Decision Support

Research question:
What graph information must be preserved during compression
for small language models to produce auditable evidence-bounded decisions?

Contributions:
1. Define evidence graph packet schema.
2. Define provenance-preserving compression objective.
3. Build derived benchmark from public claim/evidence datasets.
4. Compare packet against raw text, retrieved text, generic summary, uncompressed graph, graph pruning, and GraphRAG-style retrieval.
5. Evaluate correctness, unsupported claims, provenance retention, uncertainty preservation, decision stability, and audit time.
```

---

## 二十、最後決策

你們應該這樣做：

```text
Primary data:
公開資料集，SciFact + FEVEROUS 起步。

Secondary data:
Qasper 或 PubMedQA。

Meeting extension:
QMSum / MeetingBank，但要自己補 provenance / decision annotation。

Private data:
不要當第一篇主實驗。
當 external validation 或 later paper。

Benchmark:
沒有單一現成 benchmark 完全符合。
要建立 derived public benchmark。

Primary metrics:
unsupported-claim rate
provenance retention
citation lineage preservation
decision correctness
uncertainty preservation
decision stability

Secondary metrics:
ROUGE
BERTScore
QAFactEval
SummaC
AlignScore
FActScore-style factuality
RAGAS / ARES faithfulness
audit time
compression ratio

First pilot:
40–50 public records
6 baselines
1–2 small models
1 larger reference model
人工 audit
```

最核心一句話：

```text
第一篇不是證明「小模型摘要比較好」。
第一篇要證明「小模型在 provenance-preserving compressed evidence graph packet 上，
比在 raw text、summary、top-k text、一般 graph pruning 上，
更少越界、更可追溯、更穩定」。
```

這樣才會有研究辨識度。

[1]: https://aclanthology.org/2020.emnlp-main.609/?utm_source=chatgpt.com "Fact or Fiction: Verifying Scientific Claims"
[2]: https://aclanthology.org/2021.fever-1.1/?utm_source=chatgpt.com "The Fact Extraction and VERification Over Unstructured ..."
[3]: https://aclanthology.org/2021.naacl-main.365/?utm_source=chatgpt.com "A Dataset of Information-Seeking Questions and Answers ..."
[4]: https://aclanthology.org/D19-1259/?utm_source=chatgpt.com "PubMedQA: A Dataset for Biomedical Research Question ..."
[5]: https://aclanthology.org/2021.naacl-main.472/?utm_source=chatgpt.com "A New Benchmark for Query-based Multi-domain Meeting ..."
[6]: https://meetingbank.github.io/?utm_source=chatgpt.com "MeetingBank Dataset"
[7]: https://aclanthology.org/W04-1013/?utm_source=chatgpt.com "ROUGE: A Package for Automatic Evaluation of Summaries"
[8]: https://arxiv.org/abs/1904.09675?utm_source=chatgpt.com "BERTScore: Evaluating Text Generation with BERT"
[9]: https://aclanthology.org/2021.tacl-1.24/?utm_source=chatgpt.com "SummEval: Re-evaluating Summarization Evaluation"
[10]: https://aclanthology.org/2022.naacl-main.187/?utm_source=chatgpt.com "QAFactEval: Improved QA-Based Factual Consistency ..."
[11]: https://aclanthology.org/2022.tacl-1.10/?utm_source=chatgpt.com "Re-Visiting NLI-based Models for Inconsistency Detection ..."
[12]: https://aclanthology.org/2023.acl-long.634/?utm_source=chatgpt.com "AlignScore: Evaluating Factual Consistency with A Unified ..."
[13]: https://aclanthology.org/2023.emnlp-main.741/?utm_source=chatgpt.com "FActScore: Fine-grained Atomic Evaluation of Factual ..."
[14]: https://aclanthology.org/2023.cl-4.2/?utm_source=chatgpt.com "Measuring Attribution in Natural Language Generation ..."
[15]: https://aclanthology.org/2023.emnlp-main.398/?utm_source=chatgpt.com "Enabling Large Language Models to Generate Text with ..."
[16]: https://aclanthology.org/2025.acl-long.1162/?utm_source=chatgpt.com "Benchmarking the Long-context Referencing Capability of ..."
[17]: https://aclanthology.org/2024.eacl-demo.16/?utm_source=chatgpt.com "RAGAs: Automated Evaluation of Retrieval Augmented ..."
[18]: https://aclanthology.org/2024.naacl-long.20/?utm_source=chatgpt.com "ARES: An Automated Evaluation Framework for Retrieval- ..."
[19]: https://aclanthology.org/2024.acl-long.585/?utm_source=chatgpt.com "RAGTruth: A Hallucination Corpus for Developing ..."
[20]: https://aclanthology.org/2024.acl-long.172/?utm_source=chatgpt.com "LongBench: A Bilingual, Multitask Benchmark for Long ..."
[21]: https://aclanthology.org/2025.acl-long.183/?utm_source=chatgpt.com "LongBench v2: Towards Deeper Understanding and ..."
[22]: https://arxiv.org/abs/2407.01370?utm_source=chatgpt.com "A Challenge to Long-Context LLMs and RAG Systems"
[23]: https://arxiv.org/abs/2404.16130?utm_source=chatgpt.com "A Graph RAG Approach to Query-Focused Summarization"
[24]: https://arxiv.org/abs/2501.13958?utm_source=chatgpt.com "A Survey of Graph Retrieval-Augmented Generation for Customized Large Language Models"

