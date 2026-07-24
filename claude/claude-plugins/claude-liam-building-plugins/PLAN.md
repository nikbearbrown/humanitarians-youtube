# PLAN — Claude, Built (Ch.12: Building Your Own Plugins)

**Slug:** `claude-liam-building-plugins` · **Channel:** claude-liam (Liam, Kokoro `am_onyx`, free) · **Register:** Teardown
**Source:** `chapters/ch12-building-your-own.txt` · **One idea:** *The official plugins cover common functions, but when none fits your specific workflow you can build your own — bundling your skills, connectors, commands, and subagents into an installable package; a guided, low/no-code path whose discipline is scoping it to a real repeated workflow, not building for its own sake.*

## Act map (spine)

```
B00  COLD OPEN  ClaudeComposerAsk — "None of the official plugins fit how I work. Can I build one?" → ask lands answered, Liam signs in ("Hej — this is Liam, in for Bear.")
ACT I    Why Build Your Own    generic catalog → your specific process; the transfer   (B01 illustration, B02 Manim transfer, B03–B04 VOX run R1, B05 Manim converge)
ACT II   What's Inside         four components; a plugin is a folder of text           (B06 ChipGrid, B07 Onda folder code-block, B08 VOX skills, B09 Onda commands code-block, B10 SourceFlow connectors, B11 Manim subagents fan-out)
ACT III  How You Build It      conversation not code; the four steps                   (B12 illustration, B13 VOX describe, B14 Manim accumulate 4 steps, B15 LayerStack assemble, B16 Manim hours→minutes)
ACT IV   What to Build For     the four signals; leverage vs. judgment                 (B17 ChipGrid signals, B18 VOX "hand this off", B19 Manim replicate, B20 Manim divergence, B21 spark)
ACT V    Share & Evolve        share out, adopt in, living document                    (B22 SourceFlow share, B23 VOX peers, B24 Manim evolve, B25 illustration check-first)
V01  VERDICT   ClaudeVerdictArtifact — "Let's recap with Claude." (+0.5s lead)
H01  YOUR TURN ClaudeComposerAsk "Your turn." — prompt read aloud + discussed
O01  OUTRO     ClaudeTitleOutro — title re-read "Claude, Built" (Liam, in for Bear)
```

Acts open on a segment card (Title Case serif); the viewer always knows the position in the film.

## Lane histogram (body beats only; bookends B00/V01/H01/O01 exempt)

| Lane | Count | Share | Target | Verdict |
|---|---|---|---|---|
| VOX | 6 | 20.0% | 20–25% | ✓ at target |
| MANIM | 8 | 26.7% | 25–40% | ✓ |
| REMOTION | 10 | 33.3% | 30–45% | ✓ |
| CARD | 6 | 20.0% | remainder | 5 segment cards + 1 spark |

Body beats: **30** · Est. runtime ≈ 5:30 (measured audio is the only clock).
No lane runs past 2 consecutive beats except inside vox run R1 (allowed).

## Structural-chapter lane rationale
This chapter is about the four components *structurally*, so REMOTION carries the mechanism: **ChipGrid** names the parts (B06) and the signals (B17); **Onda code-block** shows real file/structure content — the plugin folder tree (B07) and the slash commands (B09); **SourceFlow** shows connectors reaching real tools (B10) and the plugin traveling outward (B22); **LayerStack** shows spoken answers assembling into parts (B15). MANIM carries every moving-data beat (transfer, converge, subagents fan-out, 4-step accumulate, hours→minutes compress, replicate, admin-vs-judgment divergence, evolve). VOX carries the human stakes (the solo operator, documented craft, describing aloud, "hand this off," peers adopting).

**ILLUSTRATE LAW / prose-as-code guard:** the only Onda code-blocks are B07 (real folder tree) and B09 (real slash-command tokens). The conversational describe-prompt is prose, so it is NOT boxed as code — it lands as narration over the B12 "conversation-not-code" illustration and the B13 vox still.

## Vox runs
- **R1 (B03→B04):** the solo operator, wide → push in to the method in their head/notebook. One continuous ease-out move; handoff block authored on B03 (camera + `operator` object) pinning B04's first frame. Run stays inside Act I; 2 beats. All other lane boundaries are hard cuts.

## Datable facts STRIPPED (DOUBLE-CHECK LAW; per whole-book FACTCHECK.md) — logged in SOURCES.md
- Source "the 11 official plugins" → **"the official catalog"** (no count — roster has grown past 11).
- Source "plugin directory at Claude.com/plugins" → **"the wider directory"** (URL dropped; no platform/URL that dates).
- No prices, no platform list, no plugin count anywhere on screen or in narration.
- Named tools kept generic ("your pricing spreadsheet," "a specific folder") — no third-party brand names.
- The building tool named only as **"a guided builder — itself a plugin you install"** (mechanism, not a versioned product string).

## Gates
1. Plan (this doc) — **approve**; lane histogram lints clean (VOX 20%).
2. Factcheck — inherits whole-book FACTCHECK.md; per-reel corrections in SOURCES.md.
3. **GATE P** — narration reviewed on animated slate before any audio spend (Kokoro `am_onyx`, free; no ElevenLabs).
4. Audio lock (Kokoro) → align → **SHOPPING.md** (Gate D2, after lock; vox stills B03/B04/B08/B13/B18/B23) → **Gate D1 slate previz** → pantry fill → review cut → VISUAL QC → `art final`.
