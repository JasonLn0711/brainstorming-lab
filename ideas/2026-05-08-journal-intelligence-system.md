# Journal Intelligence System

Date: 2026-05-08

Canonical YAML:

```text
ideas/structured/idea_000014_journal_intelligence_system.yaml
```

## First-Principle Read

The scarce resource is not access to more papers. The scarce resource is
submission cycles, reviewer trust, and revision energy.

Author guidelines explain the formal boundary. Recent accepted papers reveal
part of the venue culture:

- what claims are allowed to sound strong
- what evidence is considered enough
- what figures reviewers expect to inspect
- what novelty type the journal rewards
- what failure modes the editor/reviewer ecosystem fears
- what citation tribe and terminology the venue lives inside

The useful object is not a PDF pile. The useful object is a venue-fit
calibration packet that can change a manuscript before submission.

## Core Idea

Use recent accepted Open Access papers from a target journal to reverse-engineer
latent venue standards.

This does not replace:

- author guidelines
- ethical publishing rules
- scientific quality
- advisor judgment
- real reviewer feedback

It adds an evidence-driven layer:

```text
author guide + recent accepted OA papers + citation ecosystem
-> journal culture brief
-> latent scoring matrix
-> manuscript compatibility report
-> revision priorities
```

## What To Extract

### Claim Style

Measure whether accepted papers tend to say:

- `We propose`
- `We investigate`
- `We analyze`
- `We demonstrate`
- `may`
- `could`
- `practical`
- `operational`
- `real-world`

For forensic, medical, and security venues, aggressive language can create risk.
Conservative language may be a trust signal.

### Figure Style

Track:

- figure count
- architecture diagrams
- workflow diagrams
- evidence trace tables
- qualitative case studies
- ablation charts
- graphical abstracts
- large overview figures

Figure style is often a hidden venue-fit signal. It reveals what evidence the
reviewer expects to see at a glance.

### Evidence Density

Track:

- baseline count
- ablation count
- failure analysis
- limitation section
- threat model
- supplementary material
- reproducibility assets
- appendix length

This approximates the venue's minimum credibility threshold.

### Novelty Type

Classify accepted papers by the type of novelty they reward:

- engineering novelty
- forensic novelty
- governance novelty
- evaluation novelty
- theoretical novelty
- application-impact novelty

This matters because "novelty" is not one thing. FSI:DI-style venues may value
forensic defensibility and evidence workflow more than model architecture.

### Reviewer Fear Points

The higher-level question is not only what the journal likes. It is what the
journal fears.

Possible fear points:

- overclaim
- unverifiable evidence
- unrealistic simulation
- AI hallucination
- non-reproducible workflow
- weak forensic defensibility
- missing operational boundary
- unsupported generalization

Repeated limitation wording, conservative claims, traceability language, and
reproducibility emphasis can expose the reviewer ecosystem's defense mechanism.

### Citation Ecosystem

Track recurring:

- authors
- venues
- methods
- terminology
- datasets
- skepticism patterns
- evaluation philosophy

A journal is not only a publisher. It is an editor, reviewer tribe, accepted
narrative style, and citation ecosystem.

## First Calibration Packet

For one target journal, collect 8-12 recent accepted Open Access papers plus the
official author guide.

Create a CSV with:

```text
paper_id
year
article_type
claim_style
figure_style
evidence_density
novelty_type
reviewer_fear_points
reproducibility_assets
limitation_style
compatibility_lessons
```

Then write a short journal culture brief:

- formal scope
- accepted contribution patterns
- common evidence shape
- claim-language boundary
- figure/table expectation
- top reviewer fear points
- likely rejection risks
- revision checklist for our manuscript

## Reviewer Emulator

Input:

```text
paper.md
target journal
journal culture packet
```

Output:

```text
Venue compatibility: 0-100
Main risks:
- overclaim risk
- evidence-density gap
- figure/table gap
- reproducibility gap
- novelty-type mismatch
- missing limitation or threat-model discussion
Revision priorities:
- strengthen
- soften
- add
- remove
- reframe
```

## FSI:DI Fit

This is especially useful for FSI:DI because the venue likely cares about:

- forensic defensibility
- traceability
- reproducibility
- conservative claims
- failure analysis
- operational realism
- governance boundary
- evidence integrity

The first concrete test should reuse the existing FSI:DI latest-OA calibration
work and turn it into a reusable journal-culture brief.

## Safety Boundary

Use only public OA papers, official guidelines, and legitimate metadata.

Do not:

- bypass paywalls
- scrape private reviewer/editor systems
- claim hidden reviewer identity
- claim guaranteed acceptance
- pretend OA samples fully represent the whole journal

Separate:

- observed evidence
- inferred pattern
- uncertainty
- revision implication

## Smallest Next Test

Build one FSI:DI venue-culture calibration packet from 8-12 recent accepted OA
papers plus the official author guide.

Done condition:

- one CSV pattern matrix
- one 1-2 page journal culture brief
- one compatibility checklist for the current FSI:DI manuscript line
- one decision: proceed, revise-first, park, or choose another venue

## Method Decision: Do Not Start With Deep Learning

Machine learning and deep learning are possible later, but they are not the
first move.

The first 80% of value is not the classifier. It is:

- feature engineering
- rubric design
- scientometric thinking
- reviewer psychology modeling
- latent structure extraction
- deciding what is worth observing

The common failure mode is too-early AI:

```text
3000 papers -> embeddings -> clustering -> LLM summary
```

The output often becomes:

```text
This journal values rigorous experiments.
```

That is too abstract. It does not tell us what to strengthen, soften, add,
remove, or reframe in the manuscript.

Reviewer-sensitive signals often live in small details:

- claim wording
- limitation placement
- figure order
- appendix density
- operational boundary wording
- `we deploy` vs `we simulate`
- evidence-chain description
- failure-analysis placement

If those features are not defined first, AI will often miss the useful signal.

## Journal Forensic Framework

The first phase should be a quantifiable observation system:

```text
schema + rubric + feature extraction + human interpretation
```

Seed schema:

| Category | Feature |
| --- | --- |
| claim | aggressive / conservative / investigative |
| evidence | weak / moderate / strong / traceable |
| reproducibility | code, protocol, parameters, dataset availability |
| dataset realism | synthetic / public / private / operational |
| figures | workflow, table, chart, case study, architecture, evidence trace |
| evaluation | ablation, baseline, statistical test, failure analysis |
| language | may, could, practical, deploy, prove, demonstrate |
| trust signals | limitation, threat model, governance boundary, operational realism |

This is closer to forensic investigation than generic paper summarization.

The hard question is:

```text
What should be observed?
```

not:

```text
Which model should classify the papers?
```

## Accepted Manifold, Not Acceptance Prediction

This idea is better framed as latent reviewer space extraction.

We usually have:

```text
accepted papers
```

but not:

```text
rejected papers + reviewer comments
```

So supervised acceptance prediction is structurally weak. The data has serious
selection bias.

Instead, estimate an accepted-paper distribution:

- what accepted papers sound like
- what evidence they contain
- what they avoid claiming
- what figures they use
- what risks they preempt
- what limitations they acknowledge

Then compare our draft against that distribution.

The goal is not:

```text
acceptance probability = 0.71
```

The goal is:

```text
High reviewer risk:
- insufficient threat model
- weak operational boundary
- overclaim wording
- no failure vignette
- synthetic realism not defended enough
```

That output is more honest and more useful.

## Hybrid Intelligence

The practical architecture should be:

```text
rule-based extraction + LLM assistance + human scientific interpretation
```

Layer 1: metadata extraction.

- title
- abstract
- keywords
- section structure
- figure count
- table count
- appendix
- supplementary material

Layer 2: scientific feature extraction.

- claim aggressiveness
- evidence density
- reproducibility
- operational realism
- limitation style
- reviewer fear points

Layer 3: human interpretation.

Reviewer culture is context-dependent. FSI:DI may react very differently to a
synthetic dataset than NeurIPS, IEEE TIFS, or a general AI journal.

AI can assist the extraction, but the interpretation has to remain scientific
and domain-aware.

## When ML Becomes Useful

ML becomes useful after the schema stabilizes and there are enough calibrated
examples.

Useful later layers:

- embedding-based nearest accepted-paper search
- clustering accepted papers into contribution families
- topic drift detection
- novelty fatigue detection
- draft-to-venue similarity ranking
- reviewer-risk retrieval from prior calibration packets

Example:

```text
Input: paper_draft.md
Output: Top-10 nearest accepted papers and the main structural differences
```

That is useful because it supports revision, not because it pretends to know the
future editorial decision.

## Cram-School Risk

There is a shallow version of this idea:

```text
study what reviewers like -> imitate accepted papers -> raise acceptance odds
```

That is cram-school submission engineering.

Its behaviors are:

- copying accepted-paper format
- guessing reviewer preferences
- applying fixed templates
- optimizing for acceptance probability
- asking "will reviewers like this?" before asking "is this true and important?"

This is dangerous because it can slowly remove the research soul from the work.

The better version is not reviewer appeasement. It is scientific ecosystem
awareness.

## Deeper Version: Scientific Ecosystem Awareness

The deeper question is:

```text
How does this scientific community decide what counts as credible knowledge?
```

That opens stronger questions:

- Why are some ideas accepted and others resisted?
- Which evidence types count as trustworthy here?
- Which claims are considered overreach?
- Which uncertainty does this community try hardest to reduce?
- Which important problems are invisible because they do not fit the reviewer
  mental model?
- Does the accepted literature contain a structural blind spot?

Scientific writing is not only formal English. It is a trust-building protocol.

Limitation sections, threat models, conservative wording, reproducibility
details, ablation studies, failure analysis, and evidence traceability all help
reduce collective uncertainty.

So the best use of this system is not:

```text
How do I make this look like an accepted paper?
```

It is:

```text
What does this community currently trust, fear, reward, and fail to see?
```

That makes the idea closer to:

- meta-research
- scientometrics
- sociology of science
- philosophy of science
- computational analysis of scientific culture
- reviewer ecosystem modeling

## Working Name

`AI-assisted scientific publishing intelligence` is not a standard term yet.

Working definition:

```text
A human-AI workflow for extracting actionable submission strategy and scientific
ecosystem insight from accepted papers, journal guidelines, citation networks,
evidence standards, and reviewer-risk patterns.
```

Natural Chinese names:

- AI 輔助科學出版情報分析
- 期刊投稿情報系統
- 期刊文化反推系統
- reviewer ecosystem modeling
- acceptance pattern intelligence

## 科學知識如何被社群接受與建立信任

高中生版本：

```text
科學不是「一個人發現真相」就結束。
一個想法要經過很多人檢查、質疑、重做、引用、應用，
才會慢慢變成社群願意暫時相信的知識。
```

所以論文被接受，不只是寫得漂亮。更像是：

```text
把一個想法放進公共檢查系統，讓一群專業但懷疑的人判斷：
這件事值不值得暫時相信？
```

科學社群建立信任，大概靠五件事。

### 1. 問題重要

這個研究有沒有解決真問題？

例如：

- 醫學研究不是只問模型準不準，也問能不能幫助病人。
- 資安研究不是只問偵測率多高，也問能不能對真實攻擊有用。
- 數位鑑識研究不是只問技術新不新，也問能不能在證據流程中站得住腳。

### 2. 方法可信

資料、實驗、推論有沒有站得住腳？

例如：

- 醫學要看樣本數、統計方法、倫理審查。
- 資安要看 threat model、attack scenario、baseline。
- AI 要看 benchmark、ablation、robustness。
- 數位鑑識要看 evidence trace、chain of custody、procedure transparency。

### 3. 結果可重現

別人照著做，是否能得到類似結果？

如果不能完全重現，至少要能知道為什麼不能：

- 資料不公開？
- 實驗環境不同？
- 參數沒有寫清楚？
- 方法太依賴特定場景？

可重現不是形式而已，它是信任的基礎設施。

### 4. 說法克制

作者有沒有清楚說明限制？

例如，危險寫法：

```text
This model works in real-world forensic investigation.
```

比較可信的寫法：

```text
In these controlled scenarios, the method improves trace consistency,
but its performance under live investigation workflows remains untested.
```

克制不是變弱，而是讓 reviewer 看見你知道證據的邊界。

### 5. 社群驗證

其他研究者是否願意：

- 引用它
- 延伸它
- 挑戰它
- 重做它
- 應用它

科學知識不是一次審稿就完成。它是在後續引用、重現、修正、失敗、應用中慢慢變穩。

## 我們應該怎麼做

對投稿與研究訓練來說，可以用三個問題。

### 問題一：這個社群目前在害怕什麼？

FSI:DI、數位鑑識、資安、AI safety 這些領域，reviewer 可能害怕：

- 你講太滿
- 資料不可驗證
- 模擬資料太假
- 系統無法重現
- AI 結果沒有證據鏈
- 實務場景說得很大，實驗卻很小

所以 paper 要主動回答：

```text
為什麼我值得被相信？
```

這有時比「我的方法很新」更重要。

### 問題二：這個領域用什麼方式建立信任？

不同領域相信不同證據。

醫學研究常看：

- clinical trial
- sample size
- statistical significance
- ethics review
- external validation

資安研究常看：

- threat model
- attack scenario
- reproducible experiment
- baseline comparison

數位鑑識常看：

- evidence trace
- chain of custody
- procedure transparency
- limitation

AI 研究常看：

- benchmark
- ablation study
- baseline
- robustness test
- error analysis

投稿前要先知道：

```text
這個社群相信哪一種證據？
```

### 問題三：我的論文能不能被別人檢查？

成熟論文要留下檢查路徑：

- 資料怎麼來？
- 方法怎麼做？
- 為什麼這樣設計？
- 失敗案例在哪裡？
- 什麼情況下不能用？
- 別人要怎麼重現？

這些就是 trust infrastructure。

## Meta-Research 是什麼

`meta-research` 可以翻成「研究研究本身」。

高中生版本：

```text
不是在考數學，而是在研究考試制度是否公平、題目是否偏、
老師改分是否一致、大家是不是只公布高分結果。
```

它研究的是科學制度本身：

- 研究是否可重現？
- 期刊是否偏好驚人結果？
- 統計方法是否被誤用？
- benchmark 是否失真？
- reviewer 是否有偏差？

現實例子：

### 心理學 replication crisis

有些心理學研究曾經很有名，但其他實驗室重做後做不出來。

meta-research 會問：

- 原研究樣本太小嗎？
- 統計方法有問題嗎？
- 期刊是不是太愛新奇結果？
- 失敗重現的研究是不是比較難被發表？

### Publication Bias

假設 100 個團隊測某個藥，5 個做出有效結果，95 個沒有結果。

如果期刊只刊那 5 個，世界會誤以為：

```text
這個藥看起來很有效。
```

meta-research 研究的就是這種制度偏差。

### AI Benchmark 濫用

如果所有模型都在同一份資料集上刷分，久了之後模型可能只是很會考那份考卷。

meta-research 會問：

```text
這個 benchmark 還代表真實能力嗎？
```

## Philosophy Of Science 是什麼

`philosophy of science` 是科學哲學。

高中生版本：

```text
它不是問答案是多少，而是問：
為什麼這種方法可以算答案？
什麼叫做證據？
什麼叫做解釋？
我們怎麼知道一件事是真的？
```

現實例子：

### Popper 的可反駁性

如果一個理論永遠不可能被證明錯，它就很難算科學理論。

危險說法：

```text
This model works well in all situations.
```

比較科學的說法：

```text
In these three datasets and under these conditions, the model outperforms
the baseline, but performance drops in low-resource cases.
```

因為後者可以被檢查、被反駁、被改進。

### Kuhn 的典範轉移

牛頓力學曾經是理解世界的主流框架。

後來相對論、量子力學出現，大家對世界的理解方式改變了。

AI 也有類似變化：

- feature engineering
- deep learning
- representation learning
- LLM
- agents and tool use

每一次變化都會改變研究者覺得「正常方法」是什麼。

### 解釋問題

醫療 AI 裡，模型準確率高還不夠。

醫生會問：

```text
你為什麼說這是癌症？
你看的是病灶，還是影像角落的醫院標記？
```

這就是科學哲學裡的 explanation problem。

## Sociology Of Science 是什麼

`sociology of science` 是科學社會學。

高中生版本：

```text
科學世界也像一個班級或社團。
有規則、老師、學長姐、流行題目、資源分配、名聲差異，
也有誰比較有話語權的問題。
```

它研究科學作為一個人類制度：

- funding
- reputation
- journal gatekeeping
- lab hierarchy
- trend
- community language
- career incentives

現實例子：

### 熱門題目吸走資源

LLM 熱門時，funding、paper、conference attention 都往 LLM 靠。

重要但不流行的題目可能比較難被看見。

### 名校與大實驗室優勢

同樣一個 idea，如果來自 MIT、Stanford、Google DeepMind，可能更容易得到初始注意力。

小實驗室不是不能做，但通常要花更多力氣證明自己。

這就是 reputation effect。

### 跨領域研究卡住

你做：

```text
AI + digital forensics + legal governance
```

可能遇到：

- AI reviewer 覺得模型不夠新
- forensics reviewer 覺得 evidence chain 不夠嚴謹
- law reviewer 覺得制度分析不夠深

跨領域困難不只是技術問題，也是社群語言與信任標準不一致。

## Computational Scientometrics 是什麼

`scientometrics` 是科學計量學。

`computational scientometrics` 是用資料分析、NLP、圖分析、AI 方法研究大量科學文獻。

高中生版本：

```text
把很多很多篇論文當成資料，分析科學界正在往哪裡走。
```

它會看：

- 哪些主題變熱門
- 哪些作者常合作
- 哪些論文被大量引用
- 哪些期刊偏好哪些主題
- 哪些關鍵字正在上升
- 哪些研究群形成小圈圈

現實例子：

### AI Agent 趨勢

收集 2021-2026 年論文，統計：

- agent
- tool use
- RAG
- multi-agent
- workflow automation

看這些詞是否真的上升。

### Citation Network

如果很多 paper 都引用同一篇基礎論文，它可能是該領域的核心節點。

在 cybersecurity 裡，threat modeling、zero trust、malware analysis 的核心論文可能形成引用網路。

### 找研究空白

假設很多人做 phishing detection，也很多人做 LLM security。

但很少人做：

```text
AI agent 在詐騙偵查工作流中的 forensic traceability
```

那可能就是研究機會。

## Reviewer Ecosystem Modeling 是什麼

`reviewer ecosystem modeling` 是我們從這個 idea 延伸出的工作概念。

意思是：

```text
把 reviewer、editor、期刊、引用網路、accepted paper 風格，
看成一個互相影響的生態系，
分析它怎麼決定什麼研究值得被相信。
```

高中生版本：

```text
不只看考試規則，也觀察老師怎麼出題、怎麼改分、
歷屆高分作文長什麼樣，哪些錯誤常被扣分。
```

但這裡有一條重要界線。

淺層用法：

```text
模仿高分作文，猜老師喜歡什麼。
```

這是補習班思維。

深層用法：

```text
理解這個知識社群如何建立標準、如何管理不確定性、
如何判斷什麼證據可以被信任。
```

這才是科學社群分析。

現實例子：

### FSI:DI

分析近年 FSI:DI 論文後，可能看到：

- 重視 evidence handling
- 討厭 overclaim
- 喜歡清楚的 forensic workflow
- 可以接受系統方法，但要說清楚實務限制
- 對 synthetic data 比較敏感

這不是投機取巧，而是在理解：

```text
數位鑑識社群如何建立可信度？
```

### 醫療 AI 期刊

醫療 AI reviewer 可能會看：

- 是否有臨床意義
- 是否有外部驗證
- 是否討論 bias
- 不同族群表現是否公平
- 是否能融入醫療流程

所以一篇 accuracy 很高的 paper 仍然可能不夠。

### 頂級 AI Conference

NeurIPS、ICML、ICLR 可能更重視：

- 方法新穎性
- 理論或實驗完整性
- 強 baseline
- ablation
- benchmark
- open-source code

它們的信任系統和 forensic journal 不一樣。

## Integrated Workflow

把這些整合成實作，可以是：

### Step 1: 選一個 target journal

例如 FSI:DI。

### Step 2: 收集近 2-3 年 accepted papers

第一輪不用全部。

可以先用：

- 8-12 篇做 calibration packet
- 30-50 篇做 trust-pattern scan

### Step 3: 建立分析表

每篇填：

- problem type
- method type
- data type
- evidence standard
- figure type
- limitation style
- claim strength
- reproducibility level
- operational scenario depth
- reviewer 可能接受它的原因

### Step 4: 找 trust pattern

問：

- 這個期刊相信什麼證據？
- 它不太信任什麼 claim？
- 它接受哪些 novelty？
- 它常要求作者補哪些防線？
- 哪些 paper 看起來像這個期刊的典型風格？

### Step 5: 回頭檢查自己的論文

健康問法不是：

```text
我要怎麼討好 reviewer？
```

而是：

```text
我的論文是否提供了這個社群需要的信任證據？
```

最短總結：

```text
科學知識被接受，不是因為它看起來厲害。
它被接受，是因為它能讓一群專業但懷疑的人，
找到足夠理由暫時相信它。
```
