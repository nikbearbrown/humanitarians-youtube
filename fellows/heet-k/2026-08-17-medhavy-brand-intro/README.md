# Medhavy brand intro — logo reel and ident

- **Week:** 17–30 Aug 2026
- **Project:** Medhavy · **Role:** AI Software Engineer · **PM:** Clafacio L.
- **Drive (renders):** https://drive.google.com/drive/folders/1fZCmWm_aQgs1epDGp085T5Ucs0VcK7XK (`Intros/`)
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **Status:** first-pass intro set. Professor-confirmed final in Week 14 — see
  [2026-09-04-medhavy-brand-outro/](../2026-09-04-medhavy-brand-outro/).

## What this was for

The Medhavy YouTube channel had no brand sting. This builds one: a ~20s animated
logo reel that establishes the mark, the wordmark, the tagline and the URL, plus a
shorter ident for use where the full reel is too long.

No brand colour had been specified, so the palette is a decision, not a given —
ink `#15151c` with a tech-blue accent `#2A6FB0`. That choice is recorded in
[script.md](script.md) as a default that is easy to change, not as a brand ruling.

## What is here

| File | What it is |
|---|---|
| [beat_sheet.json](beat_sheet.json) | 80 beats, 16 logos, ~118s estimated. PNG tile-assembly build; each logo gets a different build pattern. |
| [medhavy_logo_reel.py](medhavy_logo_reel.py) | Manim scene for the full reel. |
| [medhavy_logo_ident.py](medhavy_logo_ident.py) | Manim scene for the shorter ident. |
| [script.md](script.md) | Visual arc, the three spoken lines, and the tunable knobs (`HERO`, `MONTAGE`, palette, wordmark tracking). |
| [assets/svg/](assets/svg/) | 10 vector marks. |
| [assets/png/](assets/png/) | 17 raster marks plus 43 build tiles. |

Fonts are not committed — Montserrat is a Google Fonts family, installed locally
per the setup instructions in the `quantum-mechanics-videos` toolkit.

## Structure of the reel

Open (accent node blinks) → Construct (hero mark draws on stroke-by-stroke) →
Wordmark (**MEDHAVY**, Montserrat Bold, 0.28em tracking) → Montage (alternate
marks, each with a different animation) → Lockup (tagline, then URL) → Outro hold.

The hero mark is `medhavy-08`, selected from 58 candidates via a contact sheet.

## Open at this point

- **16:9 only.** A 9:16 cut was flagged in [script.md](script.md) as available on
  request and deliberately not built. It was delivered in Week 16 — see
  [2026-09-17-outro-formats-and-video-fix/](../2026-09-17-outro-formats-and-video-fix/).
- Narration used the ElevenLabs Medhavy brand voice, not Kokoro. See the
  [voice note](../README.md#voice).
- No YouTube link. The renders are in Drive only.
