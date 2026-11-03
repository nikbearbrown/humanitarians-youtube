# SHOTLIST — Interest Media.

`yatra-interest-media` · 16:9 master 3840×2160 · 9:16 short 2160×3840 · 24 fps out, 30 fps scenes
Narrated by Kokoro `af_bella` ("Bella"), in for Yatra · `@Yatra`

**Total: 149.6s — 2:29.6**

---

| # | Act | Lane | Scene (16:9 / 9:16) | Dur | The ONE terracotta event |
|---|---|---|---|---|---|
| B00 | COLD OPEN — ASK | BOOKEND | `ClaudeComposerAsk` / `…916` | 13.06 | the send button arms |
| B01 | EXECUTIVE SUMMARY — BLUF | BOOKEND | `ItmBluf` / `ItmBluf916` | 10.45 | claim two — *"It runs on what you're interested in."* |
| B02 | THE SOURCE — and the rename | — | `ItmSource` / `ItmSource916` | 16.41 | the word **INTEREST** |
| B03 | YOUR OWN FEED — worked example | — | `ItmFeed` / `ItmFeed916` | 14.19 | the wire from the signal rail into the matched column |
| B04 | WHY IT HAPPENED — the volume | — | `ItmVolume` / `ItmVolume916` | 10.30 | the verdict band — *"more than a network can sort"* |
| B05 | THE QUESTION CHANGED | — | `ItmQuestion` / `ItmQuestion916` | 6.98 | the new key dropping into the slot |
| B06 | ASK — the pair opens | BOOKEND | `ClaudeComposerAsk` / `…916` | 5.21 | the send button arms |
| B07 | RESULT — the two models | — | `ItmModels` / `ItmModels916` | 13.57 | the match node that replaced the gate |
| B08 | THE NEW QUESTION — the job | — | `ItmJob` / `ItmJob916` | 9.39 | the new question card + its tick marks |
| B09 | LIMITS — what this isn't | — | `ItmLimits` / `ItmLimits916` | 12.39 | the **refusals** column |
| B10 | VERDICT | BOOKEND | `ClaudeVerdictArtifact` / `…916` | 17.73 | the artifact's accent rule |
| B11 | HANDOFF — YOUR TURN | BOOKEND | `ClaudeComposerAsk` / `…916` | 13.91 | the send button arms |
| B12 | OUTRO | BOOKEND | `ClaudeTitleOutro` / `…916` | 5.53 | the period after the title |

*(B10 carries an extra 0.5s `lead_silence_s`, so the compiled total is 149.62s.)*

**Accent audit: one terracotta event per beat, thirteen for thirteen.** In every case it
marks the interest side of the shift — never the follower side, never the attribution.

---

## The portrait cut — what was genuinely rebuilt

The Shorts law's ONDA CHECK rewires `<pattern>` → `<pattern>916` and re-renders; generated
graphics are never centre-cropped. Five of the eight `Itm*` layouts are horizontal by
nature and were re-banded rather than squeezed:

| Scene | What changes in 9:16 |
|---|---|
| `ItmSource916` | the rename STACKS (old word above, new below) — two 96px words will not fit across 972px |
| `ItmFeed916` | the two columns become two stacked GROUPS, and the signal rail moves between them so the wire points DOWN into the group it explains |
| `ItmQuestion916` | the machine runs TOP → BOTTOM: posts in from above, keyed slot mid-frame, feed out below |
| `ItmModels916` | each track becomes a VERTICAL chain, the two side by side, so the gate/no-gate comparison still reads in one glance; the gate becomes a horizontal barrier across the left chain |
| `ItmLimits916` | the two ledgers stack into two labelled groups |

`ItmBluf916`, `ItmVolume916` and `ItmJob916` are already vertical arguments and are
re-spaced, not rebuilt.

`MARKS` and `TICKS` are **imported** from the landscape module rather than redeclared, so
the two cuts of one reel cannot drift apart on how dense "too much" looks.

**Two manual steps `shorts.py` does not do for you on this channel** (both were needed here
and are logged in `_qc/QC-LOG.md`):

1. **`--handle @Yatra`.** The flag defaults to `@nikbearbrown`, which silently puts another
   channel's handle on the endcard.
2. **A 4K endcard.** `shorts.py` hardcodes the endcard PNG at 1080×1920, so a
   `--height 3840` compile upscales it. It was regenerated here at 2160×3840 with all
   metrics doubled, so the endcard is as sharp as the thirteen Remotion beats.

Portrait keep-out honoured throughout: content above y≈1440 and left of x≈960 (the
Shorts/Reels chrome region), brand bug lower-left.

---

## Slot contract

Every beat compiles to a conformed per-beat mp4 named by beat id. To replace any beat with
real footage, drop `media/<beat>.mp4` (or `.png`) and recompile — the edit is untouched.
For the portrait cut the only human override slot is `pantry/<beat>-916.mp4|png`, which
wins over everything else.

**Every slot here is filled by a Remotion render. No slates, no stock, no AI stills, no
pantry media — the reel is fully deterministic and re-renders identically from source.**
