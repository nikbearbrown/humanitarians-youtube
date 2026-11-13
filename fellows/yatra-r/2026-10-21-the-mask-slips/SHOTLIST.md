# SHOTLIST — The Mask Slips.

`yatra-the-mask-slips` · 16:9 master 3840×2160 · 9:16 short 2160×3840 · 24 fps out, 30 fps scenes
Narrated by Kokoro `af_bella` ("Bella"), in for Yatra · `@Yatra`

**Total: 168.8s — 2:48.8** · Shorts cut 173.3s (cap 3:00)

---

| # | Act | Lane | Scene (16:9 / 9:16) | Dur | The ONE terracotta event |
|---|---|---|---|---|---|
| B00 | COLD OPEN — ASK | BOOKEND | `ClaudeComposerAsk` / `…916` | 12.57 | the send button arms |
| B01 | EXECUTIVE SUMMARY — BLUF | BOOKEND | `MskBluf` / `MskBluf916` | 13.31 | phase two — the collapse half |
| B02 | THE RISE — the speed | — | `MskSpike` / `…916` | 12.69 | the tick marking how early the spike landed |
| B03 | THE MONEY | — | `MskMoney` / `…916` | 12.59 | the rule under the **caveat**, never the figure |
| B04 | ASK — the pair opens | BOOKEND | `ClaudeComposerAsk` / `…916` | 6.57 | the send button arms |
| B05 | RESULT — the arc | — | `MskArc` / `MskArc916` | 11.65 | the identification marker at the crest |
| B06 | THE REVEAL — the mechanism | — | `MskReveal` / `…916` | 12.71 | the wire turning dashed along its whole length |
| B07 | THE DROP | — | `MskDrop` / `MskDrop916` | 14.57 | the halved remainder |
| B08 | WHY IT TURNS | — | `MskTurn` / `MskTurn916` | 13.87 | the surviving line — *"They turn."* |
| B09 | LIMITS | — | `MskLimits` / `…916` | 16.53 | the **refusals** column |
| B10 | VERDICT | BOOKEND | `ClaudeVerdictArtifact` / `…916` | 20.97 | the artifact's accent rule |
| B11 | HANDOFF — YOUR TURN | BOOKEND | `ClaudeComposerAsk` / `…916` | 14.89 | the send button arms |
| B12 | OUTRO | BOOKEND | `ClaudeTitleOutro` / `…916` | 5.38 | the period after the title |

*(B10 carries an extra 0.5s `lead_silence_s`, so the compiled total is 168.80s.)*

**Accent audit: one terracotta event per beat, thirteen for thirteen.** In every case it
marks the collapse side of the story. B03 is the deliberate tell: on the money beat the
accent underlines the *caveat*, not the figure — the gold-rush half never glows.

---

## The portrait cut — what was genuinely rebuilt

| Scene | What changes in 9:16 |
|---|---|
| `MskBluf916` | the two phases STACK; the divider becomes a horizontal rule between them |
| `MskSpike916` | the lead figure sits ABOVE its two scale figures — three figures won't fit across 972px |
| `MskArc916` | the curve is re-plotted into a taller, narrower box with its labels stacked beneath rather than flanking the peak |
| `MskReveal916` | the audience→person wire runs DOWN the frame; the far node sits below |
| `MskDrop916` | each case gets its own row with the figure BELOW its bar |

`MskMoney916`, `MskTurn916` and `MskLimits916` are already vertical arguments and are
re-spaced, not rebuilt.

All refusals hold in both cuts because the **types are imported** from `MaskSlips.tsx`
rather than redeclared.

Portrait keep-out honoured: content above y≈1440 and left of x≈960, brand bug lower-left.

---

## Slot contract

Every slot is filled by a Remotion render. No slates, no stock, no AI stills, no pantry
media — fully deterministic, re-renders identically from source.

**Two manual steps `shorts.py` will not do on this channel:** pass `--handle "@Yatra"`
(its default is `@nikbearbrown`) and regenerate the endcard PNG at 2160×3840 (it hardcodes
1080×1920, so a 4K compile upscales it).
