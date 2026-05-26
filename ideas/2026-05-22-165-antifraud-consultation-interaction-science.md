# 165 Antifraud Consultation Call Interaction Science

Canonical Idea OS record: `ideas/structured/idea_000036_165_antifraud_consultation_interaction_science.yaml`

## Core Reframe

如果手上真的有 30 小時的 165 反詐騙諮詢專線語音資料，第一步不是 train 大模型。

30 小時不算大。如果把它當成：

- ASR dataset
- speech classification dataset
- scam / not scam dataset

很快會撞牆，而且別人更大的 dataset 很多。

這份資料真正珍貴的地方是：

> high-value interaction data.

它捕捉的是人在懷疑、焦慮、混亂、被操控、求助時，與員警動態互動的真實過程。

尤其珍貴的是：

- officer side
- citizen / victim side
- dynamic questioning
- escalation process
- uncertainty evolution
- intervention timing
- acoustic stress and hesitation

所以第一個研究方向應該是：

> interaction science, not classification.

## Layer 1: Interaction Structure Mining

先不要管 scam type、keyword、sentiment。

先研究：

> 對話是怎麼演化的。

可以問：

- 民眾從什麼狀態開始打進來？
- 什麼時候開始相信員警？
- 哪些問題會讓資訊突然變多？
- 哪些問法會讓人 shutdown？
- 哪些 interaction pattern 常出現在高風險案件？
- 哪些 conversation trajectory 最終導向已經匯款？
- 哪些 trajectory 最終導向成功阻止？

這比較像 conversational state transition analysis，不是 NLP classification。

## Layer 2: Temporal Dynamics

詐騙本質是時間上的操控。

研究單位不應該是單句，而是：

> interaction trajectory.

可以用：

- 每 30 秒
- 每一輪 turn
- 每個 topic shift
- 每個 phase transition

去觀察 belief transition。

例如受害者可能從：

```text
相信投資老師 -> 開始猶豫 -> 開始焦慮 -> 求確認 -> rationalize -> 接受介入或繼續相信對方
```

這種 belief transition 比 scam label 更有研究價值。

## Layer 3: Acoustic Intelligence

別人通常只做 transcript，但這份資料如果是語音，真正珍貴的是 voice。

很多 manipulation / overload / panic 不在文字裡，而在聲音裡：

- hesitation
- panic
- uncertainty
- cognitive overload
- emotional suppression
- trust seeking
- stress burst
- speaking rate change
- interruption pattern
- silence duration
- pitch instability
- emotional fluctuation
- turn-taking asymmetry

這可以形成：

> scam interaction paralinguistic analysis.

尤其台灣中文、165 諮詢語音互動資料很少見，這可能是 differentiator。

## Layer 4: AI Governance And Institutional Capacity

不要只研究民眾是不是被騙。

更大的問題是：

> 當 AI 詐騙量 scaling 時，制度如何崩潰？

可以研究：

- officer review capacity
- fatigue
- attention collapse
- inconsistent judgment
- triage overload
- escalation bottleneck
- delayed intervention
- reconstructability decay

這會直接連到 TFSC 的：

- review scarcity
- runtime governance
- institutional overload
- reconstructability

這已經不是單純 NLP paper，而是 socio-technical system paper。

## What Not To Do First

不要先做：

- scam classifier benchmark
- accuracy leaderboard
- BERT fine-tune
- Whisper + LLM pipeline
- speech emotion classifier
- public transcript dataset

這些太容易 commodity 化，也容易忽略這份資料真正珍貴的互動結構。

## Foundational Framework Objects

這份資料可以用來定義：

- interaction risk state
- manipulation trajectory
- intervention timing
- review scarcity threshold
- trust collapse point
- cognitive overload marker
- officer question type
- information-gain moment
- belief transition
- consultation outcome state

這些比 scam / non-scam label 更有研究價值。

## Sensitive Data Boundary

這不是普通 dataset。

這是高敏感 institutional data。

原則：

- 不把 raw audio 放進 git
- 不把 full transcripts 放進 git
- 不放電話、姓名、帳號、地址、案件編號、員警識別資訊
- voice 本身是 biometric / identifying data
- ASR transcript 是 derived evidence，不是 ground truth
- 任何公開成果都應優先使用 aggregate metrics、annotation codebook、redacted methods、synthetic exemplar calls

在碰真實資料前，應先建立：

- governance boundary
- anonymization protocol
- synthetic release strategy
- access control
- audit log
- retention schedule
- claim discipline
- IRB / ethics design
- public / private separation

這不是附屬工作。它會決定未來能不能公開發 paper。

## Smallest Useful Pilot

第一個最小可行測試不是模型訓練，而是：

> 10-call restricted pilot annotation packet.

如果真實資料尚未正式核准，就先做 synthetic exemplar calls。

每通電話切成 turn 或 30 秒 window，標：

- caller state
- officer action
- belief transition
- phase transition
- acoustic marker
- information-gain moment
- shutdown / resistance
- outcome state

public output 只放：

- schema
- aggregate metrics
- synthetic examples
- redacted method

pass condition：

- 兩位 reviewer 可以穩定使用 codebook
- trajectory map 能看出 intervention timing 和 high-risk transitions
- 沒有 raw audio / transcript / identifying detail 進 git

## Research Position

這個 idea 是 `idea_000035` 的 real-world consultation-data pressure test。

`idea_000035` 鎖的是：

> AI-mediated harmful interaction trajectory modeling

而這個 165 audio idea 的切口是：

> 165 antifraud consultation call interaction science

也就是用高敏感、真實、稀有的 officer-citizen hotline interaction，研究 interaction structure、temporal dynamics、acoustic intelligence、institutional capacity。

這比「再做一個詐騙分類器」更強，也更符合 TFSC 的 review scarcity / runtime governance / institutional overload 主軸。

## 2026-05-22 Focus Update: Victim Cognitive-State Data

這份資料真正要放大的重點是：

> 你現在手上的資料，其實非常有價值。

大部分人以為反詐騙模型一定要有詐騙集團的語音。

但其實不一定。

你現在擁有的是：

> 受害者認知狀態資料。

這可能比詐騙話術本身更重要。

因為詐騙真正留下痕跡的地方，很多時候不是詐騙集團說了什麼，而是：

> 民眾被影響後，呈現出的 cognitive state。

例如：

- 認知混亂
- 高焦慮
- 過度相信 authority
- 重複 rationalization
- 時間壓迫感
- 防禦 external challenge
- attention narrowing
- dependency
- emotional oscillation

這些東西會反映在：

- 語音
- 停頓
- 語速
- 問句形式
- 情緒切換
- 對話結構
- 主題轉移
- uncertainty pattern

所以真正可以研究的不是：

> 詐騙語音辨識

而是：

> 受害者狀態建模。

這差很多，而且這方向更強。

詐騙類型會變，但人類被操控後的狀態，有很多共通性。

這比較接近：

- cognitive security
- behavioral signal modeling
- manipulation-state detection
- human vulnerability dynamics

這會比單純 scam classifier 更有研究價值。

## Wrong Direction

錯誤方向是：

> 把語音轉文字 -> train classifier

這太淺，也很容易失敗。

原因：

- ASR error
- dialect
- hesitation
- fragmented speech
- overlap
- emotional speech

這些都會毀掉 token。

而且 reviewer 很容易說：

> 又是一篇 scam classification paper。

這沒有差異性。

## Multilayer Interaction Representation

真正該做的是多層 interaction representation。

### Layer 1: Acoustic Layer

不要先轉文字。

先研究：

- pitch
- energy
- speaking rate
- pause pattern
- interruption
- jitter
- turn-taking latency

因為被操控的人，聲音會變。

例如：

- 緊張時 pause 增加
- uncertainty 時語尾變化
- 被 authority 壓制時 turn-taking 改變

這些可能比文字更早出現。

這跟最近對 ASR 的懷疑一致：

> 語音本身就是訊號，不是文字的附屬品。

### Layer 2: Interaction Dynamics

這層超重要。

研究問題：

- 誰主導 conversation？
- 誰一直重複問題？
- 哪些 topic 無法 closure？
- 民眾是否出現 fixation？
- 是否反覆提到特定 authority？
- 是否拒絕 alternative explanation？

這很像 conversation graph 或 temporal interaction graph。

### Layer 3: Cognitive State Modeling

這是最有潛力的地方。

不是判斷：

> 是不是詐騙。

而是判斷：

> 目前此人的 cognitive vulnerability level。

例如：

- confusion
- panic
- dependency
- suggestibility
- emotional overload
- verification resistance

這是在研究 manipulation aftermath dynamics。

### Layer 4: Institutional Response Layer

資料裡有員警，這很關鍵。

這代表可以研究：

> 哪種 intervention 有效。

例如某些員警：

- 太快否定
- 太早 challenge
- 太像 authority command

可能讓民眾更 defensive。

但有些方式可能更有效：

- gradual reframing
- emotional grounding
- indirect questioning
- timeline reconstruction
- alternative explanation testing

這會變成：

> anti-fraud conversational intervention modeling。

這可能比偵測本身更重要。

## Representation Discovery Before Modeling

現在不要先急著做模型。

先做：

> representation discovery。

博士等級比較重要的問題是：

- 被詐騙影響的人，interaction pattern 是否存在穩定 latent structure？
- vulnerability 是否會隨時間變化？
- panic 是否有 acoustic precursor？
- conversation repair failure 是否可量化？
- effective intervention 是否存在可重現 pattern？

這些問題比 accuracy 幾 % 更重要。

可先做：

- clustering
- trajectory analysis
- representation learning
- self-supervised interaction embedding
- acoustic + interaction feature fusion
- human-readable codebook comparison

## Ground Truth Warning

這份資料可能不是真正 clean ground truth。

165 民眾可能包括：

- 有些真的被騙
- 有些只是懷疑
- 有些是妄想
- 有些是焦慮
- 有些是正常詢問
- 有些資訊不足

所以不要太早硬做 binary label。

這會毀掉研究。

反而應該先做：

> latent structure discovery。

先看看不同 cognitive states 是否自己浮現。

這比人工硬貼 scam / not scam label 更有研究價值。

## Selection Bias Boundary

這份資料還有一個更大的盲點：

> 會打 165 的人，本身已經是被篩選過的一群人。

這在研究方法上至少牽涉：

- selection bias
- sampling bias
- survivorship bias
- help-seeking interface bias

所以不能 claim：

> 我們研究的是所有詐騙受害者。

真正可 defend 的 claim 是：

> 我們研究的是 help-seeking anti-fraud interaction population。

也就是：已經願意或還能向制度尋求驗證的人。

這群人可能具備：

- 還存在懷疑
- 還願意求助
- 還能接觸外部資訊
- 還沒有被完全 isolation
- 還願意 challenge scammer narrative
- 還保有某種程度的 institutional trust

相反地，最危險的人可能根本不會打 165：

- 已經完全相信詐騙者的人
- 被完全 isolation 的人
- 拒絕外部驗證的人
- 完全防禦 external challenge 的人
- 缺乏制度信任、時間、語言能力或求助管道的人

所以 165 資料不是全體受害者樣本，而是：

> 特定 manipulation stage 的 institutional verification window。

這不是讓研究不能做。

它只是要求 paper 誠實縮小 claim。

成熟寫法不是把這件事藏在 limitation，而是把它變成理論的一部分：

> Individuals who seek institutional verification may represent a distinct cognitive state from fully isolated victims.

換句話說，help-seeking behavior 本身也是 signal。

它可能代表此人仍然處在一個「還可以被介入」的狀態：

- 還有 doubt
- 還有 verification seeking
- 還有 trust displacement 的可能
- 還能從 scammer authority 轉向 institutional authority

這會讓研究主題更精準：

> 不是偵測所有受害者，而是研究反詐騙 help-seeking interaction 中可觀察的 cognitive vulnerability dynamics。

## Intervention Boundary, Not Human Worth

這裡還有一個非常重要的 moral framing risk。

不能把問題推成：

> 那些完全沒有意識到自己被騙的人，可能不值得守護。

這個 framing 很危險，因為它混在一起了三件不同的事：

- intervention effectiveness
- institutional resource allocation
- human worth / protectability

這三個必須分開。

真正合理的研究問題是：

> 有限制度資源下，哪一種 intervention boundary 最有效？

也就是：

- 哪些 stage 比較容易介入？
- 哪些 signals 代表還有 external verification 的可能？
- 哪些 intervention timing 可以改變 trajectory？
- 制度資源應該如何支援最有機會改變結果的互動時刻？

這不是在問誰值得被救。

這是在問：

> 如何在制度資源有限時，提高介入有效性。

不求助不代表不可救。

它可能代表：

- institutional distrust
- fear
- social isolation
- cultural stigma
- dependency
- manipulation depth
- loss of external reality calibration

所以 paper 要避免任何像是「太蠢所以救不起來」的語氣。

安全寫法是：

> Intervention effectiveness varies with manipulation stage and institutional access, but this does not imply differences in human worth or protectability.

## Reversible Window Hypothesis

這個洞見可以轉成一個更強的理論：

> 165 hotline 可能是在一個特定可逆窗口進行 intervention。

會打電話的人可能代表：

- 還存在 uncertainty
- 還願意 external verification
- 還沒有完全封閉
- 還有 institutional interface
- 還可能發生 trust displacement
- 還可能從 scammer authority 轉向 institutional authority

這些都可能代表：

> cognitive capture 尚未完全完成。

這群人不一定是「最嚴重」或「最典型」的受害者。

但他們可能是最值得研究的一群，因為他們剛好位於：

> manipulation 與 recovery 的交界。

這個 transition state 很珍貴。

完全沒被影響的人，signal 少。

完全深陷的人，可能不會進入 165 的觀察範圍。

但半懷疑、半相信、反覆確認的人，會露出很多可觀察現象：

- cognitive oscillation
- uncertainty dynamics
- persuasion instability
- trust displacement
- verification seeking
- intervention response

這對 representation learning 和 interaction trajectory analysis 都很有價值。

## Help-Seeking As Cognitive-Security Signal

help-seeking 本身不只是資料偏誤，也可以是 signal。

在心理健康研究中，help-seeking 可被視為一種 adaptive coping process，也就是嘗試取得外部協助來處理 concern。

放到 165 context，願意打電話本身可能代表：

- self-awareness
- uncertainty recognition
- residual institutional trust
- cognitive openness
- external reality calibration 尚未完全斷裂

所以這篇可以提出一句很強的 framing：

> Help-seeking itself is a measurable cognitive-security signal.

但這句必須搭配 boundary：

> It is a signal of intervention interface access, not a measure of moral worth.

這會把研究自然接到：

> cognitive-security triage.

這裡的 triage 不是決定誰有價值。

而是：

> 在有限 review capacity 下，辨識哪個 intervention timing 最有機會改變 harmful trajectory。

Literature anchors to verify:

- Sax Institute Evidence Check, `Help-seeking measures in mental health`: supports help-seeking as an adaptive coping process involving external assistance for a concern.
- Fraga Dominguez and Storey, `Help-Seeking Behavior in Victims of Elder Abuse: A Systematic Review`: supports underreporting and barriers to help-seeking as reasons help-seeking populations are selected rather than representative.

## AI For Cognitive Security

這條路已經開始偏向：

> AI for cognitive security.

不是傳統 cybersecurity。

而是：

> 人類認知層的安全系統。

未來 AI 最大攻擊面，很可能不是系統漏洞，而是：

> human cognition itself.

因此，這份 165 語音資料的研究價值不是「沒有詐騙集團語音所以不足」，而是剛好相反：

它讓你看到詐騙或操控在人的認知狀態裡留下的後果。

這是 victim-side、interaction-level、cognitive-security data。

## Paper Framework Design

依據目前方向，以及饒老師一直提醒的「先定義唯一核心問題，不要先堆技術」，這篇論文應該先鎖成：

> interaction-centered cognitive vulnerability modeling

也就是：

> AI-based interaction representation for cognitive vulnerability dynamics in anti-fraud hotline conversations.

這篇不是要做：

- scam classification
- ASR system
- chatbot
- multimodal LLM demo
- anti-fraud assistant
- universal governance-collapse simulation

這篇真正要研究的是：

> AI 如何從 interaction dynamics 中辨識受操控後的 cognitive vulnerability dynamics。

換句話說，詐騙只是 case study；核心問題是 cognitive security；主要研究對象是 interaction；AI 是分析工具；制度是 deployment context。

## One-Sentence Claim

可先把 paper contract 寫成：

```text
This paper shows that manipulated cognitive-state dynamics can be studied within help-seeking anti-fraud hotline conversations by proposing an interaction-centered representation framework and validating it through restricted pilot annotation, trajectory analysis, selection-boundary and reversible-window analysis, and public-safe synthetic exemplars.
```

這句強迫整篇論文只保護：

- 一個主問題：如何從 help-seeking 165 hotline interaction 表徵 cognitive vulnerability dynamics？
- 一個主方法：interaction-centered representation framework。
- 一組主證據：restricted pilot annotation、trajectory reconstruction、selection-boundary analysis、reversible-window analysis、aggregate acoustic/interaction features、synthetic public exemplars。
- 一句主貢獻：把反詐騙研究從 scam content detection 重新定位到 help-seeking victim-side cognitive vulnerability dynamics。

## Paper Sections

### 1. Introduction

不要先講 AI，也不要先講模型。

先講現實問題：

- 詐騙快速變形
- script、domain、language、platform 都會換
- LLM 會讓 persuasion 更 personalized
- keyword、blacklist、content classifier 會越來越脆弱

然後提出核心 punchline：

> 真正比較穩定的訊號，可能不在詐騙話術本身，而在被操控後的人類 interaction dynamics。

最後才介紹 165 hotline conversations 是這個問題的研究場域。

### 2. Problem Reframing

這章是 differentiator。

要正式宣告：

> This paper is not scam content detection.

而是：

> cognitive-state-oriented interaction modeling.

這章要說清楚：

- token-centric paradigm 的限制
- semantic drift
- adaptive scam evolution
- ASR brittleness
- multilingual / dialect instability
- binary labels 不可靠
- help-seeking selection bias

核心句可以是：

> Interaction dynamics may be more invariant than scam content.

另一句更精準的 boundary 是：

> Hotline callers are not all victims; they are the visible population at an institutional help-seeking interface.

### 3. Theoretical Perspective

這章不要寫成心理學論文。

它只需要支撐一件事：

> 為什麼 interaction pattern 值得研究。

可用的視角：

- cognitive overload
- bounded rationality
- manipulation dynamics
- conversational asymmetry
- help-seeking as adaptive coping
- institutional intervention

這些只是理論支架，不是要宣稱醫學或心理診斷。

### 4. Dataset And Representation Design

這章不能一開始就 classifier。

應該把資料定位成：

> restricted high-value interaction data.

然後定義四層 representation：

- Acoustic dynamics: pause、pitch、hesitation、speaking rate、interruption、latency。
- Interaction structure: turn-taking、repair failure、repetition、topic fixation、escalation pattern。
- Cognitive vulnerability signals: uncertainty persistence、authority dependence、verification resistance、emotional destabilization。
- Officer intervention: gradual reframing、emotional grounding、timeline reconstruction、verification instruction、escalation routing。
- Population boundary: who is visible to 165, who is missing, and which claims are invalid.

### 5. Self-Supervised / Weakly-Supervised Representation Discovery

這章的邏輯是：

> Real-world cognitive manipulation states are difficult to label reliably.

所以不能硬做 binary label。

比較合理的方法是：

- trajectory embedding
- clustering
- contrastive / predictive objectives
- human-readable codebook comparison
- acoustic + interaction feature fusion

但要注意：模型是工具，不是 paper 的主角。

### 6. Interaction Trajectory Analysis

這可能是最有趣的一章。

因為 manipulation 不是單句事件，而是 temporal evolution。

這章可以分析：

- 哪些 calls 逐漸 panic
- 哪些 calls 逐漸 closure
- 哪些 intervention 讓 uncertainty 下降
- 哪些 calls 出現 persistent confusion
- 哪些 topic 不斷 repair failure
- 哪些 caller 從 rationalization 轉向 action readiness

這會讓 paper 從「分類器」升級成「interaction trajectory science」。

### 7. Institutional Implications

這章才接回 TFSC 風格。

可討論：

- cognitive-security systems
- AI-assisted hotline triage
- review scarcity
- institutional cognitive overload
- cognitive-security triage
- intervention timing under finite resources
- scalable intervention support
- public-safe restricted-data governance

但這裡只能當 implication，不要讓它吃掉主線。

主線仍然是：

> interaction representation for cognitive vulnerability dynamics.

### 8. Limitations

限制一定要主動講，這反而會讓論文成熟。

至少要講：

- 這不是 scammer-victim direct interaction。
- 沒有 clean ground-truth manipulation labels。
- hotline context 有 selection bias，而且 165 callers 是 help-seeking population，不是 all-victim sample。
- 最深度 isolation / cognitive capture 的人可能反而不會打 165。
- 不求助不代表不可救；可能只是 institutional distrust、fear、isolation、stigma、dependency 或 external reality calibration 斷裂。
- 這篇不能把 intervention feasibility 寫成人的價值差異。
- 165 caller population 本身混合 true victim、anxious caller、suspicious caller、normal consultation、insufficient-information cases。
- acoustic stress 不能等於 deception 或 victim truth。
- public release 不能包含 raw voice、full transcript、PII、case detail。

## Concrete Method Plan

第一階段不要 train 大模型。

先做：

1. 寫一頁 paper contract：one-sentence claim、not-this-paper list、contribution-to-evidence map。
2. 建立 ethics / governance protocol：access control、redaction、retention、public-private boundary。
3. 建立 codebook：caller state、officer action、acoustic marker、repair failure、phase transition、outcome state。
4. 定義 help-seeking population boundary：誰會出現在 165，誰可能缺席，哪些 claim 因此無效。
5. 定義 moral framing guardrail：intervention effectiveness 不是 human worth，不求助不是不可救。
6. 做 10-call restricted pilot；若真實資料尚未核准，先做 synthetic exemplar calls。
7. 將每通電話切成 turn、30 秒 window、topic shift 或 phase transition。
8. 只標 observable traits，不標 medical truth、legal truth、deception truth、final scam truth 或 moral worth。
9. 抽 acoustic / turn-taking features：pause、speech rate、pitch instability、latency、overlap、interruption。
10. 建 temporal interaction graph。
11. 做 latent clustering / trajectory embedding 作為 secondary analysis。
12. 用 inter-coder agreement、qualitative trajectory audit、selection-boundary audit、reversible-window audit、aggregate statistics、synthetic examples 驗證。

## Reviewer Questions To Answer

全文要回答 reviewer 會問的幾個問題：

- What exactly is cognitive vulnerability?
- Why can anti-fraud research work without scammer audio?
- Why is this not ASR, speech emotion recognition, or scam classification?
- How can cognitive-state dynamics be validated without clean labels?
- Who is visible in 165 hotline data, and who is missing?
- How does help-seeking selection bias limit the claim?
- How does the paper avoid implying that non-help-seeking people are less worthy of protection?
- What is the reversible intervention window?
- How is cognitive-security triage different from moral triage?
- How are voice biometrics and institutional sensitivity protected?
- What evidence shows interaction dynamics are useful beyond content?
- What is the boundary between AI-assisted analysis and automated judgment?

## Figure 1 First

Figure 1 應該先畫出來，再寫全文。

建議四格：

1. Scam scripts mutate, so content-level detection is brittle.
2. Hotline callers expose cognitive and interaction-state traces after possible manipulation.
3. The framework reconstructs acoustic, interaction, cognitive-state, and officer-intervention layers over time.
4. The output is trajectory representation, restricted diagnostics, synthetic public exemplars, and claim-bounded institutional implications.

如果 Figure 1 畫不出來，就代表主線還沒清楚。

## Scope Guardrail

這篇要非常克制。

先不要做：

- world model
- agent society
- full governance collapse
- multi-agent simulation
- universal scam ontology
- LLM fine-tuning as main result
- general fraud detector

這些可以放 future work。

現在最有機會成為強 paper 的切口是：

> 165 anti-fraud hotline conversations as victim-side cognitive vulnerability trajectory data.

也就是用一個很窄但成立的研究物件，提出一個 conceptually coherent 的 Q1 paper。
