# 需求、來源與查核邊界

返回[閱讀入口](README.md)。查核日：2026-10-22；網站內容可能繼續更新。

## 使用者原文

### 初始來源與學習目的

> [https://puma.taipei/heart-island](https://puma.taipei/heart-island)
> 請告訴我，這個網站是怎麼做的？我想要學習。

### 深入研究與完整筆記要求

> 請針對這個網站深入分析，並且詳實寫出他的完整架構圖，並且思考如果我們要使用同樣技術做一個自己的網站，要怎麼設計。全部都詳實筆記下來。看你想要把筆記放在哪裡，哪個repo ，你來規劃。

### 網站主題補充

> AI研究、資安研究、工作、技能等等，規劃各自特色的不同島嶼，這些島嶼都是像是阿凡達一樣的懸浮島嶼。請你依照你對我們的了解來規劃。

使用者選擇「個人研究與作品島」與「教學與工程雙層」。

### 首頁與共存方式補充

> 同時，我們現在的首頁，也必須修化設計，可以採用我們現在很喜歡的常在 notion 使用以及我們的 learning page kairos learning 裡面的格式與結構設計來研究如何改進比較適合我們當成首頁。

使用者選擇「新增探索入口」與「奇幻微縮群島」。上方保留「修化」原字；設計解讀為研究與改善既有首頁。

### 執行指示

> Implement the plan.

承接已提出的研究文件計畫：完成筆記、圖表與索引。計畫明確將網站程式、提交與部署留在後續階段；本次沒有擴大成網站實作。

## 證據分層

| 標籤 | 意義 | 本次範例 |
| --- | --- | --- |
| 來源事實 | 在本次保存的公開程式或資料中可定位 | Three.js r160、`PerspectiveCamera`、JSON 的 14／94／20 |
| 操作觀察 | 在本次瀏覽器操作看見的結果 | 搜尋 YouBike 後清單只剩對應細項 |
| 工程推論 | 從程式解讀出的機制、成本或風險 | 字串搜尋可能命中隱藏的來源 ID；不是搜尋精準度實測 |
| 採納方向 | 使用者已選定的產品方向 | 六島主題、懸浮微縮、現有網站新增入口 |
| 設計提案 | 為後續實作定出的預設值 | 六島座標、配色、手機單一底部面板 |
| 未驗證 | 沒有本次執行證據 | 真實手機 FPS、WebGL 失敗回退、人類可用性 |

## 來源與保存方式

1. [HEART 政策島](https://puma.taipei/heart-island)：觀察入口與公開 HTML。
2. 該 HTML 指向 `/heart-island-assets/` 的自訂 JS、CSS、JSON，以及 `vendor/three/build/three.module.js`。詳見 [manifest](source-manifest.json)。URL query 的版本字串不是不可變版本；SHA-256 才辨識本次 bytes。
3. [Kairos Learning](https://learn.cs-kairos.com/)與其 `style.css`：首頁結構、字級、閱讀寬度、色彩與焦點樣式。
4. 私人 Notion 的 MATLAB 教材頁：僅用來理解摘要、選案例、逐步教學、來源與下一步的結構。本包不複製私人附件、工作紀錄或私人頁面全文；公開對照可看 [MATLAB 課程入口](https://learn.cs-kairos.com/courses/matlab-practice/)。
5. 現有網站本機 `package.json`、`AGENTS.md`、`src/routes/+page.svelte`、`src/lib/content/site.ts`：確認 SvelteKit 2、Svelte 5、靜態 adapter、現有頁面與內容分工。套件版本以 package.json 宣告為準，未宣稱本次重建成功。
6. Three.js 官方 [Fundamentals](https://threejs.org/manual/pages/fundamentals.html)、[Responsive Design](https://threejs.org/manual/pages/responsive.html)、[Cleanup](https://threejs.org/manual/pages/cleanup.html)；Svelte 官方 [Lifecycle hooks](https://svelte.dev/docs/svelte/lifecycle-hooks)、[adapter-static](https://svelte.dev/docs/kit/adapter-static)。用於概念與後續整合的依據，不取代原站 r160 程式。

公開程式的完整本機查核副本放在 `reference-cache/`，由本資料夾 `.gitignore` 排除。可追蹤文件保存 URL、時間、byte 數、行數與雜湊，不把外站程式當成我們的產品原始碼。此副本是本機留存，Git clone 不包含它；未來如來源改版而無法重得同一 hash，應新增觀察版本。

本次螢幕畫面由瀏覽工具檢視，顯示在對話中；本包保存操作紀錄而沒有匯出原站截圖檔。不能把本包圖表當成原站 screenshot。自己的架構圖與線框則直接以 Markdown／Mermaid 保存。

## 實際核對到的範圍

- HTML 用 `<base>` 與 import map 指向本地 vendor；module 入口載入 10 個自訂 JavaScript 檔，核心 Three.js `REVISION` 為 `160`。
- JSON 是 14 個 islands，巢狀 buildings 合計 94，flows 為 20；另有 18 個 sources、3 個 ports、3 個 quotes、8 個 dayCycle 條目與 5 個 termTimeline 條目。
- 原站一般相機是透視相機，FOV 32°。`OrthographicCamera` 出現在 debug 區段；不能因為微縮外觀就判定全站用正交投影。
- 主流程以程序化幾何產生建物與人物。未從已查核的自訂 module 找到 GLTFLoader；不據此推斷製作團隊從未用過 Blender 或其他設計工具。
- 未查核全站其他路徑、伺服器程式、CMS、CI/CD、分析服務或作者身份。前端可靜態提供，不等於已證明整個網域沒有後端。
- JSON 的製作備註提到工具與工作檔案名稱；這是站方資料的自述，不能單獨證明製作流程或生成比例。

## 已鎖定與保留的決策

採納的是公開作品展示與設計方向。教學、工作、技能等內容先由既有公開資料映射；經歷、論文狀態、證照及客戶名稱不因加入島嶼而升級成新主張。文章詳細內容仍由網站 repo 擁有，研究島不直接讀取私人 repo。

首頁改為分層閱讀，群島作為 `/islands/`。沿用網站現有英文主頁與既有繁中路由慣例；本次文件先用繁中完整描述，不啟動全站翻譯。未來若要改成繁中主站，另列語言與路由遷移決策。

## 2026-10-22 紀錄與發布授權補充

使用者原文：

> Using FIRST PRINCIPLE, and please take notes on my day note in the `planning-everything-track` repo, and update the relevant docs, files, and contents for it.
> Please update all the commits separately on git, and push this branch to the remote main branch of the github repo. (If there were conflict among commits, i would like to keep both local commits and remote commits.)
> And build strong connection with all other relevant files, docs, and contents.

本次採納範圍：研究文件、相關索引與回鏈、Planning 日誌及網站追蹤頁分開提交並發布；保留既有本地與遠端歷史。網站實作與部署仍維持待啟動。
