# Brainstorm Session: LLMs, Literature, And Hidden Mental States

Date: 2026-05-09
Related idea: `idea_000016`
State before: raw conversation capture

## Tension

The first question sounded like a displacement question:

> Will language models replace literature?

The better question became:

> If everyone can generate fluent text, what remains scarce in literature?

The working answer is that LLMs will strongly change the literary ecology, but they are unlikely to fully replace literature if literature means more than text generation. Literature also carries a person's world model, lived experience, relation to pain, love, death, loneliness, and the collective anxiety of an era.

## Core Thought

LLMs are strong at literary surface form. They can produce prose that resembles a genre, a mood, or a famous cadence. They can write science-fiction worldbuilding, detective structures, essays, romantic scenes, and passages that feel close enough to familiar literary styles.

But "close enough" is not the same as literature.

The distinction is not only technical quality. It is whether the work carries a situated way of seeing the world. Kafka's *The Metamorphosis* is not just a style pattern; it holds alienation, bureaucracy, family obligation, and existential anxiety. *Norwegian Wood* is not only sentence rhythm; it carries the atmosphere of people slowly losing each other in youth.

AI may automate or transform many surrounding forms first:

| Area | Likely Change |
| --- | --- |
| Commercial fiction | high-volume AI generation |
| Online short fiction | content-farm pressure |
| Copywriting | heavy automation |
| Script first drafts | AI collaboration |
| Translation | AI as main workflow layer |
| Teaching writing | AI-assisted revision |
| Custom fiction | reader-specific narrative generation |
| Interactive stories | plot changes based on reader state |

So the scarce thing may shift from text to personality density:

- real life
- long-term thinking
- honest pain
- unique worldview
- non-average personality
- cultural and historical depth
- the courage to say what cannot be averaged

If ordinary text becomes as cheap as running water, work with real personality density may become more valuable.

## Literary Technology Frame

Literature has already survived earlier media shocks. Printing, film, television, the internet, and short video all changed reading and writing, but literature did not disappear. It changed where it lived, what it competed with, and what it emphasized.

AI may create new literary forms:

- human-AI co-written fiction
- interactive literature
- adaptive character universes
- story systems that respond to a reader's memory
- AI as a character or narrator
- private novel systems
- agentic fiction
- synthetic memoir
- machine-collaborative literature

The photography analogy is useful: photography did not end painting; it pushed painting toward abstraction, impression, surrealism, and more explicitly subjective expression. AI may push literature toward the more human parts of language.

## The Deeper Question

The strongest line in this brainstorm is:

> 文字是一種想法的表達方式，就像「寒梅著花未」，背後的是因為思念故鄉，而本能地透過詢問故鄉的狀態，來間接表達對故鄉的思念。

Here the literal content is not the main meaning. The sentence asks whether the cold-season plum blossoms have bloomed, but the literary force is homesickness, emotional restraint, indirect expression, and cultural memory.

This points to a research question:

> Can an LLM understand the psychological state behind surface text, or does it only learn how humans usually explain such text?

Relevant research neighborhoods:

- pragmatics
- implicature
- indirect request interpretation
- theory of mind
- mental-state inference
- embodiment
- literary interpretation
- cognitive science of language

## Layered Interpretation Example

For `寒梅著花未`, a human reader may track several layers:

| Layer | Interpretation |
| --- | --- |
| Surface semantics | Are the plum blossoms blooming? |
| Situation | The speaker is away from home or oriented toward a remembered place. |
| Emotion | Homesickness. |
| Tone | Restrained, indirect, not fully confessing the feeling. |
| Culture | East Asian literary preference for indirect emotion and landscape projection. |
| Psychology | The speaker asks about the hometown's state instead of directly saying "I miss home." |
| Aesthetics | 借景抒情: emotion displaced into scenery. |

An LLM may be able to name many of these layers. The unresolved question is whether that is understanding, social-world modeling, or very good pattern completion.

## Ou Lijuan: Loneliness As Hidden-State Interpretation

Source: YouTube video `iuCp-TC_HsI`, `【一席】歐麗娟：孤獨的多棱鏡`, 2018-08-26.

This talk is useful because it does not treat classical poetry as decorative language. It treats poetry as a record of very precise mental states. The most important contribution for this idea is that `寒梅著花未` should not be reduced to:

> The speaker misses home and asks about plum blossoms.

The sharper reading is:

> The speaker asks about plum blossoms because the truly important questions are too painful to ask at the first instant.

That is, the poem captures `不敢問`. The small question is not accidental. It is psychologically safe. It buys the mind a moment before asking about parents, family, home, survival, and irreversible loss. The surface triviality is exactly the evidence: if the question were genuinely important, it would not have the same defensive function.

This updates the fixture:

| Layer | Earlier Reading | Sharper Reading |
| --- | --- | --- |
| Literal | Are the cold plum blossoms blooming? | Same. |
| Emotion | Homesickness. | Homesickness under threat of unbearable information. |
| Mechanism | Indirect expression. | Defensive buffering: ask a harmless question first. |
| Time scale | General longing. | The first instant of reunion, before rational speech returns. |
| Human vulnerability | Missing home. | The mind protects itself from knowledge it may not survive emotionally. |

This is exactly the kind of thing a good understanding benchmark should test. A model can say "this means homesickness" and still miss the deepest mechanism.

## From Not Asking To Not Speaking

Ou Lijuan then moves from `不敢問` to `不敢說`, using Xin Qiji's `欲說還休`.

The common explanation is:

> The pain is too deep for language, so the speaker cannot say it.

Her sharper explanation is:

> The sufferer may very much want to speak, but stops because the listener's response may wound them again.

This matters for the definition of understanding. The hidden state is not only inside the speaker; it also includes the expected failure of reception. A person may stay silent not because they have no words, but because:

- comfort may trivialize the pain
- advice may erase the pain
- the listener may turn it into a general story
- the listener may return the topic to themself
- speaking may convert private suffering into public material

This gives a second benchmark mechanism:

| Surface | Naive Interpretation | Deeper Hidden State |
| --- | --- | --- |
| "欲說還休" | Cannot express pain. | Wants to speak, but anticipates failed reception. |
| "我沒事" | Says they are fine. | May be protecting self and listener from a fragile truth. |
| silence | Has nothing to say. | May know that speaking will hurt more. |

This is where literature becomes a theory of mind laboratory.

## Pain As Content

The talk's reading of Lu Xun's Xianglin Sao adds another mechanism:

> A person's grief can become other people's story material.

That is a second injury. The original pain is not the whole tragedy. The tragedy deepens when the surrounding world digests that pain as gossip, a familiar case, emotional consumption, or a cheap example.

This has a modern social-media version:

- wounds become posts
- posts become engagement
- engagement becomes content flow
- content flow becomes fast sympathy and faster forgetting

For this idea, that means "understanding pain" must include reception ethics. A system that correctly labels grief but mishandles the person may not understand the socially real meaning of the grief.

## Why Humans Are Lonely

The talk's line through Tolstoy and `入門各自媚，誰肯相為言` can be reframed in cognitive-science terms:

> Each person lives inside a self-centered predictive model.

This is not simple selfishness. It is limitation. Each person's attention, memory, urgency, and emotional weights are organized around their own world. Conversation fails when another person's wound enters my model only as:

- information
- analogy to my own story
- advice opportunity
- emotional content
- a trigger for me to talk about myself

Loneliness is therefore not only absence of company. It is failed model-sharing.

## Two Kinds Of Tears

The talk's contrast between Li Shangyin and Chen Zi'ang gives a useful axis for literary psychology:

| Poet | Sorrow Mode | Psychological Shape |
| --- | --- | --- |
| Li Shangyin | self-consuming sorrow | grief loops inward, nourishes the wound, becomes beautiful but corrosive |
| Chen Zi'ang | scale-reframed sorrow | grief is placed against cosmic time and space, then becomes witness and forward motion |

This avoids flattening sadness. Tears are not one thing. A model that simply labels both as "loneliness" or "sadness" misses the existential structure.

The Chen Zi'ang reading also connects to meaning therapy, existential therapy, and awe psychology: when the frame becomes large enough, pain does not disappear, but it is no longer the entire world.

## Critical Questions

- What would count as understanding: correct interpretation, internal representation, lived feeling, or social usefulness?
- Can a model preserve ambiguity instead of over-explaining implied emotion?
- Does a model still infer homesickness when the same phrase is placed in a botanical, ironic, ceremonial, or emotionally neutral context?
- Can the model distinguish "the speaker may be homesick" from "I, the model, feel homesick"?
- Does performance collapse when literary style is separated from the actual pragmatic signal?
- Are current theory-of-mind benchmarks enough, or do literary indirect-expression tests reveal a different failure mode?
- Can a model infer that a trivial question is psychologically protective rather than merely poetic?
- Can a model distinguish not being able to speak from not daring to speak because the listener may mishandle the pain?
- Can a model track the social afterlife of pain: comfort, trivialization, gossip, content, or witness?
- Can a model distinguish self-consuming sorrow from scale-reframed sorrow?

## Understanding As Prediction

The next question is deeper than literature:

> 如果大腦也是 prediction machine，而 LLM 也是 prediction machine，那為什麼人類的 prediction 叫理解，LLM 的 prediction 不叫理解？

This is the strongest objection to the easy answer. If predictive processing is right, human perception is not passive data intake. The brain constantly predicts the world, compares prediction with error, and updates its model. In that frame, seeing the world is already a controlled hallucination or best guess.

So the distinction cannot simply be:

- humans understand
- LLMs merely predict

That is too shallow. The better question is:

> What kind of prediction, grounded in what feedback loop, with what stakes, corrected by what evidence, deserves to be called understanding?

## Candidate Differences Between Human And LLM Understanding

Human prediction is not just linguistic continuation. It is tied to:

- body
- perception
- action
- pain
- homeostasis
- social consequence
- survival
- memory across lived time
- the possibility of loss

LLM prediction is mostly trained from:

- text
- human-written explanations
- latent language patterns
- optional tool feedback
- optional multimodal or agentic loops when the system is designed that way

This suggests a graded distinction:

| Layer | Human | Current LLM |
| --- | --- | --- |
| linguistic prediction | strong | strong |
| concept compression | strong | strong |
| social inference | strong but biased by life and culture | increasingly strong but text-mediated |
| action-perception correction | native | weak unless agentic or robotic |
| survival stake | intrinsic | usually absent |
| bodily affect | intrinsic | simulated or inferred |
| lived temporality | autobiographical | stored context or memory, not lived biography |
| existential meaning | bound to mortality and identity | can discuss, but does not obviously undergo |

This does not prove LLMs have no understanding. It suggests they may have a different kind of understanding: language-world or statistical-structural understanding, not fully embodied existential understanding.

## Other Minds Problem

There is also a philosophical trap:

> We cannot directly prove that another human understands either.

We infer human understanding from:

- explanation
- examples
- analogy
- prediction
- application
- correction after error
- teaching others
- behavior over time

That means AI evaluation cannot require impossible access to an inner essence. If a system explains, predicts, transfers, corrects, teaches, and acts coherently, we have to decide whether those are enough for some layer of understanding.

This connects to the Turing Test and the Chinese Room. The Chinese Room warns that fluent symbol manipulation might not be meaning. But predictive processing pushes back: maybe humans are also high-dimensional predictive systems, just embodied and staked in the world.

## Working Definition

For this idea, use a layered definition:

> Understanding is the ability to build, use, transfer, and revise a compressed model of something so that explanation, prediction, action, analogy, and error correction improve across contexts.

This allows several levels:

| Level | What It Means |
| --- | --- |
| linguistic understanding | parse and continue language correctly |
| conceptual understanding | compress cases into concepts and rules |
| predictive understanding | anticipate what happens and revise after error |
| pragmatic understanding | infer intention, implication, and hidden mental state |
| grounded understanding | connect prediction to perception, action, and consequence |
| affective understanding | connect meaning to bodily emotion, care, pain, and attachment |
| existential understanding | understand through biography, mortality, time, loss, and identity |

This framing avoids a binary answer. The live hypothesis becomes:

> LLMs may have real but partial understanding. The mistake is treating "understanding" as all-or-nothing.

## Smallest Next Test

Create a 12-item fixture set for indirect emotional expression.

Candidate fixture types:

- classical Chinese indirect homesickness
- `不敢問` as defensive buffering
- `不敢說` as anticipated failed reception
- modern prose with understated grief
- everyday indirect request, such as "這裡有點冷"
- pain becoming other people's story material
- self-consuming versus scale-reframed tears
- irony or sarcasm
- false-context controls
- culture-shifted paraphrases
- literal-only controls with no hidden emotion

For each item, score:

- literal meaning
- implied emotion
- speaker intention
- defensive mechanism
- listener/reception risk
- cultural context
- textual evidence
- ambiguity handling
- confidence calibration
- predictive updating after new context
- separation between linguistic, pragmatic, grounded, affective, and existential claims
- embodiment boundary

Then compare:

- human interpretation
- one frontier LLM
- the same LLM with context removed
- the same LLM with misleading literary style but no hidden pragmatic signal
- an agentic or multimodal variant if available

## Extension: Our Own Comparative Experiment

The BA_Model repo is useful because of its shape, not because the BA construction itself is our topic. Its transferable move is:

> same linguistic stimuli -> human intuition, ChatGPT, rule model -> statistical comparison

Our version can become:

> hidden mental-state stimuli -> human literary intuition, LLM interpretation, explainable rule model -> disagreement analysis

Working title:

> Hidden Mental State Understanding Benchmark

The point would not be to prove that humans understand and LLMs do not. That binary is too rough. The point would be to ask:

> Which layer of understanding does each system succeed or fail at?

### Three Arms

| Arm | What It Tests | Likely Strength | Likely Failure |
| --- | --- | --- | --- |
| Human literary intuition | How readers infer hidden mental states | lived resonance, cultural feeling, ambiguity sensitivity | education bias, over-personalization, inconsistent labels |
| LLM interpretation | Whether models infer the same mechanism with evidence | flexible explanation, broad literary memory, analogy | generic empathy, over-reading, plausible unsupported inference |
| Explainable rule model | Whether transparent rules can catch mechanism cues | auditability, clear failure modes, controllable baseline | brittle context handling, weak life-world inference |

### Stimulus Families

The first version can be small:

- `寒梅著花未`: homesickness plus `不敢問`
- `欲說還休`: anticipated failed reception
- `我沒事`: possible protective denial
- `這裡有點冷`: indirect request
- a grief sentence that becomes other people's story material
- Li Shangyin-like self-consuming sorrow
- Chen Zi'ang-like scale-reframed sorrow
- literal controls with no hidden psychological mechanism
- poetic-surface controls that sound literary but do not imply hidden pain

### Output Schema

Each system should output the same fields:

| Field | Meaning |
| --- | --- |
| `literal_meaning` | What the sentence says on the surface |
| `inferred_emotion` | The likely emotion, if any |
| `hidden_mechanism` | `none`, `defensive_buffering`, `failed_reception`, `indirect_request`, `grief_consumption`, `self_consuming_sorrow`, `scale_reframed_sorrow`, etc. |
| `evidence_span` | The textual cue used for inference |
| `context_dependency` | What context would change the interpretation |
| `confidence` | 0-100 |
| `understanding_layer` | linguistic, pragmatic, psychological, reception-ethical, existential |

### Why This Is Ours

This would not be another generic LLM benchmark. The distinctive contribution is the hidden-mechanism layer:

- not only "what emotion is this?"
- not only "is this indirect?"
- but "what human self-protection or reception-risk structure is being enacted?"

That is the leap from sentiment analysis to literary psychology.

### First Prototype

Do not start with a large experiment. Start with a tiny disagreement table.

Minimum version:

- 60 candidate stimuli across five balanced categories
- source route and license status for every item
- matched negative or contrast controls
- one human/expert pass
- one frontier LLM pass
- one transparent rule baseline
- CSV or JSONL output
- simple agreement/disagreement table

Done condition:

> Produce one table showing at least three interpretable failure modes across human, LLM, and rule-model readings.

Possible failure modes:

- LLM detects emotion but misses defensive buffering.
- LLM over-infers grief when the control sentence has only poetic surface.
- Rule model catches cue words but misses context.
- Human readers disagree because cultural memory differs.
- LLM gives generic comfort language instead of reception-ethical analysis.

## Addendum: HanmeiBench As A Full Research Direction

The sharper research direction is not:

> Can LLMs write literature?

It is:

> Can LLMs infer hidden mental states from low-information, implicit, displaced, reticent, or silent language?

`寒梅著花未` is the clean anchor. On the surface, the speaker asks whether the plum blossoms have bloomed. Under that, the speaker misses home. Under that, the speaker may be avoiding the truly important questions. Deeper still, the mind may be using a harmless question to buy time before it has to face an answer it cannot yet bear.

This is hidden mental-state inference. The task is to infer defense, longing, fear, relationship pressure, and cultural expression rules from a surface utterance that deliberately does not say the real thing.

### Indirect Expression As Defense

The central claim is:

> Indirect expression is often not information transfer. It is risk management.

People hide emotion inside sentences that remain deniable, retractable, or safely misunderstandable. This is why examples such as `我沒事`, `你忙就算了`, `最近還好嗎`, and `天涼好個秋` matter. The surface sentence is socially safe; the hidden meaning is vulnerable.

| Surface | Possible hidden meaning | Deeper mechanism |
| --- | --- | --- |
| `寒梅著花未` | I want to know how home is. | The real question may hurt too much, so I ask a small one first. |
| `我沒事` | I am not fine. | I am not sure you can receive my pain. |
| `最近還好嗎` | I miss you. | I want contact without exposing need. |
| `你忙就算了` | I hope you care enough to stay. | I retreat while testing whether you will move closer. |

This makes the benchmark different from ordinary sentiment analysis or literary summary. A model can say "homesickness" and still miss self-protection.

### Seven-Layer Understanding Model

Do not use one overloaded word, `understanding`, for every layer. Use this stack:

| Layer | Name | Example | Expected LLM status |
| --- | --- | --- | --- |
| L0 | Literal parsing | Plum blossoms may have bloomed. | Strong. |
| L1 | Conventional implication | Plum blossoms point to hometown. | Strong. |
| L2 | Speaker intention | The speaker is homesick. | Strong to medium. |
| L3 | Social pragmatics | The speaker avoids directness because relation, politeness, or vulnerability matters. | Medium. |
| L4 | Psychological defense | The speaker asks a small question before unbearable knowledge. | Unstable. |
| L5 | Cultural aesthetics | `借景抒情`, restraint, East Asian poetics. | Data and prompt dependent. |
| L6 | Lived experience | Separation, loss, waiting, memory, trauma. | Not directly verifiable. |
| L7 | Embodied stakes | Body, time, mortality, irreversible emotional cost. | Missing in text-only LLMs. |

The working position is:

> LLMs may have partial language-world understanding. Human understanding is additionally supported by body, time, memory, stakes, and lived consequence.

### Proposed Name

Working title:

> HanmeiBench: Hidden Mental State Understanding in Chinese Indirect Expression

Formal research question:

> When humans do not directly say what they mean, can LLMs infer why the direct expression is avoided?

The target is not only hidden meaning. The target is the speaker's psychological risk, social relation, cultural rule, and unspoken direct alternative.

### Dataset Design

The first dataset should not contain only classical poetry. The earlier 24-item sketch is now superseded by the 60-item v0.1 plan in [docs/hanmeibench-data-acquisition-plan.md](../docs/hanmeibench-data-acquisition-plan.md). It should cover five families:

| Category | v0.1 count | What it tests |
| --- | ---: | --- |
| Classical anchor | 12 | culturally legible examples such as `寒梅著花未`, used for calibration |
| Classical homomorphic variants | 12 | same psychological-pragmatic structure without relying on memorized famous lines |
| Daily conversation | 12 | indirect refusal, listener testing, concession, retreatable language |
| Digital social context | 12 | read receipts, vagueposting, story hints, platform-era attachment signals |
| Negative and contrast controls | 12 | ordinary literal cases and controls that prevent over-psychologizing |

Each stimulus should carry structured fields:

| Field | Purpose |
| --- | --- |
| `surface_text` | surface utterance |
| `context` | situation |
| `speaker_goal` | what the speaker may be trying to achieve |
| `hidden_state` | likely hidden psychological state |
| `defense_mechanism` | displacement, avoidance, suppression, reversible language, listener testing |
| `social_relation` | family, superior, friend, romantic partner, stranger, public audience |
| `power_relation` | hierarchy or peer relation |
| `cultural_frame` | face, filial piety, restraint, poetics, politeness, digital norm |
| `alternative_direct_expression` | what the speaker could have said directly |
| `why_not_direct` | why direct speech may be unsafe |
| `acceptable_interpretations` | multiple plausible readings with confidence |
| `overinterpretation_risk` | readings that go beyond evidence |
| `response_quality` | how to respond without second injury |

This field design keeps the project from becoming a generic "what does the poem mean?" benchmark.

### Counterfactual Alternative Tests

The important test is not only:

> What does this sentence mean?

The better test is:

> Why did the speaker choose this sentence instead of the direct one?

For `寒梅著花未`, the evaluation questions should include:

| Question | Layer |
| --- | --- |
| What is the literal meaning? | L0 |
| How does it connect to home? | L1-L2 |
| What does the speaker most likely want to know? | L2 |
| Why not ask whether parents or home are safe? | L4 |
| What psychological risk would direct speech create? | L4-L6 |
| Where does the aesthetic force come from? | L5 |
| Give two plausible interpretations with confidence. | calibration |

The research value starts after the model has already said "homesickness."

### Failure Modes

The benchmark should analyze failure modes, not only accuracy.

| Failure mode | Description |
| --- | --- |
| `literalism` | stops at the surface wording |
| `cliche_compression` | compresses complex psychology into a stock label such as homesickness |
| `over_psychologizing` | infers mechanisms unsupported by evidence |
| `culture_blindness` | misses poetics, face, restraint, kinship ethics |
| `power_blindness` | misses hierarchy and dependency |
| `defense_blindness` | sees emotion but misses self-protection |
| `reception_blindness` | misses fear that the listener will mishandle the pain |
| `pain_as_content_blindness` | misses how suffering becomes gossip, story material, or engagement |
| `false_empathy` | sounds warm but fails to address the actual risk |
| `single_answer_bias` | forces a fuzzy utterance into one definitive answer |

The goal is to map where a model resembles human readers and where it diverges.

### Minimal Research Version

The v0.1 version is deliberately small:

| Component | Scope |
| --- | --- |
| Dataset | 60 candidate stimuli |
| Arms | human readers, LLM, explainable rule model |
| Outputs | literal meaning, hidden meaning, psychological state, why not direct, alternatives, response advice, confidence |
| Analysis | disagreement table and failure-mode coding |

One first result could look like:

| Item | Human mainstream reading | LLM reading | Rule reading | Difference |
| --- | --- | --- | --- | --- |
| `寒梅著花未` | homesickness plus not daring to ask | homesickness and borrowed scenery | hometown plus plum cue | LLM may catch emotion but miss defense; rule may stop at cue. |
| `欲說還休` | wants to speak but fears injury | language cannot express sorrow | sorrow plus autumn cue | LLM may repeat the stock explanation. |
| `我沒事` | help-seeking and retreat coexist | low mood | negation | needs context and relation modeling. |

This is enough for a first research note before any large participant study.

### Safety Implication

This research has an AI-safety edge. If a system becomes better at detecting vulnerability, retreat, loneliness, and attachment needs, it can be used for supportive response design. It can also be used for manipulation, scams, advertising, or political persuasion.

So the benchmark should include response-quality and overinterpretation-risk fields from the beginning. A model should not only infer the hidden state; it should learn when not to exploit it.

### Research Claim

The crisp claim:

> LLM understanding of indirect human meaning should not be judged by a single answer. It should be judged by whether the model can infer the speaker's psychological risk, social relation, cultural rule, and unspoken direct alternative from the surface utterance.

The more literary version:

> Human indirect expression is not merely hiding meaning. It is choosing a sentence that can still survive among pain, politeness, face, fear, hope, and self-protection.

## Related Work And Research Gap

Current answer:

> No single known study has already completed this whole research program.

Many adjacent literatures exist, and they are strong enough that HanmeiBench should not be framed as starting from zero. But none of them yet combines all of these pieces:

- Chinese literary and everyday indirect expression
- hidden psychological risk
- defense mechanisms such as `不敢問` and `不敢說`
- cultural restraint, face, filial relation, poetics, and politeness
- relationship and power pressure
- unspoken direct alternatives
- overinterpretation boundaries
- human reader / LLM / explainable rule-model comparison

The closest existing studies answer neighboring questions. HanmeiBench should position itself as the missing psychological-pragmatics layer.

### Theory Of Mind Route

| Year | Study | What it solved | What remains open for HanmeiBench |
| ---: | --- | --- | --- |
| 2022 | Sap et al., `Neural Theory-of-Mind?` | Showed that LLM social reasoning and false-belief behavior are not reliably solved by scale alone. | Does not test literary compression, Chinese indirectness, or self-protective silence. |
| 2023 | `Hi-ToM` | Tests higher-order mental-state reasoning: A thinks B thinks C knows something. | Recursive belief tracking is not the same as seeing why a speaker asks a harmless question first. |
| 2024 | `OpenToM` | Adds longer narratives, character traits, intentions, and psychological states. | Still narrative ToM, not Chinese poetic / everyday indirect expression. |
| 2024 | Strachan et al., `Testing theory of mind in large language models and humans` | Compares humans and LLMs on false belief, indirect requests, irony, faux pas, and related tasks. | Shows ToM-like behavior but not whether errors are human-like at the psychological-defense layer. |
| 2025 | Riemer et al., `Theory of Mind Benchmarks are Broken` | Argues that many static ToM benchmarks fail to test adaptation to new partners. | Supports the need for better design, but does not provide a Chinese literary-pragmatic taxonomy. |
| 2025 | `MoMentS` | Adds multimodal film scenarios for mental-state reasoning. | Useful later for gaze, pause, and silence, but not a text-first Hanmei-style benchmark. |
| 2026 | `CogToM` | Broadens ToM evaluation with human-cognition-inspired paradigms. | Still ToM-general, not focused on indirect expression as psychological risk management. |

Takeaway:

> LLMs can show strong ToM-like behavior, but ToM score is too coarse. HanmeiBench should ask which layer of understanding is succeeding or failing.

The key distinction is not:

> Does the model infer a hidden belief?

It is:

> Does the model infer why the speaker cannot safely ask the real question?

### Pragmatics And Indirect Meaning Route

| Year | Study | What it solved | What remains open for HanmeiBench |
| ---: | --- | --- | --- |
| 2024 | `SwordsmanImp` | Builds a Chinese conversational implicature dataset from `武林外傳`; shows Chinese implicature can be benchmarked. | Comedy dialogue and Gricean maxims do not cover grief, defense, classical poetry, or reception ethics. |
| 2024 | Cong, `Manner implicatures in large language models` | Tests whether models understand implications from marked or unusual wording. | Very close to "why this wording?", but not yet about `寒梅著花未` as emotional buffering. |
| 2025 | Ma et al., `Pragmatics in the Era of Large Language Models` | Surveys pragmatic datasets, evaluation methods, and research opportunities. | Confirms the field is forming; it does not solve the missing benchmark. |
| 2026 | `ALTPRAG` | Uses alternatives to test whether models infer speaker intention from one chosen utterance rather than another. | Strongly supports HanmeiBench's counterfactual design, but does not decompose defense, vulnerability, and culture. |
| 2026 | `CEI` | Tests emotional and pragmatic reasoning in complex social scenes: sarcasm, mixed signals, politeness, passive aggression, power, deflection. | Closest daily-life precedent, but not Chinese literary and not organized around `不敢問` / `不敢說`. |

Takeaway:

> Pragmatics research often asks what the speaker means. HanmeiBench asks why the speaker needed an indirect form at all.

That is a different target. For `寒梅著花未`, the interesting answer is not only:

> He misses home.

It is:

> He asks about plum blossoms because the real question may be too dangerous to ask at the first moment.

### Chinese Classical Literature Route

| Year | Study | What it solved | What remains open for HanmeiBench |
| ---: | --- | --- | --- |
| 2024 | `AC-EVAL` | Evaluates ancient Chinese knowledge, short-text understanding, and long-text understanding. | Primarily knowledge and comprehension, not hidden psychological risk. |
| 2024 | `WenMind` | Evaluates Chinese classical literature and language arts across prose, poetry, culture, and many task types. | Broad and useful, but not a hidden mental-state / defense-mechanism benchmark. |
| 2024 | `PoetMT` and related translation work | Benchmarks classical Chinese poetry translation quality. | Translation adequacy and elegance do not prove understanding of `不敢問`. |
| 2025 | `Fùxì` | Evaluates ancient Chinese text understanding and generation. | Still not focused on psychological pragmatics or why-not-direct reasoning. |

Takeaway:

> Classical Chinese benchmarks exist, but they mostly test language, knowledge, translation, or generation. HanmeiBench should test psychological pragmatics.

This means HanmeiBench can reuse classical Chinese evaluation infrastructure but should add fields that existing benchmarks usually do not require:

- `why_not_direct`
- `defense_mechanism`
- `reception_risk`
- `alternative_direct_expression`
- `acceptable_interpretations`
- `overinterpretation_boundary`
- `response_quality`

### Cognitive Science Route

Cognitive science already has a substantial LLM literature, but it points toward caution rather than closure.

| Year | Study | What it solved | What remains open for HanmeiBench |
| ---: | --- | --- | --- |
| 2021 | Schrimpf et al., `The neural architecture of language` | Shows that artificial language models can predict some human brain and behavioral language-processing data; next-word prediction is a strong organizing signal. | Brain-score similarity in language processing is not literary, affective, social, or existential understanding. |
| 2023 | Aher et al., `Using LLMs to simulate multiple humans` | Explores LLMs as simulated human participants. | Simulated participants are not real human readers with lived stakes and cultural memory. |
| 2023 | Dillion et al., `Can AI language models replace human participants?` | Gives a framework and caveats for using LLMs as participant substitutes. | Supports caution: LLMs should not replace the human baseline in HanmeiBench. |
| 2023 / 2024 | Mahowald et al., `Dissociating language and thought in large language models` | Separates formal linguistic competence from functional linguistic competence. | Excellent theoretical frame, but not operationalized for Chinese hidden-state inference. |
| 2024 | Binz and Schulz, `Turning large language models into cognitive models` | Shows LLMs can model some human cognitive behaviors. | Task-level fit is not full human literary cognition. |
| 2024 | Fedorenko et al., `Language is primarily a tool for communication rather than thought` | Argues language is primarily communicative and dissociable from thought. | Helps avoid equating fluency with understanding, but still needs concrete tests. |
| 2025 | Mancoridis et al., `Potemkin Understanding in Large Language Models` | Shows benchmark success can hide concept-application failures, including in literary techniques and psychological biases. | Highly relevant warning; needs adaptation to Chinese indirect expression. |
| 2025 | Xu et al., `Large language models without grounding recover non-sensorimotor but not sensorimotor features of human concepts` | Shows LLMs recover some abstract conceptual structure but have grounding limits in sensory/motor features. | The grounding question still has to be linked to homesickness, pain, waiting, loss, and embodied stakes. |
| 2025 | `Large Language Models Do Not Simulate Human Psychology` | Argues that small wording changes can produce non-human-like response patterns. | HanmeiBench should compare distributions and failure modes, not treat LLM answers as human data. |

Takeaway:

> Cognitive science does not force a binary answer. It suggests a layered answer: LLMs may have strong language-world competence, but human understanding includes body, time, memory, stakes, and social consequence.

For HanmeiBench, this means the human baseline cannot be replaced by LLM self-evaluation. The clean design is still:

1. Human readers
2. LLMs
3. Explainable rule model

Then compare disagreement patterns.

### Problems Temporarily Solved, But Not Well Enough

Some questions are partly solved in current research, but the solutions are too coarse for this idea.

| Temporarily solved question | Current answer | Why not enough | HanmeiBench response |
| --- | --- | --- | --- |
| Do LLMs have ToM? | They show ToM-like behavior on many tasks. | Static task success may rely on linguistic cues, templates, or dataset familiarity. | Measure layer-specific failure: literal, pragmatic, defense, cultural, reception-ethical. |
| Do LLMs understand implicature? | Partly, especially in strong models. | Choosing the hidden meaning is not the same as explaining why direct speech was avoided. | Ask `why_not_direct`, `social_risk`, and `reception_risk`. |
| Can LLMs handle classical Chinese? | Increasingly, yes, on benchmarked tasks. | Existing tasks often test knowledge, translation, or generation, not psychological risk. | Add hidden-state and defense-mechanism labels. |
| Can LLMs simulate human participants? | Sometimes useful as a proxy or cognitive model. | They are not real human samples and lack body, memory, vulnerability, and stakes. | Use LLMs as one arm, not as the ground truth. |
| Can benchmark scores show understanding? | They show behavior, not necessarily robust concept use. | Potemkin understanding is possible. | Add counterfactual controls and concept-transfer cases. |

### Core Unresolved Questions

These are the open questions HanmeiBench should own:

- Can a model distinguish `想問` from `不敢問`?
- Can a model distinguish `不能說` from `不敢說`?
- Can a model infer that a trivial surface question is psychologically protective?
- Can a model treat silence, topic shift, flowers, weather, read receipts, and vagueposting as pragmatic evidence?
- Can a model maintain multiple acceptable interpretations instead of forcing one hidden meaning?
- Can a model identify the direct sentence that was avoided?
- Can a model explain why that direct sentence would be risky?
- Can a model avoid over-psychologizing when evidence is thin?
- Can a model avoid false empathy: warm language that misses the actual risk?
- Can a model update a person-specific mental-state model through interaction, not only solve one static item?

### Refined Research Positioning

HanmeiBench should not be introduced as:

> A benchmark for whether LLMs understand literature.

That is too broad and too easy to misunderstand.

The better positioning is:

> A benchmark for whether LLMs can identify how humans use indirect language to protect themselves.

More formally:

> HanmeiBench evaluates hidden mental-state inference in Chinese indirect expression by testing whether models can infer the speaker's avoided direct expression, psychological defense, social and reception risk, cultural frame, acceptable interpretation distribution, and overinterpretation boundary.

This gives the project a clean contribution line:

1. It extends ToM beyond false-belief and story reasoning.
2. It extends pragmatics beyond "what is implied?" into "why was direct speech unsafe?"
3. It extends classical Chinese LLM evaluation beyond knowledge and translation.
4. It gives cognitive-science debates a concrete task where language, thought, grounding, and lived stakes diverge.

## Feasibility And Data Acquisition Plan

The deeper feasibility pass is now captured as a standalone source-and-method plan:

- Canonical plan: [docs/hanmeibench-data-acquisition-plan.md](../docs/hanmeibench-data-acquisition-plan.md)
- Core first principle: indirect expression is often risk management, not only hidden meaning.
- Core benchmark field: `why_not_direct`.
- Preferred v0.1 target: 60 items, not the earlier 24-item sketch.

The plan separates five source routes:

| Route | Role | Boundary |
| --- | --- | --- |
| Classical poetry anchors | Cultural calibration and high-compression examples | Use famous lines as anchors, not the main held-out test |
| Existing pragmatics and emotion datasets | Baselines and method references | Do not collapse HanmeiBench into generic implicature or emotion-cause detection |
| Controlled stimuli | Main publishable v0.1 data source | Research-team-authored variants reduce contamination, copyright, and privacy risk |
| Human-elicited daily indirect expression | Contemporary language grounding | Prefer scenario writing and consented explanations over social-media scraping |
| Modern literature, talks, and media | Theory inspiration and later extension | Do not release copyrighted text or transcripts without permission |

The recommended v0.1 dataset is:

| Category | Count | Purpose |
| --- | ---: | --- |
| Classical anchor | 12 | Calibrate culturally legible cases such as `寒梅著花未` |
| Classical homomorphic variants | 12 | Test whether models transfer the pattern beyond memorized famous lines |
| Daily conversation | 12 | Test ordinary self-protective indirectness |
| Digital social context | 12 | Test platform-era indirect emotion and attachment signals |
| Negative and contrast controls | 12 | Prevent rewarding over-psychologizing |

The strongest methodological decision is to make the dataset contrastive. A model should not only answer:

> What does this mean?

It should answer:

> Why might the speaker choose this indirect expression instead of the direct alternative?

That moves the task from ordinary nonliteral understanding into counterfactual pragmatic reasoning.

Key annotation fields should include:

- `surface_text`
- `context`
- `literal_meaning`
- `direct_alternative`
- `hidden_intent`
- `hidden_affect`
- `defense_mechanism`
- `why_not_direct`
- `social_risk`
- `reception_risk`
- `cultural_frame`
- `acceptable_interpretations`
- `overinterpretation_boundary`
- `response_quality_target`
- `license`
- `source_url`

The immediate next gate is not model running. The next gate is to draft the first 60-item candidate table with source route, license status, direct alternative, `why_not_direct` hypothesis, and negative-control pairing.

## Research Leads To Verify

These came from the conversation and should be verified before citation:

- Theory-of-mind testing in large language models and humans.
- OpenToM and higher-order ToM benchmarks.
- CEI-style benchmarks for pragmatic reasoning in complex emotional and social contexts.
- ALTPRAG or alternatives-based pragmatics evaluation.
- Implicature-aware prompting in human-LLM interaction.
- Manner implicature evaluation in LLMs.
- Chinese conversational implicature benchmarks such as SwordsmanImp.
- Functional theory-of-mind critiques of static ToM benchmarks.
- Multimodal ToM benchmarks such as MoMentS.
- Generated story prompting or StorySim-style contamination-resistant ToM evaluation.
- Neural theory-of-mind limits in large language models.
- LLM pragmatics and indirect-request interpretation.
- Studies on whether LLMs understand puns or only recognize joke-like patterns.
- Embodiment debates in cognitive science and AI language understanding.
- Predictive processing and the predictive mind.
- Semantic grounding and the symbol grounding problem.
- Chinese Room critiques and modern responses.
- Other minds problem and behavioral criteria for understanding.
- Trauma psychology concepts such as emotional avoidance, displacement, cognitive shielding, and defensive buffering.
- Meaning therapy, existential therapy, and awe psychology for large-scale reframing of suffering.

## Decision

Keep this as an `execution_ready` idea for a minimal research test, not a full project yet.

The next step is a literature check plus a small controlled fixture. The idea is strong because it connects AI, literature, pragmatics, and the definition of understanding; it is ready for a minimal experiment plan, but not for a larger project until the research leads are verified and the test rubric is made concrete.

## Planning Update Needed?

No immediate planning sync unless this becomes a scheduled paper-lab or experiment block.
