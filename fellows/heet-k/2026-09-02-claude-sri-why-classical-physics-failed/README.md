# Why Classical Physics Failed — QM Vol. 1, Chapter 1

- **Week:** 31 Aug – 6 Sep 2026 · built 2 Sep
- **Project:** Medhavy · **Role:** AI Software Engineer · **PM:** Clafacio L.
- **Skill:** [`sri-explainer`](../2026-08-24-sri-explainer-skill/) — **first real test build**
- **Source chapter:** `quantum-mechanics-vol1/chapters/01-why-classical-physics-failed.md`
- **Drive (renders):** https://drive.google.com/drive/folders/15BtMVhwD9_A7J0Pt2pc2DHLcuF9RWxl7
  (`claude-sri-why-classical-physics-failed.mp4`)
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)

## Metadata

| Field | Value |
|---|---|
| Channel / persona | `claude-sri` / Prof Sridhar |
| Register | Sridhar |
| Engine / voice | `kokoro` / `am_onyx` |
| Palette / preset | `claude` / `claude-sri` |
| Clock | narration |
| Beats | 14 |
| Runtime | 228.4s (3:48) |
| Audience | students and practitioners working through Quantum Mechanics Vol. 1 |

## Structure

| Beat | Act | Shot | Content |
|---|---|---|---|
| B00 | OPEN | Remotion | Cold open — composer ask, answered |
| B01–B05 | I — The Ultraviolet Catastrophe | Manim | Iron heating red→yellow-white; Rayleigh-Jeans diverging at high frequency; Planck overlaid on Rayleigh-Jeans; golden-test reveal of the 10⁻²⁰ ratio |
| B06–B10 | II — One Photon, One Electron | Manim | Threshold / intensity-vs-count / no-delay panels; stopping potential vs frequency across three metals; sodium worked example, UV vs green; Compton scattering geometry |
| B11 | VERDICT | Remotion | Verdict artifact card |
| B12 | YOUR TURN | Remotion | Handoff — composer with suggested prompt |
| B13 | OUTRO | Remotion | Title restate |

Two acts, Claude bookends at both ends, Manim carrying every derivation beat.

## Renders

Both looks were built:

- `claude-sri-why-classical-physics-failed.mp4` — dark Notebook look
- `claude-sri-why-classical-physics-failed-CREAM.mp4` — cream/parchment look

Renders, narration `mp3/`, per-beat `clips/`, `manim/` and `media/` output stay in
Drive per the [repo rule](../../README.md#github-for-source-and-assets-drive-for-renders).
Only [beat_sheet.json](beat_sheet.json) is committed here — it carries the narration
text, shot specs, and the `actual_duration_s` measured from the rendered audio, so
the build is reproducible from it.

## Open

- No YouTube link.
- Golden-test numbers (the 10⁻²⁰ ratio, the sodium worked example) are asserted in
  the narration. No separate FACTCHECK document was produced.
