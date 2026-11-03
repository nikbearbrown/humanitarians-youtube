# PEDAGOGY GATE — What Makes an AI Agentic?

## Narration Review

**Topic:** The agentic-AI capability spectrum, tier 0 through tier 3
**Register:** Teardown (narrated by Divij Pawar)
**Audience:** Smart non-technical viewers; high-school technicality per the source script
**Series:** STEM — Agents, 1 of 3 (siblings: STEM2 *Why Agents Fail*, STEM3 *The Agent's Dilemma*)

### Source & Adaptation

Body narration (B01–B06) is carried **verbatim** from
`01_narration_tts_ready.txt`, split on its own paragraph boundaries. The
source is already TTS-normalized (`9 AM` → `nine a.m.`, visual directions
stripped), so no rewriting was needed or done.

What was **added**, because the source script has no bookends:

- **B00 (cold open)** — reuses source ¶1 verbatim; the Remotion composer
  props around it are new.
- **B07 (verdict)** — new synthesis of the four tiers, closing on source ¶18
  verbatim ("'Agentic' was never a yes-or-no label…").
- **B08 (your turn)** — entirely new. HANDOFF LAW requires a prompt read
  aloud and discussed; the source script has none.
- **B09 (outro)** — new, matching the series sign-off.

What was **cut**:

- **Source ¶19** ("If you want to see what happens when tier two and tier
  three systems go wrong… that's exactly what's up next") — a next-video
  tease. This toolkit has no publishing machinery and OUTRO LAW locks the
  final beat to a title restate, so the cross-promo has no home. The
  sibling-video relationship is preserved instead through `metadata.series`.

### Teaching Arc ✓

- **B00 (Cold open):** The marketing claim and the two ways it misleads
- **B01 (BLUF):** Executive summary — one task, four tiers, a spectrum not a definition
- **B02 (Tier 0):** Talks only; next-word prediction is the entire mechanism
- **B03 (Tier 1):** One tool call, real data back, control returned to the human
- **B04 (Tier 2):** Multi-step plan built on the fly, hits a real conflict, stops to ask
- **B05 (Tier 3):** The autonomous loop with memory carried across sessions
- **B06 (Checklist + reality check):** Three diagnostic questions, then the framework turned on the market
- **B07 (Verdict):** Four-tier recap card
- **B08 (Your turn):** Scaffolded audit prompt + 3-item rubric
- **B09 (Outro):** Title restate + handle

**EXECUTIVE-SUMMARY LAW:** satisfied at B01 — the spectrum is named, and the
running example ("book me a flight") is fixed, before tier 0 is described.
The viewer holds the whole shape before collecting any specific.

**FRAMEWORK-BEFORE-EXAMPLES:** B01 states the four-tier structure; B02–B05
are the worked instances of it. The B06 checklist is a recap of that
framework, not its first appearance.

### Factual Check ✓

| Claim | Verdict | Note |
|---|---|---|
| Tier 0 mechanism is next-token prediction | ✓ | Standard description of autoregressive LM decoding |
| "Function calling" / "tool use" describes tier 1 | ✓ | Matches industry usage across major model APIs |
| Tier 2 chains multiple tools and adapts mid-plan | ✓ | Describes the common agent-framework loop |
| Tier 3 requires persistence across sessions | ✓ | The distinguishing property, stated as definitional not empirical |
| "Most products sold as agentic sit in tier 1–2" | ⚠ soft | A judgment, not a measurement — see SOURCES.md |

No dated specifics (model names, version numbers, benchmark figures) appear
anywhere in the narration, per DOUBLE-CHECK LAW's anti-staleness rule.

### Register & Tone ✓

- Concrete throughout: one task ("book me a flight") carried across all four
  tiers, so each tier is defined by what changes rather than by abstraction.
- Every term defined at first use — "function calling," "tool use," "context."
- Teardown judgment present: B06 turns the framework on the market and names
  where the label fails, rather than only explaining the concept.
- Narration budget: body beats run 112–189 words. B04 and B05 exceed the
  ~70-word guidance, matching the sibling reel `accountability-mesh` (B04 =
  189 words / 59.7s). Accepted as the series norm — see the note below.

### Falsifiability ✓

**B06** is the stress-test beat. It applies the reel's own framework to the
products the reel is about and finds the label mostly fails: what is marketed
as agentic lands in tier 1–2, and true tier 3 is rare and unsolved. This is a
full beat with its own visual (the bracket sweeping tiers 1–2), not a caveat
folded into the verdict.

### Known deviations from house defaults

1. **Runtime.** The source script header says "~9 minutes." Measured against
   the rate Kokoro `am_onyx` actually produced on `accountability-mesh`
   (~195 wpm), this narration runs **≈5.3 minutes**. Audio is the master
   clock and cannot be stretched at compile time. Either the header target is
   aspirational or ~800 words are missing. **Flagged for the human — no
   content was invented to close the gap.**
2. **Body-beat length.** B02–B06 run 35–58s, well past the 14–22s in
   `agents.md`. This matches the established series shape
   (`accountability-mesh` body beats: 21–60s) rather than the generic
   ai-explainer template.

---

## VERDICT: PASS

**Prepared by:** Claude (beat-sheet authoring pass)
**Approved by:** Divij Pawar
**Date:** 2026-08-17

Approved for audio generation and render as documented above, including the
runtime deviation (~5.3 min vs. the source header's ~9 min target).
