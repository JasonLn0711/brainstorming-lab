# JANUS Counterfactual Decision-Stability ASR Workspace

Status: captured as `idea_000040`

## 核心命題

JANUS 目前的短期 paper axis 應該被清楚定義為 Counterfactual Decision-Stability ASR，也就是測試高風險語音系統在 ASR 不確定性下， downstream decision 是否仍然穩定。

一句話 thesis：

> We propose a method to test whether high-stakes voice-system decisions remain stable under plausible ASR transcript alternatives.

這個定位把 repo 從 ASR benchmark paper 推進成高風險對話決策系統的 decision-stability research。Whisper、Breeze-ASR、legacy partial encoder、legacy LoRA 的價值是提供 plausible ASR hypotheses；主貢獻不是 fine-tuning Whisper，也不是小幅 CER/WER 改善。

## Runtime Flow

```text
audio
-> ASR transcript + confidence / n-best / timestamps
-> risk atom extraction
-> plausible counterfactual transcript alternatives
-> downstream decision stability / CEIS
-> automatic constrained recovery or conservative machine action
```

這條線代表研究重點是 uncertainty propagation into downstream decisions。ASR 品質指標仍然重要，但它們是輸入品質與對照層；paper-facing claim 應該落在 plausible transcript alternatives 是否會造成 label flip、unsafe downrouting、high-risk miss、CEIS shift，或需要 conservative action。

## 今日進展的研究層級

今天的成果不是單純整理資料夾，也不是只跑 ASR baseline，而是完成一個 research infrastructure consolidation：

- source archive organization
- extracted part normalization
- inventory and review flag system
- purpose-oriented JANUS data library
- ASR experiment registry
- semantic-risk-ASR subsystem
- recovery-policy subsystem
- annotation subsystem
- evidence-chain readiness subsystem
- split-aware metric input subsystem
- WER/CER journal-compliance audit

這些工作把 repo 變成完整研究平台，但 paper 不能跟著變成平台介紹。平台是 supporting apparatus；主角仍然是 CDS-ASR。

## Evidence-Chain Governance

`check_evidence_chain_readiness.py` 和 `audit_publishable_evidence_chain.py` 的價值，是把 publishability、review completeness、evidence sufficiency、auditability 變成 machine-checkable。

目前 gate 的意義可以正向表述為：

- `ok=true`: repo 已經有可檢查的 evidence-chain 結構。
- `paper_ready=false`: selected-300 human risk-atom audit 還沒完成。
- `publishable_ready=false`: objective-level evidence 仍有 review_pending 或 proxy-only surface。

這不是失敗，而是很好的 scope control：在 selected-300 human audit 完成之前，paper 不應提前把 proxy evidence 寫成 final claim。

## Current Evidence Snapshot

已建立的 comparable ASR hypothesis ecosystem：

- legacy partial encoder
- legacy LoRA
- Breeze-ASR-25 base
- Breeze-ASR-26
- Whisper large-v2
- Whisper small

當前定位：

- partial encoder 仍是 ASR hypothesis generator candidate。
- manifest transcripts 已可作為 WER/CER scoring reference。
- CDS/risk-atom labels 是獨立 human-review surface。
- selected-300 human audit 目前仍是 0/30 row reviews、0/90 model assessments。
- paper-facing ASR table 應以 `cer_zh_micro` 為 primary surface metric，`wer_zh_jieba_micro` 作為 supplemental segmented-word metric。

## Complexity Risk

最大的風險是 repo 開始長成 engineering universe：

- audit layer
- recovery layer
- predictor layer
- annotation layer
- publishability layer
- split-aware layer
- proxy layer

每一層都可以自然膨脹成自己的研究題目。這對工程很有吸引力，但 reviewer 最後只會問一個問題：這篇 paper 到底解決了什麼核心問題？

因此 containment rule 是：

> Every new subsystem must either generate plausible ASR alternatives, measure decision stability, or make the CDS-ASR evidence chain publishable.

如果做不到，就先 park，不讓它變成新的主線。

## Exploration Versus Convergence

可以先讓這個系統在內部長大。這不是問題，甚至可能是長期博士研究或 lab research program 的正常型態。真正要分清楚的是兩個階段：

- exploration phase：允許 subsystem 長出來，因為你還在找哪一條研究礦脈最有價值。
- convergence phase：一次只選一條 paper lane，其他複雜度全部退到 support、appendix、future work 或 internal tooling。

所以現在不一定要停止 expansion。現在要開始做的是 knowledge compression：把看起來很多的 subsystem，往上壓縮成少數研究構念。

目前可以先壓縮成：

```text
CDS-ASR / uncertainty propagation into operational decisions
├── uncertainty generation
├── uncertainty propagation
├── decision instability
├── recovery policies
├── auditability
├── governance
└── metric validity
```

這樣 repo 可以繼續探索，但 paper 不會被整座系統拖垮。

## Possible Paper Lanes

目前這個大系統可以先被看成一個 internal research map，而不是一篇 paper 的完整目錄。

| Lane | Core Question | Current Role |
| --- | --- | --- |
| Paper 1: CDS-ASR | ASR plausible alternatives 會不會改變 high-stakes downstream decision？ | short-term paper center |
| Paper 2: Metric Validity | 為什麼 WER/CER 不足以代表高風險語音 AI 的安全性？ | future lane |
| Paper 3: Recovery Policy | 當 transcript uncertainty 讓 decision unstable，machine 應該如何保守行動？ | future lane |
| Paper 4: Human Audit Governance | 有限 human review 如何 batch、validate，並接到 publishable claim？ | future lane or methods appendix |
| Paper 5: ASR Robustness | 哪些 ASR hypothesis generator 產生的 alternatives 真的會影響 downstream risk？ | support for Paper 1, possible future lane |

這代表你的直覺是對的：一個大的 exploration repo 最後可能拆成多篇 paper。但拆分的時候不能用「我做了很多 subsystem」當理由，而是要用：

1. 單句 thesis
2. reviewer 會接受的 baseline
3. 清楚 metric
4. claim-to-evidence map
5. public/private artifact boundary
6. publishable evidence gate

來決定哪一條 lane 可以真正變成 paper。

## Knowledge Compression Rule

真正危險的不是 complexity explosion，而是沒有 knowledge compression。

如果 repo 只是不斷長出：

- risk atom extraction
- decision flip analysis
- unsafe routing
- recovery policy
- confidence instability
- human audit batching
- evidence readiness gates

那 reviewer 會覺得這是一個很大的工程系統，但不一定知道 contribution 是什麼。

但如果把它們壓縮成：

> uncertainty propagation into operational decisions

那這些 subsystem 就不再是散亂功能，而是同一個研究理論下面的 observable phenomena。

接下來每個新 subsystem 都應該被標記成五種之一：

- Paper 1 core
- Paper 1 support
- future paper lane
- appendix
- internal tool

這樣可以讓探索繼續，但不讓第一篇 paper 失焦。

## Research Compression

現在最需要練的不是更多技術，而是 research compression：把巨大、混亂、正在長大的系統，壓縮成可理解、可敘述、可驗證、可投稿的研究核心。

第一個動作是暫時不要看 implementation。先不要看 code、scripts、folders、pipelines，而是問每個東西在解什麼痛點。

| Surface Item | Deep Structure | Paper Role |
| --- | --- | --- |
| WER/CER | transcript uncertainty | input-quality evidence, not enough for safety |
| downstream label flips | decision instability | CDS-ASR main result signal |
| unsafe downrouting | operational harm under uncertainty | high-stakes failure mode |
| recovery policy | uncertainty-aware safety control | method extension or future paper lane |
| evidence-chain audit | reconstructability and accountability | claim-evidence governance |

這些東西往上壓縮後，會形成一條 theory chain：

```text
Transcript uncertainty
        ↓
Semantic uncertainty
        ↓
Risk interpretation instability
        ↓
Operational decision instability
        ↓
Potential downstream harm
        ↓
Need for recovery / governance
```

這就是 latent research structure。paper 發的不是「我寫了很多 code」，而是「我發現了這個結構，並且用方法與證據證明它重要」。

## Research Layers

這個 repo 目前混著四層東西，需要分開看：

| Layer | Examples | Paper Role |
| --- | --- | --- |
| Engineering | dataset loaders, configs, batch scripts, inventories | mostly appendix or invisible infrastructure |
| Experimental Evidence | WER, CEIS, label flips, high-risk misses | results and evidence tables |
| Research Mechanism | counterfactual transcript alternatives, recovery policy, split-aware metrics | methodology |
| Theory / Thesis | ASR accuracy is insufficient for high-stakes voice AI | paper core |

很多研究會卡在 Layer A：一直寫 code、整理資料、補工具，但沒有壓縮到 Layer D。CDS-ASR 的 paper core 應該在 Layer D：ASR accuracy alone is insufficient because transcript uncertainty can propagate into semantic uncertainty and operational decision instability.

## North Star

之後 repo 一定還會膨脹，所以需要一個固定的 North Star：

> How can high-stakes AI systems maintain auditable, safe, and stable decisions under uncertain inputs?

每個新 subsystem 都用這句話判斷：

- 它是否幫助生成、描述或測量 uncertain input？
- 它是否揭示 semantic 或 decision instability？
- 它是否降低 operational harm？
- 它是否讓 recovery 或 governance 更可稽核？
- 它是否能進入 Paper 1，或應該先變成 future paper lane？

## Paper Cutting

切 paper 不應該按照 folder、script 或 subsystem 數量切，而應該按照 core question + evidence stack 切。

目前 portfolio 可以這樣看：

| Paper | Core |
| --- | --- |
| Paper 1: CDS-ASR | decision stability under transcript uncertainty |
| Paper 2: Low-WER danger phenomenon | semantic-risk mismatch and metric validity |
| Paper 3: Recovery policies | uncertainty-aware conservative routing |
| Paper 4: Human review scarcity | auditability under limited reviewers |
| Paper 5: Evidence-chain governance | machine-checkable AI evidence readiness |

可發表的核心問題通常要通過四個測試：

1. reviewer 能不能一句話講出你的問題？
2. 方法有沒有清楚 input、output、assumption、failure condition？
3. evidence 有沒有 metric、baseline、split、人審狀態？
4. claim 有沒有 public/private artifact boundary 與 publishability gate？

如果四個都過，這條 lane 才開始像 paper。否則它只是有趣的 subsystem。

## Research Narrative

饒老師講的不是單純的寫作技巧，而是 research narrative：讓 reader 知道這篇研究為什麼存在。

一般技術型寫法常常是：

```text
我們提出方法 A
我們使用 dataset B
我們達到 metric C
```

這種寫法可能 technically correct，但張力不足。CDS-ASR 更適合用現實世界驅動型敘事：

```text
世界正在出現高風險 conversational AI 決策問題
↓
現有 ASR evaluation 主要看 transcript accuracy / confidence / benchmark
↓
真正缺的是 decision stability under plausible ASR alternatives
↓
我們提出 CDS-ASR 這個 problem framing
↓
用 CEIS、label flips、unsafe downrouting、human audit、recovery policy 驗證
↓
因此能更好支撐 safer operational AI governance
```

這裡的重點不是誇大，而是把問題的重要性講清楚。不要寫成「AI 即將毀滅社會」；要寫成：

> In high-stakes conversational systems, small transcript uncertainty can propagate into downstream operational instability.

這句話有張力，但仍然專業、可被 citation 支撐、可被實驗驗證。

### Narrative Map

| Stage | JANUS Story | Citation Need |
| --- | --- | --- |
| Real-world problem | AI 正在進入醫療、金融、客服、政府、反詐騙等高風險流程，越來越多 downstream action 依賴語音或 conversational AI。 | 高風險語音/對話 AI 採用、call-center AI、speech interface failure、domain deployment evidence |
| Existing methods | 主流評估仍大量依賴 WER、CER、confidence、benchmark、human review。 | ASR metric papers, benchmark practice, confidence/uncertainty estimation, human review practice |
| Fundamental gap | 現有方法主要衡量 transcript accuracy，不直接測試 plausible transcript alternatives 是否改變 downstream decision。 | WER/CER limitation, semantic/task-level ASR evaluation, metric mismatch, safety-critical AI reliability |
| New framing | 高風險 conversational AI 應評估 decision stability，而不只是 transcript accuracy。 | counterfactual evaluation, robustness, uncertainty propagation, AI governance/accountability |
| Validation | CEIS、label flips、unsafe downrouting、high-risk misses、human risk-atom audit、recovery policy 都是 evidence。 | ASR baseline model citations, human audit methodology, domain/dataset citations where public |

### Low-Level To High-Level Rewrite

| Low-Level Description | Research Narrative Version |
| --- | --- |
| We build CEIS. | Existing ASR metrics do not show whether transcript uncertainty changes downstream decisions, so CEIS measures operational decision stability. |
| We compare six ASR models. | Multiple ASR systems provide plausible transcript hypotheses for testing whether downstream risk decisions survive ASR uncertainty. |
| We implement recovery policies. | When decision stability fails, conservative recovery policies provide a bounded path from uncertainty detection to safer machine action. |
| We run a human audit. | Human risk-atom review anchors decision-stability claims to accountable evidence rather than unverified proxy metrics. |

這就是從「功能描述」升級到「問題敘事」。真正有 impact 的 paper 不一定是方法最花俏，而是 problem framing 讓 reader 立刻知道：這個問題以前被評估錯了，現在需要新的評估方式。

### Citation Discipline

這個敘事一定要 citation-aware：

- 現實世界正在發生或即將發生的問題，要有 citation。
- 現有方法怎麼做，要有 citation。
- 現有方法不夠好，不能只用情緒判斷；要說明它無法評估哪個 gap，並用 citation 或實驗證據支撐。
- 新 framing 要講清楚它解決的是哪個 gap。
- JANUS evidence 只支持它實際能支持的 claim，不把 proxy result 寫成 final production safety claim。

這樣文章會有吸引力，但不會 overclaim。

## Consequence-Driven Narrative

你剛剛指出的問題非常關鍵：只說「大家評估錯東西了」還不夠。錯本身不是 impact；錯了之後會造成什麼現實後果，才是 reader 會有感的地方。

CDS-ASR 的敘事不能停在：

```text
metric problem
```

而要往下挖成：

```text
metric problem
↓
wrong system belief
↓
unsafe deployment assumption
↓
real-world operational failure
↓
human / organizational cost
```

這會把 paper 從「我們提出新 metric」推進成「我們揭示一種 deployment illusion」。也就是：組織可能以為低 WER/CER、高 confidence、漂亮 benchmark 表示 downstream voice-AI workflow 可以信任；但真正需要被測試的是，plausible ASR alternatives 會不會改變 operational action。

### Impact Ladder

| Version | Wording | Why It Matters |
| --- | --- | --- |
| Weak | WER 無法反映 decision stability。 | reviewer 可能同意，但會問 so what。 |
| Medium | low-WER transcript 仍可能造成 downstream risk misclassification。 | 開始進入 task-level harm，但現實畫面還不夠清楚。 |
| Strong | transcript-level correctness 不保證 operational safety；系統可能在看似高準確率下錯過高風險案件、錯誤降低優先級，或產生 unsafe downrouting。 | metric mismatch 連到 deployment risk。 |
| Vivid | 幾個 ASR 詞差異可能讓高風險詐騙支援案件看起來像低風險一般諮詢，導致未被及時 escalation。 | reader 可以看到 operational failure，但 manuscript 必須用 de-identified 或 synthetic-safe evidence 支撐。 |

### Operational Translation

| Technical Term | Operational Language |
| --- | --- |
| unsafe downrouting | 高風險案件被錯誤降低處理優先級。 |
| decision instability | 同一通話的 plausible transcripts 讓系統產生不同 machine actions。 |
| low-WER danger case | transcript 看起來幾乎正確，但 downstream decision 已經不穩定或不安全。 |
| risk-atom miss | 一個小的 transcript 差異移除或改變關鍵風險元素，進而影響 escalation。 |

所以這篇 paper 的 punchline 不是「我們的 metric 比 WER 好」；而是：

> Low transcript error rates can create a deployment illusion when operational decisions remain unstable.

另一個更有張力但仍然專業的說法是：

> The dangerous case is not only visibly bad ASR; it is a system that appears normal while the downstream action has already changed.

這個敘事要保持兩個 scope controls：

1. 不要主張所有 ASR evaluation 都錯，應該主張 transcript-level metrics are insufficient for high-stakes downstream decision safety。
2. 不要主張 production safety 已被證明，應該主張 CDS-ASR 提供 evidence-backed deployment-risk evaluation，production readiness 需要 separate validation path。

下一步應該把這個敘事做成一張 consequence-to-evidence table：metric gap、wrong system belief、operational failure mode、JANUS evidence artifact、claim boundary。這樣文章就不是單純有情緒張力，而是每個後果都能被 evidence chain 支撐。

## Semantic Consequence Quantification

你現在提出的「把 ASR 轉出來的意思跟真實意思相比，最後累加起來看差多少」是很重要的方向。它可以叫做 semantic consequence quantification：不是只問 transcript 錯幾個字，而是問 ASR-derived meaning 跟 ground-truth case meaning 之間，造成多少現實世界偏差。

詐騙金額是一個很好的例子：

```text
ground truth: 我被騙三百萬
ASR output:   我被騙三萬
```

這種情況 WER 可能看起來只錯一小段，但 operational consequence 很大，因為 severity tier、escalation urgency、case statistics、resource allocation 都可能被改變。這就是 semantic distortion 大於 transcript distortion。

### Measurement Families

| Family | Question | Example |
| --- | --- | --- |
| Field distortion | ASR 抽出的關鍵欄位跟真實欄位差多少？ | 金額絕對誤差、金額相對誤差、是否已匯款、是否提供帳號、是否下載 APP。 |
| Threshold crossing | ASR 錯誤是否跨過決策門檻？ | 真實金額在高風險 tier，但 ASR 金額落到低風險 tier。 |
| Decision consequence | 由 ground truth 和 ASR transcript 推出的決策是否不同？ | escalation flip、unsafe downrouting、high-risk miss。 |
| Aggregate operational drift | 多筆案例累積後，ASR-derived aggregate 跟真實 aggregate 差多少？ | 總損失金額 drift、高風險案件數 drift、升級比例 drift。 |
| Risk-weighted semantic error | 不同錯誤按照風險權重計分，而不是所有 token 等價。 | filler word error 權重低；金額、匯款狀態、風險行為、escalation cue 權重高。 |
| Expected Operational Harm proxy | 錯誤機率乘上操作後果。 | `EOH = Σ(error probability × operational consequence)`。 |

這個方向的核心洞見是 error asymmetry：不是所有 ASR error 都一樣危險。

| Low-Consequence Error | High-Consequence Error |
| --- | --- |
| 今天 -> 今天啊 | 沒有匯款 -> 已經匯款 |
| 嗯 -> 呃 | 三百萬 -> 三萬 |
| filler word missing | 沒有提供帳號 -> 已提供帳號 |

所以 CDS-ASR 後面可以接一層 risk-weighted semantic evaluation。WER/CER 看所有字元或詞的表面差異；risk-weighted semantic evaluation 看哪些錯誤真的控制 downstream action。

### Aggregate Drift

你講的「幾千個案例一起看」很有研究價值，因為它把 sample-level error 推到 system-level drift。

例如在一段時間內比較：

```text
ground-truth total reported loss
vs.
ASR-derived total reported loss
```

或：

```text
ground-truth high-risk case count
vs.
ASR-derived high-risk case count
```

這會讓 paper 的後果更清楚：ASR 不只是個 transcription tool，它在這種系統裡可能變成 social sensing instrument。當這個感測器系統性低估金額、漏掉已匯款狀態、或漏掉高風險 risk atom，長期 dashboard、資源分配、升級比例、風險趨勢都會偏移。

### Important Cautions

這個方向很強，但有幾個必須先控制：

1. 金額欄位必須能被穩定 extract、normalize、compare。中文金額有「三百萬」、「300萬」、「三萬塊」、「一百多萬」這類 normalization 問題。
2. 不是每通電話都有金額；不能把 amount distortion 寫成 universal metric。若金額 coverage 不夠，就先用 transfer status、risk-atom presence、escalation cue、decision label。
3. aggregate drift 不能取代 sample-level harm。總量可能互相抵消，所以要同時看 signed error、absolute error、threshold crossing、worst-case tail。
4. 不要太快陷入 metric engineering。每個新 score 都要回答：它對應到什麼 operational failure？
5. human transcript illusion 也要納入：低 WER、流暢 transcript、高 confidence 可能讓人類 reviewer 過度相信 ASR，但 semantic meaning 已經偏掉。

所以這個新想法可以這樣定位：

> CDS-ASR tests whether decisions remain stable under plausible ASR alternatives; semantic consequence quantification estimates how much operational reality drifts when decisions are computed from ASR-derived meaning.

這不是取代 CDS-ASR，而是把「decision instability」往現實世界後果再推一層。

## Social Sensing Instrument

social sensing instrument 可以先理解成：

> 用資料系統感測社會狀態的量測工具。

一般 sensor 感測物理世界：

| Sensor | Measures |
| --- | --- |
| 溫度計 | 氣溫 |
| ECG | 心臟電訊號 |
| 雷達 | 飛機或物體位置 |
| 地震儀 | 地殼震動 |

social sensing instrument 感測的是社會世界：

| Social Sensing Surface | Possible Signal |
| --- | --- |
| search queries | public-health symptoms, public concern |
| social media posts | emergency events, crowd reports, public sentiment |
| transaction patterns | fraud, money laundering, abnormal behavior |
| emergency calls or hotlines | public-safety risk, incident patterns, service demand |

所以 165 反詐騙通話不只是客服資料。它可以被看成一個 bounded social-risk sensing surface，因為民眾在電話中回報：

- 是否已匯款
- 被騙或可能被騙金額
- 是否提供帳戶或個資
- 是否加入 LINE 群或投資群
- 是否下載 APP
- 是否面交
- 話術類型與詐騙情境
- 是否需要 escalation

在這個 frame 裡，ASR 就不是單純的 transcription engine。它是把 audio 轉成 social-risk signal 的解碼器。也就是：

```text
individual call audio
-> ASR transcript
-> risk atoms
-> case-level decision
-> aggregate social-risk signals
```

這就是為什麼 semantic distortion 很重要。如果 ASR 系統性低估金額、漏掉已匯款狀態、或把高風險 risk atom 轉錯，那不只是單句 transcript 有錯，而是整個 social-risk measurement 會偏掉。

### Measurement Integrity

這個 framing 最有價值的詞是 measurement integrity。

問題不是只問：

> ASR 有沒有把字轉對？

而是問：

> 這個 AI-mediated sensing pipeline 有沒有保留真實世界風險訊號？

如果 ASR 是壞掉的溫度計，它可能讓 downstream dashboard 看起來很穩定，但其實正在低估風險。對 JANUS 來說，measurement integrity 可以看：

- high-risk case count drift
- total reported-loss drift
- escalation distribution drift
- risk-atom prevalence drift
- unsafe downrouting drift
- model confidence 與 risk-bearing field correctness 是否校準

這個 framing 可以讓 paper 的敘事更有深度：

> In high-stakes conversational systems, ASR is part of a social-risk sensing instrument. Transcript errors can therefore become measurement errors in the operational view of risk.

但這裡要控制邊界。Paper 1 不應該宣稱「JANUS 測量整個社會詐騙活動」。比較穩的說法是：

> JANUS provides a bounded high-stakes call-center setting where ASR-mediated transcripts participate in social-risk measurement and downstream escalation decisions.

### Why This Matters

這個角度會把 CDS-ASR 從「語音辨識評估」推到「AI-mediated measurement integrity」。

也就是：

```text
ASR error
-> semantic distortion
-> risk signal distortion
-> decision instability
-> aggregate operational drift
-> measurement integrity risk
```

這也解釋為什麼低 WER 危險：如果 sensor 看起來正常，人反而更容易相信它。真正危險的不是 sensor 明顯壞掉，而是 sensor 看起來穩定、數字漂亮、confidence 高，但它測到的社會風險訊號已經偏掉。

這個 framing 需要 citation map 支撐，至少要找：

- computational social sensing / social signal processing
- crisis informatics and social-media event detection
- measurement bias or data quality in computational social science
- public-safety, emergency-call, or hotline analytics

它現在最適合當成 Paper 1 的 framing paragraph 和 future paper lane，不要讓它搶走 CDS-ASR 的主軸。

## Paper Scope Control

主 claim：

CDS-ASR evaluates downstream decision stability under plausible ASR alternatives in high-stakes conversational decision systems.

Supporting evidence：

- six-model ASR hypothesis matrix
- risk atom extraction
- counterfactual transcript alternatives
- CEIS and split-aware metrics
- selected-300 human risk-atom audit
- evidence-chain readiness and publishability gates
- constrained recovery policy evaluation

不是主角：

- Whisper fine-tuning
- small CER improvement
- generic ASR benchmark
- generic human-review workflow
- unconstrained recovery-policy platform

## Immediate Next Gates

1. Keep the one-sentence thesis visible in paper-facing README, story outline, and roadmap.
2. Complete the first selected-300 human audit batch response.
3. Run strict dry-run before any write to the ignored local audit sheet.
4. Refresh validation, aggregate status, human-reviewed predictor outputs, evidence-chain readiness, and publishability in one recorded pass.
5. Build a claim-to-evidence map: claim, script/output, current gate status.
6. Keep recovery policy as supporting evidence until selected-300 human-reviewed instability evidence is available.

## Sensitive Data Boundary

Audio, call data, transcript-bearing sheets, and call filenames stay local-only in the JANUS workspace. This brainstorming note records thesis, scope control, gate status, aggregate evidence shape, and next decisions only.
