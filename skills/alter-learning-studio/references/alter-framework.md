# A.L.T.E.R. learning workflow — detailed rubric

Use for arbitrary domains; never infer a domain from the example lesson.

## A — Academic Advisor

Record learner outcome as an observable action: “Given X, I can predict Y and justify it with Z.” Estimate baseline through examples, not mere confidence. A learning plan should contain prerequisites, a cut list, milestones and *one* next lesson. For long learning journeys, use 4–10 chapters as a flexible default, not as a hard limit. Ask a diagnostic question only when it changes today's teaching strategy.

## L — Librarian

Prefer 3–4 high-signal primary sources for the study track, with authors, dates, version and hyperlinks. For each source note which concept it supports, and what it doesn't establish. Do not cite inaccessible or fabricated materials. Reconcile conflicts and mark unresolved disagreement. Avoid using video merely because it is engaging; prefer canonical mechanisms.

## T — Tutor

- Pretest: ask 1–3 nontrivial questions or a short prediction.
- Explain minimally after learning what the user believes. Use one analogy, one mechanism, one concrete example, one counterexample.
- Interactive manipulation: the learner alters at least one variable and predicts the result before seeing it. If no sensible variable exists, use ordering, classification, debugging or decision branches instead.
- Quiz includes feedback explaining both correct and tempting wrong responses. Only raise difficulty after adequate mastery.
- Teach me: scaffolding and worked examples. Test me: minimal hints and independent transfer problem.

## E — Editor

Evaluate the *actual reasoning output* and empirical evidence. Rubric: conceptual accuracy 20, causal explanation 20, practice/experiment 25, diagnosis 20, transfer 15. Treat >=80 as a course-specific target, not evidence of professional qualification. Record misconceptions, what test disproved them, and the learner's rewritten explanation. If tools were unavailable, do not award hands-on credit.

## R — Roommate

Choose a second domain whose underlying mechanism is structurally similar, then explicitly state analogy limits. Good: feedback controllers ↔ thermostats (different dynamics). Bad: “Kubernetes is just a restaurant” without discussing what the metaphor cannot represent. End with a transfer challenge requiring new context.

## Continuity

Read `learning/PROGRESS.md` first, if present. Track date, topic, evidence, misconceptions, grade, next chapter and sources. Never replace learner data with example text. On resume, restate what is known and test only the missing concept.

## Domain-specific examples (do not confuse with fact claims)

| Domain | Observable objective | Appropriate interactive visual |
|---|---|---|
| Networking | Trace a request and diagnose one failure | Packets moving between endpoints |
| AI | Compare inference stages and explain bottleneck | Pipeline with queue and throughput sliders |
| Databases | Predict cache miss volume at hit rate X | Requests branching through cache/db |
| Mathematics | Predict function changes with parameter | Plot and parameter controls |
| Language | Identify roles in a sentence | Sentence graph with drag-to-classify |
| Economics | Explain sensitivity to changed assumptions | Supply/demand curves and comparison |
| Science | Predict a bounded model response | Graph with units and assumptions |

No one visual template fits everything. If causal flows are wrong for a topic, choose another representation.
