# Caching Pixels You've Already Seen — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-quickstarts/screenshot-prompt-caching`,
a Teardown-register scaffold: B00 `ClaudeComposerAsk` cold open stating the
numbers directly, B01–B04 body fully narrated as Manim/GRAPHIC beats, B05
verdict card and B06 your-turn drafted but never rendered (SLATE), B07 outro
drafted but never rendered, plus three abandoned BOOKEND placeholder slates
BVDT/BHTF/BOUT carrying only generic template text, never reconciled with the
earlier beats). Register: **Plain**. 8 beats. Carry-out written first
(CARRY-OUT.md, GATE C).*

**Duplicate-source note:** the same underlying facts were already built once
as `hai-simple/claude-basics--screenshot-prompt-caching` from a different
source-sheet path. See QUESTION.md for why this is a second, independently
sourced redo rather than a re-run — narration here is fresh throughout.

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no
generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "You'd guess a screenshot Claude's already seen costs nothing to resend. It doesn't — the API re-tokenizes it fresh, every single time, unless you flag it as one it's seen before." | Writer types "If Claude already\nsaw this screenshot,\ndoes sending it\nagain cost nothing?"; "nothing" hesitates and corrects to "the same" |
| B01 | 1 stakes / wrong guess | A computer-use agent takes a screenshot on every turn of a fifty-turn task. Most of those turns, nothing on the desktop has actually changed — a dialog is still open, a progress bar is still crawling. The agent sends the identical image anyway, and by default the API tokenizes it again from scratch, at roughly two thousand tokens a screenshot. Thirty-five of the fifty turns repeat a screenshot the API has already been billed for once. | the naive loop: 50 turn-slots, a dialog and a progress bar shown unchanged across several, 35 marked as repeats, a token counter climbing |
| B02 | setup — ANCHOR PLANTED | Make it concrete. Across those fifty turns the desktop only ever looks like one of five distinct states — call them A through E. Without caching, the API doesn't know that turn twelve looks exactly like turn three: it bills every one of the fifty screenshots at full price. Fifty times two thousand tokens is one hundred thousand tokens, to describe a screen that only actually changed five times. | THE ANCHOR — a 50-frame filmstrip, states A–E repeating, every frame billed the same, a counter climbing to "100,000 tokens" |
| B03 | 3 mechanism | The fix is a single field on the image block: cache underscore control, type ephemeral. Send a screenshot with that flag the first time its exact pixels appear, and the API caches it. Send the identical screenshot again with the same flag, and it's a cache hit — recognized instantly, tokenized for next to nothing. Nothing about what you send changes; what changes is whether the API has to read it again. | the JSON field typing itself onto an image block; a first-sighting screenshot flagged, an identical repeat landing as a "HIT" |
| B04 | 4 ANCHOR PAYOFF — both directions | Back to the fifty-turn task: five unique states means five cache misses and forty-five hits. Five times two thousand is ten thousand tokens, not one hundred thousand — ninety percent saved. But this is the screenshot case only: it doesn't cover the full caching protocol, minimum cacheable size, or eviction rules, and the cache itself doesn't last forever. Switch API keys, or leave the task idle too long, and the very next screenshot is a miss again — whether or not the picture actually changed. | THE ANCHOR RETURNS — the same filmstrip, 5 miss-frames in terracotta, 45 hit-frames in teal, counter dropping to "10,000 tokens"; a struck card noting scope limits |
| **BCRY** | **6 carry-out** | Claude doesn't know a screenshot repeats until you tell it to remember one — and that memory only lasts until the picture, or the session, changes. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. "My computer-use agent resends an identical screenshot up to thirty-five times across a fifty-turn task. Add ephemeral prompt caching to the screenshot blocks and report the token cost with and without it." Then ask it the harder question: what happens if the screenshot changes by one pixel — does a naive cache check still call that a hit? Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Caching Pixels You've Already Seen. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-quickstarts`, Teardown metadata) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Caching Pixels You've Already Seen." | unchanged |
| Facts | 50-turn task, 35 identical repeats; ~2,000 tokens/screenshot; `cache_control: {"type":"ephemeral"}`; concrete case 5 unique states A–E → 10,000 tokens cached vs. 100,000 uncached, 90% savings; exclusions (full protocol, minimum thresholds, eviction, session-only persistence) | unchanged |
| Beat count | 8 beats total: B00 cold open (SLATE, never rendered), B01–B04 body (filled, Manim), B05 verdict (SLATE), B06 your-turn (SLATE), B07 outro (SLATE); plus 3 abandoned BOOKEND placeholders (BVDT/BHTF/BOUT) never reconciled | 8 (B00 writer + 4 body + BCRY + BHTF + BOUT) — source's B05 verdict recap dropped as a restatement of B01–B04 (Plain register carries no separate verdict beat); source's B04 exclusions clause folded into this reel's B04 both-directions clause; the abandoned bookend placeholders are not carried forward (their artifactLines were unfilled template stubs, never real content) |
| B00 | `ClaudeComposerAsk`, never rendered (SLATE) — stated the token-savings numbers directly, no wrong-guess framing | `BrutalistHesitantWriter` (WRITER LAW) — reframed as the question the body falsifies (resending an identical image costs nothing vs. costs the same) |
| Register | Teardown (metadata `register: "Teardown"`), narration itself carried no design verdict | Plain — explicit no-judgment audit below |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| Close | `ClaudeTitleOutro`, `@NikBearBrown`, never rendered | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| Handoff prompt | source B06 (SLATE): screenshot-caching-wrapper prompt, near-identical facts | same underlying ask, reworded, plus the pixel-change follow-up question |

No source beat was `ai-video-prompt`, pantry, or a human-drop slot — every
drafted beat was already `ClaudeComposerAsk`/`ClaudeVerdictArtifact`/
`ClaudeTitleOutro` (Remotion) shapes, most simply unbuilt (SLATE) — so the
NO-GENAI/NO-PANTRY LAW required no substitution beyond B00 (already covered
by WRITER LAW).

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01; mechanism waits until B03 |
| Wrong guess surfaced, falsified by a case | B00/B01 state the guess (repeats cost nothing); B02's anchor is the falsifying case (50 billed screenshots for a screen that changed 5 times) |
| One anchor, planted early, paid off late | B02 plants the 100,000-token uncached bill (5 states, 50 turns); B04 pays it off (10,000 tokens, 90% saved) |
| Both directions | B04 — this screenshot case doesn't cover the full caching protocol (a savings result here doesn't prove the general protocol is handled); the cache not surviving a key switch or idle gap means a miss on a later turn doesn't prove the picture changed |
| No design judgment | B03–B04 describe why the flag works; nothing rules on whether computer-use is the right tool for a task, or whether Anthropic priced caching well |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not a savings guarantee.** The 90% figure is this reel's worked case (5
  unique states out of 50 turns), not a promise for every deployment.
- **Not the full caching protocol.** Minimum cacheable token thresholds and
  eviction policy are explicitly out of scope (B04's both-directions clause).
- **Not permanent.** The cache holds for a session; an API-key switch or a
  long idle gap empties it regardless of whether the screenshot changed.
- **Not a claim about partial matches.** Whether a naive cache check
  correctly treats a one-pixel-different screenshot as a miss is left as the
  open question in the handoff prompt, not asserted either way.

## Handoff prompt (BHTF, read aloud)

> "My computer-use agent resends an identical screenshot up to thirty-five
> times across a fifty-turn task. Add ephemeral prompt caching to the
> screenshot blocks and report the token cost with and without it."

Why it's worth running: it turns the reel's one-field fix into working code,
and a good answer should surface the harder case the reel flags but doesn't
solve — a screenshot that changed by even one pixel, which a naive hash-based
cache check might still call a hit (or a naive "same turn count" check might
still call a miss).

---
**GATE P — signed:** ______________________  (human)
