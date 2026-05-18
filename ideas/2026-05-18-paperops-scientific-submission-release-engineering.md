# PaperOps: scientific submission release engineering

Canonical YAML: `ideas/structured/idea_000029_paperops_scientific_submission_release_engineering.yaml`

## 核心想法

`npm run ready` 在 manuscript / submission repo 裡不是「投稿」。

它是本機的總檢查 gate：repo 先照 `package.json` 裡定義好的腳本，檢查版本、語氣、LaTeX build、submission packet、portal mapping、deviation log、whitespace、git diff 等等。

真正投稿還是在 journal portal，例如 Elsevier / TFSC 的線上投稿系統。`portal:check` 只是檢查本機準備給 portal 用的文件，不會登入，也不會送出。

這個差別很重要：

- local readiness: repo 準備好了沒有
- portal readiness: 給投稿網站填的資料齊不齊
- external submission: 人類進到投稿網站，預覽後按 submit

PaperOps 的核心價值是把「人的記憶與注意力」轉成「可重跑、可審計、可交接的流程」。

## npm 是什麼

`npm` 是 Node.js 生態系的套件管理與指令執行工具。

可以先這樣比：

- Python 有 `pip`
- Ubuntu 有 `apt`
- JavaScript / Node.js 有 `npm`

它主要做三件事：

1. 安裝套件，例如 `npm install express`
2. 管理 repo 依賴，例如 `dependencies`
3. 執行 `package.json` 裡定義好的自動化指令，例如 `npm run test`

## package.json 是什麼

`package.json` 是 Node.js / npm 專案的核心設定檔。

可以把它想成：

> repo 的專案身分證 + 指令遙控器。

它通常記錄：

- 專案名稱
- 版本號
- 需要哪些套件
- 可以跑哪些指令
- 測試、建置、格式化、檢查流程

例如：

```json
{
  "scripts": {
    "latex:build": "tectonic manuscript/main.tex",
    "portal:check": "python scripts/check_portal_packet.py",
    "ready": "npm run latex:build && npm run portal:check"
  }
}
```

這樣執行：

```bash
npm run ready
```

意思是：照 repo 定義好的順序跑總檢查。

## Real-world instances

### Frontend website

React / Vite 專案常見：

```bash
npm install
npm run dev
```

`npm install` 安裝 React、Vite 等工具。`npm run dev` 開本機開發伺服器。

### Backend API

Node.js API server 常見：

```bash
npm install express
npm run start
```

`express` 是常見 API framework。`npm run start` 啟動 server。

### Test system

```bash
npm run test
```

背後可能是 Jest、Vitest 或其他 test runner。

### Format gate

```bash
npm run format
```

背後可能是 Prettier，目的是讓團隊格式一致。

### Manuscript submission repo

```bash
npm run ready
```

背後可以依序做：

- version check
- author voice check
- LaTeX build
- portal packet check
- title / abstract / keyword consistency
- declaration checklist
- artifact completeness
- whitespace / diff check

這裡 npm 不是在做研究。

它是流程指揮官。

## PaperOps 是什麼

PaperOps 可以理解成：

> 把 scientific publication 做成 release engineering。

一般學生常把投稿想成「寫完 paper，最後 upload」。

但真實世界常見失敗不是這麼單純：

- title page 放錯匿名資訊
- abstract 和 portal 欄位不一致
- cover letter 還是舊版
- supplementary file 漏上傳
- AI-use declaration 忘記填
- PDF 是舊 build
- coauthor 最後一天改過 metadata
- reviewer packet 和 manuscript 不一致

所以 `npm run ready` 的真正價值不是檢查本身，而是把這些容易漏掉的步驟系統化。

## 可發展模組

### 1. Submission State Machine

投稿流程可以明確分 state：

```text
draft
-> internal-review
-> pre-submission
-> portal-ready
-> submitted
-> revision
-> camera-ready
```

每個 state 有 required artifacts、禁止操作、validation gate。

### 2. Artifact Hash Lock

可以設計：

```bash
npm run artifact:freeze
```

它產生 manifest：

- manuscript PDF hash
- title page hash
- figure hash
- supplementary hash
- cover letter hash
- build command
- timestamp

這樣之後可以知道哪一組檔案才是真正 submit version。

### 3. Portal Dry Run

可以設計：

```bash
npm run portal:dryrun
```

檢查：

- title length
- abstract word count
- keyword count
- author metadata
- funding / COI / AI-use declaration
- file naming
- PDF size
- supplementary list

它只做本機 dry run，不登入投稿網站。

### 4. Reviewer Simulation Layer

可以設計：

```bash
npm run reviewer:redteam
```

檢查：

- overclaim
- unsupported causal language
- vague novelty
- missing baseline
- ethical ambiguity
- synthetic / public data boundary confusion
- reviewer workload risk

這不是預測 acceptance。

它是提早暴露 reviewer 可能質疑的 claim-risk。

## Safety boundary

PaperOps 可以做：

- local validation
- artifact manifest
- portal mapping
- reviewer-risk simulation
- deviation log
- checklist

PaperOps 不應該做：

- 自動登入 journal portal
- 自動送出投稿
- 保存投稿系統 credential
- 宣稱 reviewer simulation 能預測接受率

最後的 submit 必須是人類明確確認。

## 最小下一步

對一個 manuscript repo 做最小 prototype：

1. 建一份 `submission-state.yaml`
2. 建一份 `artifact-manifest.yaml`
3. 設計 `portal:dryrun` 本機 checklist
4. 設計 `reviewer:redteam` 的 claim-risk rubric
5. 讓 `npm run ready` 串起來，但不碰外部投稿系統

研究角度上，這可以變成：

> Scientific release engineering for AI-era manuscript submission.
