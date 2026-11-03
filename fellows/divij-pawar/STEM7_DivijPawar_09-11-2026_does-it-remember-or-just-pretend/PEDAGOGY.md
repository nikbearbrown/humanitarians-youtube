# PEDAGOGY GATE — Does It Remember, or Just Pretend To?

## Narration Review

**Topic:** What "memory" actually means for an AI agent — the difference
between the temporary context window and externally stored, retrieved
persistent memory — how vector-similarity retrieval works, its two
compounding failure modes (stale and poisoned memory), why that's the
exact same structural blind spot as multi-agent shared contamination
stretched across time, and the three design requirements (provenance,
decay, contradiction-checking) responsible memory actually needs.
**Register:** Documentary, measured, quietly unsettling (per the source
script's own header)
**Audience:** High-school technicality, per the source script's own header
**Series:** STEM — Agents, Episode 7. Follows directly from STEM6
(`when-two-agents-disagree`): B00 opens on "our very first video" (the
tier-three agent framing) and B05 explicitly reprises STEM6's shared-
contamination diagram as the connecting argument. B09 closes by teasing
the next problem (whether a system can be graded at all), already
scripted as `youtube/STEM8/08_grading_the_machine.md`.

### Source & Adaptation

Narration is condensed from `07_does_it_remember_or_just_pretend.md`,
split into 10 beats matching the source's 6 body sections plus bookends
— see CHECKS-REPORT.md for the per-beat mapping. This is two fewer body
beats than STEM6's 8, because this script's sections divide cleanly into
6 single ideas (two-mechanisms, retrieval, stale, poisoned, callback,
framework) without needing the kind of mid-section split STEM6 required.

Before beat-sheet authoring, three instances of a repeated "that's not X,
it's Y" construction were rewritten in the source script for natural
spoken cadence — no factual or structural content changed. This is now a
standing house convention (first applied to STEM6 at the user's explicit
request, applied proactively here since the same drafting pipeline
produced the same pattern) — see SOURCES.md "Corrections applied to
narration."

**What was added, because the source script has no scaffolded viewer
task:**

- **B00 (cold open)** — condenses the source's opening paragraph and adds
  the required self-introduction ("Hi — I'm Divij Pawar") per house
  convention.
- **B08 (your turn)** — a new, concrete 3-question task (trace one stored
  fact's source, age, and contradiction-handling), built from the
  source's own closing logic, which poses the idea as a rhetorical
  question but gives no runnable scaffold.
- **B09 (outro)** — bridges to STEM8 ("Grading the Machine") rather than
  ending on the source's own closing aphorism, matching the house
  convention of closing on a tease to the next scripted episode (see
  STEM5's B12, STEM6's B11).

Nothing from the source's substantive content was cut; the two-mechanism
distinction, the retrieval mechanism, both failure modes, the multi-agent
callback, and all three design requirements survive intact.

### Teaching Arc ✓

- **B00 (Cold open):** Reprises the tier-three-agent framing and poses
  today's question
- **B01 (Framework/BLUF):** The context-window-vs-persistent-memory
  distinction stated before either mechanism's failure modes
- **B02 (Mechanism):** Vector-similarity retrieval, with its own worked
  example (flight vs. recipe) and the "similarity ≠ truth" caveat
- **B03 (Failure mode 1):** Stale memory, worked through the vegetarian
  example
- **B04 (Failure mode 2):** Poisoned memory, worked through a two-query
  timeline
- **B05 (Falsifiability):** The callback to STEM6's shared-contamination
  blind spot — the same structural gap, stretched across time
- **B06 (The framework):** Three transferable, numbered rules
- **B07 (Verdict):** Condensed recap card
- **B08 (Your turn):** A concrete, ordered 3-question audit task
- **B09 (Outro):** Title restate, handle, bridge to STEM8

**EXECUTIVE-SUMMARY LAW:** satisfied at B01 — the two-mechanisms
distinction is stated as the episode's organizing thesis before either
mechanism's specific problems are described.

**FRAMEWORK-BEFORE-EXAMPLES:** B01 draws the context-window/persistent-
memory line; B02 explains the retrieval mechanism that makes persistent
memory work; B03/B04 each demonstrate one consequence of that mechanism
having no truth-check; B06 collapses the response into three rules.

### Factual Check ✓

See SOURCES.md for the full claim table. Summary: this reel describes a
**general architectural pattern** (context windows, vector-similarity
retrieval, decay, provenance, contradiction-checking), not this project's
own code — per the channel's own standing note, STEM videos are
conceptual explainers and are not required to match the real product
code at `D:\Code\mycroft\verification-layer`. No model names, vendors,
versions, or benchmark figures appear anywhere.

### Register & Tone ✓

- Documentary/measured register carried through: each mechanism is
  explained before being judged, and the "quietly unsettling" tone lands
  specifically in B04 (poisoned memory resurfacing) and B05 (the blind
  spot has a "longer runway," not a fix).
- B05 refuses the easy ending — it explicitly connects this episode's
  proposed framework to a limit already established in STEM6, rather
  than presenting memory-scrutiny as a clean solution.
- Narration budget: body beats (B01–B06) run roughly 100–190 words each.
  B01 and B06 run longer (190/185 words) because each carries a genuine
  two-part or three-part structure — consistent with STEM5's precedent of
  longer body beats where the content mass warrants it.

### Falsifiability ✓

**B05** is the dedicated stress-test beat, and it stress-tests the
episode's *own* proposed framework in advance: the three design
responses in B06 (provenance, decay, contradiction-checking) all depend
on *something* eventually contradicting or aging out a bad fact — none of
them catches a false memory that a system consistently, confidently
agrees with itself about. This is the same "arbitration-by-disagreement
is blind to shared agreement" limit STEM6 established, named explicitly
rather than left implicit, so B06's framework is not oversold as a
complete fix.

### Known deviations from house defaults

1. **Beat count.** 10 beats (B00–B09), fewer than STEM6's 12. **Flagged
   for the human reviewer** as a content-mass judgment call, not an
   oversight — see CHECKS-REPORT.md "Beat-count rationale."
2. **Runtime.** The source script header says "~9 minutes." Based on the
   pattern established across STEM2, STEM5, and STEM6 (all estimated
   ~9 min, all measured shorter once real Kokoro audio was generated),
   this narration is likely to run **shorter than 9 minutes**. **The
   actual number is unknown until Step 2 of BUILD-PROMPT.md runs —
   flagged here so the human reviewer isn't surprised by the gap.**
3. **B01 and B06 are long body beats** (est. 55s and 65s respectively),
   past the 14–22s default range, matching the established pattern in
   this series for beats carrying multi-part content in one continuous
   idea.
4. **The proactive narration-style correction** (SOURCES.md) was applied
   without being asked this time, on the basis that it's now a standing
   convention rather than a one-off STEM6 request — confirm this
   judgment call is welcome before treating it as settled going forward.

---

## VERDICT: PASS

**Prepared by:** Claude (beat-sheet authoring pass)
**Approved by:**Divij Pawar
**Date:**09/11/2026

**What a human reviewer should check before flipping this to PASS:**

1. **The beat-count rationale (10, not 12)** — confirm the six body
   sections genuinely don't need further splitting (unlike STEM6's
   arbitration step), or decide otherwise before Step 2 spends any time.
2. **The proactive narration-style rewrite** (three instances, logged in
   SOURCES.md) — confirm it's welcome as a standing convention rather
   than something that should only happen on explicit request.
3. **The illustrative examples** (vegetarian preference, poisoned-memory
   timeline) — confirm they're acceptable as declared-illustrative
   teaching devices.
4. **The B08 scaffolded task** — confirm the 3-question audit is concrete
   enough to act on, or needs a sharper prompt.
5. **The runtime gap** — once Step 2 (Kokoro) runs, compare actual
   runtime to the source's "~9 min" header.

Once satisfied, replace this line with `VERDICT: PASS`, sign, and date it.
**No audio generation (Step 2 of BUILD-PROMPT.md) may run until this line
reads PASS** — this is GATE P, per `youtube/CLAUDE.md` §4 and
`brutalist.art/CLAUDE.md` rule 3.
