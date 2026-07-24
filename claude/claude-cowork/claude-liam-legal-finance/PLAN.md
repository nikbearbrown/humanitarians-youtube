# PLAN — Claude, Counsel (Ch.11: The Legal and Finance Plugins)

**Slug:** `claude-liam-legal-finance` · **Channel:** claude-liam (Kore, Kokoro `af_kore`, free) · **Register:** Teardown
**Source:** `chapters/ch11-legal-finance.txt` · **One idea:** *Legal and finance are the two "essentials" that protect a small operator — legal flags the concerning clause before you sign, finance models the scenario before you commit — but both only screen and accelerate; the consequential call stays with a human (and a real lawyer/CFO for real stakes).*

This chapter covers **TWO separate official plugins** merged by the book into one chapter. It ships as **one episode**: legal gets its own two acts (screener + hard limit), finance gets its own two acts (accelerator + hard limit), bracketed by a shared-pattern setup and a shared-habits close. See SOURCES.md for the separate-plugins note.

## Act map (spine)

```
B00  COLD OPEN  ClaudeComposerAsk — "Which two plugins protect a one-person business?" → ask answered, Kore signs in ("Shalom")
ACT I    The Shared Pattern    busy-not-careless → screen + accelerate, first-pass    (C01, B01 PredictCard, B02 vox, B03 ChipGrid, B04 Manim filter)
ACT II   The Legal Plugin      a screening tool → color flags → what it does          (C02, B05 vox drawon, B06 Onda code, B07 Manim flags, B08 ChipGrid, B09 Manim threshold)
ACT III  Not a Lawyer          four limits → screen vs counsel → triage               (C03, B10 ChipGrid, B11–B12 VOX run R1, B13 Manim branch)
ACT IV   The Finance Plugin    analysis you do → burn/runway → scenario modeling      (C04, B14 vox, B15 Onda code, B16 ChipGrid, B17 Manim depletion, B18 Manim scenario)
ACT V    Not a CFO             four limits → assumptions are yours → call stays human (C05, B19 ChipGrid, B20 vox drawon, B21 Manim branch)
ACT VI   Make It Routine       three habits → early is cheapest → keep it findable    (C06, B22 triptych, B23 Manim growth, B24 vox)
V01  VERDICT   ClaudeVerdictArtifact — "Let's recap with Claude." (0.5s lead)
H01  YOUR TURN ClaudeComposerAsk "Your turn." — prompt read aloud in full + discussed
O01  OUTRO     ClaudeTitleOutro — title re-read "Claude, Counsel"
```

The two hard-limit caveats are load-bearing and each land as their OWN act, with a spark beat inside:
- **Legal is a SCREENING tool, not a lawyer** — ACT III (B10 the four things it won't do; B11–B12 "screen catches the obvious / counsel tells you whether to sign"; B13 triage/escalate).
- **Finance is an analysis ACCELERATOR, not a CFO** — ACT V (B19 the four things it won't do; B20 "the judgment is yours"; B21 "the call stays human, real stakes → real accountant").

## Lane histogram (body beats only; B00/V01/H01/O01 exempt)

| Lane | Count | Share | Target | Verdict |
|---|---|---|---|---|
| VOX | 7 | 23.3% | 20–25% | ✓ mid-band |
| MANIM | 8 | 26.7% | 25–40% | ✓ (finance modeling carries the moving-data load) |
| REMOTION | 9 | 30.0% | 30–45% | ✓ at floor; ChipGrid/PredictCard/SourceFlow-family + 2 Onda code-blocks |
| CARD | 6 | 20.0% | remainder | 6 segment cards, one per act |

Body beats: **30** · Content beats B01–B24 = 24 + 6 act cards. Est. runtime ≈ 5:00 (measured audio is the only clock).

Lane sequence (body): `C R V R M C V R M R M C R V V M C V R R M M C R V M C R M V` — no run of 3+ same lane; the only consecutive-VOX pair is the authored run R1 (B11→B12).

## Vox runs
- **R1 (B11→B12):** "the screen catches the obvious problem" → "outside counsel tells you whether to sign." One continuous push from a flagged clause under a magnifier (B11) across to a professional marking up the contract (B12), same room grammar. Handoff block authored on B11 (camera + object), mirrored on B12. This is the ONE 2-beat vox run; every other VOX beat is a hard cut.

## VOX stills (all Tier 1 illustrative — no real people, no logos, no real party names/figures)
`B02` signing a stack in a hurry · `B05` contract page, one clause (terracotta highlight drawon) · `B11` clause under a magnifier (R1 start) · `B12` professional marking up contract (R1 end) · `B14` operator at night over statements · `B20` person paused over a decision (terracotta ring drawon) · `B24` two labeled folders on a tidy desk.

## Manim scenes (moving data; build from animated_graphics.py, cream stage, ink + one terracotta)
`coverage_net_firstpass` (filter) · `legal_flag_counts` (state, green/yellow/red — tallies illustrative) · `threshold_hours_to_minutes` (threshold) · `branch_routine_vs_highstakes` (branch) · `runway_burn_depletion` (depletion) · `scenario_model_payback` (best/likely/worst → break-even) · `branch_analysis_to_human` (branch) · `cost_rises_the_later` (growth).

## Datable facts STRIPPED (DOUBLE-CHECK LAW; see SOURCES.md + book FACTCHECK.md)
- Transcription: "Cloud" → **Claude** everywhere; "outside council" → **outside counsel**; "unglamerous" → **unglamorous**; "solar/solo printers/pranours" → **solo operators**; "SAUS/SaaS" → **SaaS**.
- **No plugin counts, no subscription prices, no platform lists** anywhere on screen or in narration.
- Illustrative hypotheticals kept but framed AS examples and softened so nothing reads as a fixed product output: the "15%" price raise stays as "say, fifteen percent"; the contractor-hire dollars are dropped for generic "a contractor / more clients"; the legal flag tally (2 red / 3 yellow / 8 green in the source) is shown as the color SYSTEM with counts explicitly illustrative, never a fixed number.

## Gates
1. Plan (this doc) — **approve**.
2. Factcheck — inherits whole-book FACTCHECK.md; per-reel notes + the legal/finance-are-separate note in SOURCES.md.
3. **GATE P** — narration reviewed on an animated slate before any audio.
4. Audio lock (Kokoro `af_kore`) → align → **Gate D2 SHOPPING.md** (7 vox stills, tier-0 library pass first, from LOCKED durations) → **Gate D1 full-length SLATE PREVIZ** → pantry fill → review cut → VISUAL QC LAW → `art final`.
