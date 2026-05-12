# AI Value Capture And Agent Security Career Positioning

Related idea: `idea_000018`

Recorded: 2026-05-09

## Context

這份筆記整理一段關於台股、美股、AI 基礎建設、digital labor、下一階段 AI 應用層價值捕獲，以及個人職涯定位的討論。

討論的出發點是：台股過去幾年大幅受惠於 AI 基礎建設供應鏈，但這不代表美股或軟體平台的 AI 故事結束。更合理的讀法是，AI 價值捕獲正在分階段發生：

```text
基礎建設瓶頸 -> cloud / model platform -> workflow / application layer -> digital labor steady state
```

這份筆記不是投資建議，也不是交易計畫。它是一份研究與職涯定位備忘錄，用來判斷接下來應該把個人能力放在哪個交叉點。

## First Principle

經濟價值會先流向當下最稀缺、最確定的瓶頸；等基礎設施逐漸成形後，長期價值會轉向能控制工作流程、使用者入口、資料、權限、分發與抽成機制的人。

一句話版本：

> 台股漲的是 AI 的建設權；下一階段全球軟體與平台公司要爭的是 AI 的抽稅權。

這裡的「抽稅權」不是法律上的稅，而是平台、workflow、distribution、data、API、治理與權限控制形成的可持續收費能力。

## Market Thesis

台股先漲，主要是因為 AI 仍在基礎建設高投入階段。市場會先重估最確定的 capex 受益者：

- 晶片。
- 先進製程。
- 先進封裝。
- AI server。
- 散熱。
- 電源。
- 網通。
- data center。

但科技革命的後段價值通常不只停留在基建。網際網路早期也是網路設備、光纖與基建先被重估；後來更大的 durable value capture 流向 search、e-commerce、social network、cloud platform 與 enterprise SaaS。

AI 也可能類似：

| 階段 | 時間判斷 | 價值捕獲位置 |
| --- | --- | --- |
| Stage 1 | 2023-2026 and continuing | chips, foundry, packaging, server, cooling, power, data center |
| Stage 2 | 2025-2027 | cloud, frontier model, API, model platform, developer platform |
| Stage 3 | 2026H2-2028H1 | coding agent, enterprise workflow agent, AI SaaS, digital labor workflow |
| Stage 4 | 2028-2030 and beyond | digital labor steady state, agent marketplace, workflow tax, governance tax |

這個 handoff 不是「基礎建設停了才輪到應用」。比較可能的情境是：

```text
基礎建設繼續燒錢，應用層與平台層同時開始出現財務證據。
```

## Value Pool Boundary

把全球白領薪資池當成 AI 可影響的 gross economic value 是有用的，但不能直接把它當成企業營收或股東利潤。

例如：

```text
45T white-collar labor pool * 60% affected = 27T gross affected labor-cost pool
```

這個數字不等於 27T 的企業利潤。它會被拆成：

- 消費者剩餘。
- 企業成本下降。
- 競爭造成的降價。
- 平台 / 應用 / 模型 / 雲端收入。
- 政府稅收與再分配。
- 新工作與新需求。
- 轉型期失業與政治壓力。

更好的投資問題是：

```text
誰能在巨大 value pool 中穩定 capture 1-2% 的稅後利潤？
```

即使只是很小的 capture rate，只要 value pool 足夠大，也可能對市值造成巨大影響。真正要判斷的是：

- 誰有 workflow control？
- 誰有 customer distribution？
- 誰有資料與權限？
- 誰能嵌進企業流程？
- 誰能提供安全、稽核、治理、合規？

## Timing Judgment

我的 working judgment：

> 下一階段已經開始，但真正被財報與股價大規模重估的時間，更可能落在 2026H2 到 2028H1。

理由：

- Coding agents 已經是最早出現明確 ROI 的 AI application layer。
- Enterprise agents 已進入 pilot-to-scale 的過渡期。
- 很多公司有 AI 策略與工具試用，但 enterprise-wide EBIT impact 還沒有全面反映。
- 企業真正卡住的不是模型 demo，而是資料整合、權限控管、稽核、責任歸屬、流程重設與安全治理。

可觀察訊號：

- AI software engineering agents 變成正式 budget line。
- SaaS 公司開始揭露 agent attach rate、retention、margin effect。
- Enterprise workflow agents 不只 demo，而有可重複 ROI case。
- Agent security / AI governance role 變成 AI deployment 的標準配套。
- 工具型 agent 的安全事件讓企業更重視 prompt injection、tool abuse、data exfiltration 與 audit trail。

## Service Map

下一階段最重要的服務不是最會聊天的 AI，而是能替代、壓縮或增強一個工作單位的 AI。

| 服務類型 | 為什麼可能先爆發 | 代表方向 |
| --- | --- | --- |
| AI software engineer / coding agent | repo、test、PR、bug、review 有明確閉環 | OpenAI Codex, GitHub Copilot, Claude Code, Cursor, Sourcegraph |
| Enterprise workflow agent | 可直接接 CRM、ERP、ITSM、HR、finance、support | Microsoft Copilot Studio, Salesforce Agentforce, ServiceNow, SAP, Oracle, Workday |
| Customer support / sales ops agent | 高頻、重複、資料密集、ROI 可量化 | Salesforce, Intercom, Sierra, Decagon, Zendesk |
| AI cyber / SOC agent | 資安人力不足，alert triage 與報告生成需求強 | Microsoft Security, CrowdStrike, Palo Alto, Wiz, Cloudflare, Mandiant, Trend Micro |
| Legal / compliance / finance analyst | 文件密集、高薪、標準化與 audit 需求高 | Harvey, Thomson Reuters, Bloomberg, Palantir, Big 4 |
| Knowledge worker platform | 企業知識散在 Slack、Drive、Email、Jira、CRM | Glean, Notion, Atlassian, Microsoft, Google, Databricks, Snowflake |
| AI agent security / governance | agent 能做事後，安全與權限問題變成剛需 | OWASP, Microsoft AI Red Team, Google Cloud, Wiz, Palo Alto, Cloudflare |

## Core Technical Capabilities

這不是單純 prompt engineering。

真正稀缺的是能把 AI agent 放進真實流程的人。

### Engineering Base

- Python。
- TypeScript / JavaScript。
- FastAPI 或 Node.js。
- SQL / PostgreSQL。
- Docker。
- Linux。
- GitHub Actions。
- 至少一個 cloud：AWS / Azure / GCP。
- REST API / webhook / OAuth / IAM。

### Agent Stack

- OpenAI / Anthropic / Google model API。
- RAG：chunking、embedding、reranking、metadata filtering。
- vector DB：pgvector、Pinecone、Weaviate、Milvus 任一。
- agent orchestration：LangGraph、Semantic Kernel、LlamaIndex workflow 任一。
- MCP server / client。
- tool calling。
- Playwright / browser automation。
- evals：task success、hallucination、prompt injection、unsafe action。
- tracing / observability：LangSmith、OpenTelemetry、Phoenix / Arize。

### AI Security

這是個人差異化的核心。

- OWASP LLM Top 10。
- OWASP agentic AI security。
- prompt injection。
- indirect prompt injection。
- tool abuse。
- excessive agency。
- least privilege。
- sandboxing。
- secrets management。
- audit logging。
- data exfiltration defense。
- SIEM / EDR 基礎。
- MITRE ATT&CK。
- Sigma / YARA 基礎。
- phishing / malware / fraud analysis workflow。

### ML / Data

- PyTorch。
- Transformers。
- embedding models。
- fine-tuning / LoRA 基礎。
- classification。
- anomaly detection。
- graph analysis。
- data pipeline。
- model evaluation。
- experiment tracking。

### Infra / Edge Bonus

如果要切台灣 AI infra / edge AI：

- CUDA 基礎。
- vLLM。
- TensorRT-LLM。
- Triton Inference Server。
- quantization。
- batching。
- latency / throughput optimization。
- ONNX Runtime。
- TensorRT。
- OpenVINO。

## Geography And Company Map

### United States

核心優勢：frontier models、cloud、SaaS、capital markets、distribution。

公司方向：

- OpenAI、Anthropic、Google DeepMind、Meta、Microsoft。
- AWS、Google Cloud、Azure、Oracle Cloud、CoreWeave、NVIDIA。
- Salesforce、ServiceNow、Adobe、Atlassian、Workday、Oracle、SAP。
- Cursor、Glean、Harvey、Sierra、Decagon、Perplexity。
- CrowdStrike、Palo Alto Networks、Wiz、Cloudflare、Snyk、Google Mandiant。

### Taiwan

核心優勢：AI infrastructure supply chain。限制是應用平台抽稅權相對弱，但 AI security、edge AI、fraud intelligence、enterprise AI integration 仍有切入點。

公司方向：

- TSMC、ASE、GlobalWafers。
- Foxconn、Quanta / QCT、Wiwynn、Wistron、Inventec、Pegatron。
- Delta、Lite-On、Advantech。
- MediaTek、Realtek、Novatek。
- Trend Micro、TXOne、TeamT5、CyCraft、Gogolook、Appier、iKala。
- Google Taiwan、Microsoft Taiwan、NVIDIA Taiwan。

### Singapore

核心優勢：APAC enterprise AI、finance AI、fraud AI、regional HQ。

公司方向：

- Google、Microsoft、AWS。
- TikTok / ByteDance。
- Grab、Sea。
- Databricks、Snowflake、Palantir。
- CrowdStrike、Palo Alto、Cloudflare、Wiz。
- 金融機構、GovTech、regtech / fraudtech。

### Australia

核心優勢：enterprise AI、AI security、fraud detection、regulated-industry workflow、product engineering。

公司方向：

- Atlassian、Canva、SafetyCulture。
- Google、Microsoft、AWS。
- Databricks、Snowflake。
- CrowdStrike、Palo Alto、Cloudflare、Wiz、CyberCX。
- CBA、NAB、ANZ、Westpac fraud AI / cyber analytics teams。

### Japan

核心優勢：industrial AI、robotics、enterprise transformation。語言門檻較高。

公司方向：

- Preferred Networks。
- Sony。
- Toyota / Woven。
- NTT Data。
- Fujitsu、NEC。
- SoftBank、Rakuten、Mercari。

## Personal Positioning

不要把自己定位成：

```text
剛轉職 AI 工程師
```

更好的定位：

```text
AI Security / Agentic AI Engineer with cybercrime investigation background
```

更尖銳的版本：

```text
懂真實犯罪、資安事件、調查流程的 AI agent builder / evaluator / red-teamer
```

這個定位有三個優勢：

1. 真實風險場景：詐欺、釣魚、證據鏈、調查流程、資安事件。
2. 技術可補：ML / CV / cyber 背景可延伸到 applied AI。
3. 時代順風：agent security 會變成企業導入 AI agents 的必要配套。

## Target Job Titles

優先找：

- AI Security Engineer。
- LLM Security Engineer。
- AI Red Team Engineer。
- Agentic AI Engineer。
- Applied AI Engineer。
- Machine Learning Engineer, Security。
- Threat Intelligence Engineer, AI。
- Fraud Detection / Trust & Safety ML Engineer。
- GenAI Solutions Architect。
- AI Governance / AI Risk Engineer。
- Cybersecurity Data Scientist。
- Security Automation Engineer。

## Portfolio Projects

### Project 1 — Agentic SOC Copilot

功能：

- 吃 phishing email、log、alert、URL、附件 metadata。
- 自動做 triage。
- 查 MITRE ATT&CK。
- 產生 incident report。
- 給 confidence score。
- 高風險 action 必須 human approval。
- 所有 tool calls 有 audit log。

面試訊號：

> 我懂 agent 如何接工具、接資料、接資安流程，也知道怎麼避免 agent 亂做事。

### Project 2 — MCP / Agent Security Lab

做一個故意有漏洞的 agent 系統，再做防禦版。

測試項目：

- prompt injection。
- indirect prompt injection from document / email。
- tool over-permission。
- data exfiltration。
- memory poisoning。
- unsafe autonomous action。
- denial of wallet。

輸出：

- GitHub repo。
- threat model。
- attack / defense demo。
- eval report。
- mitigation checklist。

### Project 3 — Cybercrime Intelligence Graph

把公開 OSINT、詐欺網址、錢包地址、domain、email、社群帳號、IP、惡意樣本 metadata 做成 graph。

功能：

- entity extraction。
- relationship graph。
- risk scoring。
- case timeline。
- natural language query。
- report generation。

面試訊號：

> 把警政 / 科技犯罪背景轉成科技公司能看懂的產品與工程能力。

## 12-Month Route

### 2026 Q2

目標：建立定位與作品集起點。

- 履歷主標改成 AI Security / Agentic AI Engineer。
- 啟動 Agentic SOC Copilot。
- 或先做 MCP / Agent Security Lab，因為它更直接打 AI security 職缺。

### 2026 Q3

目標：投台灣與 remote-friendly 角色。

優先：

- Trend Micro。
- TXOne。
- TeamT5。
- CyCraft。
- Gogolook。
- Appier。
- NVIDIA Taiwan。
- Google Taiwan。
- Microsoft Taiwan。
- MediaTek。
- Quanta / QCT。
- Foxconn。
- 金融機構 fraud / cyber AI team。

### 2026 Q4

目標：投新加坡 / 澳洲 / 國際遠端。

優先：

- Atlassian。
- Canva。
- CrowdStrike。
- Palo Alto。
- Cloudflare。
- Wiz。
- CyberCX。
- AWS / Microsoft / Google cloud AI security。
- 金融機構 fraud AI / cyber analytics。

### 2027

目標：往平台公司、cybersecurity AI vendor、cloud AI security、enterprise agent platform 升級。

第一份 AI / cyber / agent title 是跳板，不是終點。

## Claim Boundaries

- 這份筆記不是投資建議。
- 市場數據、股價、報酬、capex forecast 會快速變動；正式使用前必須重新查證。
- 公司名單是 career map，不是保證有職缺或一定適合。
- 「Digital AGI 取代 60% 白領工作」應視為 scenario assumption，不是已驗證結論。
- 作品集應以安全、防禦、治理、可稽核 workflow 為主，不做攻擊性操作指南。

## Source Leads

已在 2026-05-09 做過一次來源檢查，但正式寫作或投資判斷前仍要刷新：

- Taiwan Index: <https://taiwanindex.com.tw/en/indexes/t00>
- Fiera Capital, Taiwan Supply Chain and AI: <https://www.fieracapital.com/wp-content/uploads/insights/3181/whitepaper-taiwan-supply-chain-and-ai-eng.pdf>
- OpenAI Codex: <https://openai.com/index/introducing-codex/>
- Microsoft Work Trend Index 2025: <https://www.microsoft.com/en-us/worklab/work-trend-index/2025-the-year-the-frontier-firm-is-born>
- McKinsey State of AI 2025: <https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai>
- Salesforce Agentforce: <https://www.salesforce.com/ap/agentforce/>
- OWASP GenAI Security Project: <https://owasp.org/www-project-top-10-for-large-language-model-applications/>

## Next Test

最小下一步不是再列更多公司。

最小下一步是：

```text
選一個 4-6 週 portfolio sprint，做出可以投 AI Security / Agentic AI Engineer 的 artifact。
```

建議優先順序：

1. MCP / Agent Security Lab。
2. Agentic SOC Copilot。
3. Cybercrime Intelligence Graph。

原因：第一個最能直接展示 AI agent security；第二個最貼近資安工作流程；第三個最能把警政與科技犯罪背景轉成可見產品能力。

