# AI-native UI reverse engineering framework

Canonical Idea OS record: `ideas/structured/idea_000042_ai_native_ui_reverse_engineering_framework.yaml`

## Core Insight

你現在要學的不是先變成前端工程師，而是把視覺設計翻譯成可執行工程語言。

這個能力可以拆成：

1. 觀察 UI
2. 拆解 UI
3. 描述 UI
4. 把描述變成 deterministic specification
5. 讓 Codex 或 AI coding agent 實作
6. 用實際畫面檢查結果

## UI Observation Template

```md
# UI Observation

## Layout
- overall composition:
- stack / grid / split / dashboard / wizard / table:
- canvas or container constraint:
- card and section grouping:

## Visual Hierarchy
1. first visual focus:
2. second visual focus:
3. primary action:
4. secondary information:

## Spacing
- spacing scale:
- card padding:
- section gap:
- icon-to-text gap:
- line height:

## Color Semantics
- trust:
- warning:
- safe:
- neutral information:
- background:

## Information Density
- grouping strategy:
- wording limit:
- icon support:
- whitespace strategy:

## Cognitive Load
- target user mental state:
- panic reducers:
- avoid:
- accessibility:

## AI Implementation Prompt
- canvas:
- layout:
- spacing:
- typography:
- color roles:
- primary focus:
- secondary information:
- avoid-list:
- verification:
```

## Example Prompt Pattern

Weak prompt:

```text
做一個好看的醫療 dashboard。
```

Stronger prompt:

```text
Build a low-cognitive-load medical summary page.

Use a card-based layout with a centered fixed-width content area and a 4:3 canvas.
Use an 8pt spacing system.

The style should be calm, trustworthy, and non-panic.

Primary visual focus:
heart-rate alert.

Secondary information:
other vital signs.

Use semantic color roles:
navy for trust and headings,
orange for warning,
green for normal status,
purple or blue-gray for neutral information,
soft gray background to reduce anxiety.

Avoid high-saturation red, excessive animation, crowded information, and long clinical wording.

Each section must have clear grouping.
The UI should be readable for elderly hospital kiosk usage.
After implementation, inspect the rendered page and revise spacing, hierarchy, and text fit.
```

## Why This Matters

UI is attention routing.

好的 UI 不是只靠顏色漂亮，而是讓使用者在正確順序看到正確資訊。對醫療 UI 來說，重點不是刺激感，而是讓風險清楚、情緒穩定、下一步明確。

這個 framework 讓你可以在不先精通前端語法的情況下，開始用 PM、UX lead、AI product engineer 的方式工作。

## Smallest Next Test

Pick one medical summary UI screenshot and fill out the observation template.

Then ask Codex to build a static HTML/CSS prototype from the resulting specification and compare the rendered output against:

- visual focus order
- spacing rhythm
- semantic color roles
- information grouping
- elderly readability
- low cognitive load
