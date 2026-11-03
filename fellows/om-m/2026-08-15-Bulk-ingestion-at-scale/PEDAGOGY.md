# PEDAGOGY — bulk-ingestion-at-scale (week 2)
*Bulk Ingestion at Scale — Week 2 progress update · ai-explainer / claude-hai*

Second episode of the Private AI Valuation Agent series. Same chassis, same channel, same
persistent voice as `2026-08-08-Verifying-Private-AI-Valuations`; the source is
`narration_script.md` (438 spoken words, author-written, target 2:55).

---

## Act structure audit

| Beat | Act | Check |
|------|-----|-------|
| B00 | COLD OPEN | `ClaudeComposerAsk`. Opens directly on the Claude UI, ask lands **ANSWERED** with three output lines (COLD OPEN LAW). Personal intro kept short — week 1 did the introducing, per the script's own shot note ✓ |
| B01 | EXECUTIVE SUMMARY | The BLUF in one breath: one company by hand becomes 80 million rows by machine, and scale buys two things — a shape and a set of caught mistakes. States the whole idea, spends none of the reveals ✓ |
| B02 | THE SCALE | The funnel: 80,571,213 → 22,041,937 → 5,806, every stage reconciling ✓ |
| B03 | THE STAIRCASE | The payoff: 33 period ends of a real price history, and the shape it makes ✓ |
| B04 | SEVEN MANAGERS | The corroboration: seven independent families on one number, to the cent ✓ |
| B05 | THE PROBLEM | The author's own finding turned against the author's own data — the archive cannot reach what week 1 verified ✓ |
| B06 | TRAP ONE | A defect in the author's own code, caught before it did damage ✓ |
| B07 | TRAP TWO | A defect in the *source data*, held for human adjudication rather than auto-corrected ✓ |
| B08 | VERDICT | One-page recap; carries the Week 3 forward statement ✓ |
| B09 | HANDOFF | HANDOFF LAW: a real prompt, read ALOUD verbatim and then discussed ✓ |
| B10 | OUTRO | OUTRO LAW: title restate, `@HumanitariansAI` handle ✓ |

Act order: COLD OPEN → EXECUTIVE SUMMARY → SCALE → PAYOFF → CORROBORATION → PROBLEM → TRAP →
TRAP → VERDICT → HANDOFF → OUTRO ✓

**Where this cut departs from the script, and why.** The script pairs two things into single
shots; both are split here so no beat carries two ideas:

1. *The staircase and the archive-lag problem share one figure in the script* ("stay on the
   staircase, point to the dashed line"). Split into B03 and B05. B05 became a
   **mechanism** beat rather than an annotation — it shows WHY the archive lags (filing date vs
   period covered, ~56 days) instead of only showing that a point is missing. The cause is the
   teachable part and it is what reshapes week 3.
2. *"Two traps" is one shot in the script.* Split into B06 and B07. They are different KINDS of
   defect — one in the author's code, one in the filed data — and the distinction is the point.

Neither split adds or drops a claim. Both are logged in `BUILD-LOG.md`.

---

## Cold open + executive summary check

- B00 opens on the Claude UI, never a brand card ✓
- B00's ask lands answered — ASK→RESULT begins at the cold open ✓
- B01 states the whole idea in plain language before any specific. No "N-PORT", no "Level 3",
  no "period end" until B02–B05 earn them ✓
- The reel does not jump from cold open into a detail beat ✓

---

## ILLUSTRATE LAW audit

| Beat | Visual scheme | UI? |
|---|---|---|
| B00 | ClaudeComposerAsk | UI — the interface IS the subject (cold open) ✓ |
| B01 | `W2Bluf` — kinetic type, two mismatched cards | illustration ✓ |
| B02 | `W2Funnel` — log-scaled stage bars | illustration ✓ |
| B03 | `W2Staircase` — time-series step chart | illustration ✓ |
| B04 | `W2Convergence` — plates converging + tick grouping | illustration ✓ |
| B05 | `W2BulkLag` — mechanism chips + period axis | illustration ✓ |
| B06 | `W2FidelityTrap` — card collapse + counter | illustration ✓ |
| B07 | `W2SpacexTrap` — filing table + ratio brace | illustration ✓ |
| B08 | ClaudeVerdictArtifact | UI — the verdict artifact page ✓ |
| B09 | ClaudeComposerAsk | UI — the handoff ✓ |
| B10 | ClaudeTitleOutro | UI — the outro ✓ |

Seven body beats, seven different schemes. No two consecutive body beats share one ✓
Typing appears in exactly two beats — B00 and B09 ✓

**B04 and B06 are deliberately inverse moves.** B04 groups 24 registrations into 7 families;
B06 collapses 5 apparent managers into 1. Same underlying idea seen from both directions, two
beats apart, in two different visual languages — this is the reason B04's number is seven, and
the reel earns that by showing the mechanism rather than asserting it.

---

## Utility-framing lint

- "is critical for" — NOT PRESENT ✓
- "important to understand" — NOT PRESENT ✓
- "we'll cover" — NOT PRESENT ✓
- "in this video" — NOT PRESENT ✓

Style: narration written dash-free per the author's confirmed preference ✓

---

## Honesty check

- **B05 and B06 are the author's own work being wrong, narrated as such.** "I went looking for
  something and could not find it"; "my code counted one manager as five" ✓
- **B07 is a defect in the FILED DATA, and the reel does not fix it.** The source figure's own
  note is carried: held for human adjudication, never auto-adjusted. The reel reports the
  anomaly, it does not silently correct it ✓
- **B04 uses the honest number.** The script's note is explicit — say "independent managers",
  not "filers", and seven is the honest count. The figure layer nearly shipped "25 managers
  agree"; that error is named in `FACTCHECK.md` row 11 rather than quietly dropped ✓
- **No valuation claim.** These are marks funds report, never what a company is worth ✓
- **No trading claim.** B05 argues the opposite: the data cannot reach anything recent ✓
- **No invented figures on screen.** Every figure is a prop sourced from `figdata_week2.json`;
  the 33-point staircase is injected programmatically from that file rather than transcribed,
  so a chart here cannot drift from the panel it describes ✓

---

## Length law

Estimated ~215s across eleven beats, word-count estimates only; actual audio on this series runs
well under estimate. Duration is an OUTPUT. The script targets 2:55 for the body alone; the four
bookends are additive, and the body beats were written to the 45–70 word budget to compensate.

Per-beat narration budget (body beats only; bookends exempt):
B01 44w · B02 59w · B03 60w · B04 48w · B05 64w · B06 43w · B07 49w — all inside 45–70
(B06 at 43 is marginally under, which is correct: it is the least visual of the three findings
and the script itself nominates it as the first cut if the reel runs long) ✓

---

## Source fidelity

Every number traces to `figdata_week2.json` or `docs/worklog.md` in the Mycroft repo — see
`FACTCHECK.md`, 20 rows. **Row 16 is the one derived rather than quoted figure** and is flagged
there for the author's confirmation.

The three source PNGs and their SVG sources travel with this reel in `pantry/` as REFERENCE for
the rebuild; they are never slotted as media (REBUILD LAW). Unlike week 1 — where the SVG
sources had been lost from the Mycroft working tree — both formats survive here, and moving them
into this git-tracked folder puts them under version control for the first time.

## Palette deviation (logged, deliberate)

Identical to week 1: the Mycroft figures use crimson `#C8102E` for the data series and ochre
`#C8860E` for annotation; this rebuild renders in the Claude fidelity skin (cream `#F2F0E9`,
ink `#3D3929`, terracotta `#D97757` as the ONE accent) because `ai-explainer` is a fidelity
brand that may not be retinted. **Palette change only — no datum, ordering, or label altered.**

---

**What the author signed off on**, having watched
`bulk-ingestion-at-scale-slate.mp4`:

1. The two structural splits described above (staircase / lag, and trap one / trap two), and in
   particular that B05 teaches the lag MECHANISM rather than annotating the staircase.
2. `FACTCHECK.md` row 16 — "counted one manager as five" is derived from the worklog's
   "four independent managers" plus Fidelity's own mapped registrations. Confirm the derivation.
3. The B09 handoff prompt, which is new to this cut and is read aloud verbatim.
4. The palette deviation logged above.

VERDICT: PASS — signed by the author (Om Mali), 2026-08-16.
