# YouTube Terminal Download Workflow on Ubuntu: yt-dlp, Troubleshooting, and Legal Boundary

Recorded: 2026-05-02

## Why this note exists

這份筆記保存一次 Ubuntu terminal 下載 YouTube 影片或音訊的技術討論，重點是 `yt-dlp` 的基本用法、故障排除、檔案大小判讀，以及研究用途的法律與倫理邊界。

This note is a technical and research-boundary record, not legal advice.

## Practical terminal workflow

建議工具是 `yt-dlp`，搭配 `ffmpeg` 進行影音合併或音訊轉檔。常用命令如下：

```bash
yt-dlp "URL"
yt-dlp -f "bestvideo+bestaudio/best" "URL"
yt-dlp -x --audio-format mp3 "URL"
yt-dlp -F "URL"
```

## What went wrong first

最初執行：

```bash
yt-dlp -f bestvideo+bestaudio "https://www.youtube.com/watch?v=TnG89ChN9LQ"
```

終端機出現幾類錯誤：

- YouTube API errors:
  - `Precondition check failed`
  - `HTTP Error 400: Bad Request`
- Signature issue:
  - `Signature extraction failed`
- Format issue:
  - `Only images are available for download`
  - `Requested format is not available`

## Root cause analysis

判讀上，當時安裝的 `yt-dlp` 很可能已經相對 YouTube 當前 player / API 行為過舊或損壞。YouTube 會頻繁調整 player、signature 與 API 流程，所以 `yt-dlp` 需要維持更新；舊版常見症狀包含簽章解析失敗、格式清單異常、只抓到圖片格式，或 400 類 API 錯誤。

## Fix: replace old yt-dlp and clear Bash cache

處理方式是移除舊版 `yt-dlp`，再從 GitHub release 安裝官方最新 binary：

```bash
sudo rm $(which yt-dlp)

sudo curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp \
  -o /usr/local/bin/yt-dlp

sudo chmod a+rx /usr/local/bin/yt-dlp
```

安裝後，shell 仍然嘗試呼叫：

```text
/usr/bin/yt-dlp
```

這是 Bash command-path cache 還留著舊路徑。清掉 cache 後重新確認：

```bash
hash -r
which yt-dlp
yt-dlp --version
```

確認結果：

```text
/usr/local/bin/yt-dlp
2026.03.17
```

`PATH` 內已有：

```text
/usr/local/bin
```

結論：安裝本身成功，實際卡住的是 Bash stale command cache；`hash -r` 讓 shell 重新查找正確位置。

## Successful test result

更新後執行：

```bash
yt-dlp -f "bestvideo+bestaudio/best" "https://www.youtube.com/watch?v=TnG89ChN9LQ"
```

下載成功開始：

```text
Downloading 1 format(s): 702+251
Destination: Mount Fuji Dusk Drive ... 8K 60fps HDR ...
0.7% of 34.63GiB
```

這表示 `yt-dlp` 已可正常解析與下載該影片的影音格式。

## Why the file became 34GB

`bestvideo+bestaudio` 代表分別選擇可用的最高畫質 video stream 與最高品質 audio stream，然後由 `ffmpeg` 合併。這次選到 8K 60fps HDR 影片流，因此檔案大小膨脹到約 `34.63GiB`。最高可用格式在技術上成功，實務上常常不適合日常保存、筆記輔助或研究佐證。

## Recommended safer default command

比較穩妥的預設命令是限制到 1080p 或以下：

```bash
yt-dlp -f "bv*[height<=1080]+ba/best" "URL"
```

這樣仍然會優先拿到合理畫質的 video + audio，但避免自動選到 4K、8K、HDR 或超大檔案。

## Optional JavaScript runtime fix

終端機也出現：

```text
WARNING: No supported JavaScript runtime could be found.
```

意思是 `yt-dlp` 沒找到可支援的 JavaScript runtime。部分 YouTube extraction path 可能需要 JS runtime 來處理 player 行為；這次下載仍然成功，這個警告當下未阻斷流程。可選改善：

```bash
sudo apt install nodejs -y
yt-dlp --js-runtime node "URL"
```

## Legal and ethical boundary

保守記錄：YouTube 官方機制將離線下載包在 Premium / app 控制流程內；未授權 stream ripping 常見於服務條款禁止範圍。`yt-dlp` 具備技術能力，但技術能力不等於法律或倫理授權。

使用 `yt-dlp` 下載 YouTube 內容通常會違反 YouTube Terms of Service，除非 YouTube 提供官方 download button，或使用者另外取得授權。是否構成法律問題取決於內容、司法管轄區、授權狀態與實際用途。未經許可下載受著作權保護的影片、音樂、電影或創作者內容，會產生版權風險；重新上傳、散布、商業使用或拿來建立資料集 / 訓練模型，風險更高。

較低風險情境包括：

- 下載自己上傳的影片。
- 下載 public-domain 或明確 Creative Commons 授權內容。
- 已取得權利人明確許可。
- 狹義研究或證據保存，只保留必要 metadata、截圖、短摘錄或可驗證連結。

YouTube Premium 的離線下載屬於官方訂閱功能，通常限於 YouTube 控制的 app 環境。這個設計維持平台規則、創作者收益、DRM / 控制機制與訂閱經濟。

## Research-use boundary

研究用途應以最小保留為原則。若研究目的只需要來源佐證，優先保存 URL、影片標題、頻道名稱、發布日期、存取日期、簡短截圖、短摘錄、hash / metadata 或官方連結。只有在重現性、證據保存、內容消失風險或授權條件明確需要完整影片時，才考慮保存 full video，並限制存取、避免外流。

對 scam / misinformation / platform governance 類研究，這個 workflow 應該視為 evidence-preservation backup，而非一般娛樂下載流程。若材料可能含有受控、敏感或第三方著作權內容，筆記與公開輸出應只放安全摘要、locator、方法邊界與必要引用。

## Final takeaway

這次問題的技術核心是舊版 `yt-dlp` 跟不上 YouTube player / API 變化，加上 Bash cache 繼續指向舊 binary。更新官方 binary、執行 `hash -r`、確認 `/usr/local/bin/yt-dlp` 與版本後，下載流程恢復。實務使用時，預設限制解析度到 1080p，並先確認授權、研究必要性與保存邊界。

## Commands reference

```bash
# Basic download
yt-dlp "URL"

# Highest available video + audio, can create very large files
yt-dlp -f "bestvideo+bestaudio/best" "URL"

# Safer 1080p-or-below default
yt-dlp -f "bv*[height<=1080]+ba/best" "URL"

# Audio extraction
yt-dlp -x --audio-format mp3 "URL"

# List available formats
yt-dlp -F "URL"

# Single-file best format, often lower complexity
yt-dlp -f best "URL"

# Explicit format pair example
yt-dlp -f 137+140 "URL"

# Replace old binary with latest official release
sudo rm $(which yt-dlp)
sudo curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp \
  -o /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp

# Clear Bash command cache and verify
hash -r
which yt-dlp
yt-dlp --version

# Optional JavaScript runtime
sudo apt install nodejs -y
yt-dlp --js-runtime node "URL"
```

## Decision record

- Use yt-dlp only for authorized, self-owned, public-domain, Creative Commons, or clearly justified research/evidence-preservation cases.
- Avoid downloading copyrighted creator content for entertainment when YouTube provides official Premium offline playback.
- Avoid redistribution, re-uploading, or dataset/model-training use without permission.
- Prefer metadata, citations, screenshots, short excerpts, or official links when the research goal does not require full video retention.
