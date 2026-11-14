# SHOTLIST — Every Group Went The Other Way

Week ending 2026-11-13 · `ai-` track · 9 beats · master 16:9 3840×2160.

SHOW authored before narration. Durations are the measured Kokoro `am_onyx`
MP3s — the master clock.

| # | Act | Scene | What the viewer WATCHES |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | Serif greeting (`Privet, Jainil`) · the question types in · two output lines answer it |
| B01 | BLUF | `BrutalistHesitantWriter` | The line types out ending on **answer** · terracotta, hesitates, deletes · **opposite** types in |
| B02 | SETUP | `PairedBars` | Six department rows land, four marked WOMEN · the rule draws · the total lands marked MEN |
| B03 | BODY | `ClaudeBarChart` | Six selectivity bars step down, 64.4 → 6.4, F taking the accent |
| B04 | BODY | `CardSet` | Two cards: where men applied vs where women applied, 51% against 7% |
| B05 | BODY | `ClaudeBarChart` | Three bars: 30.4 observed, 44.5 men, then 51.6 standardised passing both |
| B06 | LAND | `StageRail` | Three stages: the total's question → the departments' answer → where the question moved |
| B07 | HANDOFF | `ClaudeComposerAsk` | "Your turn." · the prompt types in and is read aloud |
| B08 | OUTRO | `HaiTitleOutro` | Title restate, terracotta period, `@HumanitariansAI` |

---

## The spine

Cold open → hesitant-writer BLUF → the reversal → why (selectivity) → why
(application pattern) → the counterfactual → the landing → handoff → outro.

Typing appears in exactly three beats — the ask, the overview, the viewer's
prompt — as the law requires.

## B02 is the whole argument in one image

The component was built so the contradiction is **visible before it is
spoken**: the six category rows sit as one block, each marked with the side
that leads; a rule separates them; the total sits outside the block marked the
other way. A viewer who reads nothing else sees four rows saying WOMEN and a
total saying MEN.

That separation is why `PairedBars` exists rather than two bar charts — the
total is not one of the rows, and drawing it inside the block would quietly
assert that it is.

## Visual scheme, beat to beat

Paired bars → bars → cards → bars → stages. B03 and B05 are both
`ClaudeBarChart` but are two beats apart and carry opposite jobs: B03 shows
how unlike the departments are, B05 shows what happens when you hold them
fixed. Neither pair of adjacent beats shares a scheme.

## Accent discipline

One terracotta moment per beat: B01 the deleted word · B02 the rows that lead,
and then the total that does not · B03 department F · B04 the women's card ·
B05 the standardised bar · B06 the stage where the question lands · B08 the
period.

## On B06, and on what this reel is careful not to say

The landing beat is the reason the reel exists in this form. It would be easy
to end on "always disaggregate" — a tidy, useless lesson. It would be worse to
end implying the split proves nothing was wrong.

The three stages say what actually happened: the aggregate asked a question
about admissions committees, the departments answered it, and the question
moved upstream to who was applying where and why — which is where the original
authors pointed. `activeIndex: 2` puts the accent on the stage that is still
open, and `activeNote` reads *"the aggregate cannot see this"*.

## Fill (GATE V)

`PairedBars` was sized on paper before rendering: bar column 0.52W, content
spanning ~0.80 of safe width, stack ~0.80H against 0.90H — about 71% cover
against a 55% floor. Portrait restacks each row into two lines and drops to a
0.84W bar area, ~81% cover.

B01 and B08 carry `qc.sparse` waivers, as on every prior reel.

## Process note

GATE F refused the first compile: FACTCHECK.md had not been written yet. The
gate was right — the paperwork is an input to the build, not a write-up of it.
All nine master beats had already rendered; nothing was lost but a compile.
