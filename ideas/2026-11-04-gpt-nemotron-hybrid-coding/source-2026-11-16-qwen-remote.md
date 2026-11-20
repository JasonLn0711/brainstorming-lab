# 2026-11-16｜GX10 × OpenCode × Qwen 與遠端控制：使用者完整供稿

來源：本次使用者訊息。下方逐字保存引號內供稿；技術主張與設定保留原樣，查核與採納狀態另見 companion。使用者於引號外補充：「我最近的目標之一是很想做到這個。」本次要求完整筆記與跨檔連結，未要求安裝、部署或 Git 發布。

<!-- source:start -->
1. 最近想要嘗試利用 opencode ，以 gpt-6.1-max 為大腦與 orchestrator，下方控制 qwen-3.8-next-flash nvfp4 作為多個 subagents ，來當成一個 mvp 的 agent system ，在我們的 gx10 上面運行
2. 另外，除了在 gx10 上面以 opencode 操作 agent system 之外，是否可以透過 telegram 或其他方式來操作這台 gx10 上面的 agent system 呢？請給我你的專業建議。
# GX10 × OpenCode：建構混合式 Multi-Agent System 的架構建議

## 一、核心結論

我建議採用這個方向，但先建立「雲端 Orchestrator + GX10 本地 Subagents + 獨立遠端控制層」的架構，而不是一開始就追求大量並行代理。

你的目標可以拆成三層：

- 決策層（Brain）： OpenAI GPT-6.1 系列負責任務分解、分派、品質審查與最終決策。
- 執行層（Workers）： ASUS Ascent GX10 上部署 Qwen 本地模型，讓多個 OpenCode subagents 共用推論服務。
- 控制層（Control Plane）： 除了直接使用 OpenCode，也能透過 Telegram、網頁或其他電腦遠端提交任務、監控進度、核准操作。

這個設計具備研究價值，因為它可以實際測量：強大雲端模型是否能透過有效的任務分工，以較低成本的本地模型完成大部分工作，同時維持可靠性與安全性。

不過，目前有兩項需要先處理的技術問題。

模型名稱與 API 設定

需要修正

官方模型目錄列出 `gpt-6.1-sol`，並支援 `max` reasoning effort；`gpt-6.1-max` 不是目前查證到的正式 API model ID。可以使用 GPT-6.1 Sol 搭配 max 推理強度，或改用更強的 `gpt-6-astra`。

[image](https://www.google.com/s2/favicons?domain=https://developers.openai.com\&sz=32)

OpenAI API+1



Qwen3.8-Flash-Next NVFP4

硬體適配風險

NVIDIA 確實提供 `Qwen3.8-Flash-Next-NVFP4`，但原廠部署規格所需記憶體相當大，不能直接認定它能在 GX10 的 128GB unified memory 上，以一般 vLLM 設定完整運行。

[image](https://www.google.com/s2/favicons?domain=https://huggingface.co\&sz=32)

Hugging Face+1



因此，MVP 最重要的是先證明「本地模型可以可靠接收工作、回傳結果、被審查並接受遠端控制」，而不是一開始就讓最大的模型承擔所有工作。

## 二、關鍵發現：NVIDIA 已有適合單台 GX10 的 Qwen3.8 Flash-Next 版本

進一步查證後，有一項非常重要的進展：NVIDIA 在 2026 年 10 月發布了專為本地硬體最佳化的 `Qwen3.8-Flash-Next-FP4-Local`。

這比直接使用原始的 NVIDIA NVFP4 checkpoint 更符合你的需求。

[Ascent GX10的價格推薦 - 2025年11月 | 比價比個夠BigGo](https://images.openai.com/static-rsc-4/w9WV0FmE6JlWRWkg2RmBvQQpGo14q16DjfIAZkWoER3brNfJBgpQucjTgrcCAaM35xH8c0QjQrjcqJDWidAVo_5YsV54dbUgB9BuPcnsmsQZRhfjblyvyOgOQtY7ZrcsAaivZIjgVFpMD7el8g_7MPvDFLuc_yb221p8S4YuBkA?purpose=inline)

ASUS Ascent GX10

GB10 Grace Blackwell · ARM64 · 128GB unified memory · DGX OS

你的 GX10 屬於 NVIDIA DGX Spark 同級平台，可參考 NVIDIA 的 Spark 推論部署方案。

[image](https://www.google.com/s2/favicons?domain=https://www.asus.com\&sz=32)

ASUS TW - 產品規格+1



三種可行模型方案

| Qwen3.8-Flash-Next-FP4-Local | 優先實驗<br>NVIDIA 已在單台 DGX Spark 驗證，模型檔案約 96 GiB，需使用指定 vLLM 容器。 |
| ---------------------------- | ------------------------------------------------------------ |
| `Qwen3.8-Flash-Next-NVFP4`   | 原始 NVIDIA 量化版本。標準部署記憶體需求較高，單台 GX10 通常需要特製 offload 或其他最佳化。    |
| `Qwen3.8-27B-NVFP4`          | 可靠的備援與基準<br>NVIDIA 官方單機 Spark 部署指南直接支援，資源餘裕較大。               |

來源：

[image](https://www.google.com/s2/favicons?domain=https://huggingface.co\&sz=32)

Hugging Face+2

可以直接研究這兩份 NVIDIA 官方資料：

- [Qwen3.8-Flash-Next-FP4-Local 模型與部署說明](https://huggingface.co/nvidia/Qwen3.8-Flash-Next-FP4-Local?utm_source=chatgpt.com)
- [NVIDIA DGX Spark 單機 vLLM 部署指南](https://build.nvidia.com/spark/vllm/intermediate?utm_source=chatgpt.com)

這意味著你的原定模型方向不必放棄，只要改用適合 GB10 的 checkpoint 和推論容器即可。但「能載入模型」與「能同時提供多個代理可接受的延遲」是兩個不同的驗收條件。

有社群在單台 DGX Spark 上報告 Flash-Next 約 17–49 output tokens/s 的單路效能，結果因 checkpoint、推論核心、speculative decoding 與測試內容而異。這些是不同條件的社群量測，不應當成 GX10 的保證效能。

[image](https://www.google.com/s2/favicons?domain=https://huggingface.co\&sz=32)

Hugging Face+2



## 三、我建議的 MVP 系統架構

邏輯架構示意。除了 GPT 模型推論位於雲端，其餘元件原則上都部署在 GX10；Telegram 訊息另會經過 Telegram 服務。

這裡有一個容易誤解、但會直接影響系統效能的觀念：

多個 subagents 不等於 GX10 同時載入多份 Qwen 模型。

例如，你建立 `explore`、`review`、`test-analysis` 三個代理，可以讓它們使用不同的 system prompts、工具權限與工作階段，但都向同一個 vLLM endpoint 發送推論請求。

這種方式可以避免重複載入大型模型。真正需要管理的是並行請求、KV cache、上下文長度與推論排程。

對第一版，我建議：

| 角色              | 模型                  | MVP 權限                       |
| --------------- | ------------------- | ---------------------------- |
| Orchestrator    | GPT-6.1 Sol，High 起步 | 分派工作、讀取結果；修改與執行需核准           |
| Explorer        | 本地 Qwen Flash-Next  | 唯讀搜尋與分析                      |
| Reviewer        | 同一個本地 Qwen          | 唯讀檢查、找出缺陷                    |
| Writer／Executor | 第二階段再加入             | 獨立 worktree、限縮 shell、必要時人工核准 |

此處特別要注意，OpenCode 的 subagent 並不會自動繼承父代理的較低權限；每個代理必須單獨設定。OpenCode V2 也預設允許部分專案外目錄存取，因此需要明確禁止。

[image](https://www.google.com/s2/favicons?domain=https://opencode.ai\&sz=32)

OpenCode+1



### OpenCode 設定範例

以下是一份針對 OpenCode V2 的簡化 `opencode.jsonc`，目標是先跑通一個 GPT orchestrator 與兩個唯讀本地 subagents。

```

{
  "$schema": "https://opencode.ai/config.json",
  "default_agent": "orchestrator",

  "providers": {
    "gx10": {
      "package": "@opencode/ai/providers/openai-compatible",
      "settings": {
        "baseURL": "http://127.0.0.1:8000/v1"
      },
      "models": {
        "qwen-flash": {
          "modelID": "nvidia/Qwen3.8-Flash-Next-FP4-Local",
          "capabilities": {
            "tools": true,
            "input": ["text"],
            "output": ["text"]
          },
          "limit": {
            "context": 32768,
            "output": 4096
          }
        }
      }
    }
  },

  "permissions": [
    { "action": "external_directory", "resource": "*", "effect": "deny" },
    { "action": "shell", "resource": "*", "effect": "ask" },
    { "action": "edit", "resource": "*", "effect": "ask" }
  ],

  "agents": {
    "orchestrator": {
      "description": "Delegate bounded tasks, verify results, and integrate findings.",
      "mode": "primary",
      "model": "openai/gpt-6.1-sol#high",
      "permissions": [
        { "action": "subagent", "resource": "*", "effect": "deny" },
        { "action": "subagent", "resource": "explore-local", "effect": "allow" },
        { "action": "subagent", "resource": "review-local", "effect": "allow" }
      ]
    },

    "explore-local": {
      "description": "Read-only source code exploration and analysis.",
      "mode": "subagent",
      "model": "gx10/qwen-flash",
      "steps": 8,
      "permissions": [
        { "action": "*", "resource": "*", "effect": "deny" },
        { "action": "read", "resource": "*", "effect": "allow" },
        { "action": "glob", "resource": "*", "effect": "allow" },
        { "action": "grep", "resource": "*", "effect": "allow" }
      ]
    },

    "review-local": {
      "description": "Read-only review; report defects with file and line evidence.",
      "mode": "subagent",
      "model": "gx10/qwen-flash",
      "steps": 8,
      "permissions": [
        { "action": "*", "resource": "*", "effect": "deny" },
        { "action": "read", "resource": "*", "effect": "allow" },
        { "action": "glob", "resource": "*", "effect": "allow" },
        { "action": "grep", "resource": "*", "effect": "allow" }
      ]
    }
  }
}

```

這是架構起始設定，不代表已在你的 GX10 上實測成功。使用前需確認 OpenAI 帳號連線、vLLM 已啟動，以及本地模型的實際 tool-calling 格式。OpenCode 的 vLLM 自動偵測無法辨識工具呼叫能力，因此才要明確註冊 `capabilities.tools`；只有實際確認 vLLM 的 `qwen3_xml` tool-call parser 能正確工作後，才應開啟它。

[image](https://www.google.com/s2/favicons?domain=https://opencode.ai\&sz=32)

OpenCode+2



另外，這份設定對專案內檔案仍有唯讀存取能力，因此第一版應使用不含秘密金鑰的測試 repository，不要將它視為完整的作業系統沙盒。

## 四、如何在手機或其他電腦遠端操作 GX10？

可以，而且不必將 GX10 的 OpenCode 或 vLLM 服務直接公開到網際網路。

我建議將「遠端完整操作」與「手機快速指揮」分開設計。

| 遠端方式                        | 最適合的用途              | 我的建議        |
| --------------------------- | ------------------- | ----------- |
| Tailscale + OpenCode Web UI | 查看完整工作階段、檔案變更、核准操作  | 第一優先        |
| Telegram Bot                | 手機派工、查詢狀態、接收通知、取消工作 | 第二優先        |
| SSH + OpenCode CLI / tmux   | 維運、debugging、恢復服務   | 必備備援        |
| 自建 Web Dashboard            | 管理大量任務、佇列、成本及跨專案工作  | MVP 驗證成功後再做 |

### 方案 A：Tailscale + OpenCode 原生 Web UI

這是我認為最適合先建立的遠端介面。

OpenCode V2 已內建具備密碼保護的 Web UI 與背景服務，官方也支援透過 SSH port forwarding 存取。

[image](https://www.google.com/s2/favicons?domain=https://opencode.ai\&sz=32)

OpenCode+1



在 GX10 上執行：

```

opencode service start
opencode service status
opencode pair

```

假設 GX10 的 OpenCode 服務位於 `127.0.0.1:49374`，在另一台已可透過 SSH 連上 GX10 的電腦執行：

```

ssh -L 49374:127.0.0.1:49374 USER@GX10_TAILSCALE_HOST

```

然後在該電腦的瀏覽器開啟 GX10 產生的一次性配對連結。Linux 的預設埠目前是 49374，但應以 `opencode service status` 顯示的實際埠為準。

Tailscale 讓你的筆電與 GX10 維持在私有網路連線環境，不需要為了操作 OpenCode 直接開放公開 SSH、OpenCode 或 vLLM 埠。可以參考 [Tailscale 官方網站](https://tailscale.com/?utm_source=chatgpt.com)。

### 方案 B：Telegram Bot 作為 Agent Control Plane

Telegram 非常適合你的需求，但不應直接等同於「可以在 Telegram 輸入任何 Linux 指令」。

我建議第一版 Bot 支援這些操作：

使用者在 Telegram 發出

`/task 分析目前 repository 的認證流程，找出三個主要安全風險。只允許讀取，不得修改。`

GX10 回應

Task #1042 已接受

狀態：執行中

Orchestrator：GPT-6.1 Sol

Workers：Explorer、Reviewer

權限：Read-only

可透過 /status 1042 查看進度，或 /cancel 1042 取消。

實作方面有兩條路。

路線一：先試現成的 OpenCode Telegram 整合。

例如 GitHub 上已有 [opencode-telegram-remote](https://github.com/HenryYannis/opencode-telegram-remote?utm_source=chatgpt.com) 與 [opencode-telegram-bot](https://github.com/isMeStranger/opencode-telegram-bot?utm_source=chatgpt.com)，提供不同形式的 Telegram 與 OpenCode 整合。這些是第三方專案，適合先研究設計和做短期 POC；我不建議在未審查其程式碼、金鑰管理和權限處理前，讓它們直接控制你的主要開發環境。

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub+1



路線二：自建很薄的 Telegram Gateway。這是我最推薦的正式 MVP 路線。

架構如下：

`Telegram → Bot Gateway → 任務佇列 → OpenCode API → Agents → 結果回報`

Gateway 可以使用 Python 或 TypeScript，並以 Telegram Bot API 的 long polling 接收指令。這樣 GX10 只需要對外發起 HTTPS 連線，不必為 Telegram 開設 inbound webhook 埠。

[image](https://www.google.com/s2/favicons?domain=https://core.telegram.org\&sz=32)

core.telegram.org



我會要求 Gateway 至少包含：

- 使用 Telegram `user_id`、私人 `chat_id` 雙重 allowlist。
- 只開放 `/task`、`/status`、`/report`、`/cancel` 等明確定義的操作。
- 每項工作具有獨立 `job_id`，限制併發數、執行時間與資源預算。
- 不接受 `/exec 任意指令`，不提供無限制 shell 或 sudo。
- 高風險操作必須取得一次性、具時效性的核准；重要操作優先在私有 Web UI 審批。
- Bot token、OpenAI API key 與專案秘密資訊均不透過 Telegram 回傳。

Telegram Bot 並不是端對端加密的秘密工作環境。你的 GPT orchestrator 又會使用雲端 API，因此必須清楚界定哪些程式碼、文件與研究資料可以離開 GX10。

## 五、安全設計：防止合法 Subagent 取得超出用途的能力

這個 MVP 最大的風險不是本地 Qwen 推論結果不夠好，而是 Agent 的權限邊界沒有被真正落實。

例如，Reviewer 被授權閱讀一份 repository 文件，文件裡卻含有惡意指令，要求代理讀取 `.env` 並將內容發送到某個外部地址。這是典型的 indirect prompt injection。若 Reviewer 擁有 shell、網路及不受限的目錄權限，就可能形成 excessive agency。兩項風險分別對應 OWASP LLM01:2025 與 LLM06:2025。

[image](https://www.google.com/s2/favicons?domain=https://genai.owasp.org\&sz=32)

OWASP Gen AI Security Project+1



我建議用三道獨立控制：

1. Agent permission： Explorer、Reviewer 初期只能讀取專案工作樹；不得直接執行 shell、修改檔案或啟動其他代理。
2. OS isolation： 以非 root 帳號執行 OpenCode；使用隔離工作目錄，必要時加入容器、filesystem 與 network restrictions。不要掛載 Docker socket 或提供主機管理權限。
3. Approval gate： 檔案大量修改、刪除、Git push、部署、網路外傳及其他高影響操作，都應獨立核准，而不是讓 LLM 自行判定是否允許。

另外，NVIDIA 的 Spark 模型部署範例包含 `--network host` 及停用部分容器隔離控制的旗標。這些設定可能是硬體相容所需，但不能直接當成安全的網路部署範本。至少應限制 vLLM 8000 埠僅供本機或可信服務存取，並固定模型與容器版本。

[image](https://www.google.com/s2/favicons?domain=https://huggingface.co\&sz=32)

Hugging Face



## 六、實作順序與驗收標準

不建議同時投入完整 Bot、五六種 subagents、GPU 調校與 Web Dashboard。那會使故障定位過於困難。

1. 階段 1：單模型推論基線

   在 GX10 依 NVIDIA 指引啟動 `Qwen3.8-Flash-Next-FP4-Local`，驗證模型載入、一般回應、JSON tool call、記憶體使用量與推論延遲。若不穩定，先以 `Qwen3.8-27B-NVFP4` 建立可運作基線。

   通過條件：本機 API 可穩定處理測試請求，工具參數可解析，無 OOM。
2. 階段 2：OpenCode Hybrid Agents

   接入 GPT-6.1 Sol 與兩個 Qwen subagents。先執行唯讀任務，再逐步增加有審批機制的修改工具。

   通過條件：可以確認每個子任務由指定模型完成，且拒絕不被允許的工具與檔案操作。
3. 階段 3：遠端操作

   先完成 Tailscale、SSH tunnel 和 OpenCode Web 配對，確認可靠後再加入 Telegram long-polling gateway。

   通過條件：手機能提交、查詢、取消任務；未授權 Telegram 使用者無法存取；外部網路無法直接連接 vLLM。
4. 階段 4：系統量測與決策

   比較三個架構：GPT-only、Qwen-only 與 GPT + Qwen Hybrid。在同一組任務上測量品質、速度、成本、工具呼叫正確率及資源使用量。

   通過條件：取得可重複的基線，知道 Hybrid 何時比單模型更值得使用。

我會使用約 20 項具有預期結果的真實程式工程任務作為初步評估集，並將併發量由 1、2 逐步提高到 4，而不是直接開 8 個 Workers。

| 核心指標                        | 要回答的問題                     |
| --------------------------- | -------------------------- |
| Task success rate           | 交付的成果是否通過測試？               |
| Tool-call validity          | Qwen 是否正確選工具、填參數、回收錯誤？     |
| End-to-end latency（p50/p95） | Hybrid 是否因分派與排隊反而更慢？       |
| Peak unified memory         | 多工作階段是否造成 GX10 記憶體壓力？      |
| Cost per successful task    | 省下的雲端 token 是否抵銷本地執行成本與重試？ |
| Security violation count    | 是否有未經授權的讀取、修改或命令執行？        |

最有價值的研究問題不是「能不能同時跑十個 agents」，而是：

> 在固定硬體、成本與權限條件下，雲端 Orchestrator 應該將哪些任務分派給本地模型，才能使整體任務成功率最高？

這個問題可以進一步延伸為任務複雜度估計、模型路由、風險感知分派、動態併發控制與 subagent 評估方法。

## 七、最終選型建議

第一版架構

推薦

OpenCode V2 + GPT-6.1 Sol High + Qwen3.8 Flash-Next FP4-Local + Tailscale + Telegram Gateway

一台 GX10、一個本地 vLLM 推論服務、一個雲端 orchestrator、兩個唯讀 worker profiles、一個遠端控制入口。

我會保留 `max` reasoning effort 給複雜規劃、最終審查或失敗後的重新分析，而不是每個 orchestrator 回合都使用最高推理強度。

同時，不要以「多代理一定優於單一強模型」作為前提。如果 20 項任務的結果顯示 Hybrid 的成功率沒有改善，或者節省的 API 費用不值得增加的延遲與維護複雜度，就應降低分派頻率或改用更小、更快的本地 worker。

對 GX10 而言，這將是一個範圍可控、容易實驗，也能持續擴充的 Agent System MVP。

最後有一道設計理解題：如果三個 subagents 都共用同一個 Qwen vLLM Server，而測試發現從一個 agent 增加到四個後，總 tokens/s 上升、但每項任務完成時間也大幅增加，你會優先檢查 GPU 算力、KV cache、排程佇列，還是 orchestrator 的任務拆分方式？為什麼？

這道題能幫助我們決定下一步的系統量測應該從哪一層開始。
<!-- source:end -->
