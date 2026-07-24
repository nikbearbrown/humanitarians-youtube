# PLAN — Claude, On Call (Ch.10: The Support Plugin)

**Slug:** `claude-liam-support` · **Channel:** claude-liam (Kore, Kokoro `af_kore`, free) · **Register:** Teardown
**Source:** `chapters/ch10-support.txt` (~560 words — the book's shortest chapter) · **One idea:** *If you have customers you have support; the support plugin drafts consistent, on-brand responses and turns recurring questions into reusable answers — a force multiplier for a small team, with the human staying on the judgment calls and the angry-customer edge cases.*

Duration is an OUTPUT: a 560-word chapter yields a short reel. Target landing ~4:00, **do not pad**. 24 body beats at the genre's lower end.

## Act map (spine)

```
B00  COLD OPEN  ClaudeComposerAsk — "Can Claude lighten support, or just add a queue to check?" → ask lands answered; "Jambo — this is Kore, in for Humanitarians AI."
ACT I    The Reactive Burden    customers → support; reactive burden → process; team consistency   (B01 vox, B02 Manim transform, B03 Manim converge)
ACT II   What It Does           triage · draft · knowledge base · sentiment; connect + configure     (B04 ChipGrid, B05 triage, B06 Manim converge, B07 sentiment, B08 vox KB, B09 connect, B10 configure)
ACT III  A Day on Support       morning triage → frustrated customer → FAQ from patterns            (B11 Onda code, B12 Manim compress, B13–B14 VOX run R1, B15 Manim accumulate, B16 SourceFlow)
ACT IV   You Stay on the Line    draft-don't-autosend · build progressively · patterns are feedback   (B17 ChipGrid, B18 vox drawon, B19 Manim loop, B20 spark)
V01  VERDICT   ClaudeVerdictArtifact — "Let's recap with Claude." (0.5s lead)
H01  YOUR TURN ClaudeComposerAsk "Your turn." — prompt read in full + discussed; sign-off "Kore, in for Humanitarians AI."
O01  OUTRO     ClaudeTitleOutro — title re-read "Claude, On Call."
```

## Lane histogram (body beats only; bookends B00/V01/H01/O01 exempt)

| Lane | Count | Share | Target | Verdict |
|---|---|---|---|---|
| VOX | 5 | 20.8% | 20–25% | ✓ |
| MANIM | 6 | 25.0% | 25–40% | ✓ (at floor) |
| REMOTION | 8 | 33.3% | 30–45% | ✓ |
| CARD | 5 | 20.8% | remainder | 4 segment cards + 1 spark (B20) |

Body beats: **24** · Est. runtime ≈ **4:00** (measured audio is the only clock). No lane runs >2 consecutive (the one 2-beat repeat, B13→B14, is the intended vox run).

## Vox beats (all Tier 1 illustrative — no real people, no rights escalation)
- **B01** overnight inbox in a dark room (customers mean support).
- **B08** scattered notes gathering into a bound FAQ (experience, structured).
- **B13 → B14** VOX RUN R1: frustrated customer at a declined-payment screen → pull back to the drafted reply on the desk. One continuous push; handoff block on B13, B14 is the run's final beat.
- **B18** person reviewing a draft before send, hand near send; terracotta underline drawn on at previz.

## Vox runs
- **R1 (B13→B14):** "three failed payments" → "you add the human line." One continuous camera move across a single desk scene; handoff camera/objects serialized on B13. Does not cross an act boundary; length 2 (≤3). Every other lane boundary is a hard cut.

## Datable facts STRIPPED (DOUBLE-CHECK LAW; see book-level FACTCHECK.md, logged in SOURCES.md)
- **"Cloud" → "Claude"** everywhere (speech-to-text artifact: "Cloud categorizes / produces / identifies / captures").
- **Named support platforms** (Zendesk, Intercom, FreshDesk, Help Scout) — **cut from screen and narration**; compressed to "the support tools you already use" / "your existing inbox" (B09). Vendor lists date the reel.
- **No counts, no prices, no platform lists** anywhere on screen or in narration (none in this chapter to begin with — kept clean).
- Illustrative story numbers KEPT as story specifics, not on-screen product claims: "last 12 hours," "thirty minutes / two hours," "top ten," "three times," "two years," "this quarter." Framed as examples per FACTCHECK §1 row 9.

## Gates
1. Plan (this doc) — **approve**.
2. Factcheck — inherits whole-book FACTCHECK.md; per-reel notes in SOURCES.md.
3. **GATE P** — narration reviewed on an animated slate before any audio spend.
4. Audio lock (Kokoro `af_kore`) → align → Gate D2 SHOPPING.md (5 vox stills, from LOCKED durations) → Gate D1 full-length slate previz → pantry fill → review cut → VISUAL QC LAW → `./art final`.
