# Expert Review Prompt

請你以「研究方向顧問 / 領域專家 / 博士研究委員」的角度，協助審查這份資料包，判斷我們是否應該把目前的 brainstorming 方向收斂成一條正式研究線：

```text
Knowledge Graph Compression + Small Language Models
```

目前我們更精準的候選 framing 是：

```text
Evidence-preserving compressed knowledge graphs for small-model decision stability.
```

請不要只用一般 GraphRAG、RAG、LLM summarization、KG QA 的既有框架來理解這份資料包。這份資料包想請你評估的是：我們能不能把「知識圖譜壓縮」重新定義成一種給小語言模型使用的、有證據邊界、有 provenance、有 uncertainty、有 decision-stability 評估的 bounded reasoning substrate。

## 你會收到的資料

資料包中包含以下檔案：

- `00_one_page_summary.md`
- `01_expert_brief.md`
- `02_research_directions.md`
- `03_source_map.csv`
- `04_expert_review_questions.md`
- `05_decision_matrix.md`
- `source-notes/`

請先讀：

1. `00_one_page_summary.md`
2. `01_expert_brief.md`
3. `02_research_directions.md`
4. `05_decision_matrix.md`

如果你需要追溯每個想法來源，再讀 `03_source_map.csv` 和 `source-notes/`。

## 我們希望你幫忙判斷的核心問題

我們現在有幾個互相關聯、但還沒有完全收斂的研究直覺：

1. Knowledge graph 不應該只是 retrieval index，而可以是給 SLM 使用的外部記憶與 reasoning substrate。
2. KG compression 不應該只是刪 node、刪 edge、做 summary，而應該保存 task-relevant reasoning path。
3. 對 expert decision support 來說，compression 後必須保存 provenance、source lineage、claim support、uncertainty、risk boundary。
4. Small language model 的價值可能不是「變成小型 GPT」，而是能在 compressed evidence graph 上做 bounded, auditable, stable reasoning。
5. 我們想避開普通的 GraphRAG 工程題目，找出更有研究辨識度的 scientific object。

請你判斷：這些直覺是否能形成一條有價值的研究方向？

## 請你特別評估的四個候選方向

### Direction A: Provenance-preserving KG compression for SLM reasoning

核心問題：

```text
What graph information must be preserved during compression so a small language model can answer with evidence discipline and avoid unsupported claims?
```

可能貢獻：

- 定義 provenance-preserving graph packet schema。
- 壓縮 KG 時保留 source lineage、uncertainty、claim support、graph risk。
- 評估 SLM 在 raw text、uncompressed graph、generic summary、compressed evidence graph 下的回答差異。

請評估：

- 這是否是一個清楚的 research object？
- 它和 GraphRAG / subgraph retrieval / summarization 有沒有足夠差異？
- 什麼 provenance 欄位是必須保存的？
- 第一個實驗應該用什麼資料域？

### Direction B: Pheromone-based dynamic KG compression

核心問題：

```text
Can reinforcement, diffusion, and decay select better graph substructures for small-model reasoning than static top-k retrieval?
```

可能貢獻：

- 把 graph edge 視為會隨使用、修正、任務需求而強化或衰退的 signal。
- 用 dynamic path utility 產生 SLM context packet。
- 保留 backup paths，避免壓縮後過早收斂到單一路徑。

請評估：

- 這比較像 KG compression、adaptive retrieval、agent memory，還是 graph signal processing？
- 它是否適合放在第一篇 paper？
- 它需要真實資料還是 synthetic graph 即可？
- 哪些 baseline 最公平？

### Direction C: Latent-state KG compression for decision support

核心問題：

```text
Can observable graph traces be compressed into latent-state representations that support more stable small-model decisions?
```

可能貢獻：

- 從 observable trace graph 推論 hidden state graph。
- 讓 SLM 在 compressed state representation 上做 bounded decision support。
- 評估 decision stability、label flip、unsafe downrouting、missed escalation。

請評估：

- 這條線應該作為主軸，還是作為 Direction A 的 downstream evaluation case？
- 如果要測 decision stability，最小可行資料集應該長什麼樣？
- 這個方向是否會比 KG compression 本身更容易被 reviewer 理解？

### Direction D: Low-resource symbolic KG compression

核心問題：

```text
Can compressed multimodal evidence graphs help a small model rank hypotheses in sparse symbolic domains without overclaiming?
```

可能貢獻：

- 以 ancient script / archaeology / sparse symbolic systems 作為低資源測試場。
- 要求 SLM 排列 hypotheses，而不是做 confident translation。
- 測試 compression 是否保存 artifact context、uncertainty、bibliography、sign co-occurrence。

請評估：

- 這是否太跳，還是反而能形成有辨識度的 testbed？
- 它適合作為第一篇 paper 嗎？
- 這個 domain 需要哪些專家或資料條件？

## 請你回答的主要問題

請依序回答以下問題。

### 1. Primary framing

請判斷這個研究方向最應該被 framing 成哪一種：

- Knowledge graph compression method
- Evidence-preserving context construction
- Small-model decision stability
- Provenance-aware GraphRAG
- Expert-support reasoning substrate
- Adaptive graph memory
- Hidden-state graph reasoning
- 其他你認為更準確的 framing

請說明你推薦的 framing，以及為什麼。

### 2. Scientific object

這個方向最應該保護的 scientific object 是什麼？

例如：

- compressed graph packet schema
- compression objective
- provenance retention under compression
- decision stability under compressed context
- latent-state representation
- SLM behavior under evidence-preserving context

請指出最值得變成 paper contribution 的核心 object。

### 3. Novelty and differentiation

請評估它和以下方向的差異：

- GraphRAG
- KGQA
- subgraph retrieval
- summarization / context compression
- agent memory
- retrieval-augmented small models
- provenance-aware RAG

請指出：

- 差異足夠的地方；
- 還不夠清楚的地方；
- 需要怎麼改 framing 才不會被 reviewer 認為只是工程組合。

### 4. First experiment

請設計你認為最小但有說服力的第一個實驗。

請包含：

- domain；
- data unit；
- graph schema；
- compression method；
- SLM task；
- baselines；
- metrics；
- expected result；
- failure condition。

請優先考慮 30 到 50 筆 records 就能啟動的實驗，而不是一開始就需要大型資料集。

### 5. Baselines

請列出 reviewer 會期待看到的 baseline。

候選 baseline 包括但不限於：

- raw text context + SLM；
- generic summary + SLM；
- top-k retrieved text + SLM；
- uncompressed graph neighborhood + SLM；
- random or centrality-based graph pruning；
- GraphRAG-style subgraph retrieval；
- larger LLM reference；
- human expert or rule-based reference。

請指出哪些 baseline 是 must-have，哪些可以放到 later work。

### 6. Metrics

請判斷哪些 metric 最重要。

候選 metric：

- answer correctness；
- unsupported-claim rate；
- provenance retention；
- citation lineage preservation；
- uncertainty preservation；
- decision stability；
- label flip rate；
- unsafe downrouting / missed escalation；
- human audit time；
- context token budget；
- compression ratio；
- calibration；
- expert usefulness。

請幫忙排序 primary / secondary / optional。

### 7. Domain choice

請判斷第一個 domain 應該選哪個：

- public web evidence provenance；
- cybercrime / scam-prevention public evidence；
- scientific-paper claim audit；
- journal intelligence / reviewer culture；
- ancient-script symbolic hypothesis ranking；
- synthetic high-stakes decision workflow；
- personal/expert external-memory system；
- 其他。

請考慮：

- 可取得性；
- 是否能公開；
- 是否需要 IRB / ethics review；
- 是否有專家可評；
- 是否能產生清楚 metric；
- 是否有 publishable relevance。

### 8. Claim boundary

請指出第一篇 paper 必須避免哪些 claim。

例如：

- 不要宣稱 SLM 驗證真相；
- 不要宣稱 compression universally improves reasoning；
- 不要宣稱 GraphRAG 已被取代；
- 不要宣稱 ancient scripts 被 deciphered；
- 不要宣稱任何 clinical/legal/security operational deployment readiness。

也請指出可以正向主張的 scope。

### 9. Paper type and venue fit

請判斷這比較像：

- method paper；
- dataset / benchmark paper；
- systems paper；
- evaluation paper；
- position / framework paper；
- domain application paper。

也請建議可能的社群或 venue 類型，例如：

- NLP / IR；
- KDD / WWW / WSDM；
- knowledge graph / semantic web；
- digital forensics；
- AI safety / trustworthy AI；
- HCI / decision support；
- digital humanities；
- information systems。

### 10. Publishability threshold

請用一句話說明：

```text
這個研究方向要變成 publishable，最低限度必須證明什麼？
```

## 請你最後提供一份決策建議

請用以下格式輸出你的結論。

```text
Recommended primary framing:

Recommended first paper title:

Best first domain:

Minimum viable experiment:

Must-have baselines:

Primary metrics:

Main novelty claim:

Claims to avoid:

Biggest technical risk:

Biggest reviewer risk:

Most promising venue/community:

Three-month action plan:

Decision:
[ ] pursue now
[ ] pursue after narrowing
[ ] park for later
[ ] reject / not enough research value
```

## 評分表

請你也給每個候選方向 1 到 5 分。

| Direction | Novelty | Feasibility | Evaluation clarity | Reviewer legibility | Fit to our strengths | Overall |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| A. Provenance-preserving KG compression |  |  |  |  |  |  |
| B. Pheromone-based dynamic KG compression |  |  |  |  |  |  |
| C. Latent-state KG compression |  |  |  |  |  |  |
| D. Low-resource symbolic KG compression |  |  |  |  |  |  |

請在表格後補充：

- 你最高分方向的理由；
- 你最低分方向的理由；
- 你會如何重組這四個方向成一條 coherent PhD research line。

## 回答風格

請直接、具體、嚴格。  
如果你認為某個方向其實只是 ordinary GraphRAG engineering，請明確指出。  
如果你認為某個方向有潛力但 framing 錯了，請提出更好的 framing。  
如果你認為第一個實驗太大，請把它縮成一個可以在 2 到 4 週內完成的 pilot。

