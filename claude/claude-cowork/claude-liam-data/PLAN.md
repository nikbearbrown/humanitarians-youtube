# PLAN — Claude, By the Numbers (Ch.7: The Data Plugin)

**Slug:** `claude-liam-data` · **Channel:** claude-liam (Liam, Kokoro `am_onyx`, free) · **Register:** Teardown
**Source:** `chapters/ch07-data.txt` · **One idea:** *Without the data plugin your numbers sit in spreadsheets you never open; with it Claude does data exploration and the unglamorous-but-essential data cleaning, then answers real questions (which clients are declining?) — but the analysis is only as trustworthy as the data and the assumptions, so you still own the judgment.*

## Act map (spine)

```
B00  COLD OPEN  ClaudeComposerAsk — "A year of revenue I never open — what's in it?" → ask lands answered, Liam signs in ("Olá — this is Liam, in for Bear.")
ACT I    The Unopened Spreadsheet   fear of your own data → the export/stare/close loop   (B01 illustration, B02 Manim loop, B03 VOX)
ACT II   Ask It Plainly             point-and-ask → natural-language querying → the gap    (B04 SourceFlow, B05 Onda code, B06 Manim divergence, B07 spark)
ACT III  What It Actually Does      explore · clean · visualize · compare                 (B08 ChipGrid, B09 SourceFlow, B10 Manim threshold, B11 VOX, B12 illustration, B13 Manim divergence)
ACT IV   The Monthly Habit          avoided question → monthly review → client concentration (B14 Onda code, B15–B16 VOX run R1, B17 Manim accumulate, B18 Onda code, B19 Manim threshold, B20 VOX)
ACT V    You Own The Judgment       trust = data x assumptions → verify → keep the call    (B21 PredictCard, B22 Manim divergence, B23 VOX drawon, B24 Manim accumulate)
V01  VERDICT   ClaudeVerdictArtifact — "Let's recap with Claude." (0.5s lead of silence)
H01  YOUR TURN ClaudeComposerAsk "Your turn." — data-review prompt read aloud + discussed; Liam signs off ("Liam, in for Bear.")
O01  OUTRO     ClaudeTitleOutro — title re-read "Claude, By the Numbers"
```

## Lane histogram (body beats only; bookends B00/V01/H01/O01 exempt)

| Lane | Count | Share | Target | Verdict |
|---|---|---|---|---|
| VOX | 6 | 20.7% | 20–25% | ✓ in band |
| MANIM | 8 | 27.6% | 25–40% | ✓ |
| REMOTION | 9 | 31.0% | 30–45% | ✓ |
| CARD | 6 | 20.7% | remainder | 5 segment cards + 1 spark (B07) |

Body beats: **29** · Total beats incl. bookends: 33 · Est. runtime ≈ 5:30 (measured audio is the only clock).

Consecutive-lane check: longest same-lane run is 2 (B04–B05 REMOTION, B08–B09 REMOTION, B15–B16 VOX-run). No WARN. VOX-run sameness is by contract.

## Lane rationale (data-heavy chapter)
- **MANIM leans on the four house patterns:** loop/accumulate (B02, B17, B24), divergence (B06, B13, B22), threshold (B10, B19). Scale-family standing in via the loop/accumulate framings. This chapter is about numbers moving, so mechanism beats are Manim.
- **Onda code-block** carries the three real plain-language queries (B05, B14, B18) — the plugin's actual interaction surface.
- **REMOTION** patterns: SourceFlow (B04, B09), ChipGrid (B08), PredictCard (B21), illustration (B01, B12) + the code-blocks.
- **VOX (6, Tier 1 stills):** B03 (closing the laptop), B11 (the unglamorous sort), B15+B16 (vox run R1), B20 (tracing the decline), B23 (the decision, drawon ring). All pantry stills + pantry_note, all Tier 1 illustrative (no real people, no rights escalation).

## Vox runs
- **R1 (B15→B16):** "five-minute conversation" → "first-of-the-month ritual." One continuous camera move: push into the operator at the laptop (B15), then pull back to reveal the first-of-month calendar (B16). Handoff blocks authored in the sheet (same room grammar, camera + object coords pinned). Run length 2, does not cross an act boundary (both in Act IV). ✓

## Datable facts STRIPPED / framed (DOUBLE-CHECK LAW; see book-level FACTCHECK.md)
- **No counts, no prices, no platform lists** anywhere on screen or in narration.
- **Database vendor list** (source names Postgres/BigQuery/Snowflake) → compressed to the generic mechanism "point Claude at your files"; the three products are never named. Direct-DB connection is treated as the minority path, not a listed roster.
- **Named third-party tools** (Stripe/QuickBooks) → generic "your payment processor," "your invoicing tool"; fleeting at most, never a beat's subject.
- **Percentages** (60% top-three, 40% single-client) → kept ONLY as clearly-framed illustrative example answers ("say, three clients are sixty percent…"; "if a single client is, say, forty percent…"), never stated as world-facts about the viewer.
- Transcription fixes applied (full list in SOURCES.md): "Cloud"→"Claude", "unglamerous"→"unglamorous", plus VLOOKUP, "sorted", "pivot tables", "impossible values", "solo operator", "Analyze my client data", "Iterate".

## Gates
1. Plan (this doc) — **approve**.
2. Factcheck — inherits whole-book FACTCHECK.md; per-reel corrections logged in SOURCES.md.
3. **GATE P** — full narration (B00 → O01) reviewed on an animated slate before ANY audio spend.
4. Audio lock (Kokoro am_onyx) → align (word clock) → **Gate D2** SHOPPING.md (Tier-0 `pantry_search.py` pass per vox still, then write from LOCKED durations) → **Gate D1** slate previz (`art run`) → pantry fill → review cut → VISUAL QC LAW → `art final`.
