# Real-World Pressure Tests

Real-world pressure tests turn an abstract idea into a small field game.

The goal is not to make ideas more entertaining for its own sake. The goal is
to expose the point where an idea breaks when it meets messy reality.

## Rule

A good pressure test is:

- concrete enough that a person can imagine running it this week;
- playful enough that it reveals behavior, friction, and edge cases naturally;
- bounded enough that it does not become a full project;
- measurable enough to confirm, revise, or kill a bottleneck hypothesis;
- safe enough that it does not collect sensitive evidence or create external
  harm without governance.

Use a pressure test before treating an idea as `research_candidate` or
`execution_ready`.

## Template

```yaml
real_world_pressure_test:
  name: ""
  setting: ""
  playful_frame: ""
  target_bottleneck: ""
  expected_failure_modes:
    - ""
  smallest_test:
    - ""
  metrics:
    - ""
  human_decision:
    - ""
  revise_or_kill_condition: ""
  safety_boundary:
    - ""
```

## Design Pattern

Start from this question:

> What tiny real-world scene would make this idea embarrass itself?

Then make that scene observable.

Do not ask only whether the tool works. Ask whether it survives a concrete
case that includes time pressure, visual noise, confusing context, human
judgment, cost, fatigue, missing data, ambiguous labels, or deployment limits.

## Example Pressure Tests

### Bicycle ReID Treasure Hunt

Idea type: computer vision, ReID, tracking, identity persistence.

Field game: find one registered bicycle in a dense NTU-style bike lot.

Failure mode:

- detector finds bicycles but not identity;
- many bikes look nearly identical;
- stickers, locks, baskets, or scratches are occluded;
- night, rain, blur, or compression damages embeddings.

Smallest test:

- register one bicycle with 8 to 12 photos;
- collect or simulate 50 to 100 candidate bicycle crops;
- rank candidates with DINOv2, CLIP, or a ReID model;
- add location and time priors;
- ask a human to confirm from top-k candidates.

Metrics:

- top-1, top-5, and top-10 retrieval rate;
- candidate reduction from total bikes to shortlist;
- human confirmation time;
- accuracy drop under partial views and near-duplicate bikes.

### Backpack Doppelganger Test

Idea type: object identity, campus assistance, human-AI search.

Field game: identify one backpack among many similar black backpacks in a
classroom or library-like scene.

Failure mode:

- generic object detection is too coarse;
- black bags have weak visual distinction;
- personal items move or are hidden;
- privacy risk appears if people are included.

Smallest test:

- use only user-owned backpack photos;
- crop out people;
- rank candidate bag crops by embedding similarity;
- compare vision-only against a visible tag or sticker.

Metrics:

- top-k retrieval;
- false-match rate among similar bags;
- improvement from physical marker;
- human review time.

### Lost Umbrella Rain-Day Drill

Idea type: multimodal identity, low-quality vision, everyday object recovery.

Field game: find one umbrella from a set of similar umbrellas under rainy,
low-light, wet-surface conditions.

Failure mode:

- color shifts under lighting;
- folded umbrellas lose shape cues;
- many umbrellas share common colors;
- water and glare degrade images.

Smallest test:

- register the target umbrella in dry and wet states;
- compare top-k retrieval under indoor, outdoor, and low-light photos;
- test whether a small sticker or QR marker changes the result.

Metrics:

- retrieval quality by lighting condition;
- visual-only versus marker-assisted gain;
- number of false near-duplicates.

### Queue Confusion Test

Idea type: human behavior understanding, tracking, anomaly detection.

Field game: detect whether a person is queueing, cutting, leaving, or returning
in a crowded food-court-like line.

Failure mode:

- single-frame detection cannot infer intent;
- people occlude each other;
- temporary movement looks like rule-breaking;
- social context is ambiguous.

Smallest test:

- use short staged clips with consenting participants or synthetic sketches;
- compare object detection only against tracking plus temporal rules;
- ask a human to label whether the AI explanation is plausible.

Metrics:

- event-level precision and recall;
- false accusation rate;
- time needed for human review;
- explanation usefulness score.

### Desk Object Memory Game

Idea type: world model, persistent state, personal workflow assistant.

Field game: detect which object on a desk changed location between two work
sessions.

Failure mode:

- viewpoint changes hide the true change;
- lighting changes create false differences;
- clutter creates false positives;
- the system confuses object identity with object category.

Smallest test:

- take before/after desk photos;
- move one known object;
- compare detection-only, embedding matching, and human confirmation;
- repeat under changed lighting and camera angle.

Metrics:

- correct changed-object identification;
- false changed-object count;
- time-to-human-confirmation;
- robustness under viewpoint shift.

### Field-Guide For Agentic Research

Idea type: AI research workflow, claim verification, paper writing.

Field game: give an AI research assistant one messy paper folder and ask it to
produce a claim ledger under time limit.

Failure mode:

- citations drift;
- claims outrun evidence;
- the assistant hides uncertainty;
- useful negative results are dropped.

Smallest test:

- pick one paper folder;
- ask for five claims, evidence paths, and missing-evidence flags;
- manually audit the output;
- record where the assistant overclaims.

Metrics:

- unsupported-claim rate;
- missing-evidence recall;
- audit time;
- number of useful revise/kill decisions.

## Safety Boundary

Pressure tests should stay small and governed.

Prefer:

- user-owned objects;
- consented or synthetic scenes;
- local-only images and embeddings;
- cropped objects instead of identifiable people;
- short tests that answer one bottleneck question.

Avoid:

- covert surveillance;
- identifying unrelated people;
- collecting sensitive raw evidence;
- turning a playful test into production monitoring;
- publishing images, tracks, or identity data without explicit consent.

## Promotion Check

Before raising maturity, ask:

- Does the idea have a named pressure test?
- Does the pressure test reveal a likely real-world failure mode?
- Is the smallest test observable within a bounded session?
- Is there a metric or human decision?
- Is there a revise-or-kill condition?
- Is the safety boundary explicit?

If the answer is no, keep the idea lower maturity or add the missing pressure
test before promotion.
