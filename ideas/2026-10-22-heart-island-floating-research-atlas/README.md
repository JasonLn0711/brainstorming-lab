# HEART 政策島研究與 Jason 懸浮研究群島

日期：2026-10-22。對象：Jason、後續設計與前端實作者。文件語言：台灣繁體中文。

本研究把一個可操作的 3D 網站拆成內容、幾何、互動、動畫與證據管理，再把可重用的原理轉成 Jason 個人網站的設計。**成果為研究與設計文件；首頁與 `/islands/` 尚未實作。**

## 先讀哪一份

| 文件 | 讀完可以做什麼 |
| --- | --- |
| [需求、來源與查核邊界](01-source-and-evidence.md) | 分清楚使用者決定、公開程式證據、實際操作與未驗證項目 |
| [原站完整前端架構](02-original-architecture.md) | 從八張圖理解啟動、模組、資料、場景、互動、渲染與路網 |
| [工程細節與取捨](03-engineering-analysis.md) | 理解 instancing、點選、路徑、燈光、效能與維護問題 |
| [首頁與懸浮六島設計](04-experience-design.md) | 看到首頁線框、六島特色、內容分工、視覺與操作規格 |
| [自有網站工程規格](05-own-site-architecture.md) | 接續 SvelteKit 實作，掌握資料介面、狀態、生命週期與階段驗收 |
| [七步教學與原理練習](06-learning-guide.md) | 從一個物件逐步理解完整群島，不把教材生成視為學習完成 |
| [查核紀錄與下一驗收點](07-validation-and-next-gates.md) | 查閱本次完成的檢查、限制與未來實作的測試矩陣 |
| [來源清冊](source-manifest.json)／[程式定位表](source-map.md) | 以 URL、SHA-256 與行號重查本次判斷 |

原站最值得學的結構是「一份內容資料同時驅動 3D 物件與文字入口」。它把 14 個政策主題、94 個細項與 20 組關係轉成可探索的場景。我們保留這個結構，讓研究、資安、工作、技能、教學與寫作各有入口，同時維持文章的可讀性與成果的證據邊界。

## 所有權與狀態

- 稀缺資源：訪客注意力、公開主張的可信度、Jason 的學習與維護時間。
- 本 repo：來源、分析、選項、設計、圖表與實作前的驗收規格。
- [網站 repo](../../../JasonLn0711.github.io/)：未來的首頁、Three.js 程式、公開內容、部署及效能實測。
- [Planning 既有網站追蹤頁](../../../planning-everything-track/data/projects/2026-05-public-website-v3-clean-slate-rebuild.md)：入口、狀態、容量與下一決策。
- [Idea OS 記錄](../structured/idea_000048_heart_island_study_and_floating_research_atlas.yaml)：`idea_000048`，65/100；工具分類為 `research_candidate`，生命週期明確保持 `structured`、`exploration_only`。演算法成熟度不是網站開工、學員學會或公開發布的授權。
- 已採納方向：首頁分層閱讀、`/islands/` 探索入口、奇幻微縮懸浮六島、教學與工程雙層筆記。
- 下一關：審閱首屏與三筆公開內容映射，再另行啟動三島垂直切片。
- 容量：本次僅文件研究；沒有排入固定開發時段，也沒有取代個人學習 must-win。

## 維護方法

以本資料夾為起點，網站與 Planning 的相對路徑需回到 `phd-life-system`：`../../../JasonLn0711.github.io` 與 `../../../planning-everything-track`。站方更新時新增查核日期與來源版本，不把新結果回填成舊日已驗證事實。未來公開網站只引用自己撰寫的說明與經審核的成果；完整第三方程式只存在本機忽略的 `reference-cache/`。

相關構想：[UI reverse engineering](../structured/idea_000042_ai_native_ui_reverse_engineering_framework.yaml)提供從觀察到規格的方法；[Rich UI evidence interface](../structured/idea_000045_rich_ui_as_human_factors_evidence_interface_for_ai_agents.yaml)提供資訊可理解性與證據可追溯性的評估角度。此案是個人網站的具體設計，不宣稱提出新的研究方法。

- [2026-10-22 日誌](../../../planning-everything-track/weeks/2026-W43/days/2026-10-22.md#heart-island-2026-10-22)：當日成果、容量邊界與下一決策；詳細研究仍由本資料夾維護。
