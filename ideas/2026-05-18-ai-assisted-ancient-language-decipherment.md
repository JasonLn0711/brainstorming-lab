# AI-assisted ancient language decipherment and script archaeology

Canonical YAML: `ideas/structured/idea_000031_ai_assisted_ancient_language_decipherment_and_script_archaeology.yaml`

## 核心想法

現在確實已經有人用語言模型、深度學習、圖模型、embedding、computer vision 和 multimodal AI 來研究古語言、古文字、破損碑文與未破解文字系統。

但要先分清楚兩種問題：

```text
已知或部分已知語言的修復 / 轉寫 / 翻譯輔助
vs
人類還沒有破解的文字系統
```

前者 AI 已經很有用。

後者 AI 還不能直接「翻譯」，比較像在做：

```text
模式考古學
```

也就是從低資訊、破損、不完整、沒有 ground truth 的符號序列中，找出統計規律、結構、可能語法、上下文連結與不可能的假設。

## 有哪些 real-world examples

### 1. Pythia：古希臘碑文修復

Pythia 是 DeepMind 與學界合作的古文字修復模型。

它處理的是 ancient Greek inscriptions：

- 碑文破損
- 字元缺失
- 文句不完整

模型任務不是從零破解未知語言，而是：

```text
已知語言 + 殘缺文字 -> 可能補字候選
```

這很像 historian / epigraphist 的 copilot。

### 2. Ithaca：修復 + 地點 + 年代

Ithaca 延伸 Pythia。

它不只補缺字，還嘗試：

- restore missing text
- identify original location
- estimate date

這代表 AI 不只是文字模型，也開始把歷史 attribution 放進來。

### 3. Aeneas：古文本脈絡化

2025 年 Nature 的 Aeneas 更接近：

```text
contextualizing ancient texts
```

它不是只問「缺哪個字」，而是找 inscription 之間的 historical connection。

這很接近：

- retrieval
- evidence graph
- contextual reasoning
- digital humanities copilot

### 4. Fabricius：古埃及象形文字

Google Arts & Culture 的 Fabricius 使用 machine learning 幫助：

- collating
- cataloguing
- understanding hieroglyphs
- 學習與展示古埃及文化

這比較像 Egyptology workflow support，不是「AI 獨立破解古埃及文」。

古埃及文真正被破解，關鍵仍然是 Rosetta Stone。

## Rosetta Stone 的第一性原理

羅塞塔石碑重要，是因為它提供：

```text
同一段內容的多語對照
```

包含：

- Egyptian hieroglyphs
- Demotic
- Ancient Greek

對現代 NLP 來說，這非常像：

```text
parallel corpus
```

也就是跨語言 alignment 的關鍵資料。

所以 Champollion 當年做的事，可以用現代資工語言理解成：

- symbol alignment
- cross-lingual mapping
- bilingual evidence exploitation
- human-guided decipherment

這也是為什麼如果未來找到新的「雙語石碑」，AI 可能會大幅加速破解。

## 未破解文字為什麼難

像這些：

- Linear A
- Indus Script
- Rongorongo
- Proto-Elamite

困難不是「Google Translate 不夠強」。

而是人類根本可能不知道：

- 這是不是自然語言
- 符號怎麼切 token
- 閱讀方向是什麼
- 有沒有聲音對應
- 是音節、表意、行政記號，還是宗教符號
- 有沒有語法
- 有沒有雙語對照

LLM 的基本能力來自大量 pattern learning。

但未破解文字常常缺：

```text
大量語料
ground truth
parallel corpus
semantic grounding
tokenization rule
phonology
```

所以不能直接把符號丟進 LLM 然後期待它翻譯。

## AI 現在能做什麼

### 1. Image / inscription restoration

用 vision model 做：

- damaged inscription enhancement
- sign segmentation
- OCR-like transcription
- missing texture or ink detection

Herculaneum scrolls 就是代表案例之一。

Vesuvius Challenge 的研究者用 machine learning 從 charred papyrus 的 scan 裡找出文字訊號。

### 2. Known-language restoration

如果語言已知，例如 Greek、Latin、Akkadian，AI 可以做：

- missing character prediction
- damaged word restoration
- candidate ranking
- dating support
- location attribution
- translation assistance

這不是取代 scholar，而是讓 scholar 更快比較候選。

### 3. Undeciphered-script structure analysis

對 Indus Script 這類系統，AI 或統計模型可以分析：

- sign frequency
- n-gram
- entropy
- Markov transition
- sign position
- repetition pattern
- directionality hypothesis
- 是否比較像語言或非語言符號系統

但這仍然不是翻譯。

比較像：

```text
判斷這個符號系統有哪些結構限制。
```

### 4. Multimodal archaeology

古文字不是孤立 text。

它會出現在：

- 神殿
- 墓葬
- 商業封泥
- 行政文書
- 武器
- 陶片
- 王室碑文
- 宗教物件

同一個符號出現在不同 material / location / ritual context，意義可能不同。

所以未來模型應該把：

```text
text + image + artifact + site + date + material + iconography + bibliography
```

一起建成 evidence graph。

## 這跟你的研究方向為什麼接近

這個方向底層不是「古語言很浪漫」而已。

它跟你一直在做的事情很像：

```text
從不完整訊號中重建隱藏結構
```

對應如下：

| Ancient script AI | 你的系統方向 |
| --- | --- |
| broken inscription | noisy evidence |
| unknown sign system | unknown workflow pattern |
| missing bilingual anchor | missing ground truth |
| artifact context | metadata / provenance |
| expert uncertainty | human review |
| restoration candidates | ranked hypotheses |
| overclaim risk | hallucination / false confidence |

所以它可以接到：

- weak signal analysis
- metadata-only inference
- graph reasoning
- evidence reconstruction
- uncertainty-aware AI
- human-in-the-loop review

## 最小研究化切入

不要一開始說：

```text
我要用 LLM 破解 Indus Script
```

這太容易 overclaim。

更好的 first project 是：

```text
Known-language restoration vs undeciphered-script structure analysis
```

做一張對照表：

| Task | 有 ground truth 嗎 | AI 可以做什麼 | 不能宣稱什麼 |
| --- | --- | --- | --- |
| Greek inscription restoration | 部分有 | 補字、候選排序、地點/年代輔助 | AI 完全理解歷史 |
| Egyptian hieroglyph workflow | 有大量專家知識 | 轉寫、分類、學習工具、cataloguing | AI 獨立破解古埃及 |
| Akkadian translation | 有語料與 transliteration | 翻譯輔助 | 取代 Assyriologist |
| Indus Script | 幾乎沒有 ground truth | 結構分析、entropy、sign pattern | 翻譯成自然語言 |
| Linear A | 部分符號關係可比較 | cognate / sign relation hypothesis | 已破解 Minoan language |

## 最小可做 CLI fixture

做一個不用 notebook 的小 script：

```text
input:
  symbolic sequences

output:
  sign frequency
  bigram transition
  entropy estimate
  position pattern
  missing sign candidate ranking
```

然後明確標註：

```text
This is structure analysis, not translation.
```

## 一句話

AI 可以幫古語言研究，但最成熟的是已知語言的修復與輔助；對真正未破解文字，AI 目前更像 evidence reconstruction engine，而不是魔法翻譯器。

## Source Anchors

- DeepMind Ithaca: `https://deepmind.google/blog/predicting-the-past-with-ithaca/`
- Pythia paper: `https://arxiv.org/abs/1910.06262`
- Aeneas, Nature 2025: `https://www.nature.com/articles/s41586-025-09292-5`
- Google Fabricius: `https://blog.google/intl/en-mena/company-news/outreach-initiatives/fabricius-ai-machine-learning/`
- Akkadian NMT: `https://doi.org/10.1093/pnasnexus/pgad096`
- Indus Script Markov model: `https://pmc.ncbi.nlm.nih.gov/articles/PMC2721819/`
- Herculaneum scrolls: `https://www.nature.com/articles/d41586-024-00346-8`
- Neural decipherment: `https://arxiv.org/abs/1906.06718`
