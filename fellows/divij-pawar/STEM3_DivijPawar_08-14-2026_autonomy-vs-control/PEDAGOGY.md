# PEDAGOGY GATE — The Agent's Dilemma: Autonomy vs. Control

## Narration Review

**Topic:** Blast radius as the real variable behind every AI-agent permission
**Register:** Teardown, documentary-measured end of it (narrated by Divij Pawar)
**Audience:** Smart non-technical viewers; high-school technicality per the source script
**Series:** STEM — Agents, 3 of 3 (siblings: STEM1 *What Makes an AI Agentic?*, STEM2 *Why Agents Fail*)

### Source & Adaptation

Body narration (B01–B06) is carried **verbatim** from
`03_narration_tts_ready.txt`, split on its own paragraph boundaries. The
source is already TTS-normalized; no rewriting was needed or done.

What was **added**, because the source script has no bookends:

- **B00 (cold open)** — reuses source ¶1 verbatim; the composer props are new.
- **B07 (verdict)** — new synthesis of the three control models and the
  asymmetric tradeoff, closing on source ¶16 verbatim.
- **B08 (your turn)** — entirely new. See the deliberate tension noted below.
- **B09 (outro)** — new, matching the series sign-off.

Nothing was cut.

### Teaching Arc ✓

- **B00 (Cold open):** Every permission is a bet with real stakes
- **B01 (BLUF):** Executive summary — three escalating bets, and the decision you make without noticing
- **B02 (Framework):** Blast radius, established on a physical example then transferred to permissions
- **B03 (The three models):** Read-only / approval-gated / full autonomy, each demonstrating its own stopping behaviour
- **B04 (Worked example):** The asymmetric tradeoff curve, then one financial agent walked across all three tiers
- **B05 (Falsifiability):** Human delegation precedents — where the analogy holds, and the one axis where it breaks
- **B06 (The question):** Rope and reach; the reel's question held in silence
- **B07 (Verdict):** Blast-radius recap card
- **B08 (Your turn):** Scaffolded mapping prompt + 3-item rubric
- **B09 (Outro):** Title restate + handle

**EXECUTIVE-SUMMARY LAW:** satisfied at B01 — the escalating-stakes idea is
stated whole ("small bet → bigger bet → can't take back") and the reel's
actual subject is named ("a decision you make every time you set one up")
before blast radius or any tier is introduced.

**FRAMEWORK-BEFORE-EXAMPLES:** B02 establishes blast radius as the measuring
instrument; B03 applies it to three control models; B04 walks a single
financial agent across all three while the framework is on screen.

### Factual Check ✓

| Claim | Verdict | Note |
|---|---|---|
| "Blast radius" is an established engineering term for how far damage spreads | ✓ | Standard usage in systems/SRE practice |
| Read-only, approval-gated, and full autonomy are all deployed in real systems today | ✓ | Correct and observable; no specific vendor named |
| Approval-gated is where most everyday AI assistance currently sits | ⚠ **judgment** | An assessment, not a measurement — see SOURCES.md |
| Usefulness and risk do not rise at the same rate across the three tiers | ⚠ **judgment** | The reel's central argument, presented as reasoning, not data. The curve in B04 is explicitly qualitative — no axis numbers |
| Company spending limits, autopilot bounds, and power of attorney are bounded delegations | ✓ | Accurate descriptions of all three, stated at the level of the bound only |
| Autopilot is used at cruise but not takeoff | ✓ | Correct as a general characterization of the delegation bound |
| An agent can go from decision to action faster than a human shows warning signs | ✓ | Follows from the mechanism; stated qualitatively, no latency figure claimed |

No model, vendor, version, or benchmark appears. The reel should not date.

### Register & Tone ✓

- The most measured of the three reels, per the source's stated documentary
  tone. Teardown judgment is present but points at the *decision structure*,
  not at any product.
- Every tier is given its honest best case before its failure case — the
  full-autonomy beat names it "the most useful of the three" before showing
  the wrong amount to the wrong account.
- The closing refuses the easy takeaway on purpose (see below), which is the
  strongest editorial choice in the three scripts.
- Narration budget: body beats run 69–201 words. B03 (201w / ~62s) is the
  longest beat in the series; it holds one idea (the three-point control
  spectrum) across three markers, so one-idea-per-beat is not violated.

### Falsifiability ✓

**B05** is the dedicated stress-test beat, and it is unusually well built: it
takes the reel's own reassuring analogy — "humans have always delegated with
bounds" — grants it fully across three real precedents, and then finds the
single axis where it breaks (speed and visibility: no catchable interval
between decision and action). The framework survives, but only after being
genuinely attacked. Not a caveat in passing.

### The deliberate tension at B06 / B08 — read this before signing

Source ¶14 says, in the author's own voice: *"Not a rule. Not a checklist,
this time. Just the question underneath all of it."* That refusal is the
best-made choice in the script and it is preserved **verbatim** at B06.

It also collides with HANDOFF LAW and with nopunt's SCAFFOLDED-TASK
requirement, both of which demand a real, runnable prompt plus a rubric.

**Resolution taken:** the refusal is kept intact where the author put it — in
the body, as the reel's emotional close. B08 then hands the viewer a tool for
deriving their *own* answer rather than a rule to follow: map the blast radius
of permissions you have already granted. The video declines to tell you what
to conclude, and gives you the instrument to conclude it yourself. The two
beats read as complementary rather than contradictory.

**If the human disagrees**, the alternative is to drop B08's rubric and log a
SCAFFOLDED-TASK violation in `BUILD-LOG.md` per the PROOF GATE's "resolved or
explicitly justified, never silently passed" rule. That is a legitimate call
and it is the author's to make — noted here so the signature is informed.

### Known deviations from house defaults

1. **Runtime.** The source header says "~9 minutes"; measured at the rate
   Kokoro `am_onyx` actually produced on `accountability-mesh` (~195 wpm),
   this narration runs **≈5.2 minutes**. Audio is the master clock. **Flagged
   — no content was invented to close the gap.**
2. **Body-beat length.** B02–B06 run 33–62s, past the 14–22s in `agents.md`
   but matching the established series shape.
3. **B03 at ~62s** is the longest beat in the series. If it reads long on the
   animated slate at GATE P review, the natural split is read-only + approval
   -gated in one beat and full autonomy in another — but that costs a beat
   elsewhere, so it was not done pre-emptively.

---

## VERDICT: PASS

**Prepared by:** Claude (beat-sheet authoring pass)
**Approved by:** Divij Pawar
**Date:** 2026-08-17

Approved for audio generation and render as documented above, including the
runtime deviation (~5.2 min vs. the source header's ~9 min target). The
B06/B08 tension is explicitly settled: **keep both as authored** — B06 keeps
the source's verbatim refusal ("not a rule, not a checklist"), B08 keeps its
scaffolded prompt and 3-item rubric. The two read as complementary (an
instrument for the viewer's own conclusion, not a rule to adopt), not
contradictory. No BUILD-LOG.md deviation entry needed for this beat pair.
