# PEDAGOGY GATE — When Two Agents Disagree

## Narration Review

**Topic:** What happens the moment a multi-agent system produces two
independently-reasoned conclusions that contradict each other — why
averaging them is the wrong instinct, how to detect a real divergence on
structured signals rather than prose, why arbitration gets bounded to one
round, why "unresolved" has to survive as its own visible output, and the
one structural blind spot (shared contamination) the whole mechanism can't
see.
**Register:** Courtroom procedural, measured tension (per the source
script's own header)
**Audience:** High-school technicality, per the source script's own header
**Series:** STEM — Accountability, 2 of 5 (siblings: `STEM5` mechanism-
verification, `STEM7` memory-vs-pretending, `STEM8` grading the machine,
`STEM9` the agent that was told what to do). Follows directly from STEM5:
B01 opens on "everything covered in the last two videos assumed a single
agent" — the STEM5 thread about checking one agent's own reasoning — and
B11 closes by teasing the next problem (memory vs. pretending to
remember), already scripted as
`youtube/STEM7/07_does_it_remember_or_just_pretend.md`.

### Source & Adaptation

Narration is condensed from `06_when_two_agents_disagree.md`, split into
12 beats rather than the source's 7 prose sections, because "The
Arbitration Step" contains two independently-checkable ideas (the
single-round mechanic, and the resolved/unresolved branch) that need their
own on-screen artifact apiece — see CHECKS-REPORT.md "Beat-count
deviation."

Before beat-sheet authoring, the narration text itself was rewritten in a
separate pass to cut a repeated "it's not X, it's Y" contrastive
construction that recurred across nearly every section of the original
draft — no factual or structural content changed, only sentence rhythm and
word choice. The rewritten prose is what's reflected in
`06_when_two_agents_disagree.md` and `06_narration_tts_ready.txt`.

**What was added, because the source script has no bookends and no
scaffolded viewer task:**

- **B00 (cold open)** — condenses the source's opening two paragraphs and
  adds the required self-introduction ("Hi — I'm Divij Pawar") per house
  convention (a returning-series viewer still needs the self-intro; see
  STEM2's post-build correction note for why this isn't assumed to carry
  over).
- **B08 (the framework)** and **B09 (verdict)** — the source script's
  closing paragraph and its six-item Key Takeaways list are synthesized
  into four transferable, numbered rules rather than narrated as a bullet
  recap. This mirrors STEM5's B09/B10 pattern (a Manim framework beat plus
  a Remotion verdict-card recap carrying the same content in two
  registers).
- **B10 (your turn)** — a new, concrete 3-step task (name the structured
  signal you'd compare, pick a real threshold, decide what "unresolved"
  looks like before it happens) built from the episode's own mechanism,
  since the source script poses no actionable viewer task at all.
- **B11 (outro)** — the source's own ending line was replaced with a
  direct bridge to STEM7, matching the house convention (see STEM5's B12)
  of closing on a tease to the next scripted episode rather than a
  standalone aphorism.

Nothing from the source's substantive content was cut; the naive-fix
argument, the structured-detection mechanism, the single-round arbitration
rule, the resolved/unresolved branch, the unresolved-must-survive
argument, and the shared-contamination blind spot all survive intact.

### Teaching Arc ✓

- **B00 (Cold open):** States the disagreement scenario concretely (Agent
  A vs. Agent B on the same filing) and poses today's question
- **B01 (Framework/BLUF):** The reasoning stated as a thesis — disagreement
  is a signal, not a bug — before any mechanism is described
- **B02 (The naive fix):** Averaging is shown making the true answer worse,
  not better, and destroying the one useful fact in the exchange
- **B03 (Detection):** The structured-signal comparator and its threshold
- **B04 (Arbitration setup):** The single bounded round, contrasted against
  an unbounded debate's failure mode
- **B05 (Arbitration outcomes):** Resolved vs. unresolved as two
  legitimate, named outputs
- **B06 (Unresolved handling):** Why the disagreement must reach the human
  visibly, not folded into one grade
- **B07 (Falsifiability):** The shared-contamination blind spot — the
  mechanism's own structural limit
- **B08 (The framework):** Four transferable, numbered rules
- **B09 (Verdict):** Condensed recap card
- **B10 (Your turn):** A concrete, ordered 3-step task
- **B11 (Outro):** Title restate, handle, bridge to STEM7

**EXECUTIVE-SUMMARY LAW:** satisfied at B01 — the episode's central
reframe (disagreement as signal, not bug) is stated before the naive fix
or any detection mechanism is described.

**FRAMEWORK-BEFORE-EXAMPLES:** B01 states the reframe in the abstract;
B02–B07 each demonstrate one consequence of taking that reframe seriously
(don't average it, detect it structurally, bound the debate, preserve
"unresolved," know the blind spot); B08/B09 collapse all of it into four
numbered rules.

### Factual Check ✓

See SOURCES.md for the full claim table. Summary: this reel describes a
**general multi-agent arbitration pattern**, not this project's own code —
`accountability_layer/` was searched directly and contains no
arbitration/disagreement module (only `consistency.py`'s single-agent,
two-run divergence flag, already covered in STEM5). Every claim is checked
against standard multi-agent-system design reasoning rather than a
specific file/line reference. No model names, vendors, versions, or
benchmark figures appear anywhere.

### Register & Tone ✓

- Courtroom-procedural framing carried through consistently: two named
  parties (Agent A / Agent B), an arbitration step, a recorded verdict of
  "unresolved" rather than a forced resolution.
- B07 refuses the easy ending — the reel explicitly stress-tests its own
  proposed mechanism (arbitration-by-disagreement) rather than presenting
  it as solved, matching the falsifiability discipline established in
  STEM5's B07/B08.
- Narration budget: body beats (B01–B08) run roughly 95–150 words each,
  consistent with the sibling series' established body-beat length
  (STEM5's B01–B09 ran 90–180 words).

### Falsifiability ✓

**B07** is the dedicated stress-test beat, and it stress-tests the reel's
*own proposed mechanism*: arbitration only fires on disagreement, so two
agents drawing on the same contaminated source will agree their way past
it undetected. This is why B08/B09's framework closes on "it lowers your
risk, it doesn't take it to zero" rather than presenting arbitration as a
complete solution — the same discipline STEM5 applied to its own
verification/consistency mechanisms.

### Known deviations from house defaults

1. **Beat count.** 12 beats (B00–B11), not the ai-explainer default of 10.
   See CHECKS-REPORT.md "Beat-count deviation" for the per-beat
   justification. **Flagged for the human reviewer.**
2. **Runtime.** The source script header says "~9 minutes." Based on the
   pattern established across STEM2 and STEM5 (both estimated ~9 min,
   both measured shorter once real Kokoro audio was generated), this
   narration is likely to run **shorter than 9 minutes**. **The actual
   number is unknown until Step 2 of BUILD-PROMPT.md runs — flagged here
   so the human reviewer isn't surprised by the gap, not resolved by
   inventing content to close it.**
3. **The financial "margins improving/declining" scenario is illustrative**
   (declared in SOURCES.md), chosen for concreteness and consistency with
   STEM5's own financial-analysis framing, not because this reel
   references a real trace.
4. **The four-rule framework (B08/B09) condenses the source's six Key
   Takeaways.** No content is dropped — takeaway 6 (the blind spot) is
   B07's entire dedicated beat rather than a fifth recap line — but this
   is a deliberate compression, not a literal restate.

---

## VERDICT: PASS

**Prepared by:** Claude (beat-sheet authoring pass)
**Approved by:** Divij Pawar
**Date:** 09/07/2026

**Note on scope (resolved):** STEM videos are conceptual explainers and
are not required to describe this project's own implementation — the
actual product code lives at `D:\Code\mycroft\verification-layer`, not
`accountability_layer`. Whether that codebase has an arbitration/
multi-agent module is irrelevant to this reel; the SOURCES.md framing
(general architectural pattern, checked against standard multi-agent
design reasoning) is the correct and intended register for this series,
not a gap to close.

Audio generation (Step 2 of BUILD-PROMPT.md) is cleared to run.
