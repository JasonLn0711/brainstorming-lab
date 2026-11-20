# GPT × Nemotron 混合式開發代理架構

## 來源與已確認需求

[完整原文](source.md)保留本輪使用者提供的內容，包含原始提問、八節架構說明、SVG、角色對照、安裝／金鑰輸入／啟動指令、第一個任務、三種方案、資安邊界、測試目標與理解檢查。原文簡繁混用、網址標籤及單行示意程式維持原樣。

[canonical YAML](../structured/idea_000049_gpt_nemotron_hybrid_coding_agent_architecture.yaml) 是狀態、成熟度、連結及下一關的主檔。`idea_000049` 為 `structured`，規則計算 `59/100`；分數衡量資料結構與構想成熟度，模型／帳戶可用性、實作完成及真人驗收仍須各自舉證。

`confirmed`：Jason 希望在自己的電腦，以 GPT 作為前端主控大腦，讓 Nemotron 3.5 Super 處理後端工程決策與執行；本輪要求詳實紀錄。

`working assumption`：提供的長文建議使用雲端 Super、本機 Nano 與 OpenCode。這是待查核的方案組合；本輪採納的是來源保存與問題整理，工具選擇、帳戶授權、實作與部署保留後續決策。

## GX10 補充與硬體更正（2026-11-04）

[九節補充完整原文](source-gx10-opencode.md)接續最初的[八節原文](source.md)。新增 OpenCode 是否能包住整套架構的提問、平台概念表、架構圖、兩份設定檔、四個安裝步驟、混合式／本機路線、LangGraph 分工、三階段提案與理解檢查。

`confirmed`：使用者明確表示 RTX 5080 已移交其他研究生，實驗室目前改用 GX10，並要求記憶。後續本機模型、CUDA、排程與資源規劃以 GX10 為前提；前稿 RTX 5080 文字保留作歷史來源。

`pending confirmation`：ASUS Ascent、GB10、ARM64、128 GB、DGX OS 及現有可用資源仍需實機確認。提供稿的型號假設與官方規格敘述分開保存，不以本輪紀錄作實機驗證。

| 補充問題／方案 | 已保存的提案與驗證邊界 |
| --- | --- |
| OpenCode 能否包住全架構 | 提案將 Provider、Primary Agent、Subagent、Session、Tools、Permissions、MCP、Plugins 放在同一平台；各項現行能力、設定格式與跨模型交接待查核 |
| A：混合式 | GPT 在 OpenAI、Super 在 NVIDIA Cloud、Nano 在 GX10；屬先行建議，尚未採納為執行計畫 |
| B：高度本地化 | GPT 在 OpenAI、Super／Nano 在 GX10；GPT 上下文仍可能離開本機，雲端資料界線仍須核定 |
| Super NVFP4 | 單台 DGX Spark 支援、框架／parser 配置、BF16 231.84 GB 與 NVFP4 69.91 GB 均為來源主張；檔案大小不等於執行期總記憶體 |
| Nano 候選 | 原文提出 4B／30B 與 18–24 GB；模型標籤、量化與實際資源需求待查核，不新增比較實驗 |
| 新 Starter Kit | `gx10-opencode-multiagent-starter.zip` 及 cloud／local JSON 僅在來源中被提及；未取得壓縮檔、未驗證 JSON 或預設失敗測試 |
| 三階段順序 | 混合式交接 → 本機 Super → Swarm；均保留為提案，實際啟動仍須各階段證據與使用者決定 |
| 權限與隔離 | 保存 `allow`／`ask`／`deny` 說明及 Docker／VM 邊界；未在 GX10 實測權限或隔離 |

硬體更正已同步到 `idea_000043` 的 `current_hardware_override`，保留既有單一模型持有者、佇列與 API 的推理，避免將舊 RTX 5080 部署步驟當成目前設備的操作指令。

## 架構解讀與責任分工

| 層次 | 原文建議 | 本輪紀錄的責任邊界 |
| --- | --- | --- |
| 主控 | GPT supervisor | 理解需求、限定任務與驗收、分派及審查 |
| 工程決策 | Nemotron 3.5 Super implementer | 提出實作方式、差異及工具請求；實際模型識別待查核 |
| 探索 | 本機 Nemotron Nano 4B explorer | 唯讀搜尋與依賴分析；模型標籤及能力待確認 |
| 工具執行 | OpenCode／本機程序 | 接收工具請求，檢查權限，實際讀寫與測試 |
| 操作控制 | 本機權限控制器與隔離環境 | 限定檔案、命令、網路與憑證可及範圍；批准與隔離分別驗證 |
| 協調與停止 | Orchestrator | 路由、重試、交接與停止條件；原文尚無 JEV 實作證據 |
| 驗收證據 | 測試工具與 GPT reviewer | 真實模型呼叫、工具事件、批准、Git diff、exit code 與結果交叉對應 |

核心分界：模型提出決策與工具請求；本機程序執行；權限與作業系統隔離控制操作範圍。GPT 的同意屬於協作決策，操作是否獲准及執行時能接觸哪些資源，由相應控制層決定。

## 待查核清單

本輪僅保存來源，未開啟或驗證以下外部頁面；網址與數字保留於原文供後續逐項核對。

| 項目 | 原文主張／附件 | 目前證據狀態與下一關 |
| --- | --- | --- |
| Super 模型 | 2026-10-15、VL、120B／12B、模型 ID、MoE／Mamba–Transformer、多模態及工具呼叫 | 待官方模型卡與部署文件查核，記錄日期、版本及限制 |
| 本機硬體 | 前稿 RTX 5080 16 GB；續稿更正為 GX10 | RTX 5080 已移交；GX10 為目前規劃前提，實機規格與執行資源待確認 |
| OpenCode | V2 路徑、安裝方式、代理設定、provider、`--standalone`、`/connect`、`/models` | 待核對現行官方文件與實際版本，再決定是否安裝 |
| OpenAI 帳戶 | ChatGPT Plus／Pro 登入、GPT-6.1 Sol 模型識別與訂閱額度 | 待查官方授權條件、可用模型及 provider 支援；不預設訂閱可替代 API |
| Nano | `nemotron-3-nano:4b`、2.8–2.9 GB、RTX 5080 適配 | 待核對 Ollama 標籤、實際模型、下載量、工具能力及 runtime 記憶體需求 |
| NVIDIA 雲端 | endpoint、免費測試額度、金鑰 | 待確認可用性、限額、費用與資料條款；本輪未取得憑證或連線 |
| Starter Kit | `sandbox:/mnt/data/gpt-nemotron-opencode2-starter.zip` | 僅取得來源中的文字連結；未取得 ZIP，不能認定本機存在該檔案或四代理設定 |
| JSON／Python 測試 | 已檢查設定、初始一通過兩失敗、目標三項通過 | 原文主張／目標；未取得程式與報告，本輪未重現 |
| JEV 圖片 | `p=0.94`、`1,354 forks`、角色對照 | 未取得原圖及統計定義，不作效能證據；保留為待確認背景 |
| 路由程式 | 原文單行 `def route_task(...)` 示意 | 作為文字示意保存，未當作可執行 Python 或控制器實作 |
| 部分本地化 | GPT Cloud＋本機 Nano | 執行模型可在本機的方案提議；GPT 接收的上下文仍可能離開本機，資料範圍待明定 |

## FIRST PRINCIPLE 與啟動關卡

- 稀缺資源：可驗證的跨模型交接、操作權限、研究注意力、雲端資料界線與帳戶額度。
- canonical owner：brainstorming-lab 保存來源、問題、比較、反對意見與下一關；未建立獨立執行專案。
- Planning role：僅保留 ID、狀態、分數、定位、容量與下一關；本輪沒有新增研究排程。
- 下一關：Jason 先確認是否要進入查核／實作；查核產品識別與帳戶條件，取得實際 Starter Kit 或明確決定替代方式，再核定可送雲端的資料及操作範圍。
- 後續若明確啟動，才在獨立測試目錄驗證來源描述的最小交接。保留實際角色／模型、工具請求／批准／執行事件、檔案差異與真實測試結果；越權或無法辨識模型時停止。首次流程完成只證明該次可用性。
- 暫緩：大量平行 swarm、JEV 演算法、自建 LangGraph 控制器、尚待查核及另行啟動的 GX10 本機 Super 部署，以及正式敏感專案接入。須由最小流程的實際瓶頸與明確授權重新啟動。

## 連接既有構想

- [idea_000019：Codex-wrapped AI Scientist](../structured/idea_000019_codex_wrapped_ai_scientist_research_os.yaml)：重用協調器、來源／結果追溯與人類關卡；該構想的研究引擎及既有 soft-control 決策維持原有範圍，本次記錄開發代理的角色分工。
- [idea_000043：Shared GPU model-owner inference service](../structured/idea_000043_shared_gpu_model_owner_inference_service.yaml)：本機 Nano 或其他推論服務的模型持有、VRAM、排程與 API 邊界可接回此構想；本輪未啟動其 ASR-first 或模型管理器工作。
- [Idea index](../../index/idea_index.md)：由 CLI 重建的搜尋入口；雙向連結由 `scripts/link_ideas.py` 建立。
- [Planning day note](../../../planning-everything-track/weeks/2026-W45/days/2026-11-04.md#gpt-nemotron-source-2026-11-04)與[定位卡](../../../planning-everything-track/data/projects/2026-04-brainstorming-lab.md#gpt-nemotron-source-2026-11-04)：容量與下一關。

## 保存檢查

[source-manifest.json](source-manifest.json) 記錄原始內容區段的 SHA-256、位元組數、八節／五步驟／SVG 區段及結尾檢查；它驗證已寫入檔案的結構與後續完整性。逐字區段由本輪訊息轉錄保存，未將結構檢查描述成外部來源或執行結果的查核。

[gx10-source-manifest.json](gx10-source-manifest.json) 保存續稿逐字區段的雜湊與九節／四步驟結構檢查；原稿與續稿各有獨立清冊。


## 2026-11-16｜近期目標：Qwen workers 與遠端控制

Jason 明示這是近期很想完成的目標之一；[完整供稿](source-2026-11-16-qwen-remote.md)與[詳細更新／查核／關聯](update-2026-11-16-qwen-remote.md)承接 GPT 主控、Qwen FP4-Local 候選及 Web／SSH→Telegram 的提案。延續 `idea_000049`，Nemotron 選項保留歷史。CLI 重算 69/100；生命週期維持 structured，演算法候選分類不代表人工升級或部署通過。

[11/16 日誌](../../../planning-everything-track/weeks/2026-W47/days/2026-11-16.md#gx10-opencode-qwen-2026-11-16)與[W47](../../../planning-everything-track/weeks/2026-W47/weekly-plan.md#gx10-opencode-qwen-2026-11-16)保留容量／下一關。W47 Red／待重評，先確認可用容量、雲端資料／費用與既有 inference／Telegram owner；沒有新排部署時段。舊模型／Starter Kit 主張保持原證據邊界。
