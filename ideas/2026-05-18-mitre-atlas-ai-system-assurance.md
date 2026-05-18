# MITRE ATLAS for AI system assurance

Canonical YAML: `ideas/structured/idea_000032_mitre_atlas_based_ai_system_assurance_for_triage_prototypes.yaml`

## 核心想法

MITRE ATLAS 可以讓 AI triage、ASR + LLM、RAG、agent workflow、醫療 AI prototype 從：

```text
可以跑的 demo
```

提升成：

```text
有 threat model、trust boundary、mitigation、human oversight、audit evidence 的 AI assurance prototype
```

這個差別很大。

一般學生 demo 可能只有：

- model accuracy
- UI
- pipeline
- demo video

但成熟的 AI system 會問：

- failure mode 是什麼？
- misuse case 是什麼？
- attack surface 在哪？
- 哪些資料可信？
- 哪些 output 一定要 human review？
- audit log 能不能重建決策？
- residual risk 是什麼？

這就是 AI system assurance 的入口。

## MITRE ATLAS 是什麼

MITRE ATLAS 是：

```text
Adversarial Threat Landscape for Artificial-Intelligence Systems
```

可以理解成：

> AI / ML 系統版的 MITRE ATT&CK。

MITRE ATT&CK 主要整理傳統資安攻擊的 tactics、techniques、mitigations。

MITRE ATLAS 則整理針對 AI-enabled systems 的：

- adversary tactics
- techniques
- mitigations
- case studies
- AI red-team observations
- realistic demonstrations

它不是一般教科書。

比較像：

```text
AI security threat encyclopedia + threat modeling reference + attack taxonomy
```

## 可以當學習參考書嗎

可以，但不要把它當「從零學 AI」的教材。

更適合的定位是：

```text
已經懂一點 AI system 後，用它學 AI security thinking。
```

學習順序可以是：

1. AI system architecture
2. LLM / RAG / agent workflow
3. threat modeling
4. MITRE ATLAS
5. OWASP LLM / GenAI risks
6. NIST AI RMF
7. GMLP / medical AI lifecycle boundary

MITRE ATLAS 最有價值的地方不是背名詞。

而是它會逼你問：

```text
這個 AI 系統到底會怎麼被攻擊、操控、誤用、偷走、污染或騙過？
```

## MITRE ATLAS、OWASP、NIST、GMLP 的角色

| Framework | 最適合回答的問題 |
| --- | --- |
| MITRE ATLAS | 攻擊者怎麼攻擊 AI 系統？tactics / techniques / mitigations 是什麼？ |
| OWASP LLM / GenAI | LLM app、RAG、agent、tool use 會有哪些 application-layer security risk？ |
| NIST AI RMF | 這個 AI system 怎麼做 broader risk management / trustworthy AI？ |
| FDA / GMLP | 如果靠近醫療 AI，data、intended use、human-AI team、monitoring、retraining risk 怎麼管？ |

所以這些不是互相取代。

比較像分工：

```text
ATLAS = adversarial AI threat map
OWASP = LLM / GenAI app security checklist
NIST AI RMF = AI risk governance umbrella
GMLP = medical AI lifecycle discipline
```

## 放到 AI triage 系統

假設你的系統是：

```text
Patient input
-> ASR
-> LLM
-> RAG
-> Decision Engine
-> Doctor Review
```

就可以這樣做 threat model。

| Component | Possible attack / failure | Control |
| --- | --- | --- |
| ASR | adversarial audio, replay, fake voice, noise manipulation | confidence threshold, transcript confirmation, human review |
| LLM | prompt injection, hallucination, instruction conflict | schema output, system boundary, no autonomous medical advice |
| RAG | retrieval poisoning, fake guideline insertion, citation manipulation | trusted source registry, provenance, evidence tier |
| Vital signs | sensor spoofing, stale signal, manual-entry manipulation | timestamp, plausibility check, source provenance |
| UI workflow | overreliance, misleading confidence, missing override | uncertainty display, review/override, reason capture |
| Agent tools | unauthorized action, tool hijack, data exfiltration | least privilege, approval gate, tool-call audit log |

這樣作品就不只是：

```text
我做了一個 AI app
```

而是：

```text
我設計了一個 threat-modeled AI workflow prototype。
```

## Auditability 是你的優勢

你本來就有 investigation / forensic thinking。

所以你會自然想到：

- input 是哪裡來的？
- transcript 是不是可靠？
- RAG 文件來源是什麼？
- 哪個 prompt version 產生這個結果？
- 哪個 signal 觸發 escalation？
- doctor 有沒有 override？
- override reason 是什麼？
- 如果出錯，能不能回頭重建？

這些就是 AI assurance 很重要的能力。

很多 AI 團隊只看 model output。

但真正醫療、金融、政府、critical infrastructure 系統會看：

```text
decision trace + evidence chain + responsibility boundary
```

## 最小 artifact

下一步不需要做大系統。

最小 artifact 是一份兩頁：

```text
AI Triage Assurance Packet
```

內容包含：

1. Component diagram
2. Trust boundary map
3. ATLAS / OWASP threat mapping
4. Mitigation matrix
5. Human-in-the-loop boundary
6. Audit evidence checklist
7. Residual risk statement

這會讓 prototype 立刻更像 research-grade / industry-grade work。

## 不要 overclaim

不能說：

```text
因為我用了 MITRE ATLAS，所以系統安全。
```

正確說法是：

```text
我使用 MITRE ATLAS / OWASP / NIST / GMLP 作為 threat modeling 和 assurance reference，
讓系統的 attack surface、mitigations、audit trail、human oversight、residual risk 可被檢查。
```

框架不會自動讓系統安全。

框架讓你用專業語言描述、檢查、改善風險。

## 一句話

MITRE ATLAS 可以當學習參考，但最好的學法不是背，而是拿自己的 AI triage / ASR + LLM / RAG / agent 系統去對照，做出 threat model、mitigation matrix 和 audit trail。

## Source Anchors

- MITRE ATLAS: `https://atlas.mitre.org/`
- MITRE ATLAS data: `https://github.com/mitre-atlas/atlas-data`
- MITRE + Microsoft ATLAS GenAI security release: `https://www.mitre.org/news-insights/news-release/mitre-and-microsoft-collaborate-address-generative-ai-security-risks`
- MITRE CTID 2026 ATLAS update: `https://ctid.mitre.org/blog/2026/05/06/secure-ai-v2-release/`
- OWASP Top 10 for LLM Applications: `https://owasp.org/www-project-top-10-for-large-language-model-applications/`
- NIST AI RMF 1.0: `https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10`
- FDA GMLP: `https://www.fda.gov/medical-devices/software-medical-device-samd/good-machine-learning-practice-medical-device-development-guiding-principles`
