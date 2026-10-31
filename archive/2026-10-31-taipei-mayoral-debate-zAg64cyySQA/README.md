# 台北市長辯論：逐字稿、查核與文本分析資料包

本資料包集中保存 YouTube `zAg64cyySQA` 的非音訊資料，供閱讀辯論分析、追溯逐字稿及檢查查核來源。原始影片：https://www.youtube.com/live/zAg64cyySQA

## 閱讀順序

1. [辯論深入分析](source-package/辯論深入分析.md)：先讀整體判斷與各題攻防。
2. [問答證據附錄](source-package/辯論問答證據附錄.md)與[八組問答表](source-package/辯論八組問答分析.csv)：追溯原句、段號與時間。
3. [查核旁註逐字稿](source-package/逐字稿_查核旁註草稿.md)與[最新查核結論](source-package/最新查核結論表.md)：對照發言和外部證據。
4. [待確認字句](source-package/待確認字句定位.md)：查看仍需聽校的內容。
5. [Facebook 閱讀版](source-package/Facebook版_辯論分析.md)／[貼上用純文字](source-package/Facebook版_可直接貼上.txt)：保留分享草稿，尚未發佈。

## 目錄與保存方式

| 入口 | 用途 |
|---|---|
| [分類目錄](CATALOG.md) | 六類導航，涵蓋全部複製檔案 |
| [原資料包說明](source-package/README.md) | 保存原始方法、版本與查核脈絡 |
| [檔案清冊](inventory.csv) | 每檔大小、SHA-256、分類與複製／排除原因 |
| [排除紀錄](AUDIO-EXCLUSIONS.md) | 音檔和 Python 快取的原位置與依賴說明 |
| [本次複製驗證](copy-validation.json) | 原檔完整性與新增導航檢查 |

`source-package/` 保存原有檔名、目錄和內容。新增的分類目錄讓讀者按目的查找，原有文件的相互引用仍可沿用。原始逐字稿、校訂稿、來源回傳、分析、腳本與執行回條各自保留；歷史回條中的絕對路徑及數量描述對應原執行環境。

## 所有權與範圍

本次優先保護來源證據與後續查找所需的注意力。`brainstorming-lab/archive/` 是這份探索性文本分析資料的保存位置；這次整理未建立新的 Idea OS 研究計畫。Planning 維持優先序、容量與狀態管理，本次沒有新增排程或學習承諾。

資料來自 `/home/jnclaw/Downloads/YouTube_zAg64cyySQA`；Downloads 原檔保留。本次僅完成非音訊複製、分類導航與位元組一致性驗證。原分析仍有全片人工聽校、部分字句與主張核實待完成，分享稿維持草稿狀態。

## 後續使用

閱讀與查核可直接從本頁開始。若要重跑音訊處理，先依排除紀錄接回原音檔，檢查腳本中的原環境路徑、模型及依賴。下一個內容驗證步驟是複核待確認字句；本次未啟動新實驗或重新辨識。

## Planning connections

- [2026-10-31 day note](../../../planning-everything-track/weeks/2026-W44/days/2026-10-31.md#debate-archive): contribution, capacity and review gate.
- [Brainstorming project locator](../../../planning-everything-track/data/projects/2026-04-brainstorming-lab.md#debate-archive): ownership and archive status.
- [Planning bridge](../../../planning-everything-track/docs/15-brainstorming-repo-bridge.md#debate-archive): navigation across repositories.

The copy receipt records the earlier local snapshot (`published: false` at capture time). Git publication is tracked separately by commit history and the Planning handoff.
