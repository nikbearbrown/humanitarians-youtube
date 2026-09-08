# PEDAGOGY — Week 18 Topic Video (working title TBD)

Film 5. **Repo-topic lane** — rebuilt from
`claude-for-artificial-intelligence/claude-liam-bs-01-pick-and-scope` in the `humanitarians-youtube`
repo, the same lane that produced the Klarna "AI Crossroads" reel and Film 4
(`can-ai-catch-its-own-mistakes`). Deliberately *not* the work-derived lane (CommBank, Lemonade,
HSBC); the two are not mixed.

Built to `../../../PROOF.md` and `../../../PLAYBOOK.md`.

**Status: PHASE 2 COMPLETE. GATE P signed (premise and narration). Experiment run. Previz compiled
at 3840×2160. Awaiting recompile against revised audio, then Phase 3 review.**

---

## How this topic was selected

Randomly, from the 136 open topics in `claude-for-<topic>/` — folders holding a beat sheet with no
production artifacts. Method and full inventory in [../INVENTORY-SUMMARY.md](../INVENTORY-SUMMARY.md).
The draw returned `bs-02-five-component-spec`; since it is episode 2 of an unbuilt series and all
three Botspeak folders are open, we took episode 1 and queued 2 and 3 for Weeks 19–20.

## What the source draft gives us, and where it can be strengthened

The draft is an 11-beat episode teaching students to write a bounded role statement for the INFO 7375
Botspeak Prompt Adaptation assignment. **Its core craft is sound and this rebuild keeps it.** Bounding
a role statement to one job is real skill, and the adjacent-profession test — swap your statement into
a neighbour's job and see if it still fits — is a genuinely clever move that the film adopts wholesale
and hands to the viewer as its own deliverable.

What follows is the set of places the episode can be made stronger. None of it is a reason to discard
the material; all of it is why a rebuild is more useful than a patch.

Its two instruments, verbatim from `beat_sheet.json`:

> **B02:** "The 'specific enough' test has one question: if you handed this role statement to someone
> at your workplace, would they immediately recognize the exact job — or could it describe five
> adjacent roles?"

> **B03:** "The adjacent profession test is binary: take your role statement and swap it into a
> neighbor's job. If it still fits, it is not specific enough."

Six opportunities, each verifiable in the file:

| # | Opportunity | What's there now |
|---|---|---|
| 1 | **Replace the templated "why this matters" beat with something specific to the topic** | B01B uses a shared template — "belongs in your working knowledge… affect decisions at your level" — which appears in **3,160 of 3,956** beat sheets across the repo. A topic-specific beat earns more from the same runtime. |
| 2 | **Add a measured number** | The only digit string in all narration is `7375`, the course number. The episode's central claim — that specificity changes what you get back — is assertable, and would land harder with a measurement behind it. |
| 3 | **Source the course figures, or leave them out** | "A hundred points — eighty on the rubric, twenty on your relative quartile," "six deliverables," "twenty-one points," "chapters zero through thirteen." These are dated claims about a live course, and they date quickly. This rebuild cuts them rather than risk them going stale. |
| 4 | **One comparison needs a basis or a rewording** | B03: "One pass of this test is worth ten minutes of re-reading the statement yourself." The point is right; the specific ratio isn't sourced. |
| 5 | **Check whether a model can run the test before asking the viewer to rely on one** | B07 tells the viewer to paste their draft into Claude and have it run the adjacent-profession test. That's a sensible, useful habit — and nobody had yet measured how steady the model's answer is. **This is the gap the rebuild fills, and it turned out to be measurable.** |
| 6 | **Consolidate two overlapping frameworks into one** | B02 offers three axes (bounded role / named task context / visible failure mode); B03 offers a separate binary test. Both are good; merging them into a single ordered instrument makes the whole thing reusable. |

The source folder carries `README.md` and `beat_sheet.json` — the supporting paperwork
(`PEDAGOGY.md`, `FACTCHECK.md`, `SOURCES.md`) is what this rebuild adds.

**Item 5 is the interesting one, and it is the teach.** The draft's advice is good advice. The
opportunity is that it hands the judging to a model without anyone having checked how steady that
model's answer is — and once you check, there's a one-sentence improvement to hand back. Items 1–4 and
6 are why a rebuild is more useful than a patch, not a verdict on the original.

## Thesis (premise — not yet tested)

The draft's instrument asks whether a description **excludes your nearest neighbour**. That is the
right question, and it is much harder than it looks — because "describes me" and "excludes everyone
adjacent" are different properties, and only the second one is worth points.

The film's intended spine: **exclusion, not description, is what makes a specification specific** —
and the way to know whether your specification excludes is to name the phrase doing the excluding and
check that removing it flips the verdict.

We then turn the instrument on the draft's own CTA: **can a model actually run this test?** That is a
measurable question, and measuring it is the film's original research.

**The draft's practice must survive even if its CTA does not.** "Write a bounded role statement, then
check it against your nearest neighbour" is sound craft regardless of what we measure. If our data
shows the model's verdict is unreliable, the correction is *how you use the model in that loop*, not
"don't bound your role statement." Landing on "specificity doesn't matter" would be a worse outcome
than the draft's overclaim.

## The framework — four questions for any identifying description

Shown as a structure before any example. Reusable on anything that has to pick one thing out of a
crowd: a role statement, a persona, a bug report, a job posting, a search query.

| # | Question | Fails when |
|---|---|---|
| **1** | **Does it exclude, or only describe?** | The statement is true of you *and* true of your neighbour. Description is cheap; exclusion is the work. |
| **2** | **Who is the nearest neighbour?** | The neighbour chosen is far away, so the test passes trivially. A pharmacist tested against a novelist proves nothing. |
| **3** | **Which phrase is doing the excluding?** | You cannot point to it. Then the statement isn't specific — it's just long. |
| **4** | **Would a stranger draw the same boundary?** | Only you can apply it and reach your verdict. Then it's a preference, not a test. |

Questions 1–2 are cheap and catch most weak statements. **Question 3 is the one people skip** — it is
what separates specific from merely verbose. **Question 4 is the one the draft skips**, and it is
where the model comes in.

### Why this is not a retrofit

PROOF's reverse-engineering tell is categories mapping one-per-example. These don't: it is one
instrument applied to at least three artifacts — the draft's own pharmacist example, a length-matched
pair we construct, and the model's verdicts — each failing at a different question. Q3 makes a
**falsifiable prediction**: removing the load-bearing phrase should flip the verdict. If it doesn't,
the framework is wrong.

## The original research (designed, NOT YET RUN)

**Claimed cause:** the model's PASS/FAIL verdict tracks *specificity* — whether the statement excludes
adjacent roles.

**Rival explanation:** the verdict tracks *length or jargon density*. Longer, more technical-sounding
statements read as more specific whether or not they exclude anyone.

**The arm where only the claimed cause varies:** length-matched, jargon-matched pairs. Same word
count, same count of domain terms — one uniquely identifying, one not. If the model is reading
specificity, verdicts split across the pair. If it is reading length, they don't.

**Will the arm collect data (Q4)?** Not guaranteed. If the model returns PASS on everything or FAIL on
everything, there is no discrimination signal and no finding. Mitigation: include known-fail anchors
("healthcare professional") and known-pass anchors (the draft's full pharmacist statement) so the
denominator is guaranteed, and check verdict stability across repeated runs at the same temperature.

**What would falsify the framework:** if removing the load-bearing phrase does *not* flip the verdict —
Q3 is then not load-bearing, and the framework's central move fails.

**What this cannot establish:** anything about human graders, anything about whether a bounded role
statement improves the *downstream adapted prompt*, or anything about how this assignment is actually
scored. Those bounds get stated on screen, not buried.

**Blocked on:** model access. Film 4's harness shipped a deterministic `--dry-run` stand-in explicitly
labelled **NOT evidence**, because canned responses cannot support a finding. A real result needs an
`ANTHROPIC_API_KEY`. See *Open dependencies*.

## Friction — the viewer has to resolve this

The draft tells you to have a model check whether your self-description is specific enough. But
"specific enough" is exactly the kind of judgment where a model can sound confident and be reading
something else entirely. So: do you use the model in this loop or not?

The instinctive answers are both wrong. "Trust it" ignores that nobody measured it. "Don't use it"
throws away a genuinely useful second pair of eyes. The resolution has to come from the framework, not
from a preference.

## Viewer task — a scaffold, not "paste this into Claude"

The draft's B07 is already better than most CTAs — it is a structured prompt. What it lacks is any
statement of what a good versus bad result looks like, which is what makes a task gradeable.

The rebuilt task, four steps:

1. Write your role statement.
2. Name your **nearest** neighbour — the person whose job is most similar, not most different.
3. Underline the single phrase that your neighbour could not write. That is the load-bearing phrase.
4. **Delete it and re-read.** If the statement still sounds fine, it was never specific — it was long.

**Good result:** you find a statement you were happy with whose load-bearing phrase you cannot
identify. **Bad result:** every statement passes on first reading — you graded generously, or you
picked a far neighbour (Q2).

## Act structure — to be drafted in Phase 2

Must share no shape with the previous four: no ASK→RESULT cold open (CommBank), no J-curve essay spine
(Klarna), no scaffold/production interleave (Lemonade), no one-instrument-applied-three-times-with-a-
reversal (Film 4). Framework must land ahead of any example, per PROOF Phase 2.

Per PLAYBOOK §1c, beat 2 must name the subject in plain words — a viewer who watched only that beat
should be able to say what the film is about in one ordinary sentence, before any abstraction. The
subject here is "how to describe your own job precisely enough that a tool's answer is actually about
your job," not "the adjacent profession test."

Per PLAYBOOK §1a, the tone arc gets mapped before a line is written.

## Evidence discipline

| Claim | Source | Calibration |
|---|---|---|
| Draft's two tests, verbatim | `claude-liam-bs-01-pick-and-scope/beat_sheet.json` B02, B03 | Verbatim quote from the file |
| B01B is boilerplate in 3,160 / 3,956 beat sheets | Same repo, grep across all `beat_sheet*.json` | Verified programmatically; reproducible |
| Draft contains no measured number | Same file, all narration fields | Verified programmatically — only digit string is `7375` |
| INFO 7375 rubric: 100 pts, 80/20, six deliverables, 21 pts E1 | **UNSOURCED — the draft asserts it** | ❌ Must be verified against the real assignment or cut. See *Open dependencies*. |
| Botspeak chapters 0–13 end in LLM exercises | **UNSOURCED — the draft asserts it** | ❌ Needs the actual Botspeak text |
| Model verdict behaviour on length-matched pairs | Our own measurement — **NOT YET RUN** | Will cite to a results JSON that ships with the film |

**Not claimed anywhere:** that specificity doesn't matter; that the draft's advice is wrong; that any
finding about model verdicts generalises to human graders or to the downstream deliverable.

## Persona / register

Inherited from the draft: `topic: INFO 7375 BOTSPEAK PROMPT ADAPTATION`, **Pragmatist** register,
`hai` audience, `claude-liam` brand, palette `claude`, ground `#FAF9F5`.

**Voice: `af_kore`, confirmed available.** Film 4's PEDAGOGY recorded that `af_kore` "is not installed
in this toolkit — the only Kokoro voices available are `am_onyx` and `af_bella`." That is not true of
this install: `runtime/models/kokoro/voices-v1.0.bin` contains all **50** standard Kokoro voice ids,
`af_kore` among them. Film 4's `am_onyx` was a defensible choice for a first-person investigation, but
it was not forced by the toolkit.

**A brand-mapping conflict, resolved in the draft's favour.** `brutalist.art/CLAUDE-BRAND.md` maps
`claude-liam` → Liam, `@NikBearBrown`, `am_onyx`, Teardown — which contradicts the draft's metadata
(`brand: claude-liam` but persona Kore, `folderLabel: @HumanitariansAI`, register Pragmatist, voice
`af_kore`). The repo's own README explains why: *"The current HAI production default is **Kore**, using
the Kokoro voice `af_kore`… public channel references should use `@HumanitariansAI`. Historical
directory identifiers such as `claude-liam-*` remain unchanged so existing paths, manifests, and links
continue to resolve."*

So `claude-liam-` here is a legacy **directory** identifier, not a brand instruction, and
`CLAUDE-BRAND.md` is the older mapping. Use **Kore / `af_kore` / `@HumanitariansAI` / Pragmatist**, and
the in-for line is "Kore, in for Humanitarians AI" — not "in for Bear." The draft's B00 and B08 already
do this correctly.

## Components — PLAYBOOK §2 check pending

None built. **No pattern name goes into `beat_sheet.json` until it is registered in `Root.tsx`** — an
unregistered name is a hard crash that can leave a stuck lock hanging the next unrelated render.

The draft's beats reference `ClaudeComposerAsk`, `ClaudeWindow`, `ClaudeTitleOutro`. Anticipated new
generic, props-driven components: a four-question board, and a side-by-side statement comparator for
the length-matched pair (this is the beat the film turns on, and per the production gate it must be
held ≥2s with both members in frame).

---

## GATE P

**VERDICT: PASS** — premise reviewed and signed off by the author, 2026-08-18. Cleared to script.

**Phase 1 gate question:** the method a viewer walks away able to apply is — *does it exclude or only
describe; who is the nearest neighbour; which phrase is doing the excluding; would a stranger draw the
same boundary?* Is that the actual teach, or just the topic?

**Author's answer, and it refines the teach:** *"it's the actual teach where it is asking the
questions which matters."*

That distinction is load-bearing and changes emphasis downstream. The teach is **the act of
asking** the four questions — not the answers they happen to produce on any given statement.
Which is exactly what the experiment has been demonstrating the hard way: two revisions failed
because *my* answers were wrong (three of six `full` statements didn't exclude their neighbour),
while the questions themselves kept working — Q2 correctly predicted that neighbour choice would
dominate, and it did, on both models.

Consequences for the build:

1. **The film must not stake its credibility on getting verdicts right.** It teaches a procedure
   the viewer runs, and it can show that procedure catching the author's own errors. The
   experiment's failures become material rather than embarrassment.
2. **B04 changes register** — walk the questions through the pharmacist statement as an act of
   asking, showing where the answer is genuinely arguable, rather than presenting a verdict.
3. **B12's scaffold is the payoff, not an afterthought** — the four steps *are* the deliverable.
4. **Falsifiability stays honest.** If revision 3 yields no usable number, the film still teaches
   the instrument; it just cannot claim a measured rate. Scored 1, not 2, until then.

### Open dependencies at Phase 1 — both since resolved

1. ~~**The INFO 7375 assignment.**~~ **RESOLVED by cutting.** No point value from the assignment
   appears anywhere in the film, spoken or on screen (author decision, 2026-08-18). The figures did
   not reconcile internally either — 21+16+11 = 48 of a claimed 80 — so cutting was the safe call
   regardless of sourcing.
2. ~~**Model access for the experiment.**~~ **RESOLVED.** Author supplied an API key; 626 calls
   across three revisions, **$0.996 total**. Revision 3 produced the measured result at B10/B10B.

---

## GATE P — NARRATION (second sign-off)

**VERDICT: PASS** — narration reviewed by reading the script aloud, Tanmay Kulkarni, 2026-08-18.
Cleared to final audio.

Reviewed against `READ-ALOUD.md` v2, with three revisions requested and applied before sign-off:

| # | Author's note | Change made |
|---|---|---|
| 1 | The greeting appears in B00, so repeating it in B01 doesn't make sense | B01 now opens straight on the hook; the presenter is introduced once |
| 2 | Add context on the experiment rather than starting abruptly with the information | B10 now states what was tested and why — and describes the 24 descriptions across three domains — before any figure |
| 3 | Don't criticise the original base directly; if we do, do it subtly — "where it could have been improved" | Softened throughout: B02 "an admission" → "honest"; B08 "never separates" → "doesn't ask", gap reframed as good news; B09 the instruction is "sensible" and "a genuinely useful habit"; B11 "never checked why" → "where it could be stronger… something to add, not to replace" |

**The only sharp criticism remaining in the film is of the author's own pharmacist example (B04B),**
which is the point of that beat.

Runtime after revision: **8:25** (506s), from 8:03. The 22s went to the B10 context and the gentler
framing. Word count 1,837.

**Process note, recorded because it nearly went wrong.** The author's initial instruction was to record
PASS on the basis that "only 2 lines" had changed. In fact the plain-language pass had reworded all 17
beats, including the pharmacist example and all four questions. That was flagged before signing rather
than after, the author re-read, and the three revisions above came out of that read. A sign-off is
only worth what the reviewer actually saw.

### Tone policy for this film, going forward

Established at this gate and applying to bs-02 and bs-03: **the source material is treated as sound
practice with room to be strengthened, never as defective.** Criticism of the author's own work is
fair game and is the film's most valuable beat. This document was revised to match that register on
2026-08-18 — the verifiable facts are unchanged, the framing is not prosecutorial.
