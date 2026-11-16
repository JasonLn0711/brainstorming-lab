# 2026-11-16｜8 kHz 電話錄音完整特徵工程：完整供稿

來源：使用者本輪提供的完整引號內容。逐字來源與本輪判讀分開；文中 Toolkit、下載、Smoke Test 與數字保留原始主張，實際取得／查核狀態見 README。原文圖片以原連結保存，未取得圖片或附件。

<!-- source:start -->
一段類比電話的錄音，8kHz的通話錄音檔，請問可以給我們什麼樣的量化特徵呢？例如： jitt、voice embedding、利用 voice-supported embedding model 的特徵、音頻？是否可以給我完整越多特徵越好的特徵呢？以及我們可以利用什麼樣的開源套件或免費分析方式，得到所有特徵呢？
# 8 kHz 電話錄音的完整特徵工程：從聲學、Jitter、Voice Embedding 到語音行為分析

核心結論：一段 8 kHz 的電話錄音，即使頻寬有限，仍然可以萃取數百至數千個量化特徵。 這些特徵不僅能描述「聲音長什麼樣」，也能分析說話者的聲音特性、說話方式、語音內容、通話互動，以及錄音品質。

但需要區分三個概念：

1. 可量測的訊號特徵（Measured Features）：例如 F0、MFCC、RMS、頻譜、停頓時間。
2. 模型學習的表徵（Learned Representations）：例如 ECAPA-TDNN Speaker Embedding、WavLM Embedding。
3. 模型推論的屬性（Inferred Attributes）：例如情緒、緊張程度、語言、說話者是否相同。

第三類不是直接觀察到的客觀事實，而是模型根據錄音所作的估計。

對於 8 kHz 類比電話錄音，我建議建立一套分層、可追溯、能量化驗證的 Speech Feature Extraction Pipeline，而不是單純把所有套件輸出的數字拼接成一個巨大向量。

## 一、先建立完整的特徵分類地圖

8 kHz Telephone Recording

原始 Waveform：每秒 8,000 個取樣點

01

訊號與音質

RMS、SNR、頻譜、失真

02

發聲與韻律

F0、Jitter、Shimmer、HNR

03

聲道與音色

Formant、MFCC、LPC

04

深度語音表徵

ECAPA、WavLM、CLAP

05

語音內容

ASR、語速、語言、詞彙

06

說話行為

VAD、停頓、重疊、輪替

07

情緒與聲學狀態

Arousal、Valence、Disfluency

08

電話通道特徵

Codec、Clipping、Noise、DTMF

時間序列特徵 + 片段統計特徵 + 全通話特徵

依說話者、時間、通話片段建立可供研究與機器學習使用的資料

以下逐類解釋每一種特徵的物理意義、可得到的數值、分析工具及在電話錄音上的適用性。

## 二、8 kHz 電話錄音的物理限制

首先，8 kHz 指的是每秒記錄 8,000 個取樣值（Sampling Rate），不是聲音最高頻率為 8,000 Hz。

依照 Nyquist 原理，8 kHz 取樣率所能表示的最高頻率，理論上是 4,000 Hz。

傳統 PSTN 窄頻通話通常針對約 300–3,400 Hz 的語音頻帶設計。不過，實際錄音可能經過交換設備、VoIP、壓縮、增益控制、降噪或重取樣，因此必須檢查真正保留的頻率範圍。

| 特徵                  | 8 kHz 適用性 | 主要限制               |
| ------------------- | --------- | ------------------ |
| F0 / Pitch          | 高         | 噪聲、重疊發話、倍頻錯誤       |
| MFCC / Mel Features | 高         | 必須使用適合 8 kHz 的頻帶設定 |
| 語速、停頓、VAD           | 高         | 依賴語音分段與轉錄品質        |
| Speaker Embedding   | 中高        | 電話通道與訓練資料的差異       |
| F1、F2 Formants      | 中         | 需要適當的母音片段          |
| F3 Formant          | 中至低       | 可能接近電話頻帶上限         |
| F4 及高頻聲學特徵          | 低         | 可能超出實際可觀測頻帶        |
| Jitter、Shimmer      | 有條件       | 對噪聲、壓縮、非穩定發聲敏感     |
| Emotion Recognition | 有條件       | 需要適合語言、場景的驗證       |
| 4 kHz 以上原始頻譜        | 不可恢復      | 原始訊號未保留該資訊         |

重要：將錄音從 8 kHz Resample 成 16 kHz，只是改變取樣表示，不會恢復已經遺失的高頻資訊。 不過，這仍是使用要求 16 kHz 輸入的預訓練模型時經常需要做的正確前處理。

## 三、可以從錄音萃取哪些特徵？

### 3.1 基礎波形、振幅、錄音品質

這一組特徵不需要 ASR，也不需要大型神經網路。通常直接用 NumPy、SciPy、librosa 就可以計算。

| 特徵                         | 量化意義             | 單位／形式      |
| -------------------------- | ---------------- | ---------- |
| Duration                   | 錄音長度             | 秒          |
| Sample Count               | 總取樣點數            | 整數         |
| Sample Rate                | 取樣率              | Hz         |
| Channel Count              | 聲道數量             | 整數         |
| Bit Depth / Subtype        | PCM 精度或編碼格式      | 類別         |
| Peak Amplitude             | 最大瞬間振幅           | 正規化振幅      |
| RMS Amplitude              | 訊號有效振幅           | 線性值        |
| RMS dBFS                   | 相對數位滿刻度的能量       | dBFS       |
| Mean Amplitude / DC Offset | 波形是否偏離零中心        | 線性值        |
| Crest Factor               | Peak 與 RMS 的比值   | dB         |
| Dynamic Range              | 聲音強弱變化範圍         | dB         |
| Clipping Ratio             | 疑似振幅截斷比例         | %          |
| Near-Silence Ratio         | 低於指定門檻的時間比例      | %          |
| Zero-Crossing Rate（ZCR）    | 波形每秒或每框跨越零點的頻繁程度 | rate       |
| Short-Time Energy          | 每一短時間框的能量        | 序列         |
| Energy Entropy             | 能量分布的不均勻程度       | 數值         |
| Modulation Spectrum        | 音量包絡隨時間變化的頻率組成   | 向量         |
| Envelope Variance          | 振幅包絡變異程度         | 數值         |
| Spectral SNR Estimate      | 頻域訊噪比估計          | dB         |
| Noise Floor                | 背景噪聲底線           | dBFS       |
| Hum / Tone Energy          | 特定持續性雜音的能量       | dB 或 ratio |

例如，RMS 可以描述「這段訊號有多強」：

\[ RMS=\sqrt{\frac{1}{N}\sum\_{n=1}^{N}x[n]^2} \]

但要注意：錄音的 RMS 大，不代表說話者真的比較大聲或比較激動。 電話交換機或錄音設備可能使用 Automatic Gain Control（AGC），把小聲者的音量自動放大。

因此應把 `rms_dbfs` 稱作「錄音訊號位準」，而不是直接當成「真實發聲音量」。

### 3.2 基頻、聲調及韻律（Pitch & Prosody）

人類說話時，聲帶會產生週期性的振動。這個主要週期的頻率稱為基頻（Fundamental Frequency，F0）。

例如，當 F0 = 150 Hz，代表估計的聲帶振動頻率約為每秒 150 次。

可以得到的特徵：

| 特徵                       | 意義                |
| ------------------------ | ----------------- |
| F0 Mean / Median         | 平均／中位基頻           |
| F0 Min / Max             | 最低／最高有效基頻         |
| F0 Standard Deviation    | 基頻變異              |
| F0 P05 / P95             | 排除極端值後的基頻範圍       |
| F0 Range                 | 語調活動範圍            |
| F0 IQR                   | 基頻四分位距            |
| F0 Slope                 | 基頻上升或下降趨勢         |
| F0 Delta                 | 相鄰時間框的基頻變化        |
| F0 Acceleration          | 基頻變化速度的變化         |
| F0 Contour               | 完整的基頻時間序列         |
| Voiced Frame Ratio       | 具有週期性發聲的時間比例      |
| Voicing Probability      | 一個時間框被判定為有聲的機率或信心 |
| Pitch Jump Rate          | 突然大幅改變基頻的頻率       |
| Semitone Range           | 以音程尺度表達的基頻範圍      |
| Intonation Contour       | 句子或語段的語調輪廓        |
| Pitch Reset              | 語段邊界處的基頻重新起始      |
| Energy–Pitch Correlation | 基頻與訊號能量的相關性       |

對臺灣繁體中文、國語及臺語語音尤其值得注意的是：F0 不只是情緒線索，也是語言本身的聲調資訊。

舉例而言，某個人基頻上升，可能是疑問語調，也可能只是說出具有上升聲調的音節。

因此，若研究情緒或說話者特性，理想上需要控制音節、聲調、語音內容與說話者個人的基頻範圍。

推薦：Praat／Parselmouth、librosa.pyin、openSMILE、torchcrepe。優先保留 F0 Contour，不只保留整段平均值。

### 3.3 Jitter：聲帶週期有多不穩定？

Jitter 指的是連續發聲週期之間，週期長度的不規則變化。

想像兩個人都以大約 150 Hz 發聲。第一個人的每個振動週期非常一致；第二個人的振動週期則稍微忽長忽短。第二個人的 Jitter 可能比較高。

其常見定義為：

\[ Jitter\_{local}= \frac{\frac{1}{N-1}\sum\_{i=1}^{N-1}|T_i-T\_{i+1}|} {\frac{1}{N}\sum\_{i=1}^{N}T_i} \times100\% \]

其中 \(T_i\) 是第 \(i\) 個聲帶振動週期的長度。

概念示意：週期穩定與不穩定

除了 Local Jitter，也可以萃取：

| Jitter 類型       | 描述                                    |
| --------------- | ------------------------------------- |
| Jitter Local    | 相鄰週期差異的相對平均值                          |
| Jitter Absolute | 相鄰週期的絕對時間差異                           |
| Jitter RAP      | 三個相鄰週期的 Relative Average Perturbation |
| Jitter PPQ5     | 五個週期的 Perturbation Quotient           |
| Jitter DDP      | 連續週期差異的二階擾動，數值上為 RAP 的三倍              |

Praat 官方文件提供上述定義及測量方式。

[image](https://www.google.com/s2/favicons?domain=https://praat.org\&sz=32)

Praat+1



### 3.4 Shimmer：聲音振幅有多不穩定？

Jitter 衡量的是「每次振動的時間是否規律」，Shimmer 衡量的是「每次振動的幅度是否規律」。

可以萃取：

| Shimmer 類型       | 描述          |
| ---------------- | ----------- |
| Shimmer Local    | 相鄰週期振幅的相對差異 |
| Shimmer Local dB | 振幅擾動的分貝表示   |
| Shimmer APQ3     | 三週期振幅擾動     |
| Shimmer APQ5     | 五週期振幅擾動     |
| Shimmer APQ11    | 十一週期振幅擾動    |
| Shimmer DDA      | 振幅擾動差異的量度   |

這六項也有 Praat 的標準化定義。

[image](https://www.google.com/s2/favicons?domain=https://praat.org\&sz=32)

Praat+1



這裡有一個研究上非常重要的限制：Jitter 與 Shimmer 不應直接拿整通電話當成可靠的生理指標。

原因是 Praat 官方一般建議在較長的持續母音（Sustained Vowels）上量測，而不是任意的自然對話。

[image](https://www.google.com/s2/favicons?domain=https://praat.org\&sz=32)

Praat+1



電話錄音還會加入其他擾動來源：

- 語音編碼和量化誤差。
- 網路傳輸或語音處理失真。
- 背景噪聲和重疊發話。
- 說話時自然發生的音高與音量變化。
- 音訊增益控制及降噪。

因此，即使取得 `jitter_local = 0.02`，也不能立即推論某人的聲帶異常，更不能僅憑這個數值推論心理壓力或說謊。

我的建議是將 Jitter、Shimmer 設成條件式特徵：在明確標定、足夠長且相對穩定的有聲母音片段中計算，並附帶品質檢查結果。

### 3.5 聲音品質（Voice Quality）

除了 Jitter、Shimmer，這一組也值得納入。

| 特徵                            | 說明              |
| ----------------------------- | --------------- |
| HNR（Harmonics-to-Noise Ratio） | 週期性聲音與非週期性成分的比值 |
| NHR（Noise-to-Harmonics Ratio） | 噪聲與諧波成分比值       |
| Harmonicity                   | 訊號週期性程度         |
| CPP（Cepstral Peak Prominence） | 倒頻譜週期峰值的突出程度    |
| Spectral Tilt                 | 高頻能量隨頻率衰減的趨勢    |
| H1–H2                         | 第一、第二諧波振幅差      |
| H1–A1 / H1–A2 / H1–A3         | 諧波與特定共振峰附近振幅的差異 |
| Hammarberg Index              | 不同頻率區段的最大能量差異   |
| Alpha Ratio                   | 兩個指定頻帶的能量差      |
| Voice Break Ratio             | 發聲中斷的時間比例       |
| Breathiness Estimate          | 氣聲程度的模型估計       |
| Roughness Estimate            | 聲音粗糙程度的估計       |
| Creaky Voice Ratio            | 喉化音等發聲型態的比例估計   |

其中 CPP、HNR、Spectral Tilt 可以提供與聲音週期性、雜訊及音色相關的資訊，但 8 kHz 電話通道可能使原始聲學解釋改變。

尤其是高頻諧波相關指標：如果量測所需的頻率已經被電話濾波器移除，所得數值就可能無法對應原始發聲特性。

### 3.6 頻譜（Spectral Features）：聲音能量分布在哪些頻率？

將一段聲音轉為頻譜，可以回答：

「這段聲音是低頻比較強，還是高頻比較強？頻率分布集中還是分散？聲音隨時間改變得多快？」

| 特徵                         | 說明               |
| -------------------------- | ---------------- |
| Spectral Centroid          | 頻譜重心             |
| Spectral Bandwidth         | 能量頻率分布的寬度        |
| Spectral Rolloff 85% / 95% | 累積頻譜能量到達指定比例的頻率  |
| Spectral Flatness          | 頻譜接近平坦噪聲或集中音調的程度 |
| Spectral Flux              | 相鄰時間框頻譜變化量       |
| Spectral Entropy           | 頻譜能量分布熵          |
| Spectral Contrast          | 頻帶內峰值與谷值的對比      |
| Spectral Slope             | 頻譜能量隨頻率變化的斜率     |
| Spectral Spread            | 頻率分布擴散程度         |
| Spectral Skewness          | 頻譜分布偏態           |
| Spectral Kurtosis          | 頻譜分布峰態           |
| Spectral Crest             | 頻帶最高峰相對平均能量      |
| Spectral Decrease          | 隨頻率增加的平均衰減       |
| Band Energy Ratio          | 不同頻帶的能量比例        |
| Sub-band Spectral Entropy  | 每個頻帶的能量熵         |
| Spectral Modulation        | 頻譜隨時間的變化模式       |

這些特徵可由 librosa、SciPy、openSMILE 萃取。

對於 8 kHz 錄音，務必限制分析頻帶，不要使用暗中假設音訊具有 8 kHz 以上頻率內容的特徵設定。

### 3.7 MFCC、Filterbank、Formants：描述聲道與音色

這是語音辨識、說話者辨識、語音分類中特別重要的一組。

先理解兩件事。

MFCC（Mel-Frequency Cepstral Coefficients） 並不是某個單一物理器官的直接測量值，而是聲音經過頻譜分析、Mel 濾波、對數轉換與 DCT 後形成的特徵係數。

Formant（共振峰） 則是與聲道共振相關的頻率結構，尤其有助於描述母音。

| 特徵                 | 建議形式                                      |
| ------------------ | ----------------------------------------- |
| MFCC 1–13          | 13 維 × 每個時間框                              |
| MFCC 1–20          | 20 維 × 每個時間框                              |
| ΔMFCC              | 一階時間變化                                    |
| ΔΔMFCC             | 二階時間變化                                    |
| Log-Mel Filterbank | 40 或 64 維 × 每個時間框                         |
| Log-Mel Energy     | 各 Mel 頻帶能量                                |
| LFCC               | Linear-Frequency Cepstral Coefficients    |
| GFCC               | Gammatone-Frequency Cepstral Coefficients |
| PLP                | Perceptual Linear Prediction              |
| RASTA-PLP          | 經 RASTA 時域濾波的 PLP                         |
| LPC                | Linear Predictive Coefficients            |
| LPCC               | Linear Prediction Cepstral Coefficients   |
| LSF / LSP          | LPC 的 Line Spectral Frequencies 表示        |
| F1                 | 第一共振峰頻率                                   |
| F2                 | 第二共振峰頻率                                   |
| F3                 | 第三共振峰頻率                                   |
| F1–F2 Distance     | 第一與第二共振峰的距離                               |
| F2–F3 Distance     | 第二與第三共振峰的距離                               |
| Formant Bandwidth  | 共振峰帶寬                                     |
| Formant Movement   | 共振峰隨時間移動的幅度                               |
| Vowel Space Area   | 多個母音的共振峰空間面積                              |
| Formant Dispersion | 共振峰間距分布                                   |

一個常見的 MFCC 特徵設計：

每個時間框萃取 39 維

# 13

MFCC

# 13

ΔMFCC

# 13

ΔΔMFCC

若每 10 ms 計算一次，每秒約有 100 個特徵框，因此 39 維配置約產生每秒 3,900 個特徵值。這是時間序列，不是 3,900 個獨立的統計變項。

對 8 kHz 電話錄音，MFCC + Δ + ΔΔ 是成本低、可重現，而且值得保留的基本比較基準。

不過，MFCC 仍會包含通道、語音內容與說話者資訊的混合影響，不能單憑 MFCC 判定兩段錄音是否來自同一人。

## 四、Voice Embedding：把一段聲音轉換為高維向量

這部分與傳統聲學特徵最大的差異，是不再要求每一個數值都具有直接可解釋的物理意義。

例如，傳統聲學特徵可能包含：

```
F0 median         = 156 Hz
HNR               = 14.8 dB
MFCC_01_mean      = ...
Pause ratio       = 0.23
```

而深度學習模型可能直接產生：

```
Speaker embedding = [0.018, -0.231, 0.087, ...]
                    共 192 維
```

向量中每一個座標本身通常沒有可靠的「第 17 維代表音色、第 25 維代表緊張」這類語義解釋。

它們的價值主要來自向量之間的距離，以及對下游任務的預測能力。

### 4.1 必須分清楚四種 Embedding

| 類型                        | 主要希望保留的資訊         | 常見模型                        |
| ------------------------- | ----------------- | --------------------------- |
| Speaker Embedding         | 說話者身分相關聲學特性       | ECAPA-TDNN、x-vector、TitaNet |
| Speech Representation     | 語音內容、發聲與其他聲學資訊    | WavLM、HuBERT、wav2vec 2.0    |
| Speech Semantic Embedding | 口語內容的語義           | Speech-Text、SONAR 類模型       |
| General Audio Embedding   | 聲學事件、環境聲、音訊與文字的關聯 | CLAP、BEATs、PANNs            |

這四種向量不應視為可以直接互換的特徵。

### 4.2 Speaker Embedding：ECAPA-TDNN

ECAPA-TDNN 是常用於 Speaker Verification 的架構。

以 SpeechBrain 公開的 `spkrec-ecapa-voxceleb` 為例：

- 模型在 16 kHz、單聲道語音條件下訓練。
- Embedding 維度為 192。
- 可利用 Cosine Similarity 比較不同語段的聲音表徵。

官方模型卡與設定檔確認了這些條件。

[image](https://www.google.com/s2/favicons?domain=https://huggingface.co\&sz=32)

speechbrain/spkrec-ecapa-voxceleb at main+1



兩段聲音向量 \(\mathbf a,\mathbf b\) 的 Cosine Similarity：

\[ \operatorname{sim}(a,b)= \frac{\mathbf a\cdot\mathbf b} {\|\mathbf a\|\|\mathbf b\|} \]

假設兩段錄音計算出相似度 0.86，這代表模型的兩個向量方向相近。

不代表有 86% 的機率是同一位說話者。

實務上必須用目標場景的標記資料校準 Decision Threshold，並測試 False Match Rate、False Non-Match Rate、EER、minDCF 等指標。

對電話錄音，還應測試「同一人、不同電話」、「同一人、不同日期」與「不同人、相同電話設備」等條件。

### 4.3 WavLM、HuBERT、wav2vec 2.0：聲音的通用表徵

這些模型通常透過 Self-Supervised Learning（自監督學習）學習語音表徵。

以 WavLM 為例，它的設計目標涵蓋語音內容、說話者及其他語音任務。微軟公開模型指出，WavLM 的通用表徵是針對多種下游語音任務開發，而非只做說話者辨識。

[image](https://www.google.com/s2/favicons?domain=https://huggingface.co\&sz=32)

Hugging Face+1



可以萃取的資料包括：

| 特徵                          | 形式                     | 分析價值         |
| --------------------------- | ---------------------- | ------------ |
| Last Hidden State           | 時間 × Hidden Dimension  | 保留逐時間位置的聲音表徵 |
| Layer-wise Hidden States    | Layer × 時間 × Dimension | 比較不同網路層      |
| Mean-pooled Embedding       | 固定長度向量                 | 語段分類、檢索      |
| Std-pooled Embedding        | 固定長度向量                 | 表徵隨時間的變異     |
| Layer-weighted Embedding    | 固定長度向量                 | 學習各層重要程度     |
| Embedding Cosine Similarity | 數值                     | 語段相似程度       |
| Embedding Drift             | 時間序列                   | 觀察通話過程中表徵變化  |
| Cluster Assignment          | 類別                     | 將語段分群        |

WavLM Base Plus 預訓練音訊採用 16 kHz，所以 8 kHz 輸入應先正確重取樣。其在電話錄音上的實際辨識能力，仍需要測試。

[image](https://www.google.com/s2/favicons?domain=https://huggingface.co\&sz=32)

Hugging Face+1



我建議同時保留兩種輸出：

- `frame_embedding`：逐時間框的高維向量。
- `segment_embedding`：對同一語段做時間池化（Pooling）後的固定長度向量。

注意，WavLM 通用 Embedding 並不等於已經最佳化的 Speaker Embedding。若目標是辨認說話者，專門訓練的 Speaker Encoder 通常是更直接的起點。

### 4.4 CLAP：聲音與文字能不能對應？

CLAP（Contrastive Language-Audio Pretraining）把音訊與文字映射到可比較的向量空間，能執行 Audio-Text Retrieval 或 Zero-Shot Audio Classification。

例如，可以建立不同的聲音事件描述，並比較它們與錄音的相似程度。

官方 LAION CLAP 專案提供音訊與文字 Embedding 的萃取方式，並有音樂、語音及一般音訊相關的模型配置。

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub+1



但需要區分：

- CLAP 比較適合探索環境音或音訊事件語義。
- Speaker Embedding 比較適合說話者辨識。
- Speech Semantic Embedding 比較適合尋找口語內容相近的片段。
- ASR 加上文字 Embedding，對繁體中文的精確語義檢索可能更容易驗證。

對傳統 8 kHz 通話，CLAP 的頻帶與領域差異尤其需要測試，不能因為模型可以接收重取樣後的音訊，就認為它對電話語音已經具有可靠表現。

## 五、說話行為與通話互動：電話錄音最容易被低估的特徵

聲音特徵不只是「每個人的聲音如何」，還包括「兩個人如何對話」。

這類特徵對客服電話、詐騙電話、訪談、談判、醫療問診及人機語音互動都具有研究價值。

### 5.1 Speech Activity、停頓與語速

| 特徵                         | 說明             |
| -------------------------- | -------------- |
| Speech Duration            | 實際說話總時間        |
| Speech Ratio               | 語音時間占通話時間比例    |
| Silence Ratio              | 無語音時間比例        |
| Utterance Count            | 語段數量           |
| Mean Utterance Duration    | 平均語段長度         |
| Longest Utterance          | 最長連續說話時間       |
| Pause Count                | 停頓次數           |
| Mean / Median Pause        | 停頓長度           |
| Long Pause Ratio           | 長於指定門檻的停頓比例    |
| Speech Burst Duration      | 一次連續語音活動的長度    |
| Speech Rate                | 每秒或每分鐘說出的字／音節數 |
| Articulation Rate          | 排除指定停頓時間後的發音速率 |
| Speaking Rate Variability  | 語速變化           |
| Filler Rate                | 「嗯」、「呃」等填充詞密度  |
| Repetition Rate            | 字詞重複頻率         |
| False Start Rate           | 話說到一半重新開始的次數   |
| Self-correction Rate       | 自我修正頻率         |
| Silent Hesitation          | 無聲猶豫時間         |
| Filled Hesitation          | 帶填充詞的猶豫        |
| Phrase Length              | 每個語句單位的長度      |
| Rhythm Variability         | 語音節奏變異         |
| Syllable Duration          | 音節長度           |
| Vowel / Consonant Duration | 母音與子音時長        |

其中，VAD（Voice Activity Detection）負責判斷「什麼時候有人在說話」。

例如，Silero VAD 官方支援 8 kHz 與 16 kHz，適合直接處理 8 kHz 電話音訊。

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub+1



但是 VAD 只告訴我們有沒有語音，並不保證知道是誰在說話。若要計算個別說話者的語速，通常需要結合轉錄時間戳、說話者分段及語音對齊。

### 5.2 Speaker Diarization 與 Conversation Dynamics

這組特徵需要區分說話者，也就是回答：

「誰在什麼時間說話？」

| 特徵                      | 說明               |
| ----------------------- | ---------------- |
| Speaker Count           | 估計說話者數           |
| Speaker Turn Count      | 發話輪替次數           |
| Turn Duration           | 每次發話長度           |
| Speaker Talk-Time Ratio | 各說話者占據的說話時間      |
| Inter-turn Gap          | 兩人交替發話之間的時間差     |
| Overlap Duration        | 同時說話的總時間         |
| Overlap Ratio           | 重疊發話占比           |
| Interruption Count      | 符合定義的打斷事件數       |
| Response Latency        | 對方結束後多久回應        |
| Backchannel Count       | 「嗯」、「對」、「喔」等回應次數 |
| Question–Answer Delay   | 問句至答句的時間         |
| Turn-taking Entropy     | 對話輪替模式的不確定性      |
| Long Monologue Ratio    | 長時間單方面發話的比例      |
| Speaker Dominance Index | 預先定義的發話占比或控制指標   |
| Speech-rate Convergence | 雙方語速是否逐漸趨近       |
| Pitch Convergence       | 雙方基頻變化模式是否趨近     |
| Acoustic Entrainment    | 雙方聲學特徵隨互動而趨近的程度  |
| Dialog Act Distribution | 問句、陳述、要求等對話功能比例  |

以同一通電話為例：

雙人通話時間軸（示意）

綠色是 A 發話，藍色是 B 發話。黃色區段表示雙方同時發話。

有一點非常值得注意：如果錄音本來有雙聲道，而且兩個聲道分別對應電話兩端，應優先保留與分析原始聲道。

把兩端先混成單聲道，反而會使重疊發話、說話者切換與語音辨識變得更困難。

若只有單聲道混合錄音，可使用 pyannote.audio 進行 Speaker Diarization。

其 `speaker-diarization-community-1` 支援不同取樣率自動轉換至 16 kHz，並可在下載模型後離線推論；模型取得需要依照 Hugging Face 頁面接受使用條件。

[image](https://www.google.com/s2/favicons?domain=https://huggingface.co\&sz=32)

Hugging Face+1



### 5.3 內容特徵：ASR 還能產生另一個特徵空間

一旦有語音轉文字（ASR），還可以產生：

| 特徵類別   | 例子                                         |
| ------ | ------------------------------------------ |
| 詞彙統計   | 字數、詞數、詞頻、詞彙多樣性                             |
| 語言識別   | 國語、臺語、英語及語言切換                              |
| 語義     | Sentence Embedding、Topic Embedding         |
| 句型     | 問句比例、命令句比例、疑問詞                             |
| 關鍵實體   | 金額、日期、帳號、機構、地點                             |
| 對話意圖   | 詢問、要求、確認、拒絕                                |
| 語用行為   | 說服、催促、承諾、要求保密等語句                           |
| 情緒文字訊號 | 文字表達的情緒或立場                                 |
| 重複與修正  | 重複字詞、自我修正、猶豫                               |
| 跨句一致性  | 前後說法是否存在可查證的矛盾                             |
| 語音辨識品質 | ASR Confidence、Entropy、N-best Disagreement |
| 對齊資訊   | 字／詞起訖時間、發音時長                               |

需要特別注意，ASR 產生的字數、詞彙或語義特徵會受到辨識錯誤影響。中文的「字／詞／音節」並不相同，語速與詞彙特徵必須明確說明分詞和統計方式。

對繁體中文電話語音，建議保留原始轉錄、正規化轉錄、時間戳與模型版本，避免只留下最後一個文字特徵向量。

### 5.4 情緒、語音狀態與非語言行為

還能研究以下較高階的特徵：

| 特徵                              | 說明             |
| ------------------------------- | -------------- |
| Valence                         | 模型估計的正向／負向情緒維度 |
| Arousal                         | 模型估計的情緒活躍程度    |
| Dominance                       | 情緒支配感的模型估計     |
| Emotion Probability             | 不同情緒類別的模型分數    |
| Vocal Effort                    | 發聲用力程度的估計      |
| Stress-related Prosody          | 與壓力可能相關的韻律變化   |
| Vocal Fatigue Indicators        | 與聲音疲勞可能相關的聲學指標 |
| Laughter Duration               | 笑聲時間           |
| Crying / Sobbing Duration       | 哭泣或啜泣時間        |
| Sigh / Gasp Events              | 嘆氣、倒抽氣等事件      |
| Breath Event Count              | 呼吸聲事件次數        |
| Non-speech Vocalization         | 非詞彙性發聲事件       |
| Emotion Transition Rate         | 模型預測情緒狀態的切換頻率  |
| Speaker-normalized Pitch Shift  | 相對個人基準的音高變化    |
| Speaker-normalized Energy Shift | 相對個人基準的訊號能量變化  |

可用的研究工具包含 SpeechBrain、Hugging Face Transformers、公開的 Speech Emotion Recognition（SER）模型，以及自行訓練的分類器。

但情緒、壓力、說謊、詐欺意圖是不同的概念。即使模型在某個情緒資料集表現不錯，也不代表能從電話聲音可靠判斷某人是否說謊。

在你的研究場景中，我會優先保留可重複量測的原始韻律特徵，將情緒分數作為待驗證的輔助特徵，而不是 Ground Truth。

### 5.5 電話通道、音訊品質與其他聲音事件

這是分析 PSTN 語音時不可忽略的一層。

| 特徵                             | 說明           | 方法               |
| ------------------------------ | ------------ | ---------------- |
| Effective Bandwidth            | 實際有效頻帶       | 頻譜分析             |
| Low/High Frequency Cutoff      | 頻帶截止位置       | 頻譜分析             |
| Background Noise Level         | 背景噪聲位準       | 噪聲估計             |
| SNR Estimate                   | 訊噪比估計        | WADA-SNR 等方法     |
| Speech Quality MOS Estimate    | 主觀品質分數的模型預測  | DNSMOS、NISQA     |
| Noisiness                      | 噪聲造成的品質影響    | NISQA            |
| Coloration                     | 頻率響應失真       | NISQA            |
| Discontinuity                  | 語音不連續程度      | NISQA            |
| Loudness Degradation           | 音量相關品質問題     | NISQA            |
| Clipping Events                | 疑似削波事件       | 波形偵測             |
| Abrupt Audio Gap               | 突然中斷的片段      | 時序偵測             |
| DTMF Event Count               | 電話按鍵音事件      | 頻率組合偵測           |
| Dial / Busy / Ringback Tone    | 電話線路提示音      | Tone Detector    |
| Background Speech Events       | 背景其他人聲       | 音訊事件分類           |
| Music / Environmental Sound    | 音樂與環境聲       | CLAP、PANNs       |
| Codec Artifact Indicators      | 與壓縮失真相符的特徵   | 專用分類器            |
| Replay / Synthetic Voice Score | 重播或合成語音的模型分數 | Anti-spoofing 模型 |

這裡要特別區分兩種語音品質評估：

無參考（Non-intrusive）：只有一段電話錄音，也能利用 DNSMOS 或 NISQA 估計品質。但這些分數需要在 8 kHz 電話場景驗證，並不是實際使用者所給的 MOS。

有參考（Full-reference）：例如 PESQ，必須同時擁有原始乾淨語音和經過電話系統後的對應錄音。PESQ 可處理符合其設定的 8 kHz 窄頻測試，但不能只用一段未知來源的通話自行計算有效的 PESQ 分數。

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub+2



NISQA 的程式採 MIT 授權，但官方預訓練權重採非商業性授權，不能把「免費取得」直接理解為「可以任意商用」。

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub



## 六、開源工具完整選型

以下按照研究用途與實務價值整理。

| 套件／模型                                                                               | 主要用途                              | 8 kHz 使用條件      |
| ----------------------------------------------------------------------------------- | --------------------------------- | --------------- |
| [librosa](https://librosa.org/doc/latest/index.html?utm_source=chatgpt.com)         | MFCC、Mel、頻譜、RMS、ZCR、Pitch         | 可原生計算           |
| [SciPy](https://www.scipy.org/?utm_source=chatgpt.com) / NumPy                      | FFT、Filter、統計與訊號處理                | 可原生計算           |
| [Praat](https://praat.org/?utm_source=chatgpt.com)                                  | F0、Jitter、Shimmer、HNR、Formants    | 可計算，須控制品質       |
| [Parselmouth](https://parselmouth.readthedocs.io/?utm_source=chatgpt.com)           | 從 Python 呼叫 Praat                 | 同上              |
| [openSMILE](https://audeering.github.io/opensmile-python/?utm_source=chatgpt.com)   | eGeMAPS、ComParE 特徵集               | 可處理，但部分特徵不可靠    |
| [Silero VAD](https://github.com/snakers4/silero-vad?utm_source=chatgpt.com)         | 語音活動、停頓、語段偵測                      | 原生支援 8 kHz      |
| [pyannote.audio](https://github.com/pyannote/pyannote-audio?utm_source=chatgpt.com) | 說話者分段、重疊發話                        | 會重取樣至 16 kHz    |
| [SpeechBrain](https://speechbrain.github.io/?utm_source=chatgpt.com)                | ECAPA、Speaker Verification 等      | 指定模型通常需 16 kHz  |
| [NVIDIA NeMo](https://github.com/NVIDIA-NeMo/NeMo?utm_source=chatgpt.com)           | Speaker Embedding、ASR、Diarization | 依模型決定           |
| [WavLM](https://huggingface.co/microsoft/wavlm-base-plus?utm_source=chatgpt.com)    | 自監督語音表徵                           | 需重取樣至 16 kHz    |
| [HuBERT](https://huggingface.co/models?search=hubert\&utm_source=chatgpt.com)       | 自監督語音表徵                           | 多數常見模型需 16 kHz  |
| [LAION CLAP](https://github.com/LAION-AI/CLAP?utm_source=chatgpt.com)               | Audio-Text Embedding              | 依模型設定，需驗證頻寬差異   |
| [NISQA](https://github.com/gabrielmittag/NISQA?utm_source=chatgpt.com)              | 無參考語音品質                           | 需模型指定格式與驗證      |
| [DNSMOS](https://github.com/microsoft/DNS-Challenge?utm_source=chatgpt.com)         | 無參考語音品質                           | 常用模型以 16 kHz 處理 |
| [faster-whisper](https://github.com/SYSTRAN/faster-whisper?utm_source=chatgpt.com)  | ASR、語音時間戳                         | 模型前處理至要求取樣率     |
| [FFmpeg](https://ffmpeg.org/?utm_source=chatgpt.com)                                | 解碼、聲道分離、格式檢查                      | 可處理多種電話音訊格式     |

### 最值得先使用的兩套標準特徵集

eGeMAPSv02

聲學及韻律相關、較容易分析與比較的標準特徵集

# 88

維 Functionals

ComParE 2016

高維聲學特徵集，適合做特徵選擇、傳統機器學習比較基準

# 6,373

維 Functionals

數量依 openSMILE Python 官方文件，eGeMAPSv02 另有 25 項 Low-Level Descriptors；ComParE 2016 另有 65 項 LLD 及 65 項 Delta。

[image](https://www.google.com/s2/favicons?domain=https://audeering.github.io\&sz=32)

Documentation

eGeMAPS 88 維不是 88 種彼此完全不同的物理性質，而是對不同 Low-Level Descriptors 進行統計與時間分析後的結果。

例如，一個 F0 序列可以衍生出平均值、變異、百分位數、斜率等不同特徵。

對研究來說，我建議先用 eGeMAPS 88 維建立基準，再用 ComParE 6,373 維做對照。這樣比一開始直接使用數千個特徵更容易發現究竟是哪一類資訊有用。

另需注意：openSMILE 官方採雙授權模式，研究與教育可免費使用，但其免費版本不可直接用於商業產品。

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub



## 七、我已建立一套可執行的 Python 特徵萃取起始工具

這套工具可以在本地處理錄音，不需要上傳音訊到雲端。它分成基礎分析與可選的深度學習模型分析。

Phone8K Feature Toolkit

Python 程式、繁體中文 README、Smoke Test

下載完整 Python Toolkit（ZIP）

單獨下載 Python 原始碼

使用方式：

```
# 建立環境
python3 -m venv .venv
source .venv/bin/activate

# 安裝基礎套件
pip install numpy scipy pandas soundfile librosa praat-parselmouth

# 先執行基礎分析
python phone8k_features.py call.wav --out results

# 安裝可選模組
pip install opensmile silero-vad torch

# 額外取得 VAD、eGeMAPS、ComParE
python phone8k_features.py call.wav \
  --out results \
  --vad \
  --egemaps \
  --compare
```

如果要研究 Jitter / Shimmer，先手動選出一段相對穩定的持續母音，例如 5.0 至 5.8 秒：

```
python phone8k_features.py call.wav \
  --out results \
  --vowel 5.0 5.8
```

如果要抽取 ECAPA Speaker Embedding，則需要指定已確認只有一位說話者的語音區間：

```
pip install speechbrain

python phone8k_features.py call.wav \
  --out results \
  --speaker 8.0 14.0
```

核心程式已用合成 8 kHz 訊號完成 Smoke Test，驗證了聲學特徵、F0 與手動選定區間的 Jitter / Shimmer 計算路徑。

驗證範圍：核心輸出在測試中產生 94 個逐框聲學特徵欄位，對應 940 個統計欄位（94 × 10）。openSMILE、VAD、ECAPA、WavLM 等可選模組因執行環境無法安裝或下載所需模型，尚未完成端到端實測。也尚未以真實電話錄音進行量測準確性驗證。

工具會產生下列研究資料：

| 檔案                         | 內容                    |
| -------------------------- | --------------------- |
| `summary.json`             | Metadata、聲學統計、F0、HNR  |
| `frame_features_10ms.csv`  | 逐 10 ms 聲學特徵          |
| `window_statistics.csv`    | 預設每 5 秒的統計            |
| `f0_timeseries.csv`        | 基頻時間序列                |
| `vad_intervals.csv`        | 語音活動區間（可選）            |
| `egemaps_v02_88.csv`       | eGeMAPS 特徵（可選）        |
| `compare_2016_6373.csv`    | ComParE 特徵（可選）        |
| `ecapa_192_embedding.npy`  | Speaker Embedding（可選） |
| `wavlm_mean_embedding.npy` | WavLM Embedding（可選）   |

這是可擴充的研究工具起點，不是已驗證完成的所有音訊特徵引擎。

## 八、如何將這些特徵整合為真正有研究價值的系統？

我會把正式研究系統分為四層。

Layer 1

Signal & Quality

原始音訊、頻寬、噪聲、Codec、Clipping

Layer 2

Time & Speaker

VAD、Speaker Diarization、語段切分

Layer 3

Feature Extraction

聲學特徵、Embeddings、ASR、互動行為

Layer 4

Analysis & Validation

統計建模、特徵消融、泛化評估、模型校準

### 8.1 分層輸出，而不是只給一個巨大向量

對一通 20 分鐘錄音，應保留不同時間尺度的資料：

| 粒度                 | 例子                       | 主要用途               |
| ------------------ | ------------------------ | ------------------ |
| Frame-level        | 每 10 ms 的 F0、MFCC、Energy | 分析短期變化             |
| Segment-level      | 每 2–10 秒的聲學統計與 Embedding | 語段分類與相似度           |
| Speaker-level      | 個別說話者的整體語音特性             | Speaker Comparison |
| Conversation-level | 整通電話的輪替、停頓、重疊            | 對話行為               |
| Corpus-level       | 不同錄音與不同族群的統計             | 模型訓練與研究            |

這樣才能研究：

「同一位說話者在不同時間的聲音如何改變？」

而不是只有：

「整通電話的平均 F0 是多少？」

### 8.2 不應盲目追求最多特徵

假設將上述特徵合併：

| 特徵來源           | 示範維度  |
| -------------- | ----- |
| 基礎聲學統計         | 940   |
| eGeMAPS        | 88    |
| ComParE 2016   | 6,373 |
| ECAPA-TDNN     | 192   |
| WavLM Base 類表徵 | 768   |
| 合計             | 8,361 |

這是以指定配置計算的維度範例，不代表每通電話都能有效取得這些數值，也不代表是 8,361 個獨立資訊來源。

例如，同時放入 MFCC、Mel Filterbank、ComParE 可能造成大量相關性。若每個人或每種設備只出現在特定標籤中，模型甚至可能學到電話設備差異，而不是你真正想研究的行為。

所以特徵的研究價值，不只取決於能抽出多少，更取決於它是否可靠、有助於任務，以及能否跨錄音條件泛化。

### 8.3 建議的實驗設計

若用於 8 kHz 通話語音研究，我建議比較以下四個模型組別。

| 實驗組 | 特徵組合                            | 要驗證的假設           |
| --- | ------------------------------- | ---------------- |
| A   | eGeMAPS 88                      | 可解釋的傳統聲學特徵是否足夠？  |
| B   | eGeMAPS + MFCC / 韻律統計           | 額外短期頻譜資訊是否有幫助？   |
| C   | B + ECAPA / WavLM               | 深度學習表徵是否提供互補資訊？  |
| D   | C + ASR / Conversation Features | 語義與互動資訊是否提高預測能力？ |

我建議使用以下驗收原則：

- 對同一資料集進行 Group-based Split，避免同一個 Speaker、Call、Session 跨入訓練與測試。
- 若研究跨設備泛化，另外執行 Unseen Device / Channel Test。
- 針對不同訊噪比、Codec、語言與重疊發話情況分別報告結果。
- 觀察 CER、EER、F1、AUROC 或其他符合實際研究任務的指標，不能只選容易得到高分的指標。
- 執行 Ablation Study：移除某類特徵，測試績效下降多少。

特別是 Speaker Embedding 的辨識門檻，以及情緒模型的分類機率，都應經過目標資料校準，不宜直接沿用其他資料集的閾值。

## 九、以 165 反詐騙電話研究為例，哪些特徵最值得優先取得？

若要將這套方法運用在 165 類型的 8 kHz 通話錄音，我會採取以下優先順序。

P0

基礎品質與時間切分

實際頻寬、RMS、SNR 估計、Clipping、Silero VAD、Speaker Diarization、語音時間比例。先確保每一筆資料具有可靠的來源、時序及說話者資訊。

P1

eGeMAPS、F0、MFCC、ECAPA、WavLM

建立聲音特徵的傳統與深度學習雙基準，檢驗不同說話者、設備與錄音條件下的穩定性。

P2

ASR、語速、停頓、重複、修正、對話輪替

取得語言內容與互動結構，研究特徵是否與任務有關。語義標籤與聲學標籤應分開建模，以便進行歸因。

P3

Jitter、Shimmer、SER、CLAP、ComParE 6,373

作為進階探索或消融比較。只有在量測條件、任務適用性與額外資訊價值獲得驗證後，才納入正式模型。

另外，Speaker Embedding 可用於說話者相似度研究，但應避免將聲紋向量視為匿名資料。這些向量可能具有識別或跨錄音連結個人的能力，需要適當存取控制、保存期限與研究授權。

我會把最初的研究目標設定為：

建立一套對 8 kHz 電話頻寬、Codec、噪聲、說話者及語音內容差異具有可測量穩定性的多層次特徵表徵系統。

這比單純追求「最多特徵」更容易形成可以重現、比較、驗證並發展成論文的研究成果。

## 十、理解檢查

請嘗試回答三個問題，之後可以進一步依你的回答分析概念理解：

1. 一段 8 kHz 通話重取樣到 16 kHz 後，WavLM 可以正常接收。這是否代表它取得了與原生 16 kHz 錄音相同的資訊？為什麼？
2. 一通雙人電話的整段錄音算出 Jitter 1.5%，可以據此判斷某位說話者的聲帶不穩定嗎？你會如何重新設計量測？
3. 如果 6,373 維 ComParE 的訓練準確率高於 88 維 eGeMAPS，但在全新電話設備上的表現較差，你會如何解釋？下一個最值得進行的實驗是什麼？
<!-- source:end -->
