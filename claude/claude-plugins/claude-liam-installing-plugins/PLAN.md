# PLAN — Claude, Configured (Ch.2: Installing and Customizing Plugins)

**Slug:** `claude-liam-installing-plugins` · **Channel:** claude-liam (Kore, Kokoro `af_kore`, free) · **Register:** Teardown
**Source:** `chapters/ch02-installing-customizing.txt` · **One idea:** *Installing a plugin is trivial — browse, click, done; the leverage is CUSTOMIZING it — teaching the plugin your voice, your process, your terms in a plain-language conversation until generic defaults become output built for your business.*

## Act map (spine)

```
B00  COLD OPEN  ClaudeComposerAsk — "Installing is easy. So where's the actual work?" → ask lands answered, Kore signs in
ACT I    Installing Is Easy       browse → click → ready → capabilities appear → upload    (C01, B01 REM grid, B02 Manim accumulate, B03 ChipGrid, B04 vox)
ACT II   Making It Yours          defaults are generic → customize is a CONVERSATION       (C02, B05 Manim divergence, B06 REM transform, B07 Manim loop, B08 vox)
ACT III  A Real Customization     the marketing session: your business → tuned output      (C03, B09 REM Q&A, B10–B11 VOX run R1, B12 ChipGrid, B13 Manim divergence)
ACT IV   Connecting Your Tools    self-contained vs connected; authorize, optional         (C04, B14 REM compare, B15 Manim threshold, B16 SourceFlow, B17 vox drawon)
ACT V    Living With Them         disable-preserves · updates · two-or-three · local · test (C05, B18 Manim toggle, B19 REM growth, B20 Manim scale, B21 vox, B22 Onda code, B23 spark)
V01  VERDICT   ClaudeVerdictArtifact — "Let's recap with Claude." (+0.5s lead)
H01  YOUR TURN ClaudeComposerAsk "Your turn." — prompt read aloud + discussed
O01  OUTRO     ClaudeTitleOutro — title re-read "Claude, Configured. Kore, in for Humanitarians AI."
```

## Lane histogram (body beats only; bookends B00/V01/H01/O01 exempt)

| Lane | Count | Share | Target | Verdict |
|---|---|---|---|---|
| VOX | 6 | 21.4% | 20–25% | ✓ (B04, B08, B10, B11, B17, B21) |
| MANIM | 7 | 25.0% | 25–40% | ✓ (B02, B05, B07, B13, B15, B18, B20) |
| REMOTION | 9 | 32.1% | 30–45% | ✓ (B01, B03, B06, B09, B12, B14, B16, B19, B22) |
| CARD | 6 | 21.4% | remainder | ✓ (5 segment cards C01–C05 + 1 spark B23) |

**Body beats: 28** · Est. runtime ≈ 5:30 (measured audio is the only clock).
No lane runs >2 consecutive (the only 2-in-a-row is the sanctioned vox run R1, B10→B11).

## Vox runs
- **R1 (B10→B11):** "the studio" → "the clients." One continuous push across the same room grammar — the web design studio (B10), then the small professional-services clients it now writes for (B11). Handoff blocks authored on both beats (camera x 0.40 → 0.60). Never crosses an act boundary; length 2 (≤3). All other lane boundaries are hard cuts.

## VOX pantry stills (all Tier 1 illustrative — no real people, no rights escalation)
- B04 — a shared file dropping into an upload slot.
- B08 — a hand on a tuning dial mid-turn (customization depth).
- B10 — a small one-person design studio (vox run R1).
- B11 — small professional-services offices, its clients (vox run R1).
- B17 — an authorize/permission moment (key/handshake); terracotta ring at previz.
- B21 — a single laptop on a desk (plugins are local).

## Datable facts STRIPPED (per whole-book FACTCHECK.md, DOUBLE-CHECK LAW)
- **No plugin count / roster.** "An official collection plus community additions," never "11 plugins." The count has already moved past 11.
- **No prices.** Never "$20/$100" — the chapter has no price beat, so none appears.
- **No platform list.** Never "Mac and Windows." Said "in your sessions" / "on your machine" instead (Cowork now also runs web + mobile).
- **Roadmap claim cut.** The book's "organization-wide plugin management is coming, but not yet fully available" is a dated roadmap line — dropped. B21 keeps only the evergreen fact: plugins are local to your machine.
- **"20 minutes" softened** to "a few minutes" — illustrative time, kept generic to avoid over-specifying.
- **Transcription fixes:** "Cloud" → "Claude"; "Co-Work" / "co-works" → "Cowork"; "in-current" → "keeping current / updates"; "ThropX official collection" → "an official collection." Logged in SOURCES.md.
- **Named third-party tools/formats** (CRM, database/warehouse, LinkedIn posts, newsletter, "viral video scripts," press releases) appear only as fleeting illustrative examples inside the customization dialogue — never as a beat's subject (FACTCHECK §4 allowance). "TikTok" avoided by name → "viral video scripts."

## Gates
1. Plan (this doc) — **approve**.
2. Factcheck — inherits whole-book FACTCHECK.md; per-reel notes in SOURCES.md.
3. **GATE P** — full narration (B00 → O01) reviewed on an animated slate before any audio. Channel claude-liam: Kokoro af_kore, free. No ElevenLabs.
4. Audio lock (Kokoro) → align writes the word clock.
5. **Gate D2** — tier-0 library pass (`pantry_search.py`) per VOX still (B04, B08, B10, B11, B17, B21), then SHOPPING.md from the LOCKED durations.
6. **Gate D1** — full-length SLATE PREVIZ (`art run`): slates in vox slots, Manim/Remotion rendered for real, `--review` burn-in.
7. Pantry fill → review cut (only changed slots recompile) → VISUAL QC LAW pass → `art final`. Never publishes.
