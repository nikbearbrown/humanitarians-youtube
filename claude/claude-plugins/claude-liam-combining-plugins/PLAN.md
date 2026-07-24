# PLAN — Claude, In Concert (Ch.13: Combining Plugins)

**Slug:** `claude-liam-combining-plugins` · **Channel:** claude-liam (Kore, Kokoro `af_kore`, free) · **Register:** Teardown
**Source:** `chapters/ch13-combining-plugins.txt` · **One idea:** *The real power isn't one plugin, it's a stack — research feeds marketing, data feeds product, sales feeds finance; combining plugins gives a solo operator the coordinated coverage of a whole team, as long as you keep each hand-off intentional.*

## Act map (spine)

```
B00  COLD OPEN  ClaudeComposerAsk — "If I install several plugins, do I have to tell Claude which one?" → ask lands answered ("No — Claude reaches for whatever fits"), Kore signs in "Sawubona — this is Kore, in for Humanitarians AI."
ACT I    How a Stack Works           infer-from-context, route, span-both, be-explicit    (B01 LayerStack, B02 Manim branch, B03 Manim accumulate, B04 VOX, B05 ChipGrid)
ACT II   Research Feeds Marketing     survey landscape → build into the gaps               (B06 SourceFlow, B07 Manim accumulate, B08 VOX, B09 contrast)
ACT III  Research Feeds Sales         meeting prep → tactical brief                         (B10–B11 VOX run R1, B12 Manim branch, B13 contrast)
ACT IV   The Loop Closes              data→marketing + support→product, one shape           (B14 SourceFlow, B15 Manim branch, B16 VOX, B17 contrast, B18 Manim accumulate/loop)
ACT V    Deal Preparation             sales + legal stack on a contract                     (B19 LayerStack, B20 Manim accumulate/merge, B21 VOX, B22 contrast)
ACT VI   Keep the Hand-off Intentional  four habits + custom-plugin + notice the gaps       (B23 ChipGrid, B24 Manim accumulate, B25 VOX, B26 spark)
V01  VERDICT   ClaudeVerdictArtifact — "Let's recap with Claude." (0.5s lead)
H01  YOUR TURN ClaudeComposerAsk "Your turn." — prompt read aloud + discussed
O01  OUTRO     ClaudeTitleOutro — title re-read "Claude, In Concert." + sign-off "Kore — in for Humanitarians AI."
```

## Lane histogram (body beats only; bookends exempt)

| Lane | Count | Share | Target | Verdict |
|---|---|---|---|---|
| VOX | 7 | 21.9% | 20–25% | ✓ |
| MANIM | 8 | 25.0% | 25–40% | ✓ (at floor; hand-off beats are Manim branch/accumulate) |
| REMOTION | 10 | 31.2% | 30–45% | ✓ |
| CARD | 7 | 21.9% | remainder | 6 segment cards + 1 spark (B26) |

Body beats: 32 · Total beats (with bookends): 36 · Est. runtime ≈ 5:30 (measured audio is the only clock).
Lint: no lane runs >2 consecutive outside the vox run; vox share inside 20–25% (no WARN).

## Vox runs
- **R1 (B10→B11):** "walk in prepared" (threshold of the meeting room) → "their world, your angle" (seated at the table). One continuous push in the same room grammar; `vox_run: "R1"` + handoff blocks authored in the sheet on both beats (non-last beat's handoff is the binding one). Run stays inside Act III (never crosses an act boundary), length 2 (≤3). All other lane boundaries are hard cuts.

## VOX stills (all Tier 1 illustrative — no rights escalation, no real people of note)
- B04 — one operator ringed by a whole team's output.
- B08 — one distinct figure apart from a uniform crowd (accent = the standout).
- B10 / B11 — meeting prep (doorway → table), vox_run R1.
- B16 — a maker building beside a board of pinned real notes/tickets.
- B21 — two parties at a negotiation table, contract between them.
- B25 — a hand reaching across a gap between two linked blocks (bridging arc drawn on at previz).

## Datable facts STRIPPED / corrected (DOUBLE-CHECK LAW; see book-level FACTCHECK.md — logged in SOURCES.md)
- **"How a T works" → "How a Stack Works"** — transcription artifact; treated as the chapter's stack/combination framing throughout (Act I title + narration).
- **"Cloud" / "clot" → "Claude"** — speech-to-text artifact, corrected in all narration.
- **No plugin count, no prices, no platform list** anywhere on screen or in narration (roster has grown past 11; count/prices/platforms would date the reel).
- **Domains treated as capabilities, not a fixed named roster** — "research skills," "the sales plugin engages," etc., framed as evergreen domain capability rather than asserting a specific catalog (FACTCHECK §2 flags that a generic "research plugin" is really `bio-research`; the market-research *workflow* the chapter teaches is real, so it's carried as a capability, not a product claim).
- **Named example company genericized** — source's invented "Green Tech Solutions" / "accounting firms" → generic "a prospect" / "a new service" (avoids any real-company dating and keeps examples fleeting).
- **Illustrative figures kept as examples** — "six months of performance," "top three pain points" framed as examples, never empirical claims.

## Gates
1. Plan (this doc) — **approve**.
2. Factcheck — inherits whole-book FACTCHECK.md; per-reel corrections in SOURCES.md.
3. **GATE P** — narration reviewed on an animated slate before any audio spend (Kokoro `af_kore`, free; no ElevenLabs).
4. Audio lock (Kokoro) → align → **SHOPPING.md** (7 vox stills, after audio lock) → **Gate D1** full-length slate previz → pantry fill → review cut → VISUAL QC LAW → `art final`.
