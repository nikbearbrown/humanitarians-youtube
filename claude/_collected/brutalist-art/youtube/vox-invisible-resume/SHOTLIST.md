# SHOTLIST — vox-invisible-resume

**Why Your Beautiful Résumé Is Invisible** · 16:9 · ~102s est. (11 beats)
Accents: dusty navy `#3D5A80` = extracts clean / survives · crimson `#BF3339` = scrambled / vanished / lost · gold `#F5D061` = editor's pen (once per graphic).
Source: chapter 13. Hero object: a résumé page under a horizontal read-head that pulls its text into one linear strip (manim move: scan).
Card exclusions honored: no ATS vendor comparisons · **no OCR tangent** (name-in-image is invisible, then move on) · no résumé-content/keyword advice · **no 82%-stat deep-dive** (stat appears once, B09) · no Markdown/Playwright pipeline · **paste test = the ~5s closing payoff only (B11)**.

Shot-type histogram: CARD 2 · STILL 1 · DOCUMENT 1 · GRAPHIC 4 · COMPOSITE 3 — max consecutive same-type: 2 (B04–B05). Lint: pass.

---

## B01 — CARD (title) · own · ~10.0s
Cue: "The first reader of your résumé can't see…"
Copy: **Why your beautiful résumé is invisible** / sub: *the first reader is a parser*

## B02 — STILL · ai · kenburns · ~10.0s  ← MEDIA SLOT (the only generated plate)
Cue: "Here it is. A weekend's work. Two columns…"
Slot: `media/B02.png`
t2i prompt: printed screenshot of a beautifully designed two-column résumé, header banner with a large stylized name, a sidebar of labeled skill proficiency bars, small section icons, elegant typography, pinned like a clipping to aged newsprint, desaturated flat print reproduction, editorial collage
Synthetic — disclosure line in credits. `shot.focus` across the design after the plate lands.

## B03 — DOCUMENT · own · highlight · ~8.0s
Cue: "…can it pull structured text out of the page?"
Quote card: **"Can I extract the text?"** — *— the only question the parser asks*. Gold sweep on "extract."

## B04 — GRAPHIC · own · manim (scan) · ~10.0s
Cue: "…it reads your whole page as one strip of text, top to bottom."
Manim: `B04_ReadHead` — résumé page left; navy read-head sweeps top→bottom; lines stream into a single vertical navy strip on the right. Establishes the hero (clean here; broken B05–B08).

## B05 — GRAPHIC · own · manim (scan) · ~10.5s — break mode 1
Cue: "Two columns? It reads straight across…"
Manim: `B05_ColumnInterleave` — read-head sweeps full width; output strip alternates L1, R1, L2, R2; interleaved lines turn crimson. Document-order scramble.

## B06 — COMPOSITE · own · manim · ~9.0s — break mode 2
Cue: "Your name, set inside a header image?"
Manim: `B06_NameVanishes` — header name-graphic; read-head passes; strip slot stays an empty crimson-outlined blank; label "name: absent." Parser reads embedded text, not images. NO OCR tangent.

## B07 — GRAPHIC · own · manim (scan) · ~9.0s — break mode 3
Cue: "Those elegant skill bars are graphics too."
Manim: `B07_SkillBarsGap` — sidebar skill bars; read-head passes; strip slot is an empty crimson gap; label "skills: (nothing)."

## B08 — COMPOSITE · own · manim · ~9.0s
Cue: "…It scores you unqualified for everything."
Manim: `B08_Unqualified` — the scrambled strip; three crimson field tags (name/dates/skills broken); a crimson **UNQUALIFIED** stamp slaps on at a slight angle.

## B09 — GRAPHIC · own · manim · ~10.5s
Cue: "…before a human ever opens it. Around eight in ten companies…"
Manim: `B09_ForkBeforeHuman` — "Submit" splits: navy path "parses → human → interview" vs crimson path "scrambled → auto-reject → no human"; label "before any human opens it." Fig 13.1. Stat once, no deep-dive.

## B10 — COMPOSITE · own · manim · ~9.5s
Cue: "The fix is boring, and it works. One column, real text…"
Manim: `B10_SafeVersion` — single-column page; read-head sweeps; strip fills with ordered navy lines + navy check tags; label "one column · real text." No keyword/content advice.

## B11 — CARD (endcard) · own · ~8.0s — the 5-second payoff
Cue: "…Select all, copy, paste. Five seconds."
Copy: **Select all, copy, paste — that's what the parser sees.** / sub: *from The Reallocation Engine — chapter 13*

---

## Slot inventory (fill later, any order; rerun vox_run after each drop)

| Slot | Need | From |
|---|---|---|
| `media/B02.png` | the beautiful two-column résumé clipping | t2i prompt above (ai — disclosure) |

Everything else is CARD / DOCUMENT / GRAPHIC / COMPOSITE-manim — no media generation needed for the slate cut.
