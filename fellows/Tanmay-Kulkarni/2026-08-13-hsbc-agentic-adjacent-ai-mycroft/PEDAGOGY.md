# PEDAGOGY — Week 18 Work Video (HSBC)

Film 6. **Work-derived lane** — built from this week's own case study, the same lane that
produced CommBank, Klarna and Lemonade. Deliberately *not* the repo-topic lane (Klarna "AI
Crossroads", `can-ai-catch-its-own-mistakes`, `bs-01-pick-and-scope`); the two are not mixed.

Built to `../../PROOF.md` and `../../PLAYBOOK.md`.

**Status: PHASE 2. GATE P signed twice — premise and narration (2026-08-18). Voice A/B pending.**

---

## Source material, and its condition

**Case study:** `../hsbc-case-study-DRAFT.md` — *"HSBC: Agentic-Adjacent AI in Investment &
Commercial Banking"*, 7 sections plus 4b, with a consolidated `## Sources` table.

**It is finished work.** `hsbc-CRITIQ-review.md` graded it *"a Minor Revision, not a Major one
and not a Reject"* — sourcing-solid, every load-bearing claim traced to a primary source. I
checked all six of its ranked fixes against the draft on disk: **all six are applied**,
including the CRITICAL cross-reference error and the two MAJOR structural additions.

So unlike the topic video, this film is not a rebuild of something thin. **The written work is
done and good.** The film's job is to carry its argument into video, and the argument is
unusually well suited to that.

Also available: `hsbc-rebuilt-brief.md` (post-verification corrections with reasoning shown)
and `hsbc-reference-implementation/` — a tested Intake → Assistant → Human Review Gate →
Apply & Test pipeline with 5 test files, mock data only.

## Thesis

HSBC disclosed four real, precisely-dated numbers across 2025–2026:

| Thread | Figure |
|---|---|
| Coding assistants | 60% faster unit testing · 5× faster vulnerability patching · 31,000 engineers enabled |
| Legacy application demise | 1,165 applications retired in 2025 · c.36% of a ~3,000 target |
| Organisational simplification | $1.2bn annualised savings realised, against a $1.5bn target |
| Severance and restructuring | $1.8bn expected through 2026 |

**HSBC has never stated that any of these causes any other.** The case study's central
discipline is keeping them apart. The film's is the same, and that refusal *is* the content:
the story a viewer wants — "AI made HSBC leaner" — is the one the disclosures do not support.

The teach is therefore a **reader's instrument**, not a fact about HSBC: how to read a
company's AI announcements without assembling them into a story the company never told.

## The framework — four questions for any corporate AI claim

Shown as a structure before any example. Reusable on any earnings call, any vendor case study,
any "AI transformed X" headline.

| # | Question | Fails when |
|---|---|---|
| **1** | **Who drew the line — the company, or me?** | Two real numbers sit near each other and the reader supplies the causal arrow |
| **2** | **Is the outcome precise and the mechanism missing?** | Rich metrics, no disclosed tool, model, workflow or baseline |
| **3** | **Does the same number mean two different things?** | One figure, two contexts, and nobody notices the switch |
| **4** | **Which word does the company use here — and where else do they use it?** | A term is applied in one place and not in another, and nobody checks |

Question 1 is the spine. **Question 3 is the one that catches professionals.**

**Question 4 was rewritten at Gate P.** It first read *"where does the company refuse to use its
own word?"* — which asks a viewer to notice an **absence**, and that needs the company's whole
corpus, not the one document in front of them. Interesting to think about, bad to run: exactly
the axis PROOF warns about, one that sounds good and transfers badly. Reframed from absence to
**comparison**, it is mechanical: note the exact term used, then search the company's own
materials for it elsewhere. HSBC is a clean demonstration — "agentic AI" appears for financial
crime and never for coding, and you find that by looking.

## Why this is not a retrofit

PROOF's reverse-engineering tell is categories mapping one-per-example. These don't — each
question has a documented HSBC instance *and* at least one of them has a documented case of
real published journalism getting it wrong:

| Q | HSBC instance | Documented failure in the wild |
|---|---|---|
| 1 | §5.5 and §6.5 — no disclosed connection between coding productivity and headcount or app demise | Zacks (on Bloomberg) framed "up to 20,000 job cuts, 10% of the workforce" as *"tied to AI-driven transformation plans"* — an undecided review, presented as AI-connected |
| 2 | §6.1 — 60%/5×/31,000 disclosed; no tool, model, workflow or baseline | — |
| 3 | §6.4 — **$1.8bn means severance (FY2024) and, separately, Hang Seng cost reallocation (FY2025)** | **kingy.ai and metaintro.com both conflated the $1.8bn severance figure with "AI investment"** |
| 4 | §6.3 — HSBC says "agentic AI" for the Google Cloud financial-crime system, never for its coding tools | — |

That two independent outlets made the *same* error on the *same* figure is the strongest
possible evidence the instrument is worth having. It is not a hypothetical failure mode.

## Falsifiability — and the case study supplies it

The film's question 4 rests on the agentic/assistive distinction. **The case study explicitly
flags that this is an inference it draws, not an HSBC statement**, and goes further (§6.3): a
future HSBC disclosure could describe the coding assistants in agentic terms *without
contradicting anything currently on the record*, and the distinction "would then need
revision, not defense."

That is a genuine, stated falsification condition on the film's own analysis, authored before
the film existed. It goes on screen — it is the most credible thing the film can do.

**Second edge case:** §6.2's 20,000-vs-31,000 developer count. The case study reconciles them
as one population measured twice, then refuses to call that certain. An instrument that can
say "this is my best reading, not a fact" is the point.

## Friction — the viewer has to resolve this

Four true numbers from a company's own filings, sitting next to each other, and the obvious
reading is forbidden. So what is a reader *allowed* to conclude?

The instinctive answers are both wrong. "Assume the connection" is what two outlets already did
with the $1.8bn. "Assume no connection" is equally unfounded — HSBC hasn't denied it either.
The honest position is narrower and less comfortable than either, and getting the viewer to sit
in it is the friction.

## Viewer task — a scaffold, not "read critically"

Take any AI announcement — an earnings call, a vendor page, a press release.

1. List the numbers it gives you, one per line.
2. Draw the arrows **you** believe connect them.
3. Go back to the source and delete every arrow the company didn't state itself.
4. Look at what's left. That's what you actually know.

**Good result:** most of your arrows disappear. **Bad result:** all of them survive — you
either picked an unusually explicit source, or you're reading your own arrows back as theirs.

## Act structure — to draft in Phase 2

Must share no shape with the previous five films: no ASK→RESULT cold open (CommBank), no J-curve
essay spine (Klarna), no scaffold/production interleave (Lemonade), no
one-instrument-three-times-with-a-reversal (Film 4), no distinction-pulled-apart (Film 5).

Working shape: **"the line you don't draw."** Four numbers laid on a table; the film's motion is
*withholding* connections rather than building toward a synthesis. Every prior film earned its
payoff by joining things. This one earns it by refusing.

Per PLAYBOOK §1c, beat 2 must name the subject in plain words before any abstraction, and per
§1a the tone arc gets mapped before a line is written.

## Design constraint carried forward from Film 5 — read this before scripting

Film 5 shipped with **16 of 17 beats as Remotion cards (94%)**, against the toolkit's ~40%
guidance, and PROOF Phase 3 named it the film's single biggest weakness with a
`[RESHOOT/NEW SOURCE]` tag. Four verified components now exist and are reusable
(`ClaudeFourQuestionBoard`, `ClaudeSplitComparator`, `ClaudeArtifactCardFull`,
`ClaudeTitleOutroFull`) — which makes it *easy* to repeat that mistake.

**This film must not.** Treat motion variety as a Phase 2 requirement, not a Gate V surprise.
The material actively supports it: four parallel numeric threads and a $1.8bn collision are
natural Manim territory, and the reference implementation's pipeline is a diagram, not a card.
Target: no single language above ~50% of beats.

## Evidence discipline

| Claim | Source | Calibration |
|---|---|---|
| 60% faster unit testing, 5× faster patching | HSBC FY2025 Annual Results transcript, 25 Feb 2026, Elhedery, quoted | HSBC's own words; self-reported, unaudited (§6.7) |
| 31,000 engineers enabled | Same call | Reconciled against an earlier 20,000 figure; §6.2 flags the reconciliation as a reading |
| 1,165 applications demised, c.36% | FY2025 Presentation, Slide 4 fn 4 | HSBC's published figures, not derived |
| $1.2bn realised / $1.5bn target | FY2025 transcript, Kaur, quoted | HSBC's own words |
| $1.8bn severance | **FY2024** transcript, 19 Feb 2025, Elhedery, quoted | **FY2024 only.** The FY2025 $1.8bn is a different thing and is excluded entirely (§6.4) |
| "agentic AI" used for financial crime, not coding | Two disclosures ~4 months apart | **An inference this case study draws**, labelled as such, with a stated falsification condition |
| Secondary outlets conflated $1.8bn with AI investment | kingy.ai, metaintro.com | Named in §6.4. **Verify both independently before they go on screen** |
| "20,000 job cuts tied to AI" | Zacks, on Bloomberg | Explicitly an undecided review, not an HSBC plan (§6.6) |

**Not claimed anywhere:** that AI caused the headcount reduction; that AI caused the application
demise; that the four figures corroborate one another; that HSBC's coding assistants are or are
not agentic as a matter of HSBC's own statement.

**Every figure is self-reported and unaudited** (§6.7). The film says so.

## Persona / register

Carried forward from Film 5, where each was resolved and documented: presenter **Tanmay
Kulkarni from Humanitarians AI**, voice **`am_onyx`** (the toolkit rejects `af_kore`), brand
**`claude-hai`** → kicker `Irreducibly Human`, chip `@HumanitariansAI`. Pragmatist register.

Plain language throughout, per the author's Gate P direction on Film 5: a general audience
should follow it. Banking vocabulary needs the same treatment the Beers Criteria got — explain
the term in the sentence that uses it.

---

## TONE POLICY — set at Gate P, governs every beat

**Nothing in this film reads as criticism of HSBC, and nothing reads as criticism of the case
study.** This is not a softening of the argument; it makes the argument better.

**HSBC is the good example, not the target.** They disclosed precise, dated, individually
sourced figures, and they were careful with their own language — "assistive tools," not
autonomous agents. There is no HSBC failure in this film. **The whole failure is downstream, in
what a reader adds.** That reframe sharpens the teach from "watch out for companies" to "watch
out for what you supply yourself" — which is both truer to the evidence and a more useful skill.

**The two outlets are named, and framed as evidence that the trap is well-made.** Not
"kingy.ai and metaintro.com were careless" but "two independent outlets drew the same
connection, which tells you how natural that connection feels." The point is the strength of
the trap, never the competence of whoever fell into it. Same courtesy the film extends to its
own author, whose flagship example in Film 5 failed on air.

**Consequence for the ending.** The film cannot land on "so don't trust AI announcements." It
lands on what a disciplined reader is *allowed* to conclude — narrower, more honest, and more
useful than either credulity or blanket suspicion.

---

## GATE P

**VERDICT: PASS** — premise reviewed and signed off by the author, 2026-08-18. Cleared to script.

**Phase 1 gate question:** the method a viewer walks away able to apply is — *who drew the
line, the company or me; is the outcome precise while the mechanism is missing; does the same
number mean two things; which word do they use here and where else do they use it?* Is that the
actual teach, or just the topic?

**Author's answer:** confirmed as the teach, with a request for a second opinion on whether it
qualifies.

**Second opinion, recorded because it changed the framework.** Questions 1–3 pass PROOF's test
outright: a viewer with one unfamiliar document can run all three tomorrow, and Q3 is purely
mechanical. **Question 4 as originally drafted did not pass** — asking a reader to notice an
absence requires a corpus, not a document, so it was the most interesting axis and the least
usable. Rewritten as a comparison (*which word here, and where else?*) it becomes runnable.
Verdict: a teach, on four legs rather than three-and-a-half.

### Author decisions at this gate

1. **The reference implementation is IN.** It gets a late beat. Its `HumanReviewGate` ships with
   **zero default review criteria** and raises `ValueError` unless a decision function is
   supplied — because no HSBC source describes a code-specific approval gate, only a general
   bank-wide governance principle. Inventing a labelled placeholder would have implied a shape
   of answer (severity-based? threshold-based?) the record doesn't support. That is question 1
   expressed as code: **the line HSBC didn't draw, left undrawn in the software.** It earns its
   place because it is the framework applied by an engineer rather than a reader.
2. **Both outlets are named** — kingy.ai and metaintro.com — under the tone policy above.
   **Neither goes on screen until independently verified.** Right now the conflation is §6.4's
   finding, not mine, and this film cannot repeat the error it documents.


---

## GATE P — NARRATION

**VERDICT: PASS** — narration reviewed by reading aloud, Tanmay Kulkarni, 2026-08-18. Cleared to
audio.

Reviewed against `READ-ALOUD.md` v2 (the ledger structure), 16 beats, 1,553 words, ~7:21.

**Structure note.** Narration v1 was written to a four-question framework and **scrapped before
this gate** — it was the same *form* as Film 5 (`bs-01-pick-and-scope`): four numbered questions, a
board at ~14s, applied in order, four-step viewer task. A viewer watching both back to back would
have seen one container twice. The film was rebuilt on a **two-column ledger** audited line by
line. Both v1 files are kept as `.bak`.

**Standing lesson, recorded in `SCRIPT.md`:** compare the *form* against the previous film, not the
argument. Rhetorical motion is invisible to a viewer.

### Voice — open at this gate

Film 5 used `am_onyx` on the reasoning that narration wants a narrator. The toolkit's own mapping
assigns `af_bella` to the hai persona and Pragmatist register, which is what this film is; Onyx is
the nbb/Liam default. The two arguments point opposite ways, so an A/B of B01 and B09 in both
voices was generated for the author to judge by ear. **Recorded here because the choice is
aesthetic and cannot be settled from documentation.**
