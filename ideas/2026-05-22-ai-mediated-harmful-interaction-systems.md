# AI-Mediated Harmful Interaction Systems

Canonical Idea OS record: `ideas/structured/idea_000035_ai_mediated_harmful_interaction_systems.yaml`

## First Principle

The useful object is not a translated sentence or a scam label. The useful object is how an interaction changes a decision process over time.

Animal communication, ancient-script decipherment, ASR-heavy voice systems, and scam detection share the same bottleneck: surface tokens are incomplete evidence. Meaning often appears through sequence, context, response, and outcome.

## Research Turn

This shifts the research question from:

- Is this message a scam?
- What does this signal mean in human language?
- Can the model classify this text correctly?

to:

- What function does this interaction appear to serve?
- What state change follows this signal?
- Is trust, urgency, dependency, isolation, or verification behavior changing over time?
- Can a reviewer reconstruct the evidence without trusting a black-box label?

## Why This Matters

Traditional scam detection is fragile because it learns yesterday's scripts. Adaptive manipulation systems learn the person.

The deeper risk is not only fake text. It is AI-mediated interaction that can observe hesitation, emotion, uncertainty, social ties, and resistance, then adjust the persuasion policy in real time.

That makes the research object closer to a harmful interaction system than a content classifier.

## What We Have Not Discussed Enough

1. Influence is not binary. Advertising, fandom, investment groups, politics, religious recruitment, coaching, sales, and romance scams can sit on the same influence gradient.
2. Time is central. A first contact can be benign, while the 30-day trajectory creates dependency, isolation, and extraction pressure.
3. Full semantic understanding may be unnecessary. The system may only need to model which trajectory predicts risky outcomes and why.
4. ASR and translation errors are not just preprocessing noise. They can shift embeddings enough that token-first systems fail while trajectory features remain useful.
5. Human review is the scarce resource. The system should optimize reviewer-useful evidence per minute, not autonomous certainty.
6. The governance boundary is part of the idea. The output should support influence transparency and review, not final scam determinations or enforcement.

## Smallest Next Test

Build a 12-trajectory synthetic fixture:

- benign mentorship
- aggressive but legal marketing
- political or community persuasion
- emotional dependency without money extraction
- scam-like investment escalation
- romance or trust-grooming escalation
- private-channel migration
- voice-note or noisy-ASR variants
- hard negatives where urgency is legitimate
- hard negatives where authority is legitimate
- slow escalation without keywords
- explicit extraction after a long warm-up

Annotate turns for authority, urgency, isolation, verification, challenge response, dependency, commitment, and outcome. Then compare keyword, single-message embedding, and trajectory-feature baselines.

The pass condition is not "detect all scams." The pass condition is: surface review-worthy risk earlier, explain the trajectory evidence, preserve benign hard negatives, and reduce reviewer time.

## Complete 2026-05-22 Follow-Up Record

可以，而且這條線應該比「詐騙偵測」再往前推一步。

你不是只是在做 scam detector。你其實是在研究：

> 人類決策過程如何被互動系統逐步改寫。

這比 scam detector 大很多，也更有研究價值。近期公開研究也正在往這個方向靠近。例如 PreScam 明確把 conversational scam 視為跨多輪逐步升級的操控過程，而不是單句分類。它把大量 user-submitted scam reports 結構化成 conversational scam instances，標註 scam lifecycle、scammer psychological actions、victim responses，並指出 current models 仍然很難追蹤 risk 如何跨 turns 升級。

## Central Claim

English:

> Scam-like harm should be modeled as a longitudinal influence trajectory that erodes decision autonomy, rather than as a static text classification problem.

中文：

> 詐騙式傷害應被建模為逐步侵蝕決策自主性的互動軌跡，而不是單點文字分類問題。

## Not Just Scam Detection

傳統 scam detection 常問：

- 這句話是否像詐騙？
- 這個帳號是否可疑？
- 這個 post 是否該被分類為 scam?

但這個方向真正要問的是：

- 這段互動是否讓人越來越難暫停？
- 是否讓人越來越難找外部驗證？
- 是否讓人越來越依賴單一 authority？
- 是否讓人越來越不好意思退出？
- 是否把懷疑重新解釋成受害者自己的問題？
- 是否逐步把普通關係轉成 secrecy、money、credential、privacy、action extraction？

這個研究物件可以叫做 decision-autonomy erosion。

## Decision Autonomy Erosion

真正危險的不是某句話像不像詐騙，而是對方是否讓你越來越少能自由判斷：

- 越來越不能問外部意見
- 越來越急
- 越來越依賴對方
- 越來越不好意思退出
- 越來越相信單一 authority
- 越來越把懷疑解釋成自己的問題

這不是普通 NLP label。這是互動對人的決策自由造成壓縮。

## Temporal Interaction Graph

這個 repo 之後真正需要的不是 post graph，也不是 keyword graph，而是 temporal interaction graph。

基本節點可以包括：

- person or account
- channel
- claim
- authority source
- commitment
- verification source
- money, credential, privacy, or action request

基本邊可以包括：

- trust transfer
- channel migration
- authority delegation
- urgency escalation
- verification suppression
- challenge deflection
- dependency reinforcement
- commitment escalation
- extraction attempt

時間軸很重要，因為很多真實詐騙不是第一天就危險，而是：

- 第 1 天正常
- 第 10 天建立信任
- 第 20 天開始 isolate
- 第 30 天才要求投資、匯款、credential、隱私或行動

所以方法不能只看單點 message。

## Hard Negatives Are Central

最重要的 benchmark 不是 scam positive，而是 hard negative。

如果沒有 hard negative，系統會變成道德恐慌機器。它會看到 urgency 就喊 scam，看到 authority 就喊 scam，看到 intimacy 就喊 scam。

必須放進 fixture 的 hard negatives：

- 正常 mentor 給 urgent 但合法的建議
- 家人在真實急難中請求匯款
- 合法行銷或 sales funnel，且有清楚 opt-out
- 投資教育，但沒有 private extraction 或 verification suppression
- 政治或社群動員，但有公開 accountability
- 宗教或支持社群招募，但沒有 isolation 或 secrecy
- 情緒支持關係，但沒有金錢、秘密或依賴剝削
- 合法專業 authority，且鼓勵 second opinion

好的系統不能只看 urgency、authority、emotion、privacy。它要看這些訊號是否一起形成 trajectory pattern，例如：

> isolation + verification suppression + authority concentration + commitment escalation

## Safety Boundary

這條線很敏感，因為它很容易從防禦研究滑向 manipulation playbook。

研究輸出應該是：

- defensive rubric
- reviewer-assist schema
- influence transparency label
- reconstructable evidence trail
- synthetic or consent-safe fixture
- aggregate-only reporting when linked to real data

不要輸出：

- 如何更有效操控人
- 如何繞過懷疑
- 如何個人化詐騙腳本
- 如何讓受害者更難退出
- 如何逃避平台審查
- 自動判定誰是詐騙犯
- enforcement、takedown、public warning、accusation

系統輸出應該是 reviewer-facing influence transparency signal，不是 final scam determination。

## Why This Connects To TFSC

這其實跟 TFSC 很深地相連。

TFSC 目前的核心語彙包括：

- review scarcity
- reconstructability
- runtime governance
- institutional overload
- agentic AI

這個新 idea 補上的點是：

> AI 最危險的地方不只是生成錯誤內容，而是它可以動態調整互動策略，逐步改變人的 decision process。

如果 AI 詐騙或 AI persuasion system 可以根據人的 hesitation、emotion、uncertainty、personality、social ties 即時調整，它就不只是 fake content problem，而是 adaptive manipulation system。

這會讓治理問題從「內容真假」升級成：

- 誰能重建互動如何升級？
- 誰能判斷決策自主性何時被侵蝕？
- 哪些證據能讓 human reviewer 不用讀完整長對話也能判斷？
- institution 是否有足夠 review capacity 處理這類 runtime interaction harm？

## Comparative Advantage

這個方向適合你，不是因為你現在有最大模型，而是因為你同時有幾個少見組合：

- cybercrime
- governance
- AI systems
- review systems
- organizational failure
- real-world deployment
- ASR and multimodal uncertainty
- reconstructability and evidence trail thinking

很多 ML researcher 會做 classifier，但不懂制度與 reviewer burden。

很多治理研究者會講風險，但不懂模型、ASR、embedding、pipeline。

很多資安人會抓 indicators，但不一定會看 interaction dynamics。

你的可貢獻位置是把這些合成一個 reviewer-reconstructable harmful-interaction framework。

## Recommended Next Experiment

不要先找大資料，也不要先訓練模型。先做一個小型 synthetic fixture。

建立 12 條 30-day interaction trajectories，每條 20-40 turns，包含：

- benign mentorship
- aggressive but legal marketing
- political or community persuasion
- emotional dependency without money extraction
- scam-like investment escalation
- romance or trust-grooming escalation
- private-channel migration
- voice-note or noisy-ASR variants
- hard negatives where urgency is legitimate
- hard negatives where authority is legitimate
- slow escalation without keywords
- explicit extraction after a long warm-up

每個 turn 標註：

- actor
- channel
- authority
- urgency
- isolation
- verification
- challenge response
- dependency
- commitment
- outcome

第一個研究問題：

> Do trajectory features surface review-worthy risk earlier and more reconstructably than keyword or single-message embedding baselines?

中文：

> trajectory features 是否比 keyword / single-message embedding 更早、更可解釋地提示 review-worthy risk？

評估指標：

- early risk surfacing
- hard-negative false-positive pressure
- reviewer reconstructability
- reviewer time per useful candidate
- preservation of uncertainty
- whether the system outputs watch / ask for context / park / human review instead of scam / not scam

## Scope Lock: 2026-05-22

先鎖定：

> AI-mediated harmful interaction trajectory modeling

只做一件事：

> interaction structure reconstruction

先不碰 semantics。先不做 LLM fine-tuning。先不做 scam classifier。先不把主軸放在 embedding retrieval。

第一階段只研究：

- interaction phase transition
- escalation dynamics
- trust-state evolution

換句話說，下一步不是立刻問「怎麼辨識詐騙」，而是重新定義：

> 什麼是 harmful interaction dynamics？

## Why The Scope Must Be Narrow

現在這個方向站在三條路的交叉口：

1. NLP / ASR engineering
2. scam detection
3. AI-mediated interaction governance

前兩個很多人做。第三個比較少，也更接近你的優勢。

如果現在直接跳進 LLM fine-tuning、scam classifier、embedding retrieval，很容易變成又一個 AI 偵測系統。那不容易做出 TFSC 等級的東西。

真正應該往下挖的是：

> interaction systems 如何在 scale 下改變人類 decision process。

但這個大問題不能一開始就全做。第一個窄切口應該是：

> reconstruct interaction structure before semantics.

## Five-Layer Research Plan

### Layer 1: Problem Definition

先不要問：

> 怎麼辨識詐騙？

先問：

> 什麼是 harmful interaction dynamics？

這一層的產物是 interaction primitive taxonomy。

可能 primitives：

- urgency escalation
- authority assertion
- emotional synchronization
- dependency reinforcement
- verification suppression
- isolation transition
- reciprocity imbalance
- reward baiting
- uncertainty masking
- compliance steering

這些是 interaction building blocks。要像協議逆向工程那樣看人類互動，而不是像一般 NLP classification。

### Layer 2: Structure Before Semantics

不要先掉進「理解語言」這個大坑。

很多時候 structure 比 semantics 穩定：

- 詐騙者可以換詞
- 可以換語言
- 可以換題材
- 可以從投資換成戀愛、AI 創業、靈性成長

但 escalation pattern、pressure timing、trust-building sequence、migration path 比較難完全換掉。

這一層研究 conversation topology：

- turn-taking
- response latency
- question avoidance
- topic transition entropy
- conversational dominance
- channel migration path
- commitment request timing
- emotional phase transition

這些可以先作為 semantics-light features。

### Layer 3: Temporal Modeling

真正的 manipulation 是長時間演化，不是單句。

可以把關係當成 latent state machine：

```text
stranger -> rapport_building -> trust_established -> emotional_attachment -> isolation -> commitment_pressure -> extraction_attempt
```

研究問題變成：

- 哪些 structural signals 讓關係進入更高壓狀態？
- 哪些 signals 開始 suppress verification？
- 哪些 signals 增加 dependency？
- 哪些 signals 出現在 extraction 之前？

這會導向：

- temporal graph
- sequential influence modeling
- hidden-state evolution
- behavioral trajectory prediction
- state-transition system

### Layer 4: Institutional Capacity

這是 TFSC 味道最強的地方。

大部分人研究 fake content、misinformation、scam detection，但比較少人研究：

> 當 interaction scale 超過 review capacity 時，制度如何崩潰？

這一層才開始接：

- AI interaction scaling law
- review scarcity threshold
- institutional overload dynamics
- governance latency
- reconstructability decay

這時候研究物件從 AI classifier 變成 sociotechnical system。

### Layer 5: Simulation

simulation 是後面真正可能有 impact 的方向，但不是第一步。

未來可以建立 large-scale interaction simulation。agent 可以有：

- trust
- fatigue
- review capacity
- emotional susceptibility
- social connectivity
- verification behavior

然後觀察在不同 AI interaction density 下：

- 哪種制度先壞掉
- 哪種 review system 最先 overload
- 哪種 governance latency 最危險
- reconstructability 何時崩潰

這會比只追求 scam accuracy 更接近高價值研究。

## Knowledge To Build Over The Next Year

### A. Interaction And Social Dynamics

這塊目前需要補，因為這個研究其實不是文字，而是 human decision steering。

需要碰：

- persuasion theory
- behavioral economics
- social psychology
- influence dynamics
- cult recruitment
- trust systems
- cognitive overload

### B. Complex Systems

institutional collapse 本質上是 complex system problem。

需要碰：

- network science
- system dynamics
- graph processes
- emergence
- agent-based modeling

### C. Representation Learning

這是技術底座，但不是主角。

需要懂：

- contrastive learning
- self-supervised learning
- sequence representation
- latent dynamics
- multimodal alignment

重點不是追 SOTA model，而是：

> representation 如何對應 interaction structure。

## Scope Explosion Risk

最大風險是 scope explosion。

這個方向很容易把以下全部捲進來：

- world model
- AGI
- social governance
- scam detection
- ASR
- NLP
- agent
- LLM

這樣會失焦。

所以現在的 anti-scope rule 是：

> If a proposed next step does not improve structure reconstruction, phase-transition detection, escalation modeling, or trust-state tracking, park it.

短期不要做「全世界 AI interaction governance」。先只做：

> AI-mediated harmful interaction trajectory modeling through interaction structure reconstruction.

這樣才比較可能做出一篇強 paper。

## Sources Checked On 2026-05-22

- PreScam: A Benchmark for Predicting Scam Progression from Early Conversations, arXiv 2605.12243: https://arxiv.org/abs/2605.12243
- On the conversational persuasiveness of GPT-4, Nature Human Behaviour: https://www.nature.com/articles/s41562-025-02194-6
- The potential of generative AI for personalized persuasion at scale, Scientific Reports: https://www.nature.com/articles/s41598-024-53755-0
- Love as Bait: A Scoping Review and Crime Script Analysis of Online Romance Scams: https://journals.sagepub.com/doi/10.1177/15248380251361046
- Internet fraud transaction detection based on temporal-aware heterogeneous graph oversampling and attention fusion network, PLOS One: https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0337208
