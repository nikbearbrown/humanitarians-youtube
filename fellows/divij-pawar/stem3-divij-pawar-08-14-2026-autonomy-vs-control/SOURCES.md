# SOURCES.md — autonomy-vs-control

Primary source: `03_agents_dilemma_autonomy_vs_control.md` (the authored
script with inline `[VISUAL: …]` stage directions) and
`03_narration_tts_ready.txt` (the TTS-normalized narration derived from it).
Both live in this folder.

This is an explanatory/argumentative piece about permission design, not a
first-person project account — claims are checked against common engineering
description, and the reel's central argument is declared as reasoning rather
than data.

## Factual claims (DOUBLE-CHECK LAW)

| Beat | Claim | Verdict | Basis |
|------|-------|---------|-------|
| B00 | Granting a permission is a bet with real stakes | ✓ | The reel's framing; developed and supported through B02 |
| B01 | Calendar read < email send < moving money, in recoverability | ✓ | Correct ordering by reversibility |
| B02 | "Blast radius" means how far damage spreads from a failure | ✓ | Standard systems/SRE terminology |
| B02 | The failing mechanism's severity and the consequence's severity are independent | ✓ | Correct, and the load-bearing insight of the beat |
| B02 | Same mistake, different consequence, purely from what it could touch | ✓ | Follows directly |
| B03 | Read-only can inform but cannot send, delete, or change | ✓ | True by definition of the permission class |
| B03 | Approval-gated systems propose and halt until a person confirms | ✓ | Accurate description of the pattern |
| B03 | Most everyday AI assistance currently sits at approval-gated | ⚠ **judgment** | An assessment of the current landscape, not a measurement. Narrated as "a huge amount," never as a proportion. Declared here per DOUBLE-CHECK LAW |
| B03 | Full autonomy is both most useful and most dangerous, for the same reason | ✓ | Valid reasoning; the "same reason" identity is the beat's point |
| B04 | Usefulness and risk rise at different rates across the three tiers | ⚠ **judgment** | The reel's central argument, presented as reasoning. **The B04 curves carry no axis numbers** — they are explicitly qualitative shapes, not plotted data |
| B04 | Removing the human removes the last thing that caught mistakes | ✓ | Follows from the definitions in B03 |
| B05 | A company card with a spending limit is a bounded delegation | ✓ | Accurate |
| B05 | Autopilot is delegated at cruise, not at takeoff | ✓ | Correct as a general characterization of the bound |
| B05 | Power of attorney can be scoped to specific accounts and limits | ✓ | Correct; the reel hedges appropriately with "sometimes… within specific bounds" |
| B05 | A human about to err usually shows a catchable sign first | ✓ | Stated as a tendency ("usually"), not a rule |
| B05 | An agent can act faster than any warning sign appears | ✓ | Follows from the mechanism; no latency figure claimed |

## Anti-staleness check (DOUBLE-CHECK LAW)

No model, vendor, version number, benchmark, or drifting count appears in the
narration. The three permission classes are structural, not product-specific.
The reel should not date.

## Simplifications (declared)

- **Three discrete control models are a teaching device.** Real permission
  systems are per-scope and mixed — one agent is commonly read-only on one
  resource and fully autonomous on another. The reel treats the tier as a
  property of a permission rather than of an agent, which is the more accurate
  framing and is what makes B08's mapping exercise coherent.
- **The B04 curves are qualitative.** They carry no units and no axis values,
  and are drawn to show *shape* (steady rise vs. flat-then-bend). They must
  not be re-drawn later with numbers on them — that would convert a declared
  argument into a fabricated measurement.
- **"Irreversible" is treated as binary.** Real recovery is a spectrum
  (chargebacks, undo windows, backups, rollbacks). The binary framing is the
  useful one for permission design and is where the stakes actually bite.
- **The three human precedents are described only at the level of their
  bound.** No claim is made about how any of the three institutions actually
  operates beyond the existence of the limit.

## Content carried and cut

| Source | Status | Note |
|---|---|---|
| ¶1–¶16 narration | **All carried** | Every paragraph of the source narration appears in the reel |
| `[VISUAL]` title card — a dark, ajar door | Rebuilt | B00 is locked to `ClaudeComposerAsk` by COLD OPEN LAW. The door motif is carried instead into B06 as the rope-and-reach figure, and the title-card question survives verbatim as the B09 subline |
| `[VISUAL]` B03 — "Send button greyed until it turns green" | Retinted | Green is not in the Claude fidelity palette. Rebuilt as an inactive control released by a human mark; the state change is carried by activation and label, not by hue |
| `[VISUAL]` B05 — "three quiet images: a company credit card, an autopilot switch, a power-of-attorney document" | **Rebuilt as line marks** | Under nopunt, only a *genuine archival photograph of a real person, place, document, or event* is a legitimate HOLD. Generic stock objects standing in for concepts are a PUNT. Redrawn as three line-mark precedent cards, each stating its bound |
| `[VISUAL]` B04 — "a large stack of dollar signs" | Simplified | Carried as the qualitative risk curve instead; a stack of currency marks would imply a magnitude the reel does not claim |

## Scene / beat map

| Beat | Scene / pattern | Notes |
|------|------------------|-------|
| B00 | ClaudeComposerAsk (Remotion) | Cold open — every permission is a bet |
| B01 | B01_TheBet (Manim) | BLUF — three escalating stakes, one marked unrecoverable |
| B02 | B02_BlastRadius (Manim) | Framework — concentric radii, then transferred to permissions |
| B03 | B03_ThreeModels (Manim) | Spectrum line, three markers, each with its own stopping behaviour |
| B04 | B04_TheTradeoff (Manim) | Two qualitative curves, then the financial agent walked across all three |
| B05 | B05_SpeedAndVisibility (Manim) | Three precedent line-marks, then two timelines on one axis |
| B06 | B06_TheQuestion (Manim) | Rope and reach; the question held alone |
| B07 | ClaudeVerdictArtifact (Remotion) | Blast-radius recap |
| B08 | ClaudeComposerAsk (Remotion) | Your Turn — mapping prompt + 3-item rubric |
| B09 | ClaudeTitleOutro (Remotion) | Title restate + @DivijPawar; subline is the source's own title-card question |

## Correction (post-build)

B00 was revised after the initial render to add an explicit self-introduction
and topic statement ("Hi — I'm Divij Pawar. This video is about how much
autonomy you should actually give an AI agent…") ahead of the existing hook,
per the house B00 cold-open rule: every reel's opening beat must have the
narrator say who they are and what the video covers, not just show the
welcome-screen UI — a returning-series viewer still needs the self-intro; it
is never assumed to carry over from a prior video. The original narration,
adapted directly from the source script's cold open, had no self-intro
convention and jumped straight into the hook. B00 audio, its Remotion render,
the compiled master, and captions were all regenerated to match.

## Free pipeline — no paid spend

Kokoro `am_onyx` (local, free) for all narration. No ElevenLabs, no FLUX, no
paid services. No publishing — the master stays in this folder.
