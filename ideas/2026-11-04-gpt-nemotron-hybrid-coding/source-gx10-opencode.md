# GX10 與 OpenCode 全架構補充：使用者原文

- 收錄日期：2026-11-04。
- 來源：本輪使用者訊息三引號內全文；保留來源措辭、數字、連結與指令。
- 已確認的使用者更正：RTX 5080 已移交其他研究生，實驗室目前改用 GX10。
- 證據邊界：ASUS Ascent／GB10／128 GB、OpenCode 功能、NVFP4 支援與檔案大小、帳戶條件及 Starter Kit 測試為提供稿主張，未本輪查核。ZIP 與原圖未取得；未執行部署或代理。

## 原始記錄（逐字）

我們是否可以直接用 OpenCode直接把上面的你給我的那個完整的架構全部包起來呢？包含 GPT嘛，也要包含包含 Nemotron 3.5跟 Nano的部分，全部包起來。還是說 OpenCode只能包到下面託 execution的部分呢？請你給我 OpenCode的相關的介紹以及教學。
以下請記憶下來，我們的 rtx 5080 已經移交給其他研究生使用，我們的實驗室電腦現在換成 gx10。
# OpenCode × GPT × Nemotron：在 GX10 上建立完整的多代理 AI 系統

## 一、結論：OpenCode 可以整合整套架構，不只是 Tool Execution

**可以直接使用 OpenCode 2，把 GPT、NVIDIA Nemotron 3.5 Super、Nemotron Nano，以及本機工具執行環境整合在同一個系統中。**

OpenCode 本身已經是一套 AI Coding Agent 平台，具備模型管理、主代理（Primary Agent）、子代理（Subagent）、任務分派、工具呼叫、工作階段管理與權限控制等功能。

因此，**你的第一版系統不需要另外開發 LangGraph Orchestrator，也不需要使用 Claude Code。** OpenCode 2 官方文件已明確支援不同代理指定不同模型，並能透過子代理工作階段處理任務。[OpenCode](https://opencode.ai/v2/docs/agents?utm_source=chatgpt.com)

### 我已更新你的實驗室硬體資訊

你提供的硬體異動已納入後續規劃：

- 原本的 **RTX 5080 已移交其他研究生使用**。
- 實驗室目前改用 **GX10**。
- 未來討論本機 LLM、CUDA、模型部署與多代理系統時，不再預設 RTX 5080 可用。

以下先以 **ASUS Ascent GX10（NVIDIA GB10）** 為規劃基礎。如果你們使用的是不同廠牌或規格的 GX10，硬體細節再依實際機型調整。

## 二、GX10 讓你的架構出現一個重要的新選擇：Super 可以考慮完全本機部署



ASUS Ascent GX10 的主要硬體為：

| 項目 | 規格 |
|---|---|
| 處理器 | NVIDIA GB10 Grace Blackwell Superchip |
| CPU | 20-core ARM |
| GPU | NVIDIA Blackwell GPU |
| 記憶體 | 128 GB LPDDR5X 統一記憶體 |
| 作業系統 | NVIDIA DGX OS，基於 Linux |
| AI 運算能力 | 最高 1 PFLOP，特定低精度條件 |
| 主要用途 | 本機 AI 模型推論、開發與微調 |

來源：ASUS 官方產品規格。[ASUS Global](https://www.asus.com/tw/networking-iot-servers/desktop-ai-supercomputer/ultra-small-ai-supercomputers/asus-ascent-gx10/techspec/?utm_source=chatgpt.com)

### 關鍵發現：Nemotron 3.5 Super 的 NVFP4 版本正式列出支援 DGX Spark

NVIDIA 官方模型部署資料顯示：

**Nemotron 3.5 Super VL 120B-A12B 的 NVFP4 量化版本，支援單台 DGX Spark（GB10）。**

它支援 vLLM、SGLang、TensorRT-LLM 等推論框架。NVIDIA 的硬體對照表將 DGX Spark 列為 NVFP4 可以使用單台設備部署的配置。[NVIDIA NIM](https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard?utm_source=chatgpt.com)

這代表你目前有兩條可行路線：

| 方案 | GPT | Nemotron Super | Nemotron Nano |
|---|---|---|---|
| A：混合式 | OpenAI 雲端 | NVIDIA 雲端 API | GX10 本機 |
| **B：高度本地化** | OpenAI 雲端 | **GX10 本機** | **GX10 本機** |

我建議你**先建立方案 A，再驗證方案 B**。

原因是方案 A 的整合成本較低，可以先驗證多代理工作流程；方案 B 則能進一步降低 Super 推論資料傳送至 NVIDIA 雲端的需求。

要注意：**官方支援單台 GB10 部署，不代表模型在所有上下文長度、並行數量及吞吐量要求下都能順暢運作。** 尤其 Super 與 Nano 若同時常駐 GX10，仍然需要考量統一記憶體、KV Cache、頻寬及推論速度。

---

## 三、OpenCode 的技術架構：從主代理到工具執行

先建立一個核心觀念：

**OpenCode 是 Agent Orchestration Platform，不是 LLM，也不只是 Shell 工具。**

它負責把使用者需求、模型、子代理、工具和執行紀錄串在一起。

```text
                  使用者
                    │
                    ▼
          ┌─────────────────────┐
          │      OpenCode 2     │
          │  統一協調與控制平台  │
          └──────────┬──────────┘
                     │
                     ▼
          ┌─────────────────────┐
          │    GPT Supervisor   │
          │                     │
          │ 理解需求、規劃、派工 │
          │ 審查結果、決定完成   │
          └──────────┬──────────┘
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
 ┌──────────────────┐  ┌──────────────────┐
 │ Nemotron Super   │  │ Nemotron Nano    │
 │                  │  │                  │
 │ 技術決策         │  │ 搜尋檔案         │
 │ 程式修改         │  │ 找函式、依賴     │
 │ Debug            │  │ 唯讀分析         │
 │ 測試與修復       │  │                  │
 └─────────┬────────┘  └────────┬─────────┘
           │                    │
           └─────────┬──────────┘
                     ▼
          ┌─────────────────────┐
          │    OpenCode Tools   │
          │                     │
          │ Read / Edit / Shell │
          │ Git / MCP / Tests   │
          └──────────┬──────────┘
                     │
                     ▼
          ┌─────────────────────┐
          │    GX10 / Ubuntu    │
          │                     │
          │ 專案檔案、測試環境   │
          │ Git、Docker、vLLM   │
          └─────────────────────┘
```

其中 GPT 可以是 OpenAI 雲端模型，Super 可以在 NVIDIA 雲端或 GX10 本機執行，Nano 則可以透過 GX10 的 Ollama 提供推論服務。

### OpenCode 提供的主要功能

| OpenCode 功能 | 白話文解釋 |
|---|---|
| Provider | 管理模型要連線到哪裡 |
| Primary Agent | 直接接收你的需求的主代理 |
| Subagent | 接受主代理派工的專門代理 |
| Session | 保存對話、任務與工具執行狀態 |
| Tools | 真正讀寫檔案、執行命令的工具 |
| Permissions | 決定哪些操作允許、拒絕或需要批准 |
| MCP | 讓代理接入其他工具或外部系統 |
| Plugins | 擴充 OpenCode 的既有能力 |

OpenCode 2 的子代理可以使用自己的模型、System Prompt 與權限，並在獨立的子工作階段運作。它也支援背景子代理任務。[OpenCode](https://dev.opencode.ai/v2/docs/agents/?utm_source=chatgpt.com)

但 OpenCode **不會自動提供你圖片中的 JEV 評分演算法**。如果未來要求代理依照成本、成功率、延遲及風險進行精確路由，才需要進一步開發專用 Router。

---

## 四、我已為 GX10 製作新的 OpenCode Starter Kit

這次的版本同時包含兩種部署設定。

**gx10-opencode-multiagent-starter.zip[下載 GX10 × GPT × Nemotron Multi-Agent Starter Kit](sandbox:/mnt/data/gx10-opencode-multiagent-starter.zip)**

壓縮檔包含：

| 檔案 | 用途 |
|---|---|
| `opencode.cloud.json` | GPT + 雲端 Super + 本機 Nano |
| `opencode.local.json` | GPT + GX10 本機 Super + 本機 Nano |
| `demo/normalize.py` | 用來實際修復的 Python 程式 |
| `demo/test_normalize.py` | 三項單元測試 |
| `README.md` | 安裝、設定、執行與安全說明 |

設定檔已通過 JSON 語法檢查；Python 範例也已確認初始狀態包含兩項預設的失敗測試。

**尚未完成的部分：** 在你的 GX10 上實際啟動模型、連線 GPT，以及驗證完整多代理交接流程。

### Step 1：確認 GX10 環境

在 GX10 的 Terminal 執行：

```bash
uname -m
nvidia-smi
free -h
```

正常的 ASUS Ascent GX10 應使用 ARM64 架構，並具備 GB10 與約 128 GB 統一記憶體。

特別提醒：GX10 使用的是 Unified Memory。不能直接沿用一般獨立顯示卡的 VRAM 使用經驗來估算模型部署能力。

### Step 2：安裝 OpenCode 2

```bash
curl -fsSL https://opencode.ai/v2/install | bash

opencode --version
```

官方提供 Linux ARM64 版本，因此 OpenCode 本身可以安裝於 GX10。[OpenCode](https://opencode.ai/v2/docs?utm_source=chatgpt.com)

請確認安裝的是 V2，避免混用 OpenCode 1 的設定格式。

### Step 3：讓 GPT 成為主代理

進入解壓縮後的專案資料夾。

啟動 OpenCode，輸入：

```text
/connect
```

選擇 OpenAI，使用 ChatGPT 帳戶登入。

OpenCode 2 官方目前支援符合條件的 ChatGPT Plus／Pro 登入方式，使用量依方案限制計算。這不代表 OpenAI API 可以無限制使用，也不會自動匯入你目前的 ChatGPT 對話紀錄。[OpenCode](https://opencode.ai/v2/docs/providers/?utm_source=chatgpt.com)

接著輸入：

```text
/models
```

確認 GPT 模型可以使用。

Starter Kit 預設以 `openai/gpt-6.1-sol` 作為 Supervisor 與 Reviewer。若實際模型清單不同，應以你登入後能使用的模型 ID 為準。

### Step 4：讓 Nano 在 GX10 本機運作

先依照 Ollama 官方 Linux 安裝方式完成安裝。

接著執行：

```bash
ollama pull nemotron-3-nano:4b

ollama list
```

再確認本機 API：

```bash
curl http://127.0.0.1:11434/api/tags
```

OpenCode 2 可以自動探索預設本機位址上的 Ollama 模型。[OpenCode](https://opencode.ai/v2/docs/models/?utm_source=chatgpt.com)

另外，GX10 不一定只能執行 Nano 4B。

Ollama 也提供 `nemotron-3-nano:30b`。其量化模型大小依版本約為 18–24 GB，因此可以列入 GX10 的測試候選。[Ollama](https://ollama.com/library/nemotron-3-nano?utm_source=chatgpt.com)

我的建議是：若 Super 使用雲端 API，可以比較 Nano 4B 與 30B 的任務準確率；若 Super 與 Nano 都要在 GX10 本機運作，先從 Nano 4B 開始，避免資源競爭。

---

## 五、先啟動混合式架構

這是最容易驗證的第一版。

在 NVIDIA 取得 API Key：

[NVIDIA Nemotron 3.5 Super](https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b?utm_source=chatgpt.com)

於 Bash 輸入：

```bash
read -rsp 'NVIDIA API Key: ' NVIDIA_API_KEY
echo

export NVIDIA_API_KEY
```

進入 Starter Kit 資料夾後：

```bash
OPENCODE_CONFIG="$PWD/opencode.cloud.json" \
opencode --standalone
```

這時候預期的模型配置是：

| Agent | 模型 | 推論位置 |
|---|---|---|
| Supervisor | GPT | OpenAI |
| Implementer | Nemotron 3.5 Super | NVIDIA Cloud |
| Explorer | Nemotron Nano 4B | GX10 |
| Reviewer | GPT | OpenAI |

你現在只需要與 GPT Supervisor 溝通。

GPT 再根據任務指派 Nemotron，而不是你必須手動在三個模型之間複製貼上訊息。

---

## 六、第二階段：把 Super 也放到 GX10 本機

這部分現在值得研究。

根據 NVIDIA 官方模型檔案：

| 精度 | 模型檔案大小 |
|---|---:|
| BF16 | 約 231.84 GB |
| NVFP4 | 約 69.91 GB |

對單台 128 GB GX10 而言，應優先考慮 **NVFP4 版本**。[NVIDIA NGC](https://catalog.ngc.nvidia.com/orgs/nim/nvidia/models/nemotron-3.5-super-vl-120b-a12b/bf16-ga-20261003?utm_source=chatgpt.com)

NVIDIA 的 Nemotron 3.5 Super NVFP4 模型卡已提供針對 DGX Spark GB10 的 vLLM 配置，包含特殊 Tool Calling 與 Reasoning Parser 設定。[Hugging Face](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4?utm_source=chatgpt.com)

### 本機部署要分成兩件事

**第一件：讓 vLLM 在 GX10 上提供模型服務。**

例如：

```text
Nemotron Super NVFP4
        │
        ▼
  vLLM Inference Server
        │
        ▼
 http://127.0.0.1:8000/v1
```

建議依 NVIDIA 官方模型卡的完整部署指令操作，不要直接把一般 vLLM 的簡短啟動命令當成已驗證的 GX10 配置。

官方模型與部署指引：

[Nemotron 3.5 Super NVFP4 官方模型卡](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4?utm_source=chatgpt.com)

**第二件：讓 OpenCode 連線這個本機服務。**

當 vLLM 成功啟動後，先檢查：

```bash
curl http://127.0.0.1:8000/v1/models
```

再使用 Starter Kit 的本機設定：

```bash
OPENCODE_CONFIG="$PWD/opencode.local.json" \
opencode --standalone
```

這時候 OpenCode 不必改變整個多代理架構。

唯一主要差別是：

```text
原本：

Implementer
    ↓
NVIDIA Cloud API


改成：

Implementer
    ↓
GX10 本機 vLLM API
```

**GPT 仍然是前端主代理，Super 仍然是後端工程代理，Nano 仍然是探索代理。**

需要注意，NVIDIA 的單台 Spark 配置以有限並行數為主要測試情境。模型雖然可以部署，但同時執行 Super、Nano 與多個 Agent，不保證具有理想吞吐量或延遲。

---

## 七、實際操作時，OpenCode 怎麼幫你工作？

假設你有一個網站專案。

你可以直接對 GPT Supervisor 說：

> 請分析目前網站的登入系統。先讓 Nano Explorer 找出相關檔案與依賴，再交給 Nemotron Super 判斷最小修改方案。
>
> 修改前請求批准，完成後執行測試。最後由 GPT Reviewer 審查安全性、程式品質與測試證據。
>
> 不要推送 Git、不准部署正式環境。

OpenCode 便能依照 Agent 設定與模型回應，發起子任務和工具呼叫。

但是，**模型決定要呼叫哪個工具，不等於它已獲得執行權限。**

OpenCode 的權限系統會先判斷：

- `allow`：允許執行。
- `ask`：需要你批准。
- `deny`：拒絕執行。

OpenCode 2 允許針對不同 Agent 和工具指定不同政策。[OpenCode](https://opencode.ai/v2/docs/permissions?utm_source=chatgpt.com)

Starter Kit 讓主要檔案修改與 Shell 指令先經過批准，並讓探索及審查代理維持唯讀。

但仍須注意：這不是完整沙箱。對於不可信程式，應額外使用隔離的 Docker 容器或 VM。尤其實驗室專案若涉及患者資料、醫療系統或機密程式碼，不能只依賴 OpenCode 的提示與權限規則。

---

## 八、OpenCode 與 LangGraph，應該如何分工？

| 需求 | OpenCode 2 | 額外 Orchestrator |
|---|---|---|
| GPT 管理多個子代理 | 支援 | 不需要 |
| 不同 Agent 使用不同模型 | 支援 | 不需要 |
| 子代理平行探索 | 支援 | 通常不需要 |
| 編輯檔案、執行測試 | 支援 | 不需要 |
| 人工審批 | 支援 | 不需要 |
| 固定多階段流程與轉移條件 | 可部分實現 | 建議擴充 |
| 依歷史成功率自動選模型 | 需客製 | 建議 |
| 完整任務狀態機與重試政策 | 需客製 | 建議 |
| 研究級 Agent Routing Benchmark | 需額外實作 | 建議 |

如果你只是要建立一個好用的 AI 開發團隊，OpenCode 已經足夠當第一版平台。

如果未來的研究主題是 **Multi-Agent Orchestration、模型路由最佳化、成本與效能評估**，那麼 OpenCode 可以成為底層執行平台，而你自己開發的 Router 或 Workflow Controller 則負責高階控制邏輯。

---

## 九、我建議的實作順序

你現在最值得優先完成的是：

**第一階段：OpenCode + GPT + NVIDIA Cloud Super + GX10 Nano。**

先確認三種模型可以正常連線，並完成一次真正的多代理程式修復。

**第二階段：把 Nemotron 3.5 Super NVFP4 部署在 GX10。**

先單獨測試模型載入、工具呼叫、推論延遲和記憶體使用情形，再讓 OpenCode 指向本機 vLLM。

**第三階段：建立真正的 Agent Swarm。**

加入多個 Nano 探索代理、Git Worktree、任務佇列與結構化測試報告。等這些功能穩定後，才加入圖片中的動態評分、Retry Router 與成本控制機制。

這樣可以把每一階段的成功與失敗原因分開驗證，而不是一開始就面對所有模型、工具和框架同時出錯。

### 官方教學資源

[OpenCode 2 官方入門](https://opencode.ai/v2/docs?utm_source=chatgpt.com)

[OpenCode Agents 與 Subagents](https://opencode.ai/v2/docs/agents?utm_source=chatgpt.com)

[OpenCode 模型與 Ollama 整合](https://opencode.ai/v2/docs/models/?utm_source=chatgpt.com)

[OpenCode 工具權限與安全控制](https://opencode.ai/v2/docs/permissions?utm_source=chatgpt.com)

### 理解檢查

假設 GPT Supervisor 已經要求 Nemotron Super 修改程式，而 Super 必須執行一段 Shell 指令。

**你認為真正決定這段指令能否在 GX10 上執行的，是 GPT、Nemotron Super，還是 OpenCode 的權限系統？**

再進一步想：如果我們要確保惡意程式即使被批准執行，也無法讀取實驗室其他研究資料，光靠 OpenCode 的權限設定是否足夠？
