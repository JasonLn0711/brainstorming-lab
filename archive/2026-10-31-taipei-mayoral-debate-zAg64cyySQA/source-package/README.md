# 台北市長辯論直播：音訊、逐字稿與查核

原始網址：https://www.youtube.com/live/zAg64cyySQA

## 先開啟這些檔案

| 用途 | 檔案 |
|---|---|
| 最高可取得音質的原始音訊 | [source_best.webm](source_best.webm) |
| 帶時間碼、疑句與查核旁註的閱讀稿 | [逐字稿_查核旁註草稿.md](逐字稿_查核旁註草稿.md) |
| 全長校訂文字草稿 | [best_transcript_corrected_draft.txt](best_transcript_corrected_draft.txt) |
| 對應原始音訊時間的字幕草稿 | [best_transcript_corrected_draft.srt](best_transcript_corrected_draft.srt) |
| 正式辯論逐段對照（含待核項目） | [逐段查核覆蓋.csv](逐段查核覆蓋.csv) |
| 最新查核結論與限制 | [最新查核結論表](最新查核結論表.md) |
| 查核主題與來源 | [查核索引](查核索引.md) |
| 尚未確認的字句與時間 | [待確認字句定位](待確認字句定位.md) |
| 疑句的 5 份聽校音訊與對照 | [待聽校片段](待聽校片段.md) |
| 會前背景聲、採訪與彩排閱讀範圍 | [會前內容閱讀紀錄](會前內容閱讀紀錄.md) |
| 每次規則替換 | [best_correction_log.csv](best_correction_log.csv) |
| 逐段文字與時間校訂依據 | [best_reviewed_overrides.json](best_reviewed_overrides.json) |
| 原始品質警示的目前處理狀態 | [best_quality_flag_status.json](best_quality_flag_status.json) |

## 辯論分析與 Facebook 草稿

以下為依逐字稿的文本分析，包含八組交叉詰問、兩個媒體題與相關申論、結論；不代表已完成全片聽校或心理實驗。

- [深入分析](辯論深入分析.md)：逐題回應、追問效果、攻防策略與都更比較。
- [完整問答證據附錄](辯論問答證據附錄.md)：原文字句、段號及原片連結。
- [八組問答分析表](辯論八組問答分析.csv)。
- [Facebook閱讀版](Facebook版_辯論分析.md)／[可直接貼上的純文字版](Facebook版_可直接貼上.txt)。尚未發佈。
- [分析交付檢查](辯論分析交付檢查.json)。

## 音訊與轉錄

`source_best.webm` 是 yt-dlp 使用 `bestaudio` 選出的 format 251，Opus、48 kHz、雙聲道。容器時長約 3 小時 30 分 11.5 秒；保留下載格式，未重新壓縮成 MP3。下載證據見 `download_best.log`、`source_best.info.json`、`formats_recheck.log`。完整音訊解碼已通過，見 `best_audio_validation.log` 與 `best_integrity_check.json`。

主要轉錄使用 `SoybeanMilk/faster-whisper-Breeze-ASR-25`，完整輸出 3,653 段；模型版本、執行設定與音訊雜湊記錄於 `best_transcription_receipt.json`。原始輸出為 `best_transcript.txt`、`best_transcript.srt`、`best_segments.jsonl`，校訂另存，沒有覆寫原始文字。正式辯論從原音約 01:29:29 開始；開頭包含會前連線、採訪、重播、測音與背景交談。

早先下載的 `source.m4a` 及不含 `best_` 前綴的逐字稿是另一份 AAC 版本，較主版本短約 10 秒，保留作為比對紀錄。兩者時間軸不能混用。

## 校訂與查核狀態

全部文字已閱讀，兩音訊版本的正式辯論差異亦已檢查；部分字句另以短音訊重辨識。這些步驟不等於人工全程聽校，也尚未完成所有主張的獨立核實。背景聲存在不連貫、循環重複與疑似辨識幻覺；目前稿件保持草稿狀態。

查核紀錄區分發言內容、可確認事實、未取得證據、政治評價及未來承諾。發言中的爭議數字保留，不因外部資料不同而偷偷改寫。例如兩段分別說 1.3 倍、1.4 倍，仍各自保留。新聞轉述只能佐證發言或事件報導，不能自動視為對所有主張的獨立驗證。

`correction_rules.json` 保存規則與來源；`best_reviewed_overrides.json` 保存逐段校訂與時間修正依據。`web_sources_*.json` 保存查詢回傳；各查核文件提供可點擊原始來源。`best_quality_review.json` 保留195段原始自動品質提示；現況另見 `best_quality_flag_status.json`，其中189段開場前警示待複核，6段正式內容的過長時間條件已修正。警示不是已確認錯誤清單，未觸發警示也不代表文字正確。

目前校訂計數及狀態見 [校訂回條](best_correction_receipt.json)；主版本欄位見 [檔案清單](task_manifest.json)。第1399–3653段的223組對照已連續覆蓋，這是分類與來源定位完成，並非所有主張已證實。會前第1–1398段已建立閱讀與分類定位；背景疑似幻覺、破句及尚無來源的主張仍待處理。
