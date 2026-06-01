# Expert Review Response

Date recorded: 2026-06-01

Status: expert direction-setting response recorded verbatim from user-provided expert review.

## Full Expert Response

結論：**值得收斂成正式研究線，但不能叫成一般的 `Knowledge Graph Compression + SLM`。**

這個名稱太寬，會被 reviewer 直接丟進 GraphRAG、KGQA、graph summarization、context compression 的既有桶子裡。你們真正有辨識度的東西是：

```text
Provenance-bounded evidence graph packets for stable small-model decision support.
```

也就是：把大型證據圖壓縮成小模型可用的「有邊界、有來源、有不確定性、有反證、有稽核軌跡」的 reasoning packet。

這條線有研究價值。資料包裡的 A 是第一篇 paper 主軸；C 是最好的 downstream evaluation；B 是第二篇之後的方法擴充；D 是漂亮但太跳的 later testbed。

GraphRAG 已經很擠。Microsoft GraphRAG 已經把 LLM-derived KG、community summaries、partial answers、global answer 這套做成代表性框架；GraphRAG survey 也已經把 Graph-Based Indexing、Graph-Guided Retrieval、Graph-Enhanced Generation 形式化了。KG + LLM for QA 也已經有系統性綜述。你們若只是「建圖、取子圖、餵給 SLM、看 QA accuracy」，會被視為 ordinary GraphRAG engineering。([arXiv][1])

你們能切出的縫隙在這裡：現有 provenance-aware RAG 多半在處理 citation、claim-evidence alignment、sentence-level attribution；現有 KG compression / graph summarization 多半在處理儲存、查詢、規則挖掘或圖摘要效率。你們要處理的是「壓縮後，小模型是否仍然守住 evidence boundary」。這個 object 夠清楚，也夠不同。citation 是否存在不等於 claim 被證據支持；近年 citation faithfulness、sentence-level grounding、claim-evidence interface 都在證明這個問題仍然沒有解完。([UvA FNWI Staff][2])

---

## 1. Primary framing

我建議 framing 成：

```text
Evidence-preserving graph packet construction for small-model decision stability.
```

更正式一點：

```text
Provenance-bounded evidence graph packets as a bounded reasoning substrate for small language models.
```

不要主打：

```text
Knowledge graph compression method
```

原因很簡單。這會把你們拉進傳統 graph compression / KG summarization 的審稿標準。那個社群會問 query preservation、lossless reconstruction、storage efficiency、rule mining efficiency、graph sparsification bound。這些不是你們第一篇的核心。已有工作如 GAME+ 已經把 knowledge-graph summarization、size-reduced abstract KG、provenance maintenance、lossless reconstruction 用在 rule mining 效率上；你們如果只說「KG compression」，reviewer 會拿這些工作來壓你。([Springer][3])

也不要主打：

```text
Provenance-aware GraphRAG
```

這會讓貢獻看起來像 GraphRAG 的一個安全插件。

最好的 framing 是把 `compressed graph packet` 定義成一種 **bounded reasoning substrate**。也就是小模型不是在「閱讀更多東西」，而是在一個受約束的證據環境裡做判斷。

這個 framing 保留三個研究鉤子：

```text
compression objective
+
provenance / uncertainty retention
+
decision stability under constrained context
```

這三個放在一起，才是你們的辨識度。

---

## 2. Scientific object

最值得保護的 scientific object 是：

```text
provenance-bounded compressed evidence graph packet
```

不是一般 KG。不是一般 summary。不是一般 retrieved subgraph。

它應該有三層 object。

第一層是 **packet schema**。這是可發表但不能單獨成為強 paper 的部分。

第二層是 **compression objective**。這才是 method contribution。

第三層是 **SLM behavior under evidence-preserving compressed context**。這是 evaluation contribution。

我會把核心 object 寫成：

```text
Given a large evidence graph G, a task q, and a token budget B,
construct a compressed packet P_B such that P_B preserves
task-relevant support paths, source lineage, uncertainty, counterevidence,
and decision boundaries needed by an SLM to produce auditable answers.
```

這句話比「壓縮知識圖譜」強很多，因為它指定了壓縮要保留什麼，以及為誰保留。

必備 schema 欄位如下：

```text
claim_id
claim_text
normalized_claim
decision_question
allowed_answer_space

source_id
source_type
source_span
source_timestamp_or_version
source_authority_level
source_access_path

support_relation
support_polarity
evidence_force
warrant_scope
counterevidence_flag
conflict_group_id

lineage_parent
lineage_depth
citation_chain
derived_from
extraction_method
human_or_model_generated

uncertainty_type
uncertainty_value
ambiguity_note
temporal_validity
missing_evidence_flag

risk_boundary
unsupported_extension_warning
safe_abstention_condition

compression_operation
retained_reason
dropped_reason
lossy_field_notice
audit_reconstruction_pointer
```

其中最重要的是這六個：

```text
source_span
support_relation
evidence_force
lineage_depth
uncertainty
counterevidence_flag
```

缺這六個，packet 就會退化成漂亮的 GraphRAG context。

---

## 3. Novelty and differentiation

和 GraphRAG 的差異：GraphRAG 的核心是用圖改善 retrieval / global sensemaking / generation。你們的核心是壓縮時保留 evidence discipline，並測量小模型在壓縮後是否仍然穩定。GraphRAG 問的是「圖能不能幫助回答」。你們問的是「壓縮到小模型可消化時，哪些證據結構不能丟」。這是不同的 scientific object。([arXiv][1])

和 KGQA 的差異：KGQA 多半假設 KG 是可查詢知識庫，模型或工具要回答問題。你們不是只問答案對不對，而是問答案是否有支持路徑、是否保留不確定性、是否避免 overclaim、是否在壓縮擾動下保持 label stability。KGQA 的 crowdedness 很高；你們要避開「又一個 KG + LLM QA pipeline」。([ACL Anthology][4])

和 subgraph retrieval 的差異：subgraph retrieval 是選相關子圖。你們要做的是在 token budget 下建立 **evidence-safe packet**。選到相關節點不夠。packet 必須保留反證、來源階層、support strength、claim boundary。這裡是你們最需要寫清楚的地方。

和 summarization / context compression 的差異：一般 context compression 會優化長度與 retrieval / answer performance；近期 ACL 也已經有 passage compression for long-context retrieval。你們不能只說「我們把 graph 壓短」。你們要說「我們把 graph 壓短，同時明確保存 provenance、uncertainty、counterevidence，並以 unsupported-claim rate 與 decision stability 作為 primary metrics」。([ACL Anthology][5])

和 agent memory 的差異：B 方向會撞 agent memory。ARM 這類 dynamic RAG memory 已經在做 selective remembrance / decay；DyG-RAG 也在做 dynamic event-centric graph retrieval。B 若放第一篇，很容易被說成 adaptive retrieval 或 dynamic memory。([arXiv][6])

和 provenance-aware RAG 的差異：已有工作在做 sentence-level citation、claim-evidence interface、citation faithfulness。你們的差異要落在 **graph-level compression objective + small-model decision stability**。如果只做 citation alignment，就會輸給 provenance-aware RAG。([ACL Anthology][7])

還不夠清楚的地方：目前資料包仍然容易把 `provenance`、`uncertainty`、`latent state`、`pheromone`、`ancient scripts` 全部放進同一篇。這會稀釋貢獻。第一篇只保留 A + C 的最小交集：

```text
provenance-preserving compression
→ SLM answer discipline
→ decision stability
```

B 和 D 先不要進主 paper。

---

## 4. First experiment

我建議第一個實驗選：

```text
scientific-paper claim audit
```

使用 SciFact 或 PubMedQA 的小樣本啟動。SciFact 已經有 scientific claims、evidence-containing abstracts、support/refute labels、rationales；這比自己從 web 或 cybercrime 內容建立 ground truth 乾淨很多。PubMedQA 也有 biomedical research QA 的 yes/no/maybe 結構，可作為第二資料源。([ACL Anthology][8])

### Domain

```text
scientific claim verification / claim audit
```

不要說 clinical decision support。說 scientific evidence audit。

### Data unit

30–50 筆 record。每筆包含：

```text
claim
2–5 source snippets or abstracts
gold support label: support / refute / insufficient / mixed
gold evidence spans
gold uncertainty note
one decision question
```

### Graph schema

```text
Claim node
Evidence sentence node
Paper/source node
Entity/concept node
Method/result node
Support edge
Refute edge
Partial-support edge
Contradiction edge
Lineage edge
Uncertainty edge
Temporal-validity edge
```

最小 schema：

```json
{
  "claim": "...",
  "question": "...",
  "allowed_answers": ["supported", "refuted", "insufficient", "mixed"],
  "evidence_nodes": [
    {
      "source_id": "...",
      "span_id": "...",
      "span_text": "...",
      "source_type": "primary_study",
      "support_relation": "supports",
      "evidence_force": "direct",
      "uncertainty": "low",
      "lineage": ["paper", "abstract", "sentence"],
      "risk_boundary": "does not justify causal claim"
    }
  ],
  "counterevidence_nodes": [],
  "compression_log": [
    {
      "dropped": "...",
      "reason": "background only"
    }
  ]
}
```

### Compression method

先做一個可解釋、可手動 audit 的 method。不要一開始上 GNN 或 RL。

```text
EPC-Packet v0
```

規則：

```text
Hard-retain:
- direct support/refute evidence
- source span
- source lineage
- counterevidence
- uncertainty
- temporal validity
- risk boundary

Soft-rank:
- concept bridge
- related entity
- background definition
- redundant support
- low-relevance context

Drop:
- duplicate entity mentions
- unsupported inferred relation
- low-value generic background
```

壓縮目標：

```text
maximize evidence coverage + provenance coverage + counterevidence coverage
subject to token budget B
```

不要第一篇就追求最強壓縮。先追求「壓縮後不會讓 SLM 亂講」。

### SLM task

給 <10B 模型同一個問題，要求輸出：

```text
answer label
one-sentence answer
evidence spans used
uncertainty note
unsupported claims avoided
```

### Baselines

第一輪至少做六組：

```text
B1 raw text context + SLM
B2 top-k retrieved text + SLM
B3 generic summary + SLM
B4 uncompressed graph neighborhood + SLM
B5 random / centrality graph pruning + SLM
B6 provenance-bounded compressed graph packet + SLM
```

再加一個 larger LLM reference 作 ceiling，不要把它當 gold truth。

### Metrics

Primary：

```text
answer correctness
unsupported-claim rate
provenance retention
citation lineage preservation
uncertainty preservation
decision stability / label flip rate
```

Secondary：

```text
token budget
compression ratio
human audit time
counterevidence retention
abstention correctness
```

Optional：

```text
ROUGE
BERTScore
generic helpfulness score
```

ROUGE 不該當主 metric。這不是摘要 paper。

### Expected result

合理成功訊號是：

```text
compressed evidence graph packet
≈ or > raw text correctness
< generic summary unsupported claims
> top-k text provenance retention
< uncompressed graph context token budget
< label flip rate under perturbation
```

### Failure condition

這篇 paper 應該在以下情況被重做：

```text
uncompressed graph neighborhood 明顯勝過 compressed packet；
generic summary 一樣能降低 unsupported claims；
packet 壓縮掉反證；
SLM 無視 provenance 欄位；
human audit 無法一致判斷 evidence_force；
decision stability 只來自 prompt wording，不來自 graph packet。
```

---

## 5. Baselines

Must-have：

```text
raw text context + SLM
generic summary + SLM
top-k retrieved text + SLM
uncompressed graph neighborhood + SLM
random graph pruning + SLM
centrality-based graph pruning + SLM
provenance-bounded compressed packet + SLM
gold label / human annotation reference
```

Strongly recommended：

```text
GraphRAG-style subgraph / community-summary baseline
larger LLM reference model
```

Later work：

```text
dynamic pheromone compression
personalized memory baseline
GNN-based graph compressor
learned compressor
latent-state model
multi-agent summarization
ancient-script multimodal packet
```

Reviewer 一定會問：「你的方法是不是只是 top-k retrieval 加 JSON 格式？」
所以 random pruning、centrality pruning、top-k text、uncompressed graph 這四個 baseline 很重要。它們能把「格式效果」和「compression objective 效果」分開。

---

## 6. Metrics

我會這樣排序。

Primary metrics：

```text
1. unsupported-claim rate
2. provenance retention
3. citation lineage preservation
4. answer correctness / decision label correctness
5. uncertainty preservation
6. decision stability / label flip rate
```

這六個是 paper 的核心。尤其 unsupported-claim rate 要放第一。因為你們不是在做一般 QA accuracy，而是在做 evidence discipline。近期 cited RAG 的問題已經不是「有沒有 citation」，而是 citation 是否真的 warrant claim；非常新的 evidence-force calibration 工作也把這點講得很清楚。([arXiv][9])

Secondary metrics：

```text
context token budget
compression ratio
human audit time
counterevidence retention
abstention correctness
calibration
```

Optional metrics：

```text
expert usefulness
latency
cost
ROUGE / BERTScore
user preference
```

`expert usefulness` 很重要，但第一篇容易太主觀。除非你有固定 rubric，不然先放 secondary 或 appendix。

---

## 7. Domain choice

第一篇我建議：

```text
scientific-paper claim audit
```

理由：

```text
public
ethical risk low
ground truth exists
evidence spans exist
metrics clear
reviewer understands the task
no IRB burden if using public dataset
```

SciFact 最適合 2–4 週 pilot。FEVER 也可用，但 Wikipedia claim verification 太接近一般 fact-checking，會弱化 expert-support framing。PubMedQA 可作補充，但 biomedical 題材容易讓 reviewer 期待 clinical rigor；第一篇不要碰 clinical deployment claim。([ACL Anthology][8])

我不建議第一篇用 cybercrime / scam-prevention public evidence。它符合你們長期強項，但第一篇會卡在資料標註、法律敏感、operational safety、來源真偽、受害者風險、平台政策。這些不是不能做，是不適合當第一篇。

我也不建議第一篇用 ancient-script symbolic hypothesis ranking。它很有辨識度，但太需要 domain expert。沒有 epigraphist / archaeologist / artifact bibliography control，reviewer 會覺得像概念展示。

排序如下：

| Domain | 第一篇適合度 | 判斷 |
| --- | ---: | --- |
| Scientific-paper claim audit | 5 | 最乾淨 |
| Public web evidence provenance | 4 | 好，但標註成本高 |
| Cybercrime / scam-prevention public evidence | 3.5 | 很 fit，但 first paper 風險偏高 |
| Synthetic high-stakes workflow | 3.5 | 可控，但 reviewer 可能嫌 toy |
| Ancient-script symbolic hypothesis ranking | 2.5 | 有特色，但太早 |
| Personal/expert external-memory system | 2 | 容易變產品系統 |
| Journal intelligence | 2.5 | 有趣，但 metric 較難 |

---

## 8. Claim boundary

第一篇必須避免這些 claim：

```text
不要宣稱 SLM 可以驗證真相。
不要宣稱 compression universally improves reasoning。
不要宣稱取代 GraphRAG。
不要宣稱 KG 是 ground truth。
不要宣稱 provenance 等於 correctness。
不要宣稱有 citation 就有 evidence support。
不要宣稱可部署到 clinical / legal / security operations。
不要宣稱 small model 具有 large model understanding。
不要宣稱 ancient scripts 可以被 deciphered。
不要把 AI-generated content 等同於 false content。
```

可以正向主張：

```text
In bounded evidence-audit tasks,
a provenance-preserving compressed graph packet can reduce unsupported claims
and improve evidence-lineage retention for small language models
under a fixed context budget.
```

也可以主張：

```text
Decision stability is a useful evaluation target for small-model expert support,
because correctness alone misses unsupported overreach and evidence-boundary failures.
```

這個 claim 夠強，也不超線。決策不確定性與 uncertainty propagation 已經是活躍問題；LLM decision support 在 uncertainty 下需要可稽核程序，這點已有 ICLR 2025 decision-under-uncertainty 工作與 2026 uncertainty propagation survey 可支撐。

---

## 9. Paper type and venue fit

第一篇最像：

```text
method + evaluation paper
```

不是純 systems paper。不是 position paper。不是 dataset paper，除非你們把 30–50 records 擴到 200+ 並做穩定 annotation。

合適社群：

```text
NLP / IR
Trustworthy AI
RAG evaluation
Knowledge graph / semantic web
Scientific claim verification
HCI decision support
```

具體 venue 類型：

```text
ACL / EMNLP / NAACL Findings
ACL workshops: NLP for Science, Trustworthy NLP, Knowledge-Augmented NLP
SIGIR / CIKM / WSDM workshops or short papers
ISWC / ESWC / Semantic Web venues
FAccT / AIES if decision-support and audit framing strong
CHI / CSCW only if加入 human audit interface study
Digital forensics later, not first
Digital humanities later, not first
```

如果第一篇只有 30–50 records，最實際是 workshop / Findings-style short paper / arXiv + workshop。要衝主會或 journal，需要擴到 200+ records，至少 2–3 domains，並加入 ablation。

---

## 10. Publishability threshold

最低限度必須證明：

```text
在相同或更低 token budget 下，provenance-preserving compressed graph packet 能讓 <10B 小模型比 raw text、generic summary、top-k retrieved text、uncompressed graph neighborhood、generic graph pruning 產生更少 unsupported claims，保留更多 evidence lineage，並維持不更差的 decision correctness / stability。
```

這句就是 paper 的生死線。

---

# 四個方向評分

| Direction | Novelty | Feasibility | Evaluation clarity | Reviewer legibility | Fit to our strengths | Overall |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| A. Provenance-preserving KG compression | 4.5 | 4.0 | 4.5 | 4.0 | 5.0 | 4.4 |
| B. Pheromone-based dynamic KG compression | 4.0 | 2.5 | 2.5 | 2.5 | 4.0 | 3.1 |
| C. Latent-state KG compression | 4.5 | 3.5 | 3.5 | 4.0 | 5.0 | 4.1 |
| D. Low-resource symbolic KG compression | 4.5 | 2.0 | 2.5 | 2.5 | 3.0 | 2.9 |

最高分是 A。理由：它有清楚 object、清楚 baseline、清楚 metric，也最容易跟 ordinary GraphRAG 拉開距離。A 可以在 2–4 週做出 pilot，不需要等大型資料集。

最低分是 D。不是因為它差，而是它太早。Ancient script / archaeology 作為 testbed 很有辨識度，但第一篇會被 domain validity 拖住。沒有專家、資料授權、artifact metadata、bibliography control，這個方向很容易變成漂亮但不可信的 demo。

我會這樣重組成 coherent PhD research line：

```text
Thesis:
Small language models can provide useful expert decision support
when their reasoning context is transformed into bounded,
auditable, provenance-preserving evidence substrates.

Paper 1:
Provenance-bounded graph packets for SLM decision stability.
(A + C minimal version)

Paper 2:
Latent-state evidence graph packets for high-risk workflow triage.
(C as main object)

Paper 3:
Adaptive / pheromone graph packet selection under repeated expert feedback.
(B after packet schema is established)

Paper 4:
Low-resource symbolic hypothesis ranking with multimodal evidence graph packets.
(D as stress-test domain)
```

這樣四個方向不再互相競爭，而是形成一條主線：

```text
static evidence packet
→ decision stability
→ dynamic adaptation
→ sparse symbolic generalization
```

---

# 對四個方向的嚴格判斷

## Direction A: Provenance-preserving KG compression for SLM reasoning

這是第一篇。

它是清楚 research object。前提是你們把 object 定義成：

```text
compressed evidence graph packet
```

而不是：

```text
compressed KG
```

它和 GraphRAG / subgraph retrieval 的差異足夠，但必須靠 metric 站住。文字 framing 不夠。你們要用 unsupported-claim rate、lineage preservation、uncertainty retention、label flip rate 證明差異。

第一個資料域：scientific-paper claim audit。不要從 scam 開始。

## Direction B: Pheromone-based dynamic KG compression

這比較像：

```text
adaptive retrieval + graph signal processing + agent memory
```

不是第一篇的 KG compression。

它有研究潛力，但第一篇放它會失焦。它需要 temporal workload、feedback loop、drift、decay、backup paths。這些設計很漂亮，也很危險。Reviewer 會問你是在做 GraphRAG、reinforcement learning、bandit retrieval、還是 memory management。

Synthetic graph 可以做第一個 method sanity check；要發好 paper，最好有 repeated-query log 或 expert-feedback trace。

公平 baseline：

```text
static top-k retrieval
personalized PageRank
random walk with restart
centrality pruning
recency-weighted retrieval
MMR diversity retrieval
bandit retrieval: UCB / Thompson sampling
DyG-RAG-style temporal retrieval
static GraphRAG
adaptive memory RAG
```

## Direction C: Latent-state KG compression for decision support

這條線很有價值，但我不建議第一篇把它當主軸。它應該先作為 Direction A 的 downstream evaluation case。

理由：latent-state representation 會引入另一個大問題：

```text
你推論的 hidden state 憑什麼成立？
```

這會把第一篇從 KG compression 拖到 HMM / state inference / decision theory。除非你們第一篇投 HCI / decision support / AI safety，否則 NLP / KG reviewer 會覺得主軸飄掉。

最小資料集可以長這樣：

```text
40 synthetic workflow cases
每案 5–10 observable traces
1 hidden state label
1 escalation decision
2 plausible counterfactual variants
gold: escalate / monitor / insufficient evidence
```

Metric：

```text
label flip rate
unsafe downrouting
missed escalation
evidence-to-state traceability
uncertainty note quality
```

C 比 KG compression 本身更容易被非 KG reviewer 理解，但也更容易被要求 domain validation。所以先放在 A 的 evaluation 裡，不要讓它吃掉第一篇。

## Direction D: Low-resource symbolic KG compression

這不是第一篇。

它可以變成非常有辨識度的第三或第四篇，但需要條件：

```text
domain expert
public artifact metadata
known-script control task
undeciphered-script non-translation task
bibliography graph
uncertainty rubric
```

正確任務不是 translation，而是：

```text
rank hypotheses
preserve uncertainty
show evidence paths
avoid overclaiming
```

這跟你們的核心精神一致。但第一篇用它，reviewer 會分心在 archaeology validity，而不是 compression substrate。

---

# 決策建議

```text
Recommended primary framing:
Provenance-bounded evidence graph packets for stable small-model decision support.

Recommended first paper title:
Provenance-Bounded Graph Packets: Evidence-Preserving Context Construction for Stable Small-Model Decision Support

Best first domain:
Scientific-paper claim audit, starting from SciFact-style claim/evidence records.

Minimum viable experiment:
30–50 claim-centered records; construct evidence graphs; compare raw text, top-k text, generic summary, uncompressed graph neighborhood, random/centrality-pruned graph, and provenance-bounded compressed graph packet using two <10B SLMs plus one larger reference model.

Must-have baselines:
raw text + SLM;
generic summary + SLM;
top-k retrieved text + SLM;
uncompressed graph neighborhood + SLM;
random graph pruning + SLM;
centrality graph pruning + SLM;
gold human/dataset label reference.

Primary metrics:
unsupported-claim rate;
provenance retention;
citation lineage preservation;
answer / decision correctness;
uncertainty preservation;
decision stability / label flip rate.

Main novelty claim:
A compressed graph packet can be optimized not merely for relevance or brevity, but for preserving the evidence boundaries that small models need to produce auditable and stable expert-support decisions.

Claims to avoid:
No truth-verification claim.
No clinical/legal/security deployment claim.
No universal compression-improves-reasoning claim.
No GraphRAG replacement claim.
No ancient-script decipherment claim.
No claim that citation presence equals evidence support.

Biggest technical risk:
The SLM may ignore provenance and uncertainty fields, or the compression method may silently drop counterevidence.

Biggest reviewer risk:
Reviewer says this is just GraphRAG plus JSON summarization. The defense is a compression objective, ablation, and metrics showing provenance/uncertainty/counterevidence preservation.

Most promising venue/community:
NLP/IR + trustworthy RAG evaluation first; then KG/Semantic Web; later AI safety, HCI decision support, digital forensics, or digital humanities.

Three-month action plan:
Week 1–2: freeze packet schema, annotation rubric, and 40-record SciFact pilot set.
Week 3–4: implement graph construction and six baselines.
Week 5–6: run two SLMs with fixed prompts, repeated seeds, and context-order perturbations.
Week 7–8: human audit unsupported claims, provenance retention, uncertainty preservation.
Week 9–10: run ablations removing provenance, uncertainty, counterevidence, and compression log fields.
Week 11–12: write paper draft with claim-boundary section, related-work differentiation, and failure analysis.

Decision:
[ ] pursue now
[x] pursue after narrowing
[ ] park for later
[ ] reject / not enough research value
```

實際意思是：**現在就做 pilot，但只做 A + C 的最小版本。**
B 與 D 先停在 roadmap。不要讓第一篇長成一個「什麼都想解釋」的大系統。

[1]: https://arxiv.org/abs/2404.16130 "[2404.16130] From Local to Global: A Graph RAG Approach to Query-Focused Summarization"
[2]: https://staff.fnwi.uva.nl/m.derijke/wp-content/papercite-data/pdf/wallat-2025-correctness.pdf "Correctness is not Faithfulness in Retrieval Augmented Generation Attributions"
[3]: https://link.springer.com/article/10.1007/s41060-025-00911-y "GAME+: lossless knowledge-graph compression for improving the efficiency and effectiveness of rule mining | International Journal of Data Science and Analytics | Springer Nature Link"
[4]: https://aclanthology.org/2025.emnlp-main.1249/ "Large Language Models Meet Knowledge Graphs for Question Answering: Synthesis and Opportunities - ACL Anthology"
[5]: https://aclanthology.org/2025.acl-long.740/ "Efficient Long Context Language Model Retrieval with Compression - ACL Anthology"
[6]: https://arxiv.org/abs/2507.13396 "[2507.13396] DyG-RAG: Dynamic Graph Retrieval-Augmented Generation with Event-Centric Reasoning"
[7]: https://aclanthology.org/2025.findings-naacl.55/ "Ground Every Sentence: Improving Retrieval-Augmented LLMs with Interleaved Reference-Claim Generation - ACL Anthology"
[8]: https://aclanthology.org/2020.emnlp-main.609/?utm_source=chatgpt.com "Fact or Fiction: Verifying Scientific Claims"
[9]: https://arxiv.org/html/2605.28044v1 "Relevant Is Not Warranted: Evidence-Force Calibration for Cited RAG"

