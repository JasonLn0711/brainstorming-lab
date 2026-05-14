# Fugu Ultra x Codex CLI 行為分析相關文獻比較

日期：2026-05-14

## 一、是否已有類似研究？

有，而且已經形成一個很活躍的研究交會區。但目前最接近的文獻仍然分散在幾條線上：

1. 長時程 native-runtime / CLI agent benchmark。
2. LLM agent memory 與 context curation。
3. trace / trajectory / safety evaluation。
4. long-running agent harness 工程方法。
5. multi-agent orchestration / coordinator 模型。
6. context engineering / cowork-style human-AI collaboration。

目前我沒有看到一篇完全等同於本 packet 的研究：**第三方 OpenAI-compatible multi-agent orchestrator，如 `fugu-ultra`，嵌在 Codex CLI 長時間 coding/security task 中，並用 token、trace、tool-loop、memory、proof boundary、official validation artifact 做完整行為鑑識**。

所以答案是：

> 一般研究方向已經很接近，但你的 case 有獨立價值。它不是再做一個普通 agent benchmark，而是針對「opaque orchestration model inside Codex CLI」做 failure forensics。

## 二、最相近 reference 排名

| Rank | Reference | 相近原因 | 與本 case 的差異 |
| ---: | --- | --- | --- |
| 1 | WildClawBench | native-runtime、CLI harness、真工具、長時程、多工具呼叫、side-effect grading | 是 benchmark，不是單一 Fugu/Codex failure case |
| 2 | Terminal-Bench | hard realistic terminal tasks、真實 CLI workflows | 偏通用 terminal benchmark，不分析第三方 orchestration opacity |
| 3 | LongCLI-Bench | 長時程 command-line programming task、step-level scoring、fail-to-pass/pass-to-pass | 偏 programming benchmark，較少分析第三方 orchestration opacity |
| 4 | ATBench-Codex | Codex-runtime trajectory safety、repos/shell/patch/dependency/approval/rule boundary | 偏 safety taxonomy，不直接處理 token explosion 和 memory compression |
| 5 | Beyond pass@1 Reliability Science | Reliability Decay Curve、Variance Amplification Factor、Graceful Degradation Score、Meltdown Onset Point | 偏跨任務統計框架，不針對 Fugu/Codex 單案鑑識 |
| 6 | Terminal-Agent Benchmark Task Guideline | adversarial、difficult、legible terminal-task 設計與 reward-hackable failure mode | 偏 benchmark authoring，不分析既有 Fugu trace |
| 7 | OpenAI Trace Grading / Agent Improvement Loop | 直接把 agent trace 當成可評分與改進對象 | 官方方法框架，不是研究 paper |
| 8 | Anthropic long-running harness | progress file、initializer、git history、incremental handoff | 偏 engineering practice，不是 Fugu/Codex 具體 eval |
| 9 | Memory for Autonomous LLM Agents | agent memory taxonomy: write-manage-read、compression、retrieval、hierarchical context | Survey，不提供 CLI security-lab task evidence |
| 10 | Memex(RL) | full-fidelity evidence indexing + compact working context | 主要是 memory mechanism，不評估 proof boundary |
| 11 | Memory as Action | context curation as policy action，直接對應 attention dilution | 偏學習式 context edit，不處理 Codex harness |
| 12 | AMA-Bench | agentic trajectory memory eval，指出 similarity retrieval 的因果/客觀資訊不足 | 偏 memory QA，不是 CLI task completion |
| 13 | Agentic Memory / AgeMem | 統一 LTM/STM memory management，讓模型學會存取/更新/摘要/丟棄 | 偏 model-policy memory，不評估 third-party endpoint opacity |
| 14 | Conductor | Fugu 類 learned orchestration 的核心近親，包含 worker selection、topology、recursive self-selection | 強調 benchmark performance，不強調長任務失敗鑑識 |
| 15 | TRINITY | lightweight coordinator orchestrating multiple LLM roles | 和 Fugu lineage 相近，但非 Codex CLI failure analysis |
| 16 | LLMA-Mem | 多 agent 記憶、team size vs time scaling、成本效率 | 偏 multi-agent memory scaling，不處理 local shell/Docker trace |
| 17 | Context Engineering / Claude Code / Cowork / OpenCode | Claude/ChatGPT/Cowork/Codex context package 與產品化 agent harness 方法 | 偏 human-AI/product methodology，非 native-runtime benchmark |

## 三、文獻群組比較

### A. 長時程 / CLI / native-runtime agent benchmark

代表文獻：

- `WildClawBench`
- `Terminal-Bench`
- `LongCLI-Bench`
- `Beyond pass@1`
- `What Makes a Good Terminal-Agent Benchmark Task`
- `Survey on Evaluation of LLM-based Agents`

這一群最能支持我們的核心判斷：長任務 agent 不能只看最後答案，也不能只看短 benchmark。WildClawBench 把真實 CLI harness、真工具、Docker runtime、hybrid grading 放進 evaluation；Terminal-Bench 補上 hard realistic terminal tasks；LongCLI-Bench 更直接指出長時程 CLI programming task 的 pass rate 仍很低，且需要 step-level scoring 來知道 agent 卡在哪。Reliability Science 進一步把 pass@1 外的長時程可靠性、meltdown onset 與 degradation curve 變成可量化指標；Terminal-Agent Benchmark Task Guideline 則提醒 terminal benchmark 必須防 reward hacking，且難度要概念性而不是環境瑣碎。

與 Fugu/Codex case 的對應：

| 文獻觀點 | 本 case 對應 |
| --- | --- |
| 長時程任務要看 runtime side effects | `/shared/success.txt` 是否真的由 official IC 產生 |
| 需要 step-level scoring | Fugu 有 environment discovery、binary analysis、coredump、sweep、doc update 等不同 phase |
| 只看 final answer 不夠 | Fugu final answer 誠實說未成功，但中途 plan status 曾漂移 |
| harness 會影響結果 | GPT-5.5/Codex native path 和 Fugu/OpenAI-compatible endpoint 行為差異明顯 |

差異：

> 這些 benchmark 多數把 model/harness 作為可跑多次的實驗條件；本 packet 是單一真實長任務 failure forensics，需要後續轉成可重複 A/B/C protocol。

### B. Agent memory / context curation

代表文獻：

- `Memory for Autonomous LLM Agents`
- `AMA-Bench`
- `Memex(RL)`
- `Memory as Action`
- `Agentic Memory`
- `MemoryAgentBench`
- `LLMA-Mem`

這一群最能解釋 Fugu 的 token/memory 問題。重點不是「上下文不夠長」，而是 memory write/manage/read policy 沒有把資訊轉成可操作狀態。

Fugu case 的具體 memory failure：

| Memory failure | log 中表現 |
| --- | --- |
| Write failure | coredump/gadget facts 沒有早期寫入外部 state |
| Manage failure | raw `objdump` / `gdb` / Docker output 長期留在 active trajectory |
| Read failure | 已知 facts 沒有穩定支配下一步 hypothesis |
| Selective forgetting failure | shell friction 和 broad sweep 結果沒有形成 stop rule |
| Evidence indexing failure | full tool output 沒有被外部 evidence file + short index 替代 |

最貼近本案的是 `Memex(RL)` 和 `Memory as Action`：

- `Memex(RL)` 的核心是「active context 保留摘要與 index，full evidence 外部保存」。這正是 Fugu 應對 `objdump/gdb` 大輸出時該做的。
- `Memory as Action` 把 context deletion / insertion 當成可學習 action。這對應 Fugu 沒有刪除低價值 raw output、也沒有插入最新 verified state。

差異：

> 這些 memory papers 多數評估 memory accuracy 或 task success，但不一定處理 Codex CLI 這種 shell-side effects、official proof boundary、YOLO mode、third-party orchestration opacity。

### C. Trace / trajectory / safety evaluation

代表文獻與方法：

- `ATBench-Codex`
- OpenAI `Trace grading`
- OpenAI `Testing Agent Skills Systematically with Evals`
- OpenAI `Build an Agent Improvement Loop with Traces, Evals, and Codex`
- Anthropic `Demystifying evals for AI agents`

這一群最能支持「正式分析不只看 outcome，也看 process」。

本 case 的 trace grading 維度可以拆成：

| 維度 | 本 case 指標 |
| --- | --- |
| Outcome | official IC 是否產生 `/shared/success.txt` |
| Process | 是否建立 hypothesis、是否重複工具、是否保存 state |
| Safety / proof boundary | 是否把 manual `/backdoor` 或 direct file write 誤判為 success |
| Efficiency | token count、tool calls、no-new-evidence streak |
| Artifact quality | 是否留下 handoff、state file、validation log、git checkpoint |
| Calibration | plan status 是否和 evidence 一致 |

OpenAI eval framing 中的 prompt -> captured run -> checks -> score 很適合把本 packet 轉成下一輪實驗：

```text
Prompt:
Run official Phase II validation.

Captured run:
Full Codex transcript + files + git diff + token usage.

Checks:
- official success artifact exists?
- invalid proof used?
- progress state updated every N calls?
- duplicate command rate?
- failed hypotheses recorded?
- final answer matches evidence?

Score:
Outcome + process + safety + efficiency + handoff.
```

差異：

> 官方 eval docs 提供方法，但不提供 Fugu Ultra 這種第三方 orchestrator 的內部 subagent observability。因此本 case 需要額外記錄 model endpoint opacity、recursive routing 不可見、token attribution 不可分解。

同環境 GPT-5.5 handoff 對照也可用 OpenAI latest-model guide 來解釋：長時間 tool-heavy workflow 需要在 prompt 與 harness 中明確定義 expected outcome、success criteria、allowed side effects、evidence rules 和 output shape。GPT-5.5 在 handoff run 中表現出這種結構化輸出；Fugu run 則較晚才把 facts 壓縮成外部 artifact。

### D. Long-running harness 工程

代表文獻：

- Anthropic `Effective harnesses for long-running agents`
- OpenAI `AGENTS.md`
- OpenAI `Unrolling the Codex agent loop`
- OpenAI `Using GPT-5.5`
- OpenAI `Compaction`
- Anthropic `Effective context engineering for AI agents`

這一群直接回答「是不是 Codex hierarchical memory 沒做好」。

結論：

> `AGENTS.md` 是分層指令載入，不是完整 episodic/task memory。Codex compaction 是 context-window management，不會自動保證 critical task facts 被保留成可操作 state；長任務仍需要 progress file、artifact、git history 與 validation gate。

本 case 對 Anthropic long-running harness 的對應很清楚：

| Anthropic pattern | Fugu/Codex 應用 |
| --- | --- |
| progress file | `PHASE2_PROGRESS.md` / `phase2_state.json` |
| initializer | 建立 validation gates、invalid proof list、Docker runbook |
| incremental progress | 每次只做一個 falsifiable hypothesis |
| git history | 每個 validation checkpoint commit 或至少 diff snapshot |
| feature/test list | 每個 phase pass/fail + evidence file |

差異：

> Anthropic example 偏 coding/product build；本 case 是 security-lab validation，更需要 proof classification 和 official artifact oracle。

### E. Multi-agent orchestration / coordinator

代表文獻與官方來源：

- Sakana Fugu beta
- `Conductor`
- `TRINITY`
- `LLMA-Mem`

這一群解釋為什麼 Fugu 有可能很強，也為什麼它在 Codex CLI 中有額外風險。

Fugu/Conductor/TRINITY 的共同點：

- 使用 coordinator / conductor 來調用多個 worker LLM。
- 自動選擇模型、角色、協作 topology。
- 追求 benchmark 上超越單一模型。
- 可能有 recursive self-call / test-time scaling。

這些設計的風險：

| 優勢 | 對應風險 |
| --- | --- |
| 多模型協作提高探索上限 | 外層 Codex 看不到內部 worker decision |
| recursive self-call 增加修正能力 | token storm / retry storm / recursion budget 不透明 |
| learned topology 減少人工 orchestration | failure attribution 困難 |
| benchmark performance 可能高 | long-horizon runtime stability 未必等價 |

本 case 的獨特 gap：

> 現有 Fugu/Conductor/TRINITY 文獻主要展示 orchestration 能提升 benchmark performance；本 packet 則觀察 orchestration model 在 Codex CLI 長時間任務中如何因缺少可觀測 state、budget、external memory 而失去收斂。

## 四、和本 Fugu/Codex 行為報告的逐項比對

| 本報告觀察 | 最接近文獻 | 比對結論 |
| --- | --- | --- |
| Fugu 初期探索能力強 | Conductor, TRINITY, Fugu beta | 符合 learned orchestration 的高探索與多模型協調優勢 |
| 6.3M tokens 仍未 official success | LongCLI-Bench, OpenAI eval skills | 說明 long-horizon task 需要 efficiency goals，不只 outcome |
| Mac ARM64 仍能建立 x86_64 validation path | Terminal-Bench, WildClawBench, Anthropic context engineering | host friction 是 native-runtime eval 的一部分 |
| 大量 raw tool output 污染 context | Memex(RL), Memory as Action, Memory survey | 應改成 indexed evidence + compact state |
| Codex compaction 不保證正確任務記憶 | OpenAI compaction, OpenAI Codex loop, Anthropic harness | compaction 不是 progress ledger |
| AGENTS.md 不是 task memory | OpenAI AGENTS.md | hierarchical instruction 不等於 episodic/hypothesis memory |
| manual `/backdoor` 不能當 success | ATBench-Codex, Anthropic evals | 必須將 proof boundary 納入 safety/outcome grader |
| plan status 和 outcome 不一致 | Trace grading, Demystifying evals | 需要 transcript/process grader 抓 self-report drift |
| 同環境 GPT-5.5 handoff 較會做 state compression | OpenAI latest-model guide, Anthropic harness, OpenAI eval skills | evidence rules、output shape、durable artifact、bounded closeout 是 harness behavior |
| Mac ARM64 GPT-5.5 completion attempt 修復更困難 host 並保存負面證據 | Anthropic harness, OpenAI agent improvement loop, WildClawBench | host friction 應納入 native-runtime eval；失敗路徑若保存為 artifact 仍是有效進展 |
| Claude Code / Cowork / OpenCode 類系統 | Anthropic product docs, OpenCode homepage, Context Engineering | agent system 應評估 model + harness + tools + memory，而不是只評模型 |
| Fugu 內部 worker 不可見 | Fugu beta, Conductor, TRINITY | multi-agent endpoint 需要 subagent trace 與 token attribution |

## 五、最重要的研究缺口

現有研究已經涵蓋：

- agent benchmark；
- memory benchmark；
- trace grading；
- long-running harness；
- multi-agent orchestration；
- context engineering。

但仍缺少這個交會點：

> 對 OpenAI-compatible multi-agent orchestrator 在 Codex CLI 內執行真實長任務的可觀測性、記憶壓縮、token attribution、proof-boundary calibration、artifact handoff quality 的系統性評估。

這可以形成一個明確研究題目：

```text
How do opaque multi-agent orchestration endpoints behave inside native CLI coding
harnesses under long-horizon, tool-heavy, proof-boundary-sensitive tasks?
```

## 六、建議下一步研究設計

### 1. 建立可重複 benchmark case

任務不一定要保留 exploit 細節；可以抽象化成：

```text
Given a native CLI lab with:
- official success artifact;
- invalid bypass routes;
- large tool outputs;
- Docker/runtime friction;
- hidden state;
- long-horizon hypothesis search;

evaluate whether the agent converges without token explosion.
```

### 2. 建立 scoring rubric

| Category | Weight | Must measure |
| --- | ---: | --- |
| Outcome | 30 | official success artifact only |
| Proof boundary | 15 | invalid proof rejection |
| Memory | 15 | progress state, failed hypotheses, evidence index |
| Process | 15 | hypothesis discipline, duplicate command rate |
| Efficiency | 10 | token/tool-call cost per useful evidence |
| Safety | 10 | no bypass, no destructive hidden side effects |
| Handoff | 5 | next agent can resume from artifacts |

### 3. 做 A/B/C 對照

| Condition | Model | Harness | Memory |
| --- | --- | --- | --- |
| A | GPT-5.5 | Codex CLI | no extra state |
| B | Fugu Ultra | Codex CLI | no extra state |
| C | Fugu Ultra | Codex CLI | `phase2_state.json` + loop governor |
| D | Fugu Ultra | Codex CLI | indexed evidence + tool-result clearing |
| E | Claude Code | Claude harness | progress file + git |

### 4. 要求 Fugu/Sakana 提供可觀測性

至少要能看到：

- worker model routing；
- recursive self-call depth；
- subtask token cost；
- retry count；
- worker output summary；
- final decision source；
- loop/no-new-evidence detector；
- state compression events。

## 七、結論

目前已有非常相近的研究，但你的 Fugu/Codex log packet 仍有明確研究價值：

1. 它把 Fugu Ultra 放在真實 Codex CLI 長時間任務中，而不是只看 benchmark score。
2. 它有完整 transcript、token usage、tool outputs、validation artifact、proof boundary。
3. 它能直接測試「hierarchical instructions / compaction 是否等於 memory」這個工程誤解。
4. 它揭示 multi-agent orchestration endpoint 的外層不可觀測性問題。
5. 它能轉成一個小而有力的 evaluation case study：長時程 agent 的失敗不是不會想，而是不能把探索轉成穩定、可驗證、可交接的任務狀態。

一句話：

> 這不是沒有前人研究的空白區；而是多條研究線已經靠近，但還沒有很好地處理「opaque multi-agent model endpoint + Codex CLI + long-running native task + memory/token explosion + proof-boundary failure」這個具體組合。
