# Rich UI As Human-Factors Evidence Interface

## Thesis

Rich UI 的核心價值不是「比純文字漂亮」，而是把 AI 系統的狀態、證據、不確定性與下一步行動變成可以快速檢查的介面物件。

在 AI Agent、醫療問診、ASR-supported intake 這類系統裡，使用者真正需要的不是更多文字，而是更快看懂：

- 目前知道什麼
- 哪些資訊來自使用者回答、ASR transcript、模型推論或 staff review
- 哪些地方仍然不確定
- 下一個安全行動是什麼
- 哪些證據支撐目前的 summary

因此 Rich UI 可以被定義成一種 human-factors evidence interface：它用 cards、timelines、charts、flow graphs、buttons、trace panels 等元件，把認知負荷從「讀一大段文字」轉成「檢查一組清楚的 decision objects」。

## Why It Matters

純文字或 raw JSON 適合機器交換，但不適合高壓、需要快速判讀的人類工作流。醫療問診與 ASR 系統尤其需要把資訊包裝成 reviewer 可以迅速檢查的形式。

更好的介面不是把模型輸出美化，而是讓每個 Rich UI component 都有明確工作：

- symptom timeline: 協助看出症狀發生時間與進展
- vital-sign trend: 協助看出數值變化與門檻
- risk-factor cards: 協助分組檢查重要風險
- question-flow graph: 協助理解 agent 為什麼問下一題
- staff-review summary: 協助醫護快速確認下一步
- evidence trace panel: 協助追蹤 source answer、transcript、model interpretation、uncertainty、review action

這讓 Rich UI 從視覺設計問題，變成 trustworthiness、traceability、cognitive load 與 decision-support 的工程問題。

## Scope Controls

這個想法的運作範圍是 staff-review intake support、synthetic-data demo context、human review workflow 與 future validation path。

Rich UI 應該提升 evidence inspection，而不是讓弱證據看起來更權威。介面需要把 uncertainty、source boundary、review state 與 next action 放在同一層，讓 reviewer 可以快速判斷輸出是否值得信任。

## Smallest Test

建立一個小型對照 prototype：

1. Plain baseline: 以文字或 JSON 顯示同一份 synthetic medical intake summary。
2. Rich UI version: 顯示 symptom timeline、risk-factor cards、staff-review summary、evidence trace。
3. Seeded errors: 加入 ASR drift、missing field、錯誤 risk factor 或不安全 next action。
4. Measure: review speed、seeded-error detection、trace inspection completeness、cognitive-load rating、miscalibrated trust。

如果 Rich UI 只提升 perceived polish，卻沒有提升判讀速度、錯誤偵測、trace 檢查或 completion，這個方向就應該停在設計參考，不升級成核心研究或產品工作。

## Links

- Canonical Idea OS record: `ideas/structured/idea_000045_rich_ui_as_human_factors_evidence_interface_for_ai_agents.yaml`
- Related design method: `idea_000042`
- Related medical triage lane: `idea_000001`
- Related ASR decision-stability lane: `idea_000040`
