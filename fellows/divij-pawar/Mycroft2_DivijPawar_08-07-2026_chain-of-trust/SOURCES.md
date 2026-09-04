# SOURCES.md — chain-of-trust (Video 2)

All claims trace to `../context/video_script_2.md`, which continues the narrative from Video 1. This is a second-installment account. `B00` is a production addition (standard welcome/self-intro bookend), not from the script.

## Factual claims (DOUBLE-CHECK LAW)

| Beat | Claim | Source (video_script_2.md) |
|------|-------|----------------------------|
| B00 | Self-intro + series/topic framing | Production addition — standard Brutalist welcome bookend, mirrors Video 1's B00 pattern |
| B01 | Tagline recap from Video 1 | §0, "Last time I ended on this" |
| B01 | If we can't prove truth yet, what CAN we prove? | §0, "today's question" |
| B02 | LangFuse is an execution tracer — records what the system actually did | §1, "security camera on the AI" |
| B02 | A camera doesn't verify truth; it records action | §1, "doesn't know if you lied" analogy |
| B03 | Four-part chain: call the tool, data real, claim matches filing, reasoning caused answer | §2, "chain of proof" |
| B03 | Fourth link (reasoning causation) is unbuilt | §2, "That link doesn't exist yet" |
| B04 | Correlation ≠ causation: rooster crows before sunrise but doesn't cause it | §3, vignette 1 |
| B04 | Longer trace looks impressive but doesn't mean it's correct | §3, vignette 2 |
| B04 | Wrong audience access breaks the accountability rule | §3, vignette 3 |
| B05 | We can prove what the system did; we still can't prove it was right | §4, "honest ceiling" |
| B06 | Ablation: pull a fact out and see if the answer falls | §5, tool 1 (Jenga) |
| B06 | Interpretability: look inside the wiring (locked for frontier models) | §5, tool 2 (circuit + lock) |
| B07 | Calibration: grade track record over time, like weather forecasts | §6, tool 3 (forecaster) |
| B08 | Frontier models are closed boxes | §7, first blocker |
| B08 | Calibration requires real time, real predictions, no shortcuts | §7, second blocker |
| B08 | Building a fake-accountable system (dashboard, checkmark) is cheaper and faster | §7, third blocker |
| B09 | What's real: structure enforced, claims checked, behavior traceable | §8, PROVEN column |
| B09 | What's open: whether reasoning is genuine | §8, STILL OPEN column |
| B10 | Behavior is now observable (added to the original tagline) | §9, outro |

## Cross-reference to Video 1

- **B00:** New welcome/self-intro bookend, mirroring Video 1's B00 `ClaudeComposerAsk` pattern
- **B01:** Continues from `accountability-mesh/beat_sheet.json` B09 tagline
- **B05:** Mirrors Video 1 B06's framing ("proof of what ran, not proof it was right")
- **B06–B07:** Introduces three new research directions not covered in Video 1
- **B10:** Reuses Video 1's title and adds a second line to complete the tagline

## Simplifications and coverage

- **New tool (LangFuse):** Explained via security camera metaphor (B02). No technical internals; visual contrast does the explaining.
- **Three blockers (B08):** Simplified to "locked" / "time" / "cheaper fake" — not a deep technical dive, just the constraints.
- **Three forward paths (B06–B07):** Condensed to visual metaphors (Jenga, lock, forecast). Full research details deferred.

## Scene/beat map

| Beat | Scene / Source | Type |
|------|----------------|------|
| B00 | ClaudeComposerAsk | Remotion — welcome screen + self-intro |
| B01 | B01_ChainOpen | Manim — Video 1 B09 card cracks open |
| B02 | B02_SecurityCamera | Manim — split screen (foggy vs. sharp) |
| B03 | B03_ChainOfTrust | Manim — four links, last broken |
| B04 | B04_ThreeWaysFooled | Manim — three vignettes |
| B05 | B05_HonestCeiling | Manim — text card + slow zoom |
| B06 | B06_ToolboxPartOne | Manim — toolbox, two tools, one slot empty |
| B07 | B07_ToolboxPartTwo | Manim — continues B06, tool 3 slides in, closes |
| B08 | B08_WhatsHoldingUsBack | Manim — three quick vignettes |
| B09 | B09_Scorecard | Manim — two-column table |
| B10 | ClaudeTitleOutro | Remotion — title + handle + paired tagline |

## Free pipeline — no paid spend

Kokoro `am_onyx` (local, free) for all narration. No ElevenLabs, no FLUX, no paid services. No publishing — master stays in the reel folder.
