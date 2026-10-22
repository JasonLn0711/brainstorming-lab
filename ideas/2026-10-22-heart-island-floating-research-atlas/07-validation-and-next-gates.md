# 查核紀錄與下一驗收點

返回[閱讀入口](README.md)。日期：2026-10-22；作者角色：協助來源查核、架構解讀與設計整理。Jason 提供學習目的、懸浮島主題、首頁參考與探索入口決策。

## 本次可宣告的成果

| 層次 | 狀態 | 證據 |
| --- | --- | --- |
| 需求來源 | `source preserved` | 使用者原文與選項保存在來源章 |
| 公開程式來源 | `source preserved` | 16 個資源的 URL、擷取時間、hash；完整本機副本由 Git 忽略 |
| 原站資料參照 | `validated`，限宣告範圍 | [source-checks.json](source-checks.json)：唯一 ID、sources／flows／endpoints／quotes／dayCycle 參照，0 筆發現 |
| 文件與圖表 | `validated`，限語法與本機預覽 | 12 張 Mermaid 通過 parser；瀏覽器預覽產生 12 個 SVG、0 個 error icon，抽看第一張整體圖 |
| 教學範例 | `validated`，限純數學 | NDC 範例中心、左上、右下、零尺寸拒絕共 4 項通過 |
| 構想方向 | `adopted decision` | 閱讀首頁、六島主題、微縮懸浮、`/islands/` 與雙層筆記 |
| 自有網站 | `implementation pending` | 沒有改網站程式、沒有新增 Three.js 到網站依賴 |
| Git／網站發布 | 未執行 | 沒有 commit、push 或 deploy |

[document-checks.json](document-checks.json)記錄 parser 版本與文件檢查結果。來源 hash 證明副本一致，不能證明遠端部署歷史或作者身份。圖表成功產生 SVG 也不等於所有輸出平台的換行與可讀性均已驗收。

## 原站操作觀察

| 操作 | 實際結果 | 範圍 |
| --- | --- | --- |
| 桌面載入 | 出現 3D 城市、政策清單、14／94 數字與控制列 | 本次 Brave；非跨瀏覽器驗收 |
| 選擇「交通」 | 清單展開七個細項，顯示主題卡、協作與來源 | DOM 選取路徑 |
| 選擇「通學區」 | 顯示細項、對象、說明、時程與來源 | 不查核政策內容是否實現 |
| 選擇 F6 | 顯示協作卡、角色、攜帶圖示與三項來源 | 資料與 UI 對應 |
| 搜尋 YouBike | 只顯示交通的單一符合細項 | 一筆正向搜尋，不宣稱搜尋全面正確 |
| 桌面開卡後縮到 390×844 | 進入底部面板布局，清單與卡片同時占位 | 視窗尺寸模擬；不是手機冷啟動或觸控測試 |
| 手機布局點「關閉清單」 | accessibility tree 未回報變化 | 不據此宣稱關閉成功或永久故障 |
| 恢復桌面 | 桌面控制列恢復 | 視窗 override 已 reset |

原站畫面與上述操作顯示於對話中的瀏覽工具；本資料夾未匯出外站 screenshot 檔。持久證據為來源 snapshot hash、定位表與操作記錄。FPS、記憶體、canvas 點擊命中率、觸控拖曳、完整鍵盤路徑、導覽播放與 WebGL 失敗都未實測。

## 文件與 repository 檢查

- `python3 scripts/normalize_problem.py idea_000048`：通過，`normalization_status=validated`。
- `python3 scripts/score_maturity.py idea_000048`：65/100，工具分類 `research_candidate`。
- 自動工具會將 maturity level 寫入 status。本案依已採納的探索範圍，把生命週期保留為 `structured`，另有 `activation_status=exploration_only` 與明確 `status_basis`；分數保持原計算結果。未修改評分器或藉分數啟動實作。
- `link_ideas.py` 對 `idea_000042`、`idea_000045` 建立雙向連結；保留原檔格式與既有 dirty 內容，只加入新 connection。
- `generate_clusters.py` 與 `generate_index.py` 已執行；clusters 內容無差異，idea／tag indexes 增加新項目。
- `uvx --with pytest pytest tests/test_idea_os.py -q`：23 passed。
- 新文件的本地 Markdown 連結、空白與配對 code fence 另外檢查；兩 repo 的 `git diff --check` 結果記入 `document-checks.json`。
- 新圖以 Mermaid parser 驗證，並用本機暫存預覽檢查 SVG 生成；preview server 於檢查後停止，沒有公開網站。
- `docs/document-contracts.md` 在此 checkout 不存在；本次讀取現有 `docs/agent-deliverable-contracts.md` 與 voice contract。這是本機文件路徑狀況，不替其他任務建立或改寫契約。

原站 source-cache、解析工具與臨時預覽不加入網站 repo，也不引入正式專案依賴。沒有執行網站 build，因為本輪沒有修改網站程式；不能引用歷史 build 結果當成本輪新設計的驗證。

## 自有網站未來驗收矩陣

下表為後續實作的驗收規格，全部仍為 `not_run`。

| 情境 | 檢查方式與通過條件 |
| --- | --- |
| 首頁閱讀 | 文字與文章入口不需 Three.js；首頁無 3D bundle 請求 |
| 三筆內容映射 | ID、卡片、地標與全文皆指向同一公開 record，狀態不變形 |
| 六島辨識 | 桌面與手機全景能選到六島；名稱不只靠顏色區分 |
| 清單與 canvas | 任一路徑選同一內容，卡片與 URL 一致 |
| 拖曳與點擊 | 旋轉結束不誤選；窄小地標有足夠 hit proxy |
| 深連結 | 有效 island／item、未知 ID、雙參數與瀏覽器前後返回均符合規格 |
| 搜尋 | 空字串、大小寫、無結果、跨島作品都可恢復操作 |
| 手機狀態轉換 | 清單與詳情互斥，轉向與 resize 後可讀；關閉恢復合理焦點 |
| 無障礙 | Tab／Enter／Escape 可完成任務；減少動態沒有強制鏡頭飛行 |
| WebGL 或載入失敗 | 文字清單仍存在；重試不疊加 canvas 或事件 |
| 生命周期 | 連續進出 route 十次，RAF、listener 與 GPU 資源不持續累增 |
| 三維一致性 | 島浮動時模型、名牌、hit proxy、航線端點保持一致 |
| 效能 | 按工程章的具名設備、30 秒路徑與 p95 frame-time 目標記錄結果 |
| 公開內容 | 網站 bundle 中沒有私人來源、工作區連結或未核定內容；讀取為公開資料 allowlist |
| 現有頁面回歸 | 首頁改版後原 research／projects／teaching／blog／resume 路由仍可用 |
| 使用者理解 | 找到研究貢獻與作品證據兩項任務；觀察成功率與困難，不以漂亮截圖推定理解 |

## 下一決策與停止條件

下一個具體交付是「首頁首屏＋三筆內容映射的審閱」，其後才是 AI／資安／工作三島切片。六島完整設計已保存，切片只是控制實作規模。

若群島造成閱讀負擔、手機效能未達標或維護成本不值得，保留閱讀首頁與文字入口，縮減或暫停 3D 功能。只有使用者明確啟動後才排入開發；研究文件不自動變成日週承諾。

可重用於前端學習、網站實作交接與公開作品敘事。若要轉成履歷成果，現階段只能稱為「完成技術研究與設計規格」，不能稱為已發布個人 3D 網站。
