# Expert Review: Second Narrowing For First Paper Design

Date recorded: 2026-06-01

Status: expert narrowing guidance recorded verbatim from user-provided review.

## Full Expert Review

判斷：**研究方向值得做，但目前設計還需要再收窄一次。**

你們現在的主軸已經有辨識度；真正危險的地方不是想法太普通，而是實驗設計太容易被 reviewer 說成：

```text
GraphRAG + JSON formatting + citation prompting
```

所以第一篇 paper 必須把貢獻壓到一個可驗證的核心：

```text
在相同 token budget 下，
provenance-bounded evidence graph packet
是否比 top-k text、generic summary、一般 graph pruning、context compression
更能降低 unsupported claims、保留 provenance、維持 decision stability？
```

這句話就是 paper 的主軸。其他東西先不要放進第一篇。

---

# 1. Primary framing

推薦 framing：

```text
Provenance-bounded evidence graph packet construction for stable small-model decision support
```

這比以下幾個名稱都好。

`Knowledge graph compression` 太危險。這會把你們拖進傳統 graph summarization / graph compression 的審稿標準：節點壓縮率、查詢保真、圖重建、儲存效率。你們真正研究的不是圖本身變小，而是壓縮後的 evidence substrate 是否仍能約束小模型的回答邊界。

`Trustworthy GraphRAG evaluation` 也不夠好。GraphRAG 已經有清楚既有框架，例如 graph-based indexing、graph-guided retrieval、graph-enhanced generation；Microsoft GraphRAG 也已經用 entity graph、community summaries、partial responses 來做 corpus-level query-focused summarization。你們若採用這個 framing，reviewer 會期待你們跟一整套 GraphRAG system 比較。([arXiv][1])

`Small-model decision stability` 是很好的 evaluation lens，但不適合作為唯一 framing。它容易讓人問：「這跟 KG 有什麼必然關係？」所以它應該放在 subtitle 或 evaluation section。

最好的結構是：

```text
Method object:
provenance-bounded evidence graph packet construction

Target model:
sub-10B small language models

Evaluation target:
decision stability + evidence discipline
```

建議 paper title 類型：

```text
Provenance-Bounded Evidence Graph Packets for Stable Small-Model Decision Support
```

或更偏 NLP / IR：

```text
Evidence-Preserving Graph Packet Construction for Auditable Small-Model Decisions
```

---

# 2. Scientific object

你們現在的 object 清楚、可研究、可投稿，但要補上兩個條件。

目前定義：

```text
Given a large evidence graph G, a task q, and a token budget B,
construct a compressed packet P_B such that P_B preserves task-relevant support paths,
source lineage, uncertainty, counterevidence, and decision boundaries needed by an SLM
to produce auditable answers.
```

這是好的，但正式 paper 應該寫成：

```text
Given:
- an evidence graph G;
- a task q;
- a token budget B;
- a target small model family M;
- an allowed answer space Y;

construct:
- a packet P_B;

such that:
- P_B fits B;
- P_B preserves task-relevant evidence paths;
- P_B retains provenance and uncertainty;
- P_B exposes counterevidence and risk boundaries;
- outputs generated from P_B are auditable against source spans.
```

你們要避免讓 `P_B` 看起來只是 JSON prompt。它必須是一個有 constraints、schema、objective、evaluation 的 object。

## 必須保留的 packet 欄位

你們列的六個是核心：

```text
source_span
support_relation
evidence_force
lineage_depth
uncertainty
counterevidence_flag
```

但 formal paper 至少要擴成四組欄位。

第一組是 source anchoring：

```text
source_id
source_type
source_span_id
source_span_text
source_offset / sentence_id / table_cell_id
source_date_or_version
source_authority_or_origin
```

`source_span` 不能只是文字。一定要有可重建的位置，例如 doc_id + sentence_id 或 table_id + cell_id。否則 provenance retention 會變主觀。

第二組是 evidence relation：

```text
claim_id
target_claim_text
support_relation
relation_polarity
evidence_force
scope_of_support
counterevidence_flag
conflict_group_id
```

`support_relation` 要非常小心。若它直接來自 gold label，就會洩漏答案。正式實驗要分成 oracle track 與 predicted track。主實驗應以 predicted relation 或 relation-agnostic evidence packet 為主；oracle relation 只能作 upper bound。

第三組是 boundary control：

```text
uncertainty_type
uncertainty_level
limitation_note
risk_boundary
abstention_condition
unsafe_inference_warning
```

這一組才是你們和一般 GraphRAG 最大差異。GraphRAG 通常強調找得到、合成得好；你們強調「不該說的東西不能說」。

第四組是 audit trail：

```text
lineage_path
lineage_depth
compression_operation
retained_reason
dropped_reason
dropped_counterevidence_warning
audit_reconstruction_pointer
```

`compression log` 很重要。沒有它，reviewer 很難判斷壓縮是否把不利 evidence 靜悄悄刪掉。

---

# 3. Data strategy

你們的資料策略大方向正確：**第一篇主實驗用公開資料集，自有資料只做 external validation 或 case study。**

SciFact 是合理第一候選。它是 scientific claim verification dataset，包含約 1.4K expert-written scientific claims，並有 evidence-containing abstracts、labels、rationales，剛好能轉成 claim-centered evidence graph。([ACL Anthology][2])

FEVEROUS 可以補 structured evidence，因為它有 87,026 verified claims，evidence 形式包含 Wikipedia sentences 和 table cells，label 包含 supports / refutes / not enough information。([arXiv][3])

但我會調整你們的正式 paper 資料組合。

## Pilot 可以用 SciFact + FEVEROUS

PB-EGP-50 用 SciFact + FEVEROUS 沒問題。這能快速測：

```text
text evidence
structured/table evidence
support/refute/insufficient
provenance reconstruction
```

## Formal paper 不建議只主打 SciFact + FEVEROUS

原因：兩者 domain 不一致。SciFact 是 scientific claim verification；FEVEROUS 是 Wikipedia fact verification。混在一起會讓 reviewer 問：

```text
你們到底在做 scientific decision support，
還是在做 general fact verification？
```

更好的 formal data strategy：

```text
Main:
SciFact

Structured scientific evidence supplement:
SciTab

Robustness / structured provenance supplement:
FEVEROUS

Long-document secondary:
Qasper

Decision-label secondary:
PubMedQA
```

SciTab 比 FEVEROUS 更貼近你們主題，因為它是 scientific table claim verification，包含 1.2K expert-verified scientific claims，且 claims 來自 authentic scientific publications，需要 compositional reasoning over scientific tables。([arXiv][4])

Qasper 適合作 long-document secondary，因為它有 5,049 questions over 1,585 NLP papers，並提供 supporting evidence。([ACL Anthology][5])

PubMedQA 適合 decision label stability，因為它是 yes/no/maybe biomedical QA，包含 1K expert-annotated examples；它的弱點是 provenance / evidence span 結構不如 SciFact 或 Qasper 直接。([ACL Anthology][6])

QMSum 和 MeetingBank 適合後續 meeting-decision extension。QMSum 有 1,808 query-summary pairs over 232 meetings；MeetingBank 有 1,366 city-council meetings、3,579+ hours of video、transcripts、minutes、agenda 和 metadata，平均 transcript 超過 28K tokens。這兩個非常適合長會議，但需要你們補 decision span、speaker role、evidence span、uncertainty、risk boundary。([ACL Anthology][7])

自有會議、醫療、詐騙資料不該當第一篇主證據。可以做 external validation。原因不是資料不好，而是 reproducibility、IRB、privacy、annotation bias 都會消耗 reviewer 信任。

---

# 4. Derived benchmark

PB-EGP-50 足以作為 pilot benchmark。

目前 record schema 合理：

```text
claim / question
source document
gold evidence span
gold decision label
candidate evidence graph
compressed packet
model output
audit annotation
```

但我會加三個欄位：

```text
gold_lineage_path
gold_counterevidence_or_conflict
gold_boundary_note
```

理由：你們要測 provenance、counterevidence、risk boundary，資料裡就必須有 gold target。不能只在 output audit 階段才補。

## Pilot 規模

40–50 records 足夠做 feasibility pilot。

但你們現在 pilot 設計太大：

```text
50 records
× 10 baselines
× 3 token budgets
× 2 SLMs
× perturbations
```

這會爆炸。你們會花太多時間跑模型，太少時間看錯誤。

我建議 pilot 收斂成：

```text
50 records
1 primary SLM
1 larger reference model
1 token budget: 1024 或 2048
6 context conditions
2 perturbations
human audit all key outputs
```

等 pilot 成功，再擴 token budgets 和模型數。

## Formal paper 規模

最低 workshop / short paper：

```text
100–150 records
```

比較像正式 Findings / IR / KG paper：

```text
300–500 records
```

我建議正式 paper：

```text
Main:
300 SciFact records

Structured supplement:
100 SciTab or FEVEROUS records

Long-document secondary:
50 Qasper records

Human audit:
至少 600–1000 outputs 的 stratified subset
```

如果你們要投稿主會長文，50 筆太少。50 筆只能證明 pilot；不能承載強 method claim。

---

# 5. Experiment design

你們列的 baselines 整體合理，但少了一個重要 baseline：

```text
context compression baseline
```

例如 LLMLingua、LongLLMLingua、RECOMP、Selective Context。這些工作已經專門處理 prompt / retrieved context compression；若你們不比較，reviewer 會說你們只是重新包裝 context compression。LLMLingua 和 LongLLMLingua 已經是 prompt compression 代表性方法；RECOMP 則是 retrieval-augmented LM 的 context compression；Selective Context 則直接剪除冗餘 context。([ACL Anthology][8])

## Must-have baselines

正式 paper 必須有：

```text
1. Equal-budget raw text + SLM
2. Top-k retrieved text + SLM
3. Generic summary + SLM
4. Equal-token evidence list + SLM
5. Context compression baseline + SLM
6. Uncompressed graph neighborhood + SLM
7. Centrality-based graph pruning + SLM
8. Provenance-bounded graph packet + SLM
```

其中 `equal-token evidence list` 很重要。它能回答 reviewer 的核心質疑：

```text
到底是 graph packet 有用，
還是只要列出 evidence spans 就夠了？
```

如果 flat evidence list 跟 graph packet 一樣好，graph 結構貢獻會變弱。

## 可以延後的 baseline

```text
random graph pruning
full Microsoft-style GraphRAG
multi-agent summarization
dynamic memory / pheromone routing
learned graph compressor
```

Random pruning 可放 pilot，但 formal paper 不一定要放主表。它說服力低於 centrality pruning、top-k text、context compression。

## GraphRAG-style baseline 是否第一篇一定要有？

Pilot 不一定。

Formal paper 若你們的 related work 明確講 GraphRAG 差異，那就一定要有至少一個 GraphRAG-style baseline。它不必完整重現 Microsoft GraphRAG 的所有 global / local pipeline，但至少要有：

```text
graph-based indexing
subgraph retrieval
graph-to-text context
SLM answer generation
```

否則 reviewer 會覺得你們只是在文字上區分 GraphRAG。GraphRAG survey 已經把這個領域整理成既有流程；你們需要用 baseline 對話。([arXiv][9])

## Oracle evidence packet 怎麼處理？

Oracle evidence packet 可以有，但只能作 upper bound。

最危險的洩漏點是：

```text
support_relation
evidence_force
counterevidence_flag
```

如果這些直接來自 gold label，模型其實不用 reasoning。它只要讀 label。

正確做法：

```text
Track A: Oracle packet
只測 schema / compression upper bound。
清楚標成 oracle setting。
不能用來支持 end-to-end 主 claim。

Track B: Predicted packet
用 retriever + relation extractor / NLI / 小模型建立 candidate graph。
主 claim 只建立在 Track B。

Track C: Relation-hidden packet
保留 source_span、lineage、uncertainty、source type，
拿掉 support/refute relation labels，
測 SLM 是否仍能判斷。
```

這三條 track 可以避免 reviewer 說你們把答案塞進 packet。

---

# 6. Metrics

你們列的 primary metrics 大致合理，但太多。Formal paper 最好把 primary 壓成 4 個，其他放 secondary。

## 我建議的 primary metrics

```text
1. unsupported-claim rate
2. provenance / citation validity
3. decision correctness
4. decision stability under non-evidential perturbation
```

這四個足以支撐主張。

## Secondary metrics

```text
uncertainty preservation
counterevidence retention
human audit time
compression ratio
context token budget
QAFactEval / SummaC / AlignScore
FActScore-style factuality
RAGAS / ARES faithfulness
ROUGE / BERTScore
```

ROUGE 和 BERTScore 只適合放 secondary。ROUGE 是摘要重疊指標；BERTScore 是 contextual embedding similarity。兩者都不能直接判斷 evidence support。([ACL Anthology][10])

QAFactEval、SummaC、AlignScore、FActScore-style metrics 比 ROUGE / BERTScore 更貼近 factuality。QAFactEval 是 QA-based factual consistency；SummaC 是 NLI-based consistency；AlignScore 是 unified alignment function；FActScore 把生成拆成 atomic facts，再判斷哪些 atomic facts 被 reliable source 支持。([ACL Anthology][11])

Citation / attribution 可以參考 AIS 與 ALCE。AIS 明確要求 NLG output 能被 identified sources 驗證；ALCE 評估帶 citation 的 answer generation，包含 citation quality。([ACL Anthology][12])

RAGAS、ARES、RAGTruth 可作 RAG faithfulness 背景與 secondary comparison。RAGAS 是 reference-free RAG evaluation；ARES 評 context relevance、answer faithfulness、answer relevance；RAGTruth 提供 RAG 場景下 word-level hallucination annotation。([ACL Anthology][13])

## Unsupported-claim rate 怎麼標註？

用 atomic-claim audit。不要整段判斷。

流程：

```text
1. 把模型回答拆成 atomic claims。
2. 每個 atomic claim 對照 cited span。
3. 若 citation 不足，再對照整個 packet。
4. 若 packet 仍不足，再標為 unsupported。
```

標籤建議：

```text
SUPPORTED_BY_CITED_SPAN
SUPPORTED_BY_PACKET_BUT_BAD_CITATION
CONTRADICTED_BY_EVIDENCE
NOT_IN_PACKET
OVERGENERALIZED
UNCERTAIN_BUT_STATED_AS_CERTAIN
UNVERIFIABLE_OR_EXTERNAL_KNOWLEDGE
```

公式：

```text
unsupported-claim rate =
(CONTRADICTED + NOT_IN_PACKET + OVERGENERALIZED + UNCERTAIN_AS_CERTAIN + UNVERIFIABLE)
/
total atomic claims
```

半自動做法可以讓 LLM 先拆 atomic claims，但人工必須審核 atomic decomposition 和 support label。這裡可以借用 FActScore 的 atomic fact 思路。([ACL Anthology][14])

## Provenance retention 怎麼定義？

不要用主觀評分。用 set overlap。

對每筆 record 定義 gold lineage set：

```text
L_gold = {
  source_id,
  span_id,
  sentence_id / table_cell_id,
  section_id,
  source_type,
  lineage_path
}
```

packet retention：

```text
Provenance retention =
weighted retained lineage components / total required lineage components
```

可拆成：

```text
source_id recall
span_id recall
table_cell / sentence recall
lineage_path recall
source_type retention
```

Output-level citation validity 另算：

```text
citation precision =
valid cited spans / all cited spans

citation recall =
atomic claims with valid citation / atomic claims requiring citation
```

這樣 provenance retention 就不會變成「看起來有來源」的主觀印象。

## Decision stability 怎麼設計？

要分兩種 perturbation。

第一種是 **non-evidential perturbation**。理論上 label 不該變。

```text
evidence order shuffle
JSON field order shuffle
irrelevant distractor node
prompt paraphrase
equivalent serialization
```

第二種是 **evidential perturbation**。label 可能應該變，或 uncertainty 應該升高。

```text
remove direct evidence
add counterevidence
reduce budget until key evidence missing
add low-authority conflicting source
```

你們的 label flip rate 只應該把第一種當「不穩定」。第二種要測的是 appropriate sensitivity。

建議兩個指標：

```text
Invariance stability =
1 - label flip rate under non-evidential perturbations

Evidence sensitivity =
correct adjustment rate under evidential perturbations
```

這樣 reviewer 比較不會說：「你們把所有 label flip 都當壞事，這不合理。」

---

# 7. Perturbation and ablation

你們的 perturbation 設計方向正確，但要補兩個。

目前 perturbation：

```text
evidence order shuffle
irrelevant distractor nodes
low-authority related source
reduced budget
counterevidence stress
prompt paraphrase
```

我建議新增：

```text
serialization perturbation
```

也就是同一個 packet 用三種格式：

```text
JSON
YAML-like bullet list
plain evidence table
```

如果 JSON 表現明顯最好，可能只是格式誘導，而非 graph packet 本身有效。

再新增：

```text
field-name perturbation
```

把欄位名稱從 `evidence_force` 改成中性名稱，例如 `relation_note`。如果結果劇烈改變，表示模型靠 prompt semantics，不一定靠結構。

目前 ablation：

```text
full packet
remove provenance
remove uncertainty
remove counterevidence
remove compression log
remove graph relation labels
remove source type
equal-token summary
```

這組足夠，但還要加：

```text
flat evidence list, no graph relation
gold evidence spans only
predicted evidence spans only
same packet without JSON structure
same packet with relation labels hidden
```

這四個是防守「JSON prompt trick」的關鍵。

最重要的 ablation 是：

```text
Full packet
vs
flat evidence list
vs
same-token generic summary
vs
same-token top-k text
```

如果 full packet 只贏 random pruning，沒有意義。它必須贏過真正強的 text / compression baseline。

---

# 8. Human audit

需要兩位 annotator。正式 paper 最好三位，其中兩位標註、一位 adjudicator。Pilot 可以兩位。

要報：

```text
Cohen’s kappa：二位 annotator、categorical label
Krippendorff’s alpha：多位 annotator、ordinal / missing labels / multi-class
percent agreement：輔助報告
adjudicated final label：主分析使用
```

不要只報 LLM judge。LLM judge 可以輔助，但 unsupported-claim rate 與 citation support 至少要有人審 subset。

## Human audit rubric

每個 output 分三層。

第一層：decision label

```text
Correct
Partially correct
Incorrect
Should abstain
```

第二層：atomic claim support

每個 atomic claim 標：

```text
Supported by cited span
Supported by packet, citation wrong or missing
Contradicted
Unsupported
Overgeneralized
Uncertainty lost
External knowledge introduced
```

第三層：evidence behavior

```text
Citation supports the sentence? yes/no/partial
Counterevidence acknowledged? yes/no/not applicable
Uncertainty preserved? yes/no/partial
Risk boundary respected? yes/no/partial
Audit trail sufficient? yes/no/partial
Audit time in seconds
```

正式 paper 至少人工審：

```text
20–30% of all outputs，且 stratified by dataset / method / model / label
```

但如果 unsupported-claim rate 是 primary metric，我會更嚴格：

```text
至少 600 outputs 或 100 records × 3–4 key systems × 2 models
```

Pilot 則建議：

```text
audit all outputs for 1 primary SLM
只保留 5–6 context conditions
不要一開始 audit 10 baselines × 3 budgets
```

---

# 9. Statistical analysis

你們的 paired design 正確。每筆 record 跑多個方法，不能當獨立樣本。

你們列的統計方法合理：

```text
McNemar / paired bootstrap for decision correctness
Wilcoxon / paired bootstrap for unsupported-claim rate
paired bootstrap CI for provenance retention
paired comparison for label flip rate
Wilcoxon for audit time
effect sizes + confidence intervals
```

我會補三點。

第一，formal paper 建議用 mixed-effects model 做輔助分析：

```text
logistic mixed-effects model for decision correctness
beta / quasi-binomial model for unsupported-claim rate
random intercepts for record, dataset, model
fixed effects for method, budget, perturbation
```

因為你們有 repeated measures：

```text
same record
same model
same dataset
same budget
multiple context methods
```

只用 pairwise tests 會漏掉層級結構。

第二，要做 multiple comparison correction：

```text
Holm-Bonferroni
或 Benjamini-Hochberg
```

尤其你們 baseline 很多，pairwise comparison 一多，p-value 很容易亂。

第三，報 practical effect size，不只報顯著性。

例如：

```text
unsupported-claim rate relative reduction
provenance retention absolute gain
label flip rate absolute reduction
audit time median reduction
```

Reviewer 更在乎：

```text
少了多少 unsupported claims？
省了多少 audit time？
有沒有犧牲 correctness？
```

---

# 10. Go / no-go gate

你們目前 gate 還不夠嚴格。

目前：

```text
Go:
packet lowers unsupported claims and improves provenance retention.

Revise:
packet helps, but instability remains high or uncertainty disappears.

Stop:
top-k text + prompt or generic summary is equally strong.
```

我會改成更硬的版本。

## Go

至少滿足：

```text
1. packet beats top-k retrieved text on unsupported-claim rate;
2. packet beats generic summary on provenance retention;
3. packet beats flat evidence list or context compression baseline on at least one primary metric;
4. decision correctness does not drop meaningfully;
5. full packet beats key ablations;
6. gains appear in predicted-track setting, not only oracle setting.
```

最好設定量化門檻：

```text
unsupported-claim rate relative reduction ≥ 20%
provenance retention absolute gain ≥ 10 points
decision correctness drop ≤ 3 points
label flip rate reduction ≥ 10–15%
counterevidence retention ≥ 75% on stress subset
```

## Revise

```text
packet lowers unsupported claims but loses uncertainty;
packet improves provenance but hurts correctness;
benefit only appears with relation labels;
benefit disappears under serialization perturbation;
human audit agreement is low;
small model ignores citation / uncertainty fields.
```

## Stop / reframe

```text
top-k text + strong prompt equals packet;
flat evidence list equals packet;
context compression baseline equals packet;
oracle packet works but predicted packet fails badly;
full packet does not beat remove-provenance / remove-uncertainty ablations;
gains come only from leaking support/refute labels;
counterevidence is systematically dropped;
human audit cannot reliably apply the rubric.
```

這些 failure condition 很重要。它們會逼你們判斷這到底是 research object，還是 prompt engineering。

---

# 最終建議格式

```text
Recommended framing:
Provenance-bounded evidence graph packet construction for stable small-model decision support.

Best first dataset:
Pilot: SciFact + FEVEROUS.
Formal paper: SciFact main; SciTab or FEVEROUS structured-evidence supplement; Qasper secondary long-document evidence QA. PubMedQA only for yes/no/maybe decision-label stability, not provenance as main claim.

Minimum viable pilot:
50 public records; 1 primary <10B SLM; 1 larger reference model; 1 token budget first, preferably 1024 or 2048; 5–6 context conditions; 2 perturbations; full human audit on primary SLM outputs.

Formal paper dataset size:
300–500 records total.
Suggested: 300 SciFact, 100 SciTab or FEVEROUS, 50 Qasper.
Human audit subset: at least 600 outputs or 20–30% stratified outputs, whichever is larger for the key comparisons.

Must-have baselines:
equal-budget raw text + SLM;
top-k retrieved text + SLM;
generic summary + SLM;
flat evidence list + SLM;
context compression baseline + SLM;
uncompressed graph neighborhood + SLM;
centrality-based graph pruning + SLM;
provenance-bounded graph packet + SLM.
GraphRAG-style subgraph retrieval is optional for pilot, required for formal paper if the paper explicitly differentiates from GraphRAG.
Oracle evidence packet is allowed only as upper bound, clearly separated from main results.

Primary metrics:
unsupported-claim rate;
provenance / citation validity;
decision correctness;
decision stability under non-evidential perturbation.

Human audit design:
two annotators minimum; three preferred with adjudication.
Atomic-claim-level audit.
Report Cohen’s kappa for categorical labels, Krippendorff’s alpha where appropriate, percent agreement, and adjudicated labels.
Audit all key pilot outputs; in formal paper audit stratified subset across methods, datasets, models, and labels.

Key ablations:
remove provenance;
remove uncertainty;
remove counterevidence;
remove relation labels;
remove source type;
remove compression log;
flat evidence list;
same-token generic summary;
same packet rendered as non-JSON;
relation-hidden packet.

Key perturbations:
evidence order shuffle;
serialization change;
irrelevant distractor nodes;
prompt paraphrase;
low-authority related source;
counterevidence insertion;
budget reduction.
Separate invariance perturbations from evidential perturbations.

Main reviewer risk:
Reviewer says the method is ordinary GraphRAG / context compression / JSON formatting with citations.

How to defend against “ordinary GraphRAG + JSON” critique:
Define packet construction as a constrained evidence-preservation objective, not a retrieval pipeline.
Compare against top-k text, flat evidence list, context compression, uncompressed graph neighborhood, centrality pruning, and GraphRAG-style subgraph retrieval.
Show ablations where removing provenance, uncertainty, counterevidence, or relation labels measurably changes unsupported-claim rate, provenance retention, or label stability.
Run serialization perturbations to show the effect is not merely JSON formatting.
Separate oracle and predicted graph tracks to avoid gold-label leakage.

Go / no-go criteria:
Go if packet reduces unsupported claims by at least ~20% relative to top-k text or generic summary, improves provenance retention by at least ~10 absolute points, preserves decision correctness within ~3 points, improves non-evidential stability, and beats flat evidence list or context compression on at least one primary metric.
Revise if gains depend on oracle relations, uncertainty disappears, citation use is unstable, or human audit agreement is weak.
Stop or reframe if top-k text + prompt, flat evidence list, or context compression performs equally well across primary metrics.

Three-month execution plan:
Weeks 1–2:
Freeze schema v0; define gold lineage; write audit rubric; select 50 pilot records from SciFact + FEVEROUS; prepare source/span IDs.

Weeks 3–4:
Build oracle graph and predicted candidate graph; implement greedy packet compressor; implement baselines: equal-budget text, top-k text, generic summary, flat evidence list, centrality pruning, context compression.

Weeks 5–6:
Run one <10B SLM and one larger reference model at temperature 0; use one token budget first; run two perturbations: order shuffle and distractor nodes.

Weeks 7–8:
Human audit primary outputs; compute unsupported-claim rate, provenance retention, citation validity, decision correctness, label flip rate; adjudicate disagreements.

Weeks 9–10:
Run ablations: remove provenance, uncertainty, counterevidence, relation labels, source type, compression log; run serialization perturbation.

Weeks 11–12:
Analyze paired results; write failure analysis; decide whether to scale to 300–500 records; prepare workshop / arXiv draft if pilot clears gate.

Decision:
[ ] pursue now
[x] pursue after narrowing
[ ] park for later
[ ] reject / not enough research value
```

最後的硬判斷：**可以做，且有發表潛力；第一篇必須砍掉野心。**

第一篇只證明一件事：

```text
provenance-bounded graph packets create measurable evidence-discipline gains
for sub-10B models under fixed token budgets.
```

只要這件事證明得乾淨，你們才有資格往 meeting decision support、medical/scam workflows、dynamic graph memory、latent-state reasoning 擴展。

[1]: https://arxiv.org/abs/2404.16130?utm_source=chatgpt.com "From Local to Global: A Graph RAG Approach to Query-Focused Summarization"
[2]: https://aclanthology.org/2020.emnlp-main.609/?utm_source=chatgpt.com "Fact or Fiction: Verifying Scientific Claims"
[3]: https://arxiv.org/abs/2106.05707?utm_source=chatgpt.com "FEVEROUS: Fact Extraction and VERification Over Unstructured and Structured information"
[4]: https://arxiv.org/abs/2305.13186?utm_source=chatgpt.com "SCITAB: A Challenging Benchmark for Compositional Reasoning and Claim Verification on Scientific Tables"
[5]: https://aclanthology.org/2021.naacl-main.365/?utm_source=chatgpt.com "A Dataset of Information-Seeking Questions and Answers ..."
[6]: https://aclanthology.org/D19-1259/?utm_source=chatgpt.com "PubMedQA: A Dataset for Biomedical Research Question ..."
[7]: https://aclanthology.org/2021.naacl-main.472/?utm_source=chatgpt.com "A New Benchmark for Query-based Multi-domain Meeting ..."
[8]: https://aclanthology.org/2023.emnlp-main.825/?utm_source=chatgpt.com "Compressing Prompts for Accelerated Inference of Large ..."
[9]: https://arxiv.org/abs/2408.08921?utm_source=chatgpt.com "Graph Retrieval-Augmented Generation: A Survey"
[10]: https://aclanthology.org/W04-1013/?utm_source=chatgpt.com "ROUGE: A Package for Automatic Evaluation of Summaries"
[11]: https://aclanthology.org/2022.naacl-main.187/?utm_source=chatgpt.com "QAFactEval: Improved QA-Based Factual Consistency ..."
[12]: https://aclanthology.org/2023.cl-4.2/?utm_source=chatgpt.com "Measuring Attribution in Natural Language Generation ..."
[13]: https://aclanthology.org/2024.eacl-demo.16/?utm_source=chatgpt.com "RAGAs: Automated Evaluation of Retrieval Augmented ..."
[14]: https://aclanthology.org/2023.emnlp-main.741/?utm_source=chatgpt.com "FActScore: Fine-grained Atomic Evaluation of Factual ..."

