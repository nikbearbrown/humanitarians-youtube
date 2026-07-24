# PLAN — Claude, Shipping (Ch.9: The Product Plugin)

**Slug:** `claude-liam-product` · **Channel:** claude-liam (Liam, Kokoro `am_onyx`, free) · **Register:** Teardown
**Source:** `chapters/ch09-product.txt` · **One idea:** *The product plugin helps you build and ship — turning scattered feedback and analytics into prioritized decisions (specs, roadmaps, release notes) — but prioritization is a judgment call the plugin accelerates, not one it makes for you.*

## Act map (spine)

```
B00  COLD OPEN  ClaudeComposerAsk — "How do I decide what to build next?" → ask lands answered, Liam signs in ("Annyeong — this is Liam, in for Bear.")
ACT I    The Missing Product Team   solo builder has no PM → the four questions       (B01 PredictCard, B02 vox, B03 Manim divergence, B04 illustration, B05 ChipGrid)
ACT II   What It Makes              five deliverables → idea becomes a spec           (B06 ChipGrid, B07 SourceFlow, B08 vox spec)
ACT III  Break It Into Stories      spec → testable stories → build story by story    (B09 Manim branch, B10 Onda code-block, B11 Manim accumulate)
ACT IV   What Should I Build Next   ten ideas/few hours → rank feedback → loud vs common   (B12 Manim scale, B13 Manim rank, B14–B15 VOX run R1, B16 Manim compare)
ACT V    Ship It, Remember Why      release notes user-benefit → decision docs        (B17 Manim transform, B18 vox reader, B19 illustration, B20 PredictCard)
ACT VI   Who Makes the Call         it accelerates → it ranks, you decide             (B21 ChipGrid, B22 Manim converge/gate, B23 vox drawon, B24 spark)
V01  VERDICT   ClaudeVerdictArtifact — "Let's recap with Claude." (0.5s lead)
H01  YOUR TURN ClaudeComposerAsk "Your turn." — prioritization prompt read aloud + discussed
O01  OUTRO     ClaudeTitleOutro — title re-read "Claude, Shipping." + "Liam, in for Bear."
```

## Lane histogram (body beats only; bookends B00/V01/H01/O01 exempt)

| Lane | Count | Share | Target | Verdict |
|---|---|---|---|---|
| VOX | 6 | 20.0% | 20–25% | ✓ at floor of band |
| MANIM | 8 | 26.7% | 25–40% | ✓ |
| REMOTION | 9 | 30.0% | 30–45% | ✓ (largest lane, as intended) |
| CARD | 7 | 23.3% | remainder | 6 segment cards + 1 spark (B24) |

Body beats: **30** · Est. runtime ≈ 5:30 (measured audio is the only clock).
No lane runs 3+ consecutive (the only 2-in-a-row VOX pair is the intended R1 run).

## Vox runs
- **R1 (B14→B15):** "a wall of voices" → "common beats loud." One continuous push from the busy corner of a feedback board into the single recurring note; handoff block authored in the sheet (camera x0.4/y0.5, scale 1.6 → 2.1). Stays inside Act IV; 2 beats.
- All other VOX beats (B02, B08, B18, B23) are standalone — hard cuts on every lane boundary.

## Datable facts STRIPPED / COMPRESSED (per whole-book FACTCHECK.md §3–§4)
- **Analytics tool names** (Amplitude, Mixpanel, PostHog) — kept as at most ONE fleeting spoken example if used; NEVER an on-screen list and never a beat's subject. The plan carries the *mechanism* ("point it at your feedback and usage data") not the vendor roster.
- **PM-tool roster** (Jira/Linear/Notion/GitHub issues) — genericized to "your project-management tool"; no platform list on screen.
- **Third-party build tools** — "cursor/bolt" → "an AI coding tool"; "Clerk" → "an outside service" (build-vs-buy stays evergreen).
- **No plugin counts, no prices, no platform lists** anywhere on screen or in narration.
- Transcription fixes applied (see SOURCES.md): "Cloud" → "Claude", "mix panel" → Mixpanel, "post-hog" → PostHog, "hedge cases" → edge cases.
- Source file's internal header ("Chapter 7. Product") is a mislabel — this is **Ch.9** in the book; not surfaced on screen.

## Gates
1. Plan (this doc) — **approve**.
2. Factcheck — inherits whole-book FACTCHECK.md; per-reel notes in SOURCES.md.
3. **GATE P** — narration reviewed on animated slate before any audio.
4. Audio lock (Kokoro) → align → Gate D2 SHOPPING.md (6 vox stills, all Tier 1) → Gate D1 previz → pantry fill → review cut → VISUAL QC → final.
