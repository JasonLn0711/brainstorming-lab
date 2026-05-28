# Shared GPU model-owner inference service

## 核心想法

這個想法的貢獻是把「同一支 ASR 被載入兩次導致 VRAM 變兩份」重新定義成 production GPU inference 的 ownership 問題。

模型不應該跟著每個使用者、每個 UI session、每個 API worker、每個 background job 一起被載入。模型應該是常駐的 GPU 資產，由明確的 inference service 擁有；使用者請求只是排隊、batch、route、限流、執行、回傳結果的工作。

## 原始觀察

當兩個 Python process、worker 或 service instance 各自呼叫一次 ASR model loader 時，GPU 通常會看到兩份 allocation。即使 checkpoint 名稱相同，CUDA context、PyTorch allocator、model object、weights copy、runtime buffer、decoder state、beam-search cache、activation、workspace 仍然可能是 process-local。

所以 naive deployment 很容易變成：

```text
UI loads ASR
API loads ASR
worker loads ASR
```

這會讓 VRAM 被 deployment 邊界放大，而不是被真正的使用需求放大。

## Production 方向

比較合理的架構是：

```text
many users
  -> API gateway / backend
  -> scheduler / router
  -> ASR service / LLM service / embedding service / reranker service
  -> one controlled model owner per service
  -> GPU
```

這個方向與 vLLM、SGLang、Triton Inference Server、TensorRT-LLM、Ray Serve、KServe 這類 inference-serving 工具的精神一致：模型權重由 engine 或 service 常駐擁有，多個 request 透過 queue、continuous batching、KV-cache 管理、admission control 和 timeout policy 進入同一個服務。

## 本機 RTX 5080 版本

最新收斂是先不要從一櫃 H100/H200 開始，而是把目前的 RTX 5080 工作站當成一台本機小型 AI server。

現在的問題是每個 project 都各自寫一支程式，每支程式又各自呼叫 ASR、LLM 或 embedding model。這會讓 VRAM 壓力跟 project 數量一起放大。比較穩的設計是：

```text
Project A
Project B
Project C
    -> Local AI Gateway
    -> resident ASR / LLM / embedding worker
    -> RTX 5080
```

各 project 只保留業務邏輯，不直接 `load_model()`。模型載入、GPU 排程、queue、semaphore、log、cache、model version、VRAM 狀態都放到 Local AI Gateway 或 model worker。

第一版 API 可以很小：

```text
GET  /health
GET  /models/status
POST /asr/transcribe
POST /llm/chat
POST /embed
```

project 端只需要一個 shared client：

```python
from local_ai_client import transcribe

text = transcribe("sample.wav")
```

這個 client 背後可以先打：

```text
http://127.0.0.1:8001/asr/transcribe
```

未來如果模型搬到實驗室 server、H100/H200、雲端 GPU，project 端仍然維持同一個 client contract。

## 邊界

模型權重可以靠 service ownership 避免重複載入；每個 request 的 runtime state 仍然需要獨立管理。LLM 的 KV cache 會隨 context length 與 concurrent request 數量成長。ASR 也有 audio length、mel feature、encoder buffer、decoder state、beam search 等 runtime 成本。

MoE 的重點也要分清楚：MoE 可能省 active compute，但不代表 VRAM 會依照 active expert 比例下降。expert weights 的放置、routing、tensor parallel、pipeline parallel、expert parallel 和 GPU topology 仍然決定實際記憶體壓力。

在單張 RTX 5080 上，邊界更直接：不要假設 ASR、LLM、embedding、大模型都能同時常駐。比較務實的 residency policy 是：

- 最常用的小模型常駐。
- 偶爾才用的大模型按需載入。
- ASR / LLM 這類重型任務用 queue 或 semaphore 互斥執行。
- `/models/status` 回報目前載入模型、device、queue depth、VRAM 狀態。
- project code 不允許直接繞過 gateway 載共享模型。

## 最小下一步

先做一個可測量的對照實驗：

```text
Path A: two API workers each load the same ASR or small LLM
Path B: one model-owner service behind HTTP/gRPC queue
```

使用相同 request trace，在 1、2、4、8 concurrent users 下記錄：

- peak VRAM
- steady-state VRAM
- model-owner process count
- cold-start time
- p50 and p95 latency
- requests per second
- queue depth
- timeout rate
- GPU utilization
- failure behavior

如果 shared model-owner service 明確省下一份模型權重，且吞吐量或 p95 latency 在可接受範圍內，就把它推進成 JANUS ASR 或 broader GPU inference governance 的部署 recipe。

如果 off-the-shelf engine 已經完整滿足需求，下一步不是重造 serving engine，而是寫出可重複的 deployment recipe、monitoring checklist 和 ownership boundary rule。

## 5080 第一版實作路線

第一版不要做完整平台。先做一個最小可用的本機模型服務。

```text
~/ai-local-services/
  asr_service/
    server.py
    model_loader.py
    queue.py
  llm_service/
    server.py
    model_loader.py
  clients/
    asr_client.py
    llm_client.py
  scripts/
    measure_vram.py
    smoke_asr_client.py
```

第一個實作可以只選一個 endpoint，例如 `/asr/transcribe`。原因是目前的痛點最像 duplicate ASR loading。驗證方式是讓兩個 project client 同時送音檔，但 GPU 上只有一個 ASR model owner。

可觀察結果：

- naive path：兩個 project 各自載 ASR，VRAM 出現兩份 model allocation。
- gateway path：兩個 project 呼叫同一個 ASR service，VRAM 只保留一份主要 model weight allocation。
- 如果 latency 變差，就調整 queue、batch、timeout 和 request class。
- 如果 VRAM 還是爆，就明確決定哪些模型常駐、哪些模型按需載入。

## 可行性結論

這方案可行，而且是現在最應該採用的單機架構。

核心原則：

```text
Project 永遠不要直接碰共享 GPU model。
Project 只送任務。
Model service 才擁有 GPU model。
```

project 裡面不要再寫：

```python
model = load_asr_model()
result = model.transcribe(audio)
```

改成：

```python
from ai_clients.asr import transcribe

result = transcribe("audio.wav")
```

`ai_clients.asr` 背後只是打本機 API：

```python
import requests

def transcribe(audio_path: str):
    with open(audio_path, "rb") as f:
        response = requests.post(
            "http://127.0.0.1:8001/transcribe",
            files={"audio": f},
            timeout=600,
        )
    response.raise_for_status()
    return response.json()
```

真正載模型的地方只留在 ASR service：

```python
from fastapi import FastAPI, File, UploadFile
import asyncio

app = FastAPI()
model = None
gpu_lock = asyncio.Semaphore(1)

@app.on_event("startup")
def load_model_once():
    global model
    model = load_asr_model_to_cuda()

@app.get("/health")
def health():
    return {"ok": True, "model_loaded": model is not None}

@app.post("/transcribe")
async def transcribe(audio: UploadFile = File(...)):
    audio_bytes = await audio.read()
    async with gpu_lock:
        result = model.transcribe(audio_bytes)
    return {"text": result}
```

這樣多個 project 同時呼叫時，它們只是排隊進同一支 ASR，不會各自在 GPU 上長出一份模型。

## 分階段路線

第一階段：ASR service。

- 啟動時載入 ASR。
- 提供 `/health`。
- 提供 `/transcribe`。
- 用 semaphore 控制一次一個重型 GPU 任務。
- 回傳 JSON。
- 每個 project 統一改用 `from ai_clients.asr import transcribe`。

第二階段：LLM service。

LLM 不一定要自己手寫 server。比較穩的做法是先用 vLLM、llama.cpp server、Ollama 或 SGLang，讓 project 走 OpenAI-compatible API。這樣 project 的 chat 呼叫像 OpenAI API，但實際跑在本機 RTX 5080。

第三階段：embedding / reranker service。

embedding 比較容易 batch，可以等 ASR 和 LLM 的邊界穩定後再加入。

第四階段：model manager。

model manager 不要一開始就做。等到你真的遇到這些情況再做：

- ASR、LLM、embedding、TTS、reranker 同時常駐會壓爆 VRAM。
- 某些大模型偶爾要用，但不值得一直載著。
- 需要 `/models/status` 顯示 loaded、warming、unloading、queued、failed。
- 需要 VRAM 不夠時 unload 舊模型或拒絕新任務。

單機 RTX 5080 的合理策略是：

```text
ASR: 常駐
Embedding: 常駐或第二階段常駐
LLM: 用 vLLM / llama.cpp / Ollama / SGLang，需要時啟動
TTS: 需要時才載入
Reranker: 視 VRAM 與使用頻率決定
```

## 第一個實驗

最小實驗不需要完整平台。只需要兩條路徑：

```text
Path A:
  project_a.py loads ASR
  project_b.py loads ASR
  measure VRAM

Path B:
  asr_service loads ASR once
  project_a.py calls asr_client
  project_b.py calls asr_client
  measure VRAM
```

如果 Path B 省下一份模型 VRAM，而且 latency 可接受，就把這個模式定為所有本機 AI project 的 shared model rule。

## 論文敘事版本

老師提醒的重點是對的：論點四平八穩還不夠，第一頁要讓人感覺「這個問題正在發生，而且接下來會更嚴重」。這個 idea 的寫法可以從單機研究工作站的真實痛點切入，而不是一開始就講抽象的 model serving。

### 1. 現實問題

可以這樣開場：

> 單張高階 GPU 工作站正在變成研究者與工程師的本機 AI 基礎設施。ASR、local LLM、embedding、RAG、醫療 demo、研究自動化都可能在同一台機器上反覆執行。但是現在很多 project 仍然用 demo-style 寫法：每支 script 自己 import model、自己載入 checkpoint、自己 `.to("cuda")`。結果是每個 project 都變成獨立 GPU owner，讓有限的 VRAM 被 deployment 邊界放大，而不是被真正的任務需求使用。

這裡要放 citation 與實測證據。候選 citation：

- PyTorch multiprocessing/CUDA 文件可支撐「跨 process 的 CUDA 使用有明確限制，不能把同名模型視為自動共用」。見 PyTorch multiprocessing best practices 與 torch.multiprocessing 文件。
- 你自己的 RTX 5080 實測可支撐「兩個 project 分別載入同一支 ASR 時，VRAM 出現重複配置」。

這段的吸引力在於：它不是在說「我想包一個 API」，而是在說「本機 AI 工作站正在從單一 demo 變成多 project 基礎設施，但寫法還停在 demo 階段」。

### 2. 既有解法

要公平承認現有工具已經解決很多 serving 問題。

- vLLM / PagedAttention 把 LLM serving 的核心問題放在 KV-cache memory management、request scheduling、batching 與 throughput。它證明 LLM serving 不是只把模型載上 GPU，而是要管理每個 request 的 runtime state。
- NVIDIA Triton Inference Server 提供 dynamic batching、concurrent model execution、model serving configuration。它證明 production inference 本來就需要由 serving layer 管理資源。
- Ollama、llama.cpp server、vLLM、SGLang 這類工具可以讓 local LLM 透過 API 被 project 呼叫，OpenAI-compatible API 也讓 project 與模型位置解耦。

這段不是批評它們，而是說它們開出了一條路：模型應該由 service 擁有，project 只送 request。

### 3. 剩餘缺口

這篇文章可以提出的缺口不是「世界上沒有 model server」。世界上已經有很多 model server。

真正缺口是：

> 對單一研究者或小型實驗室的 RTX 5080 工作站來說，問題不是如何重新發明 vLLM 或 Triton，而是如何把一堆已經存在的 project 從 direct model loading 遷移成 local model-owner architecture。

也就是缺一個很實用的 migration discipline：

```text
project code owns business logic
local service owns GPU model
client owns API contract
measurement owns the decision
```

這個缺口的理由是：

- 直接上大型 serving framework 可能太重。
- 每個 project 自己載模型又會浪費 VRAM。
- in-process singleton 不能解決多 process / 多 project 問題。
- 本機 5080 的限制需要 residency policy：哪些模型常駐、哪些按需載入、什麼時候才需要 model manager。

### 4. 我們的新觀點

新觀點可以命名為：

```text
Local Model-Owner Architecture for Single-GPU AI Workstations
```

核心主張：

> 把 RTX 5080 工作站視為一台本機 AI server。project 只送任務；model service 才擁有 GPU model。第一階段先把 ASR 從 project 裡拔出來，做成 resident ASR service；第二階段讓 LLM 走 OpenAI-compatible local server；第三階段再加入 embedding / reranker；第四階段才在真實 VRAM 壓力下加入 model manager。

這個觀點的好處是它有清楚的工程順序，不會一開始就做太大的平台。

### 5. 回到開頭問題

文章最後要回到一開始的問題：本機 AI 工作站會越來越像個小型 shared infrastructure，但 project 寫法還停留在 demo-style direct loading。

你的貢獻可以寫成：

> We propose a local model-owner architecture for single-GPU AI research workstations. The architecture separates project logic from GPU model ownership by routing ASR, LLM, and embedding requests through local services and shared clients. We validate the first stage with an ASR migration experiment on an RTX 5080 workstation, comparing duplicate project-level loading against a resident ASR service in terms of peak VRAM, warm-start latency, queue behavior, and failure modes.

中文意思是：

> 我們不是要重新發明大型推論服務，而是提出一個單機研究工作站的模型 ownership 遷移規則，讓多個 project 能共享同一張 GPU 上的常駐模型，並用實測證據確認 VRAM、啟動時間、排程與失敗行為是否改善。

## 候選 citation

- PyTorch multiprocessing best practices: https://docs.pytorch.org/docs/stable/notes/multiprocessing.html
- PyTorch torch.multiprocessing: https://docs.pytorch.org/docs/stable/multiprocessing.html
- vLLM / PagedAttention paper: https://arxiv.org/abs/2309.06180
- NVIDIA Triton dynamic batching and concurrent model execution: https://docs.nvidia.com/deeplearning/triton-inference-server/archives/triton-inference-server-2600/user-guide/docs/tutorials/Conceptual_Guide/Part_2-improving_resource_utilization/README.html
- Ollama OpenAI compatibility: https://docs.ollama.com/api/openai-compatibility

這些 citation 的角色不同。PyTorch 支撐「跨 process/GPU ownership 不是自動共用」；vLLM 和 Triton 支撐「serving layer 管理 memory、batching、request scheduling 是成熟方向」；Ollama 支撐「本機模型可以透過相容 API 讓 project 與模型位置解耦」。你的實測則支撐本文真正的新焦點：單機 RTX 5080 多 project 的 migration discipline。
