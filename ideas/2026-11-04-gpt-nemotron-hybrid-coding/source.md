# 使用者提供原文

- 收錄日期：2026-11-04。
- 來源：本輪使用者訊息中三引號內的完整文字；以下保留原有簡繁混用、程式碼、SVG、網址、下載連結與測試主張。
- 證據邊界：原文是提供的架構建議稿。文中的「我已製作」「我已完成」「已在範例中驗證」均屬來源敘述；本輪未取得所指 ZIP、原圖片或測試報告，也未查核外部連結。

## 原始記錄（逐字）

请解释像这样的技术架构，我要如何在自己的電腦使用或架構呢？然後我使用的是GPT，所以說呢我可能前端的大腦，就前面的大腦我可能用GPT。那後面的決策跟執行我想要用Nemotron 3.5 Super。那去執行.
# GPT × NVIDIA Nemotron 3.5 Super：打造自己的多代理 AI 開發系統

**結論：你提出的架構可以實現，而且不需要使用 Claude Code。** 可以由 GPT 擔任主控大腦（Supervisor），讓 NVIDIA Nemotron 3.5 Super 負責程式設計、技術決策與任務執行，再使用本機工具執行程式、測試與驗證。

不過，我建議將架構設計成：

- **GPT：** 理解需求、規劃任務、分派工作、審查最終結果。
- **Nemotron 3.5 Super：** 分析程式碼、決定實作方式、產生修改、處理錯誤。
- **小型 Subagents：** 平行搜尋檔案、查詢函式、檢查風險。
- **本機執行環境：** 實際讀寫檔案、執行測試，並提供安全隔離。
- **Orchestrator（協調控制器）：** 決定哪些代理可以執行、何時重試、如何交接及何時停止。

這裡最重要的設計原則是：**模型負責提出決策，程式框架負責執行決策，權限系統決定哪些操作被允許。**

## 一、先確認：Nemotron 3.5 Super 真正的規格

NVIDIA 已於 2026 年 10 月 15 日推出 Nemotron 3.5 Super VL，正是你想使用的模型系列。



**NVIDIA Nemotron 3.5 Super VL**

`nvidia/nemotron-3.5-super-vl-120b-a12b`

120B 總參數、12B 活躍參數，採用 Mixture of Experts（MoE）與 Mamba–Transformer 混合架構，支援推理、Coding、Tool Calling，以及文字、圖片與影片輸入。[build.nvidia.com](https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard)[docs.nvidia.com](https://docs.nvidia.com/nemotron/nightly/nemotron/super35/README.html)

它特別適合作為 Agent 的工作模型，但有一個關鍵限制：

**12B 活躍參數不代表只需要儲存 12B 的模型權重。** 完整模型仍有約 120B 參數。

依照你先前提供的 RTX 5080 16 GB 顯示記憶體配置，不適合直接在單張 GPU 上執行完整的 Nemotron 3.5 Super。NVIDIA 官方 NIM 部署規格也以多張資料中心 GPU 為主。[docs.nvidia.com](https://docs.nvidia.com/nim/large-language-models/2.0.13/reference/support-matrix.html)[docs.nvidia.com](https://docs.nvidia.com/nim/large-language-models/2.0.13/get-started/advanced/get-started-nemotron-3.5-super-vl.html)

因此，我推薦先採用 **本機 Orchestrator + GPT API + NVIDIA 雲端 Nemotron 3.5 Super + 本機安全執行環境** 的混合架構。之後再視硬體與資料保密要求，逐步把執行模型移到本機。

## 二、推薦的完整架構

```svg
<svg viewBox="0 0 340 420" width="100%" xmlns="http://www.w3.org/2000/svg"><rect x="69" y="4" width="202" height="39" rx="12" fill="#64748b" fill-opacity=".12" stroke="#64748b" stroke-opacity=".5" /><text x="170" y="20" font-size="12" fill="currentColor" font-weight="600" text-anchor="middle">使用者自然語言需求</text><text x="170" y="34" font-size="10" fill="currentColor" text-anchor="middle">例如：建立網站、修復 Bug</text><path d="M170 43 V65" stroke="#64748b" stroke-width="1.5" /><path d="M166 60 L170 66 L174 60" fill="none" stroke="#64748b" stroke-width="1.5" /><rect x="44" y="67" width="252" height="69" rx="12" fill="#3972bd" fill-opacity=".12" stroke="#3972bd" /><text x="170" y="87" text-anchor="middle" font-size="14" font-weight="700" fill="currentColor">GPT · Supervisor</text><text x="170" y="103" text-anchor="middle" font-size="10.5" fill="currentColor">理解需求 · 規劃 · 分派 · 驗收</text><text x="170" y="120" text-anchor="middle" font-size="10" fill="#3972bd">主控大腦</text><path d="M94 136 V157 H86 V174 M246 136 V157 H254 V174" fill="none" stroke="#64748b" stroke-width="1.4" /><path d="M82 169 L86 175 L90 169 M250 169 L254 175 L258 169" fill="none" stroke="#64748b" stroke-width="1.4" /><rect x="7" y="177" width="157" height="75" rx="11" fill="#15966b" fill-opacity=".1" stroke="#15966b" /><text x="85" y="195" text-anchor="middle" font-size="11.5" fill="currentColor" font-weight="700">Nemotron 3.5 Super</text><text x="85" y="211" text-anchor="middle" font-size="10" fill="currentColor">Coding · 工程決策</text><text x="85" y="226" text-anchor="middle" font-size="10" fill="currentColor">修改程式 · 修復錯誤</text><text x="85" y="242" text-anchor="middle" font-size="9.5" fill="#15966b">NVIDIA 雲端 API</text><rect x="176" y="177" width="157" height="75" rx="11" fill="#8b68c8" fill-opacity=".1" stroke="#8b68c8" /><text x="254" y="195" text-anchor="middle" font-size="11.5" font-weight="700" fill="currentColor">Nemotron Nano 4B</text><text x="254" y="211" text-anchor="middle" font-size="10" fill="currentColor">搜尋程式 · 找依賴</text><text x="254" y="226" text-anchor="middle" font-size="10" fill="currentColor">資料分析 · Read-only</text><text x="254" y="242" text-anchor="middle" font-size="9.5" fill="#8b68c8">Ollama · 本機 GPU</text><path d="M85 252 V273 M254 252 V273" stroke="#64748b" stroke-width="1.5" /><path d="M81 268 L85 274 L89 268 M250 268 L254 274 L258 268" fill="none" stroke="#64748b" stroke-width="1.4" /><rect x="28" y="276" width="284" height="64" rx="11" fill="#c18a36" fill-opacity=".10" stroke="#c18a36" /><text x="170" y="294" font-size="12" font-weight="700" text-anchor="middle" fill="currentColor">OpenCode · Tool Execution</text><text x="170" y="310" font-size="10" text-anchor="middle" fill="currentColor">讀寫檔案 · Terminal · Git · 測試工具</text><text x="170" y="327" font-size="10" text-anchor="middle" fill="#c18a36">權限審核 / 人工批准</text><path d="M170 340 V362" stroke="#64748b" stroke-width="1.5" /><path d="M166 357 L170 363 L174 357" fill="none" stroke="#64748b" stroke-width="1.5" /><rect x="44" y="365" width="252" height="48" rx="11" fill="#64748b" fill-opacity=".1" stroke="#64748b" stroke-opacity=".6" /><text x="170" y="385" font-size="12" text-anchor="middle" font-weight="700" fill="currentColor">隔離工作目錄 / 測試環境</text><text x="170" y="401" font-size="10" text-anchor="middle" fill="currentColor">驗證結果 → 回報 GPT → 決定完成或重試</text></svg>
```

建議的 Hybrid Multi-Agent Coding 架構。箭頭表示主要控制與執行路徑；GPT 可在收到結果後再次派工。

這是一種 **Hierarchical Multi-Agent Architecture（階層式多代理架構）**。

它和圖片中的 Claude Code 架構具有相同核心思想，但使用的模型與控制框架不同。

| 原圖片的角色 | 你的系統 |
|--------|--------|
| Opus Advisor | GPT 主控、重大決策與審查 |
| Sonnet Lead | Nemotron 3.5 Super 實作 |
| Haiku Swarm | Nemotron Nano 4B 本機子代理 |
| JEV Fork Layer | Orchestrator 的任務路由與重試邏輯 |
| Session Log | Git Diff、執行紀錄、測試報告 |

圖片中 JEV 顯示的 `p=0.94`、`1,354 forks` 等數值，不能單憑畫面認定是真正的效能統計。這些也不是建立多代理系統必備的元件。

## 三、最適合的現成開源工具：OpenCode 2



**OpenCode**

開源 Coding Agent／Orchestrator

可管理多種模型、工具權限、主代理與子代理，並在 Terminal、桌面或 Web 介面操作。

[OpenCode 2 官方文件](https://opencode.ai/v2/docs)

我查到一項對你非常有利的功能：**OpenCode 2 支援使用 ChatGPT Plus／Pro 登入 OpenAI 模型。**

因此，如果你的方案與登入方式符合支援條件，就能直接使用 ChatGPT 帳戶提供的 GPT 額度，而不一定需要另外購買 OpenAI API。模型使用仍受訂閱額度限制；NVIDIA 則需要自己的 API Key。[opencode.ai](https://opencode.ai/v2/docs/providers)[opencode.ai](https://opencode.ai/v2/docs/agents)

這比自己從零編寫 LangGraph Orchestrator 更適合作為第一版，因為 OpenCode 2 已經處理代理的建立、工具調用、子任務交接與權限審批。自訂路由政策可以等第一版驗證成功再開發。

## 四、我已製作一份可以直接使用的 Starter Kit

**GPT × Nemotron Multi-Agent Starter**

OpenCode 2 設定檔、四個代理、Python 測試專案、連線檢查與繁體中文 README

gpt-nemotron-opencode2-starter.zip[下載完整 Starter Kit（ZIP）](sandbox:/mnt/data/gpt-nemotron-opencode2-starter.zip)

我已完成設定檔的 JSON 語法檢查及 Python 範例程式測試。範例刻意保留兩項失敗測試，讓你使用代理實際修復。

**目前尚未實際連線你的 OpenAI、NVIDIA 帳戶或執行 OpenCode 代理流程。** 這部分需要在你的電腦上完成驗證。

### Step 1：Ubuntu 安裝 OpenCode 2

在 Ubuntu Terminal：

```
curl -fsSL https://opencode.ai/v2/install | bash
opencode --version
```



這是官方提供的安裝方式。執行前應確認下載來源；也可以使用官方 npm 套件安裝。特別注意使用 **V2**，因為它的代理設定格式已經與 V1 不同。[opencode.ai](https://opencode.ai/v2/docs)[opencode.ai](https://opencode.ai/v2/docs/permissions)

### Step 2：本機安裝小型 Nemotron

如果你已經安裝 Ollama，就直接執行：

```
ollama pull nemotron-3-nano:4b

ollama run nemotron-3-nano:4b
```



**這個 4B 模型適合你的 RTX 5080 16GB。**

Ollama 官方列出的 4B 模型下載大小約 2.8–2.9 GB，具體顯示記憶體需求仍會隨上下文長度及執行配置增加。[ollama.com](https://ollama.com/library/nemotron-3-nano)

它不負責高難度主要程式開發，而是快速完成唯讀搜尋、檔案定位和簡單分析。

### Step 3：設定 NVIDIA Super API

前往 [NVIDIA Nemotron 3.5 Super](https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b) 取得 API Key。

NVIDIA 目前列有供原型測試使用的免費 Endpoint，但這不代表無限免費或具備正式服務保證。[build.nvidia.com](https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b)

切換到 Bash，安全輸入金鑰：

```
bash

read -rsp 'NVIDIA API Key: ' NVIDIA_API_KEY
echo
export NVIDIA_API_KEY
```



不需要下載完整 120B 模型；你自己的電腦透過 HTTPS 呼叫 NVIDIA 模型服務即可。

### Step 4：啟動多代理系統

將下載的 ZIP 解壓縮，進入其中的 `gpt-nemotron-starter` 資料夾：

```
cd gpt-nemotron-starter

python3 scripts/check_config.py

opencode --standalone
```



首次啟動，在 OpenCode 輸入 `/connect`，選擇 OpenAI，並使用 ChatGPT 帳戶授權。接著用 `/models` 確認模型是否可用。

Starter Kit 已設定四個代理：

| Agent | 實際模型 | 權限 |
|--------|--------|--------|
| `supervisor` | GPT-6.1 Sol | 規劃、派工，不直接修改 |
| `implementer` | Nemotron 3.5 Super | 修改需批准，測試需批准 |
| `explorer` | Nemotron Nano 4B | 唯讀 |
| `reviewer` | GPT-6.1 Sol | 唯讀審查 |

其中 `supervisor` 是預設入口，因此你只要向它提出需求，它就可以根據任務選擇子代理。OpenCode 2 的代理設定確實支援指定不同模型、主代理與子代理，以及對每種工具指定不同權限。[opencode.aiopencode.ai](https://opencode.ai/v2/docs/agents)

### Step 5：給 GPT 第一個任務

可直接複製到 OpenCode

我希望修復 `demo/normalize.py` 中的字串正規化錯誤。

請先使用 explorer 搜尋相關程式和測試，再由 implementer 決定修復方法、修改程式與執行測試。修改檔案或執行命令之前，請先請求我的批准。

最後由 reviewer 獨立審查，並由 supervisor 回報修改內容、測試是否通過，以及仍然存在的風險。

[複製任務]

理想情況下，你會看到 GPT 將工作分派給不同模型，而不是單一模型從頭處理到尾。是否真的依序呼叫所有代理，仍需要在第一個實測中檢查執行紀錄。

## 五、這套系統實際上怎麼運作？

最核心的是 **Tool Calling（工具呼叫）與 Agent Orchestration（代理協調）**。

假設你要求：「幫我修復網站登入功能，確保不會出現重複 Session。」

| 階段 | 誰負責 | 實際工作 |
|--------|--------|--------|
| 1\. 規劃 | GPT | 定義問題、限制和驗收標準 |
| 2\. 探索 | Nano 4B | 找出登入程式、Session 管理和測試位置 |
| 3\. 工程決策 | Nemotron 3.5 Super | 判斷應修改哪些檔案、採用哪些技術 |
| 4\. 實作 | Nemotron + OpenCode 工具 | 提出程式修改，經批准後寫入檔案 |
| 5\. 測試 | 本機測試工具 | 真正執行測試，取得 Exit Code 與結果 |
| 6\. 審查 | GPT | 檢查是否符合目標、是否引入其他問題 |
| 7\. 完成或重試 | GPT + Orchestrator | 接受結果，或要求修復未通過部分 |

注意第 4、5 階段：Nemotron 不是真的用自己的模型權重去操作檔案系統。

它會產生工具請求，例如「修改 `auth.py`」或「執行單元測試」。**OpenCode 接收請求、執行權限檢查，再由本機程序完成操作。**

這也是為什麼同一套工具框架能夠替換 GPT、Nemotron 或其他模型，而不必重新開發整個執行系統。

### 那麼圖片中的 JEV Fork Layer 呢？

它可以理解成更進階的 Routing / Retry Controller。

例如，你未來可以自己制定這樣的政策：

```
def route_task(task):    if task["read_only"]:        return "explorer"    if task["risk"] == "high":        return "human_approval"    return "implementer"
```



這只是路由政策的示意程式，**Starter Kit 目前採用的是 GPT 主代理依任務指派子代理**，並沒有實作圖片中聲稱的 JEV 分數演算法。

等你能穩定完成多代理協作後，再使用 LangGraph 設計明確的 State Machine、重試次數、平行佇列與人工審批關卡，會更容易驗證每一項控制決策。

另外，唯讀搜尋通常可以平行執行；修改同一組程式碼的代理則應優先採取序列化寫入，以避免檔案衝突。

## 六、三種架構如何選擇？

| 方案 | 優勢 | 主要限制 | 適合階段 |
|--------|--------|--------|--------|
| **OpenCode 2 + GPT + Nemotron Cloud** | 整合快、少寫框架程式、有現成工具與權限 | 依賴雲端模型與額度 | **現在首選** |
| LangGraph + GPT API + Nemotron API | 可完全自訂路由、狀態、重試與紀錄 | 需要維護自己的代理程式 | 進階研發 |
| GPT Cloud + 本機 Nemotron Nano | 低本機資源需求、執行模型不送雲端 | 小模型複雜 Coding 能力有限 | 部分本地化 |

對你的需求，第一個方案最有利於先完成可運作的系統。當你確定要研究自動派工、動態路由、Agent 協作效能時，再選擇第二個方案。

## 七、正式使用之前需要注意的資安問題

這套系統會有兩個重要的信任邊界。

第一個是**雲端資料邊界**。GPT 與 NVIDIA Hosted Super 都是在遠端推論，代理讀取並送入模型上下文的程式碼、紀錄等資料可能離開本機。因此醫院資料、患者資訊、機密原始碼，都需要先確認資料傳輸與使用條件。

第二個是**本機執行邊界**。即使代理設定要求執行前批准，模型仍可能產生不安全命令。OpenCode 的權限設定是控制與審批機制，不能取代作業系統隔離；官方也明確區分 `allow`、`ask` 與 `deny`。[opencode.ai](https://opencode.ai/v2/docs/permissions)

實際部署時，建議使用獨立的 Git 工作目錄，將不可信程式的執行與測試放到受限 Docker 容器或 VM，不提供 SSH Key、雲端金鑰、Docker Socket 或不必要的網路權限。

## 八、第一版的驗收標準

Starter Kit 已經建立了一個可以觀察成果的實驗：

**初始狀態（已在範例中驗證）** (2 項失敗)

`test_simple`：通過

`test_repeated_spaces`：失敗

`test_tabs_and_newlines`：失敗

---

**代理執行後的目標**

3/3 測試通過、只有核准的檔案被修改、沒有未經批准的命令，並且 GPT 能提供實際測試證據與最終審查結果。

這個實驗可以同時驗證模型連線、跨模型派工、檔案操作、權限機制以及測試回饋。比一開始就做大量平行代理更容易定位問題。

**建議下一步：** 先下載 Starter Kit，在獨立的 Ubuntu 測試資料夾執行一次 GPT → Nemotron 3.5 Super → 測試 → GPT 審查的完整流程。確認穩定後，再擴充成圖片中的多代理 Swarm。

**理解檢查：** 如果 Nemotron 3.5 Super 要求執行一段會刪除專案檔案的 Shell 指令，為什麼即使 GPT 已經同意這項修改，我們仍然需要由本機權限控制器及隔離環境檢查？
