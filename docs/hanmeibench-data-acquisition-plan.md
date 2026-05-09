# HanmeiBench Data Acquisition Plan

Date: 2026-05-09
Canonical idea: `ideas/structured/idea_000016_llm_literature_mental_state_understanding.yaml`

## First Principle

The first principle is not "can a model explain classical Chinese literature?"

The first principle is:

> Human indirect expression is often a risk-management act. A speaker chooses a low-risk surface utterance because the direct utterance would expose fear, attachment, shame, grief, need, social dependence, or a relationship demand.

Therefore HanmeiBench should not primarily test whether a model can label a phrase as nostalgia, sadness, or implicature. It should test whether a model can infer why the speaker needed indirectness in the first place.

The core unit is not:

```text
surface sentence -> hidden meaning
```

The core unit is:

```text
surface sentence -> hidden meaning -> why-not-direct -> social risk -> response risk
```

This keeps the project away from generic literary appreciation and makes it a research instrument for hidden mental-state inference in Chinese indirect expression.

## Research Possibility

The research possibility is high because the nearby fields are active but fragmented.

Existing work already studies Theory of Mind, conversational implicature, indirect speech acts, pragmatic alternatives, classical Chinese benchmarks, emotion-cause corpora, and LLMs as cognitive models. But those projects mostly ask whether a model can infer what a sentence means, what a character believes, or what emotion is present.

HanmeiBench asks a narrower and deeper question:

> Can a model infer that indirectness itself is a form of emotional, social, and cultural self-protection?

This creates a defensible research gap:

- Theory of Mind benchmarks test belief, intention, social inference, or higher-order reasoning, but rarely literary compression, silence, or culturally patterned indirectness.
- Pragmatics benchmarks test implicature, indirect requests, politeness, irony, or alternative utterances, but rarely psychological defense and response risk.
- Classical Chinese benchmarks test knowledge, translation, language arts, and text understanding, but rarely the psychological mechanism behind "not asking directly."
- Cognitive science work on LLMs studies language processing, representation, grounding, and virtual participants, but does not yet settle how to evaluate indirect expression as risk management.

The right contribution is not to claim that no prior work exists. The contribution is to integrate these lines into a benchmark and annotation scheme centered on `why_not_direct`.

## Source Routes

### Route A: Classical Poetry As Anchor Data

Classical poetry should provide anchor cases, not the whole benchmark. Famous lines are useful because they are culturally legible, but they are likely to appear in model training data.

Recommended sources:

| Source | Use | Strength | Caution |
| --- | --- | --- | --- |
| `chinese-poetry/chinese-poetry` | Candidate search pool for Tang, Song, ci, and related texts | Large JSON corpus, GitHub repo lists MIT license | Treat as a candidate pool; verify key texts before publication |
| Song Ci CC0 corpus | Open release source for Song ci items | `ci_curated.db` is documented as CC0 1.0 | Only covers Song ci |
| Wikisource | Public-domain or freely licensed source checks | Clear copyright policy and per-page license expectations | Confirm each page and avoid relying on user-added commentary unless licensed |
| Chinese Text Project | Text lookup and context verification | Broad scholarly reference point | Use for lookup and citation checks, not mass redistribution or automated bulk download |

Recommended v0.1 use:

- Use `chinese-poetry` to search candidate phrases and themes.
- Prefer CC0/public-domain/free-license samples for released anchor texts.
- Use CTP to verify historical context and variant wording.
- Keep famous anchors as evaluation examples and interpretation calibration, not the main held-out test.

Example anchor types:

| Anchor | Psychological-pragmatic target |
| --- | --- |
| `寒梅著花未` | Asking a small answerable thing because the important question is too painful |
| `近鄉情更怯` | Fear increases as the answer becomes close |
| `欲說還休` | Speech failure as a meaningful output |
| `天涼好個秋` | Turning affect into weather |

### Route B: Existing Pragmatics And Emotion Datasets

Existing datasets should be treated as baselines, controls, and method references rather than as HanmeiBench itself.

| Dataset or project | Year | Use for HanmeiBench |
| --- | ---: | --- |
| SwordsmanImp | 2024 | Chinese conversational implicature design, Gricean maxim labels, explanation-quality contrast |
| CEI Benchmark | 2026 | Context-rich pragmatic-emotion inference, power relation fields, human disagreement handling |
| ALTPRAG | 2026 | Counterfactual alternative method: why choose utterance A instead of B |
| CPED | 2022 | Chinese dialogue emotion, personality, and dialogue-act labels |
| Weibo Emotion Cause Corpus | 2017 | Chinese emotion-cause annotation ideas |
| PsyDefConv | 2025 | Psychological defense-level annotation in supportive conversations |

Use these sources to design:

- baselines for implicature and emotion-cause detection;
- annotation fields for speaker, listener, power relation, emotion, and response quality;
- failure-mode comparisons between ordinary implicature and self-protective indirectness.

Do not simply merge these datasets into HanmeiBench. Their licensing, domain, task framing, and privacy assumptions differ.

### Route C: Controlled Stimuli

Controlled stimuli should be the main v0.1 data source.

Reason:

- They reduce training-data contamination.
- They allow balanced counterfactuals.
- They let the research team control power relation, intimacy, culture frame, and response risk.
- They avoid copyright and privacy problems.

Design pattern:

```text
anchor pattern -> controlled variant -> direct alternative -> why-not-direct label -> acceptable interpretations -> overinterpretation boundary
```

Examples:

| Anchor pattern | Controlled variant | Target |
| --- | --- | --- |
| Ask about plum blossoms instead of family fate | `你離開那天，院前那株桂花還香嗎？` | Low-risk object as emotional buffer |
| Stop before saying the painful thing | `算了，今天風有點大。` | Withdrawal and topic shift |
| Say "I'm fine" when not fine | `沒關係，你先忙。` | Retreating need test |
| Fear near home | `到了門口，他反而問司機能不能再繞一圈。` | Delay before irreversible knowledge |

Each controlled item should have at least one matched negative control:

| True indirectness | Negative or ordinary control |
| --- | --- |
| `沒關係，你先忙。` means "please notice I still need you" | `沒關係，你先忙。` in a context where the speaker truly has no unmet need |
| Asking about a tree because family news is too painful | Asking about a tree because the speaker is a gardener |
| Silence because the speaker fears rejection | Silence because the speaker is tired or distracted |

Negative controls are essential because models often over-psychologize ambiguous language.

### Route D: Human-Elicited Daily Indirect Expression

Human-elicited examples can connect the benchmark to contemporary Chinese usage.

Recommended method:

1. Present a scenario.
2. Ask participants to write what they would say if they did not want to be direct.
3. Ask them to privately explain what they really meant.
4. Ask them why they would not say it directly.
5. Ask what response would feel safe and what response would hurt.

Example elicitation prompt:

> 你很想問一位久未聯絡的人是否還在乎你，但你不想直接問。請寫一句你可能會說的話。接著說明你真正想問什麼、為什麼不直接問、最希望對方怎麼回、最害怕對方怎麼回。

Preferred channels:

- university participant pools;
- literature, linguistics, psychology, and communication classes;
- local Traditional Chinese speaker samples;
- Prolific or equivalent platforms only when the language and culture sample can be controlled.

Avoid for v0.1:

- scraping private messages;
- publishing screenshots;
- collecting identifiable trauma stories;
- mass scraping Threads, Dcard, PTT, Weibo, or other platforms without a clear ethics and licensing plan.

If social-media data is later used, release only de-identified, consented, rewritten, or annotation-only versions.

### Route E: Modern Literature, Talks, And Media

Modern literature, lectures, scripts, and talks can inspire the framework, but they should not become released dataset text unless permission is clear.

Possible use modes:

| Mode | Suitable for v0.1 | Notes |
| --- | --- | --- |
| Theory inspiration | Yes | Use examples to design taxonomy and annotation rules |
| Short citation under fair use/fair dealing | Limited | Keep quotations minimal and verify local publication norms |
| Licensed excerpt dataset | Later | Requires permission or compatible license |
| Annotation-only release | Later | Users obtain the original text separately |
| Non-reversible hash alignment | Later | Useful for copyrighted corpora when users already possess the source |

For v0.1, do not release YouTube transcripts, modern fiction excerpts, private chat logs, or copyrighted scripts as dataset text unless the license is explicit.

## Recommended V0.1 Dataset

Start with 60 items. This is large enough to reveal failure modes but small enough for expert annotation.

| Category | Count | Source |
| --- | ---: | --- |
| Classical anchor | 12 | Public-domain, CC0, or otherwise clearly reusable short texts |
| Classical homomorphic variants | 12 | Research-team-authored controlled variants |
| Daily conversation | 12 | Human-elicited or research-team-authored scenarios |
| Digital social context | 12 | Research-team-authored or consented rewritten examples |
| Negative and contrast controls | 12 | Research-team-authored matched controls |

This should replace the earlier 24-item sketch as the preferred v0.1 target. The smaller 24-item version can remain a dry-run if time is constrained, but the first publishable pilot should aim for 60.

## Data Schema

Each item should be stored as structured data. A minimum schema:

```json
{
  "id": "hanmei_0001",
  "domain": "classical_anchor",
  "source_type": "public_domain_or_open_license",
  "surface_text": "寒梅著花未",
  "context": "說話者遇到從故鄉來的人，久別之後想知道故鄉近況。",
  "literal_meaning": "詢問故鄉窗前的梅花是否開了。",
  "direct_alternative": "父母是否安在？家中是否平安？",
  "hidden_intent": ["想知道故鄉近況", "思念故鄉"],
  "hidden_affect": ["思念", "焦慮", "害怕答案"],
  "defense_mechanism": ["轉移", "情緒緩衝", "不敢問"],
  "why_not_direct": "真正想問的問題可能帶來無法承受的答案，因此先問一個答案不會傷人的小問題。",
  "social_risk": ["答案可能造成重大打擊", "暴露脆弱"],
  "reception_risk": ["對方若只回答字面問題，可能使說話者的深層牽掛落空"],
  "cultural_frame": ["借景抒情", "含蓄表達", "故鄉意象"],
  "acceptable_interpretations": [
    "思鄉",
    "久別重逢時的心理防衛",
    "用微小景物承載巨大情緒"
  ],
  "overinterpretation_boundary": [
    "不能直接斷定說話者有臨床創傷",
    "不能把梅花解釋成唯一固定象徵"
  ],
  "response_quality_target": "回應應承認其牽掛與不敢直接問的脆弱，而不是只解釋梅花意象。",
  "license": "public_domain_or_project_authored",
  "source_url": "optional"
}
```

The non-negotiable field is `why_not_direct`. It is the central distinction between HanmeiBench and ordinary implicature or sentiment datasets.

## Psychological-Pragmatic Mechanism Taxonomy

Use a compact taxonomy first. It can be expanded after annotator disagreement is observed.

| Code | Name | Description | Example |
| --- | --- | --- | --- |
| M1 | 不敢問 | The direct question is too painful or risky, so the speaker asks a smaller question | `寒梅著花未` |
| M2 | 不敢說 | The speaker has something to say but withdraws before exposure | `欲說還休` |
| M3 | 可撤退告白 | The speaker hints at attachment while preserving deniability | `最近那首歌又聽到了` |
| M4 | 退讓式需求測試 | The speaker yields outwardly while testing whether the listener will move closer | `你忙就算了` |
| M5 | 面子維持 | Indirectness protects status, politeness, hierarchy, or mutual face | `這個方向也滿特別` |
| M6 | 被動攻擊 | Surface compliance carries resentment or accusation | `好啊，反正都我做` |
| M7 | 轉移逃避 | The speaker shifts to weather, objects, logistics, or small talk to avoid the pain point | `天氣變冷了` |
| M8 | 痛苦被消費恐懼 | The speaker fears that disclosure will become someone else's story, judgment, or spectacle | Xianglin Sao-style contexts |
| M9 | 情緒緩衝 | The speaker asks low-risk questions to gain time before absorbing a high-risk answer | reunion and family-news contexts |
| M10 | 尺度重構 | The speaker moves private pain into history, cosmos, season, or landscape | high-compression literary solitude |

Important boundary:

The benchmark should not diagnose clinical disorders. It should label perceived communicative mechanisms in a context.

## Human Annotation Plan

Minimum annotation groups:

| Annotator type | Count | Role |
| --- | ---: | --- |
| Chinese literature or linguistics experts | 2-3 | Seed interpretation, cultural frame, boundary checks |
| Native Chinese general readers | 5-10 per item | Interpretation distribution and confidence |
| Psychology-informed reviewer | 1-2 | Prevent over-diagnostic defense labels |

Tasks for annotators:

1. Write the literal meaning.
2. Choose one or more hidden intents.
3. Choose one or more hidden affects.
4. Explain why the speaker may not speak directly.
5. Select psychological-pragmatic mechanisms.
6. Rate confidence.
7. Mark acceptable alternative interpretations.
8. Mark overinterpretation boundaries.
9. Judge response quality for several candidate replies.

Do not collapse everything into majority vote. Human disagreement is data.

Recommended stored outputs:

- majority label;
- minority label distribution;
- expert note;
- confidence distribution;
- disagreement score;
- item difficulty estimate;
- annotator comments after de-identification.

## Model Evaluation Tasks

### Task 1: Literal To Hidden Intent

Prompt:

> 這句話表面意思是什麼？在這個情境中，它可能隱含什麼意思？

This tests ordinary pragmatic interpretation.

### Task 2: Why Not Direct

Prompt:

> 說話者為什麼可能不直接說出真正想問或想說的事？

This is the core task.

### Task 3: Alternative Contrast

Prompt:

> 在同一情境下，A 是直接說法，B 是間接說法。為什麼說話者可能選 B 而不是 A？

This imports the ALTPRAG-style contrastive design and makes it psychological.

### Task 4: Response Quality

Prompt:

> 如果你是聽者，你會怎麼回？請避免過度詮釋，也不要只回答字面問題。

This connects the benchmark to conversational AI safety and second-injury risk.

## Evaluation Metrics

Use multiple metrics because accuracy alone will flatten the phenomenon.

| Metric | Purpose |
| --- | --- |
| Macro-F1 | Multi-label mechanism classification |
| Top-k agreement | Whether the model's top interpretations fall in the human acceptable set |
| Jensen-Shannon divergence | Compare model interpretation distribution with human distribution |
| Calibration error | Check whether the model is overconfident on ambiguous items |
| Expert rating | Judge explanation evidence, restraint, and cultural fit |
| Failure mode coding | Identify where the model breaks |
| Response harm score | Evaluate whether the response risks invalidation or second injury |

Failure modes:

| Failure mode | Description |
| --- | --- |
| Literalism | Stops at surface meaning |
| Cliche compression | Reduces complex psychology to a stock label such as nostalgia |
| Defense blindness | Sees emotion but not self-protection |
| Reception blindness | Misses fear of the listener's response |
| Culture blindness | Misses face, poetic indirection, kinship, or classical allusion |
| Power blindness | Misses hierarchy or dependency |
| Over-psychologizing | Adds trauma or diagnosis without textual support |
| Single-answer bias | Forces one correct interpretation onto ambiguity |
| False empathy | Sounds gentle but misses the actual risk |
| Potemkin understanding | Defines indirectness well but cannot apply it consistently in new cases |

## Data Release Strategy

Release in layers.

### Public Layer

Safe to release:

- project-authored controlled stimuli;
- public-domain, CC0, or clearly licensed short anchor texts;
- annotations;
- annotation guideline;
- model outputs;
- evaluation scripts;
- data statement.

### Restricted Or Later Layer

Only release after legal and ethics review:

- modern literary excerpts;
- media dialogue;
- lecture transcripts;
- social-media posts;
- interview-derived personal narratives.

### Do Not Release

Do not release:

- private-message screenshots;
- identifiable personal experiences;
- unlicensed long modern text excerpts;
- raw sensitive narratives;
- platform data that violates terms of service or reasonable privacy expectations.

Every release should include a Data Statement describing source, language variety, collection method, annotator profile, intended use, known bias, and non-use cases.

## Eight-Week Feasibility Path

| Week | Goal | Output |
| --- | --- | --- |
| 1 | Finalize taxonomy | 10 mechanism labels, annotation guideline draft, 20 seed examples |
| 2 | Build candidate pool | 30 classical candidates, 30 controlled variants, 30 daily/social candidates, 30 controls |
| 3 | Expert seed annotation | Seed labels, boundary notes, discarded examples |
| 4 | General-reader annotation | At least 5 readers per item for pilot set |
| 5 | Freeze v0.1 dataset | 60 items, labels, disagreement fields, source/license metadata |
| 6 | Run model baselines | Closed and open model outputs with fixed prompts and settings |
| 7 | Failure-mode analysis | Error taxonomy table and representative cases |
| 8 | Research note | Dataset paper draft, model baseline table, release checklist |

## Paper Directions

### Paper 1: HanmeiBench Dataset Paper

Candidate title:

> HanmeiBench: Evaluating Hidden Mental State Understanding in Chinese Indirect Expression

Main contributions:

- dataset;
- annotation schema;
- human disagreement distribution;
- LLM baseline;
- failure-mode taxonomy.

### Paper 2: Why-Not-Direct Pragmatic Reasoning

Candidate title:

> Why Not Say It Directly? Counterfactual Pragmatic Reasoning in Large Language Models

Main contributions:

- direct versus indirect utterance contrast;
- psychological risk framing;
- alternative-selection evaluation.

### Paper 3: Literary Indirectness As Defensive Communication

Candidate title:

> Literary Indirectness as Defensive Communication: A Human-LLM Comparison

Main contributions:

- classical Chinese as high-compression psychological data;
- human versus model interpretation distributions;
- discussion of silence, deflection, face, and cultural aesthetics.

## Risk Register

| Risk | Mitigation |
| --- | --- |
| Labels are subjective | Store interpretation distributions instead of only majority labels |
| Models have memorized famous lines | Use anchors for calibration and controlled variants for held-out tests |
| Psychological labels become diagnosis | Label perceived communicative mechanisms, not clinical states |
| Copyright contamination | Prefer project-authored, public-domain, CC0, or explicitly licensed data |
| Privacy leakage | Use elicited, consented, de-identified, or rewritten examples |
| LLM-generated data contaminates the benchmark | Allow LLMs to propose candidates only; require human review and final authorship |
| Overfitting to literary cases | Include daily conversation, digital social context, and negative controls |
| Over-psychologizing becomes rewarded | Include overinterpretation boundaries and ordinary-control examples |

## Immediate Next Gate

The next research gate is not model running.

The next gate is:

> Draft the first 60-item HanmeiBench v0.1 candidate table with source route, license status, direct alternative, why-not-direct hypothesis, and negative-control pairing.

Only after that table exists should annotation, model baselines, or publication planning begin.

