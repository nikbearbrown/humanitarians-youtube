# Script — Why the Most Dangerous Pipeline Is the One That Runs Perfectly

**Series**: Computational Skepticism for AI  
**Episode**: Why the Most Dangerous Pipeline Is the One That Runs Perfectly  
**Candidate**: Candidate 29  
**Source**: *Computational Skepticism for AI*, Chapter 9 (*Delegation, Trust, and the Supervisory Role*)  
**Register**: Plain (explain the epistemic mechanism, then stop)  
**Narrator**: Liam (Kokoro `am_onyx`, in for Bear)  
**Palette**: Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`

---

### B00 — Brutalist Hesitant Writer Cold Open
**Visual**: Writer types the naive framing in serif type on cream ground, pauses in hesitation, deletes the misconception with a terracotta strike, and writes the real question.  
**Typing text**:
```
When an AI pipeline runs with zero errors,
doesn't that mean
it's working safely?
```
**Hesitate & Replace**:
- `triggerWords`: "it's working safely?"
- `replacementWords`: "it's just running unsupervised?"

**Narration (Liam)**:
> When an automated AI pipeline executes from start to finish with zero errors, we assume the system is reliable. But a crash only tells you code broke. A green checkmark can mean something much worse. Let's trace why.

---

### B01 — Stakes: The Loud Failure vs The Silent Failure
**Move**: 1 Stakes  
**Visual**: Manim diagram comparing loud software failures (red crash icons, stack traces, halting execution) against silent epistemic failures (unbroken green pipeline flow).  
**Narration (Liam)**:
> In software engineering, a broken system announces itself. A missing parameter throws a type error; an unreachable API returns five hundred; a corrupted payload crashes the parser. The pipeline stops. The developer is alerted immediately.

---

### B02 — The Wrong Guess: Green Equals Correct
**Move**: 2 Wrong Guess  
**Visual**: Manim illustration of an automated pipeline with glowing green status checks at every node, labeled "Exit Code 0: Success", then struck with a terracotta warning marker.  
**Narration (Liam)**:
> The intuitive assumption is that an AI pipeline works the same way: if execution completes with exit code zero and passes schema validation, the job succeeded. But language models do not fail by crashing. They fail by generating fluent nonsense that satisfies every syntactic rule.

---

### B03 — The Delegation Map: Items 1 to 4
**Move**: 3 Mechanism (Part 1: The Engineering Contract)  
**Visual**: Manim layout of the Delegation Map. The top four items light up: Task Definition, Input Contract, Output Contract, and Tool Inventory.  
**Narration (Liam)**:
> To see why, look at how we document pipelines. The first four items of any delegation map are standard engineering: the task definition, the input schema, the output format, and the tool inventory. These four items define execution.

---

### B04 — Why Items 1 to 4 Fail Loudly
**Move**: 3 Mechanism (Loud Failures)  
**Visual**: Manim animation showing an invalid JSON schema input striking Box 2 and an unauthorized tool call striking Box 4, both triggering immediate red halt barriers.  
**Narration (Liam)**:
> If any of these first four pieces fails, it fails loudly. Feed invalid JSON into step two, and the validator halts the run. Omit a required database credential, and the network connection drops. The system refuses to proceed.

---

### B05 — The Anchor Plant: The Six-Stage Pipeline
**Move**: 4 Anchor (Planted)  
**Visual**: Manim diagram of a horizontal six-stage pipeline: Ingestion, Retrieval, Model Inference, Formatting, Plausibility Audit, and Action Dispatch. A glowing token enters containing a fluent but factually inverted assessment.  
**Narration (Liam)**:
> Now trace a six-stage automated clinical triage pipeline. A patient symptom report arrives. Context is retrieved. A model infers the clinical assessment. An action plan is formatted. Everything looks standard, but there is a fatal factual inversion inside.

---

### B06 — The Kinetic Move: Tracing Through 1 to 4
**Move**: Kinetic Move (`trace`)  
**Visual**: Manim animation tracing the inverted token through Stages 1, 2, 3, and 4. At each step, syntactic validators pass and green checkmarks illuminate brightly.  
**Narration (Liam)**:
> The token enters stage one: valid format, green check. Stage two: context retrieved, green check. Stage three: fluent clinical prose generated, green check. Stage four: strict JSON schema validated, green check. Every engineering monitor lights bright green.

---

### B07 — The Omission: Items 5 to 8
**Move**: 3 Mechanism (Part 2: The Supervisory Additions)  
**Visual**: Manim schematic expanding the Delegation Map to reveal the bottom four items: Plausibility Check, Failure Routing, Audit Trail, and Sign-Off Authority — shown grayed out and bypassed.  
**Narration (Liam)**:
> Here is the danger. The pipeline has items one through four, but completely omits items five through eight: the plausibility check, failure routing, the audit trail, and sign-off authority. Those four are the supervisory additions.

---

### B08 — Why Items 5 to 8 Fail Silently
**Move**: 3 Mechanism (Silent Failures)  
**Visual**: Manim animation showing the lack of supervisory gates. The toxic token glides effortlessly past empty supervisory checkpoints.  
**Narration (Liam)**:
> A pipeline missing items one through four is broken: it cannot run. But a pipeline missing items five through eight is unsupervised: it runs beautifully. Without an independent semantic check, a lethal medical hallucination sails straight through the gate.

---

### B09 — The Anchor Payoff: Downstream Delivery
**Move**: 4 Anchor (Paid Off)  
**Visual**: Manim payoff: Stage 6 dispatches the inverted dosage directly into production. The recipient node flashes with a terracotta alert: "Error Discovered Downstream."  
**Narration (Liam)**:
> Because no failure routing caught the contradiction, no audit trail recorded the generation prompt, and no named clinician was forced to sign off, the action executes automatically. The error is not discovered by a developer in a log. It is discovered by the patient it harms.

---

### B10 — The One Flag: Testable Handoffs
**Move**: One Flag (Testable Contract)  
**Visual**: Manim callout focusing on the handoff boundary between human and AI, highlighting the single non-negotiable property: testability.  
**Narration (Liam)**:
> Here is the load-bearing rule. A supervisory check is only real if its handoff condition is testable. Declaring that a human must review the output is an empty gesture if the pipeline gives them three seconds to click approve without an independent verification standard.

---

### B11 — Both Directions
**Move**: 5 Both Directions  
**Visual**: Manim split screen: Left side shows "Syntactic Overconfidence" (all green checks, zero semantic safety). Right side shows "Rubber-Stamp Fatigue" (human reviewer overwhelmed by meaningless review clicks).  
**Narration (Liam)**:
> Both failure modes matter. If you rely solely on syntactic pipeline checks, you mistake execution for correctness. But if you demand human review without testable handoff criteria, you build rubber-stamp fatigue where humans mindlessly approve toxic outputs.

---

### BCRY — Carry-Out Line
**Move**: 6 Carry-Out Line  
**Visual**: Remotion `WantQuote` component. Cream background, warm ink serif type, terracotta accent.  
**Quote**: "The failure that costs you is the one that does not stop the pipeline."  
**Narration (Liam)**:
> The failure that costs you is the one that does not stop the pipeline.

---

### BHTF — Your Turn Handoff
**Move**: Your Turn Audit Prompt  
**Visual**: Remotion `ClaudeComposerAsk` component.  
**Narration (Liam)**:
> Your turn. Here's the prompt — read it with me. Take the most critical automated AI pipeline in your system. Map its steps against items one through eight. Where are the plausibility checks, the failure escalation routes, the audit trail, and the named human sign-off? If any of those four are missing, what stops a fluent, dangerous output from executing directly into the real world? Liam, in for Bear.

---

### BOUT — Outro CTA
**Move**: Series Outro  
**Visual**: Remotion `OutroCTA` component.  
**Narration (Liam)**:
> Why the Most Dangerous Pipeline Is the One That Runs Perfectly. Liam, in for Bear.
