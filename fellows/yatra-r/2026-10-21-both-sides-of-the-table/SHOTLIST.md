# SHOTLIST — Both Sides of the Table.

`yatra-both-sides-of-the-table` · 16:9 master 3840×2160 · 9:16 short 2160×3840
Narrated by Kokoro `af_bella` ("Bella"), in for Yatra · `@Yatra`

**Total: 169.4s — 2:49.4** · Shorts cut 173.9s (cap 3:00)

---

| # | Act | Lane | Scene (16:9 / 9:16) | Dur | The ONE terracotta event |
|---|---|---|---|---|---|
| B00 | COLD OPEN — ASK | BOOKEND | `ClaudeComposerAsk` / `…916` | 11.09 | the send button arms |
| B01 | EXECUTIVE SUMMARY — BLUF | BOOKEND | `TblBluf` / `TblBluf916` | 11.80 | claim three — *"Neither side trusts it."* |
| B02 | SIDE ONE — the employers | — | `TblSide` / `TblSide916` | 12.44 | — (ink only: adoption never glows) |
| B03 | SIDE TWO — the candidates | — | `TblSide` / `TblSide916` | 12.22 | — (ink only) |
| B04 | ASK — the pair opens | BOOKEND | `ClaudeComposerAsk` / `…916` | 5.25 | the send button arms |
| B05 | RESULT — the table | — | `TblTable` / `TblTable916` | 11.31 | the machine-to-machine traffic |
| B06 | THE INTERVIEW | — | `TblInterview` / `…916` | 10.88 | the +13-point delta chip |
| B07 | WALKING AWAY | — | `TblWalk` / `TblWalk916` | 10.88 | the marks that leave the row |
| B08 | TRUST — both directions | — | `TblTrust` / `TblTrust916` | 13.16 | both figures (this beat IS the subject) |
| B09 | THE ESCALATION | — | `TblInject` / `TblInject916` | 13.91 | the hidden layer inside the page |
| B10 | LIMITS | — | `TblLimits` / `TblLimits916` | 13.31 | the **refusals** column |
| B11 | VERDICT | BOOKEND | `ClaudeVerdictArtifact` / `…916` | 21.08 | the artifact's accent rule |
| B12 | HANDOFF — YOUR TURN | BOOKEND | `ClaudeComposerAsk` / `…916` | 14.91 | the send button arms |
| B13 | OUTRO | BOOKEND | `ClaudeTitleOutro` / `…916` | 6.70 | the period after the title |

*(B11 carries an extra 0.5s `lead_silence_s`, so the compiled total is 169.44s.)*

**Accent audit.** Terracotta always marks THE DISTRUST — never adoption. B02 and B03 are
the deliberate tell: the two biggest adoption figures in the reel (86%, 4 in 5) render in
plain ink, because the episode is not about how fast AI arrived.

---

## Composition sharing — and how it is sized

`TblSide` backs **two** beats (B02 at 12.44s, B03 at 12.22s). It is registered at the
**shorter** of the two (12.22s → 367 frames), because `remotion_scenes.py` freeze-extends
a clip shorter than its beat (lossless) while `compile.py` trims one that is longer
(lossy) — and this scene's source line lands at ~88% of its span, so trimming would cut
exactly the citation.

---

## The portrait cut — what was genuinely rebuilt

| Scene | What changes in 9:16 |
|---|---|
| `TblTable916` | the two sides become TOP and BOTTOM; traffic runs vertically through the table. Four seats across 972px would be 230px each |
| `TblWalk916` | the row of marks wraps to two rows; the leaving share still departs DOWNWARD, so the motion still reads as withdrawing rather than being filtered |
| `TblTrust916` | the two figures STACK, each keeping its own separate citation |
| `TblInject916` | the page sits above its figure instead of beside it |
| `TblSide916` | the "other side of the table" ghost moves BELOW the active side |

All refusals hold in both cuts — the types are **imported** from `TableSides.tsx`, not
redeclared.

---

## Slot contract

Every slot is a Remotion render. No slates, stock, AI stills or pantry media.

**Two manual steps `shorts.py` will not do on this channel:** pass `--handle "@Yatra"`
(default is `@nikbearbrown`) and regenerate the endcard PNG at 2160×3840 (it hardcodes
1080×1920, so a 4K compile upscales it).
