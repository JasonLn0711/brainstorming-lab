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

- 12-20 stimuli
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

## Research Leads To Verify

These came from the conversation and should be verified before citation:

- Theory-of-mind testing in large language models and humans.
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
