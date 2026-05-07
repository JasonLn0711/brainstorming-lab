# Problem Statement Normalization

Each idea should express the underlying problem in one normalized shape:

```text
Given X, optimize Y under constraints of Z.
```

The format makes ideas comparable. Two ideas with different surfaces may still
solve the same problem if their `given`, `optimize`, and `constraints` fields
match.

## YAML Shape

```yaml
problem_statement:
  raw: "AI triage"
  normalized: "Given multiple patients entering a clinical workflow, optimize prioritization and routing under constraints of urgency, fairness, safety, and limited resources."
  structure:
    given: "multiple patients entering a clinical workflow"
    optimize: "prioritization and routing"
    constraints:
      - urgency
      - fairness
      - safety
      - limited resources
normalization_status: normalized
```

If deterministic rules cannot infer the structure confidently,
`normalization_status` is set to `needs_review`.

## Friction-First Gate

Before treating a technique impulse as a mature idea, name the friction that
created the question. Acceptable friction sources include implementation,
bounded experiments, operations, field observation, lecture-time mental
execution, and paper-to-workflow simulation.

Then separate:

- problem: the real bottleneck, cost, risk, or blocked transformation
- symptom: the visible pain
- tool: a possible method or technology
- metric: the measurement proxy
- constraint: the boundary that shapes the answer

If the idea cannot name a bottleneck and a smallest falsifiable test, keep it as
a lower-maturity spark or structured note instead of promoting it because the
tool sounds exciting.

## Examples

AI triage:

```text
Given multiple patients entering a clinical workflow, optimize prioritization
and routing under constraints of urgency, fairness, safety, and limited
resources.
```

Hospital queue optimization:

```text
Given patients, clinicians, and rooms competing for limited capacity, optimize
queue order and resource assignment under constraints of acuity, wait time,
staff load, and safety.
```

Risk-based prioritization:

```text
Given many review candidates with uneven risk, optimize review order under
constraints of false negatives, reviewer capacity, evidence quality, and audit
needs.
```
