# SOURCES.md — what-makes-ai-agentic

Primary source: `01_what_makes_an_ai_agentic.md` (the authored script, with
inline `[VISUAL: …]` stage directions) and `01_narration_tts_ready.txt` (the
TTS-normalized narration derived from it). Both live in this folder.

This is an explanatory piece about general AI-system architecture, not a
first-person project account — so the claims below are checked against
common industry description rather than against a project's own files.

## Factual claims (DOUBLE-CHECK LAW)

| Beat | Claim | Verdict | Basis |
|------|-------|---------|-------|
| B00 | Products marketed "agentic" span from trivial to genuinely autonomous | ✓ | Observable across current product marketing; stated as the reel's premise, not as data |
| B02 | A tier-0 system produces text by predicting the next likely token, repeatedly | ✓ | Standard description of autoregressive language-model decoding |
| B02 | Tier 0 has no browser, no search, no payment capability | ✓ | True by definition of the tier — no tools bound |
| B03 | "Function calling" / "tool use" is the industry term for tier-1 behaviour | ✓ | Consistent naming across major model provider APIs |
| B03 | The tier-1 sequence is recognize → format → wait → use | ✓ | Describes the standard tool-call round trip |
| B03 | Control returns to the human after one tool call | ✓ | True by definition of the tier — no chaining |
| B04 | Tier 2 chains several tools and adapts the plan to what it finds | ✓ | Describes the common multi-step agent loop |
| B04 | Tier 2 checks back with the human before irreversible spend | ✓ | Stated as the tier's *bound*, i.e. what makes it tier 2 rather than 3 |
| B05 | Tier 3 requires memory persisting across separate sessions | ✓ | Definitional — this is the property that separates 3 from 2 |
| B05 | Tier 3 acts over hours/days without step-by-step supervision | ✓ | Definitional |
| B06 | Most products sold as "agentic" sit in tier 1 or tier 2 | ⚠ **judgment** | An editorial assessment, not a measured statistic. Narrated with the hedge "comfortably sits," never as a percentage. Declared here per DOUBLE-CHECK LAW |
| B06 | True tier 3 is rare and still being figured out | ⚠ **judgment** | Same — an assessment of the state of the field, deliberately undated and unquantified |

## Anti-staleness check (DOUBLE-CHECK LAW)

The narration names **no model, no vendor, no version number, no benchmark
score, and no count that drifts**. The flight-booking example is generic. The
reel should not date.

One vendor name survives inside a quoted tier-0 reply ("Try Google Flights…")
— it is quoted as an example of the kind of advice a tier-0 system gives, not
as a claim about a product, and it carries no capability assertion.

## Simplifications (declared)

- **Four discrete tiers are a teaching device, not a taxonomy.** Real systems
  sit between and across them. The reel says so explicitly in B07 ("it's a
  spectrum"), so the simplification is disclosed inside the video rather than
  only here.
- **Tier 0's mechanism is compressed to next-token prediction.** Sampling,
  instruction tuning, and RLHF are all omitted. Correct at this level of
  technicality and not load-bearing for the tier distinction.
- **Memory in tier 3 is treated as a single property.** Real implementations
  differ (retrieval, summarization, scratchpads, fine-tuning). The reel's
  claim is only that *something* carries across sessions, which holds
  regardless of implementation.
- **Tier 2's "checks in before spending your money" is normative.** Some
  tier-2 systems do spend without asking. The reel presents the check-in as
  the tier's defining bound, which is the pedagogically useful framing and is
  consistent with how B06's third question is posed.

## Content cut from the source script

| Source | Cut | Why |
|---|---|---|
| ¶19 — "…that's exactly what's up next" | Cut | Next-video tease. No publishing machinery in this toolkit; OUTRO LAW locks B09 to a title restate. Series relationship preserved via `metadata.series` |
| ¶12 — trailing clause "…which happens to be an entire video on its own" | **Partially cut** | The judgment that opens the sentence ("This is genuinely powerful — and genuinely risky") IS carried, at the end of B05. Only the trailing cross-promo clause is dropped, for the same reason as ¶19 — it points at a video the viewer has no on-screen way to reach |
| `[VISUAL]` end card — "subscribe prompt, two thumbnail cards" | Cut | Same reason |
| `[VISUAL]` title card — "swirling tech-blue background" | Rebuilt | Blue is removed from every palette in this toolkit; the reel is on the Claude fidelity palette (cream / warm ink / one terracotta accent). Rebuilt as the four-tier spectrum bar |
| `[VISUAL]` B05 — corner thumbnail "Why Agents Fail →" | Cut | Same as the end card — a YouTube cross-promo device, no beat home |

## Scene / beat map

| Beat | Scene / pattern | Notes |
|------|------------------|-------|
| B00 | ClaudeComposerAsk (Remotion) | Cold open — the marketing claim and its two failure directions |
| B01 | B01_TierSpectrum (Manim) | BLUF — four-segment bar, task chip fixed |
| B02 | B02_TierZero (Manim) | Chat with tools locked out; token-by-token prediction |
| B03 | B03_TierOne (Manim) | One round trip to a tool API, control handed back |
| B04 | B04_TierTwo (Manim) | Flowchart builds step by step, conflict found, hard stop |
| B05 | B05_TierThree (Manim) | Monitor→Decide→Act→Remember ring, days ticking, memory persisting |
| B06 | B06_TheChecklist (Manim) | Three questions, then the bracket over tiers 1–2 |
| B07 | ClaudeVerdictArtifact (Remotion) | Four-tier recap |
| B08 | ClaudeComposerAsk (Remotion) | Your Turn — audit prompt + 3-item rubric |
| B09 | ClaudeTitleOutro (Remotion) | Title restate + @DivijPawar |

## Correction (post-build)

B00 was revised after the initial render to add an explicit self-introduction
and topic statement ("Hi — I'm Divij Pawar. This video is about what actually
makes an AI 'agentic'…") ahead of the existing hook, per the house B00
cold-open rule: every reel's opening beat must have the narrator say who they
are and what the video covers, not just show the welcome-screen UI — a
returning-series viewer still needs the self-intro; it is never assumed to
carry over from a prior video. The original narration, adapted directly from
the source script's cold open, had no self-intro convention and jumped
straight into the hook. B00 audio, its Remotion render, the compiled master,
and captions were all regenerated to match.

## Free pipeline — no paid spend

Kokoro `am_onyx` (local, free) for all narration. No ElevenLabs, no FLUX, no
paid services. No publishing — the master stays in this folder.
