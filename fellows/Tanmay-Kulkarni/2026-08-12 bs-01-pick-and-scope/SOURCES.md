# SOURCES — role/persona specification

## The theme, stripped of the assignment

**How precisely do you have to describe your own job before a generic prompt becomes useful for it?**

That is what the source draft is about once the course, the point values, and the Botspeak vocabulary
are removed. It needs no chapter citations, so it is unblocked by the missing book.

## What is published

Both current papers are **preprints — not peer-reviewed.** Label as such on screen.

### 1. Xiao et al., "When Does Persona Prompting Actually Help?"

arXiv [2605.29420](https://arxiv.org/html/2605.29420), 28 May 2026. Preprint.

Finds a **tradeoff, not an improvement**:

| Metric | Baseline | Role-prompted (hybrid retrieval) |
|---|---:|---:|
| Expertise depth | 3.638 | **3.923** (+0.285) |
| Clarity | **4.896** | 4.550 |

> "role prompting performs best on advisory questions and in domains such as medicine and psychology"

> "baseline prompting performs better on conceptual and explanatory questions in finance, legal,
> science, and technology domains"

**Two things worth noting.** The draft's worked example is a *clinical pharmacist* — medicine, the
domain where the research says role prompting actually works. And the domains where it reportedly
*hurts* include finance, which is the lane of our own case-study series.

**Stated limitations:** synthetic role-structured benchmark rather than real user traffic; limited model
set; automated LLM judging is imperfect.

### 2. Hu, Rostami & Thomason, "Expert Personas Improve LLM Alignment but Damage Accuracy"

arXiv [2603.18507](https://arxiv.org/pdf/2603.18507), March 2026. Preprint (PRISM).

The title is the finding: expert personas improve alignment with human expectations and damage factual
accuracy.

**`[VERIFY]` CLEARED 2026-08-18** — read out of the paper's own HTML (Figure 1b, investigation
section) at [arxiv.org/html/2603.18507v1](https://arxiv.org/html/2603.18507v1), after the PDF
fetch returned unrenderable content. The figures were previously sourced only to secondary
coverage; they are now first-party.

| MMLU condition | Accuracy |
|---|---:|
| Baseline | **71.6%** |
| Minimum persona | **68.0%** |
| Long persona | **66.3%** |

Verbatim, on length monotonicity: **"Longer persona prompts damage more."** Screen-eligible
with a `PREPRINT` label.

> ⚠️ **Do not use the paper's stated mechanism.** The extracted explanation for *why* longer
> prompts hurt was internally inconsistent (it read as longer prompts interfering *less* while
> shorter variants are preferable). The numbers and the quoted sentence above are solid; the
> causal explanation is not, and must not be narrated.

**Why this matters for the film:** the draft tells students to "tighten until the description
uniquely fits you." The research says tightening is right — and adds a reason the draft never
gives, that length itself carries a measured accuracy cost. Convergence, not contradiction.
This is beat B11.

### 3. Secondary coverage (not citable as evidence)

- [Search Engine Journal — "Research Shows Where Persona Prompting Works And When It Backfires"](https://www.searchenginejournal.com/research-you-are-an-expert-prompts-can-damage-factual-accuracy/570397/)
- [learnprompting.org — Role Prompting](https://learnprompting.org/docs/advanced/zero_shot/role_prompting)

## The gap in the literature — where our own work contributes

**Neither paper separates two different things that both get called role prompting:**

| | What it is | Example |
|---|---|---|
| **Persona-as-expertise-claim** | A claim about who the *model* should be | "You are a senior clinical pharmacist." |
| **Role-as-task-context** | A specification of the *situation the work happens in* | "Night shift, reviewing discharge medications before the patient leaves the unit." |

Xiao et al. explicitly does not distinguish them — it "treats expert personas uniformly as prompting
interventions." The published measurements are all of the first kind.

**The source draft's instrument is entirely the second kind.** Its passing example — *"Clinical
pharmacist on a night shift reviewing discharge medications before a patient leaves the unit"* — supplies
shift, task, artifact, and deadline. It is not asserting the model has expertise; it is stating the
situation.

So the draft's advice is not contradicted by the literature. **It is unmeasured by it.** That is a
cleaner and more honest position than "the draft is wrong," and it is a real gap our experiment can
address.

## Botspeak / course sources — for the citation layer only

| Claim | Source | Status |
|---|---|---|
| Primary text is *Botspeak: **The Nine Pillars** of AI Fluency*, Nik Bear Brown | [Course repo README](https://github.com/nikbearbrown/INFO-7375-Computational-Skepticism-and-AI), Primary Texts | ✅ Confirms the name is **Pillars**, not "Capacities" |
| The nine pillars: Strategic Delegation, Effective Communication, Critical Evaluation, Technical Understanding, Ethical Reasoning, Stochastic Reasoning, Learning by Doing, Rapid Prototyping, Theoretical Foundations | [humanitarians.ai/botspeak](https://www.humanitarians.ai/botspeak) | ✅ Two independent sources |
| Interaction Modes: Automation, Augmentation, Agency | Both above | ✅ Two independent sources |
| Nine Pillars taught in **Module 1**; course runs **Modules 1–15** | Course repo README | ✅ |
| "the Loop — predict, decide, verify" | — | ❌ Not located in either source |
| "the five Specification components" (Intent, Constraints, Success Criteria, Exclusions, Output Format) | — | ❌ Not located in either source |
| Assignment rubric: 100 pts, 80/20, six deliverables, 21/16/11 | — | ❌ No handout found anywhere |

Bound: the book itself was not read. ❌ above means **not verifiable from reachable sources**, not
"does not exist."
