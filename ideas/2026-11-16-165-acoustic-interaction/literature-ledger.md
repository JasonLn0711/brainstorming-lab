# 165 聲學主線：供稿文獻查核

查核日期：2026-11-16。回到[方法與範圍](README.md)／[原始供稿](source.md)。這是相關研究定位及 claim-to-source 對照，不是系統性回顧，也不是我們的實驗證據。`confirmed` 僅指本次頁面可支持的具體主張；部分讀取及待查細節明列。原文追蹤參數與連結仍完整保留於 source。

| ID／來源 | 本次可核對內容 | 適用範圍／待確認 |
| --- | --- | --- |
| L01 [Praat Jitter](https://praat.org/manual/Voice_2__Jitter.html) | 既有同日特徵筆記已核五類 jitter、相鄰週期定義與持續母音條件。 | 沿用 [063 查核](../2026-11-16-phone8k-feature-validity/README.md)；不將 jitter 等同整句語調或情緒真值。 |
| L02 Kappen 等，2022，[Scientific Reports](https://www.nature.com/articles/s41598-022-26375-9)，DOI 10.1038/s41598-022-26375-9；[PMC 備援](https://pmc.ncbi.nlm.nih.gov/articles/PMC9767914/) | `partially verified`：首次摘要可讀，支持 within-subject 社會評價壓力設計與自陳／生理驗證；後續全文讀取被 redirect／captcha 限制。 | 原文 F0／HNR 上升、shimmer 下降、jitter 無顯著改變四項方向保留來源主張，本輪未逐表重核。研究不能直接外推 165；其驗證來源也不移入我們的主判準。 |
| L03 Chang 等，2023，[PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0283635)，DOI 10.1371/journal.pone.0283635 | `confirmed`：演員產生聲調／情緒語音；F0、振幅、時長的影響依聲調及情緒不同，另有感知實驗。 | 臺灣華語情境提醒，並非真實 165 心理狀態標準；沒有觀測內容時保留詞彙聲調混雜。 |
| L04 Pommée／Morsomme，[作者機構 repository](https://orbi.uliege.be/handle/2268/298163?locale=en)，DOI 10.1016/j.jvoice.2022.08.027；[原 PubMed](https://pubmed.ncbi.nlm.nih.gov/36192289/) | `partially verified`：PubMed 本次只返回空殼，機構頁列研究、作者、DOI 與電話通道比較目的／方法。 | 各指標穩健性未逐表確認；不把此文當作所有電話／codec 不影響擾動的證據。 |
| L05 Zhu 等，2010，[VoIP perturbation study](https://pmc.ncbi.nlm.nih.gov/articles/PMC2945273/)，DOI 10.1159/000285807 | `confirmed`：G.729 模擬傳輸研究比較傳輸前後 jitter／shimmer，報告增加。 | 補上原文提及但未單列的第二篇文獻；特定語音及傳輸條件不代表所有 165 通道。 |
| L06 Bone／Lee／Narayanan，2014，[BIIC 作者研究頁](https://biic.ee.nthu.edu.tw/research.php?id=120)，DOI 10.1109/TAFFC.2014.2326393 | `confirmed`：三個知識導向特徵、speaker baseline 與無當前 affect label 的連續 arousal 路線；偏好中性 baseline，部分無標籤條件有初步證據。 | 無監督仍有假設；不能把 arbitrary 通話平均叫中性或聲學分數叫獨立情緒真值。 |
| L07 Levitan／Hirschberg，2011，[ISCA](https://www.isca-archive.org/interspeech_2011/levitan11_interspeech.html) | `confirmed`：多維 acoustic-prosodic entrainment、全局／逐回合、相對／絕對比較。 | 原文把自然電話雙語料研究接在此引用後；該額外主張應連下列 L08，避免用一個引用承擔兩項研究。 |
| L08 Gálvez 等，2020，[ACL Anthology](https://aclanthology.org/2020.sigdial-1.27/)，DOI 10.18653/v1/2020.sigdial-1.27 | `confirmed`：兩個 spontaneous telephone corpora 上比較 entrainment 指標與 positive social aspects 的預測。 | 本次補足的直接來源；外部 social outcome 不改成本研究主判準，也不證明員警聲音有因果效果。 |
| L09 Kruyt 等，2023，[JSLHR 方法比較](https://pubs.asha.org/doi/10.1044/2023_JSLHR-23-00094)，DOI 10.1044/2023_JSLHR-23-00094 | `confirmed`：同一 corpus 比較 12 方法，proximity／convergence／synchrony 與 surrogate／norming 差異會影響結果。 | 支持明定指標與 null；我們保留時間結構的配對方案是待定的設計提案，不宣稱與該文完全相同。 |
| L10 [statsmodels MixedLM 文件](https://www.statsmodels.org/dev/mixed_linear.html) | `confirmed`：支援依賴觀察、random effects／variance components。 | 官方 `dev` 文件不是本機版本；尚未固定實作、估計器或驗證巢狀／crossed 結構，不能以框架支持代替模型有效性。 |
| L11 [ECAPA 模型卡](https://huggingface.co/speechbrain/spkrec-ecapa-voxceleb)／[WavLM 作者頁](https://www.microsoft.com/en-us/research/publication/wavlm-large-scale-self-supervised-pre-training-for-full-stack-speech-processing/) | `confirmed`：ECAPA 的 speaker-verification 目標與 16 kHz 單聲道條件沿用 063；WavLM 作者說明 identity、paralinguistics、spoken content 的多面資訊。 | 音訊-only 不等於 content-free；本輪未取得或執行這些模型。 |
| L12 [JMIR 危機專線研究](https://www.jmir.org/2025/1/e67772/)，2025 | `confirmed`：方法描述 8 kHz 雙聲道來源、保留 caller channel，評估者依內容／風險標準建立分類與片段。 | 支持窄頻專線研究背景；它使用外部標準，不是「純聲學無外部判準已驗證心理狀態」的先例。不同專線對象不外推至 165。 |
| L13 [NIJ 2008 研究摘要](https://nij.ojp.gov/library/publications/voice-stress-analysis-only-15-percent-lies-about-drug-use-detected-field-test)，NCJ 221502 | `confirmed`：319 位 recent arrestees、以後續尿液檢驗比對；平均只找出約 15% 說謊者，屬敏感度，非總體準確率。 | 特定系統與藥物使用回答情境；不外推所有欺瞞研究、也不與我們的無情緒外部判準主線混同。 |
| L14 Harnsberger 等，2009，[PubMed 摘要](https://pubmed.ncbi.nlm.nih.gov/19432740/)，DOI 10.1111/j.1556-4029.2009.01026.x | `confirmed`：controlled stress／deception、double-blind；摘要列 hit 42–56%、false positive 40–65%。 | 範圍跨該文各條件／材料／examiners，不是一般聲音測謊準確率或我們的結果。 |
| L15 [Silero VAD](https://github.com/snakers4/silero-vad)／[openSMILE](https://audeering.github.io/opensmile-python/) | 沿用 [063 同日已核](../2026-11-16-phone8k-feature-validity/README.md)：8／16 kHz 與 eGeMAPSv02 88 維、版本／授權界線。 | 接受取樣率與有特徵輸出，均不等於心理構念有效；本輪沒有安裝或 runtime。 |

這些研究共同提供可量測的聲音與互動方法、混雜反例及推論界線。新穎性、相較完整文獻的剩餘缺口與期刊適配尚未系統查核；「研究可以成立」保留為供稿建議，不提升成資料／方法／論文已驗收。
