# QC REPORT — A Quantum Sphere Is Never the Size It Looks

Week 20 topic video · Humanitarians AI · Tanmay Kulkarni · 2026-08-30

---

## Deliverables

| File | Aspect | Resolution | Duration | Loudness | Verified |
|---|---|---|---|---|---|
| `2026-08-28-a-quantum-sphere-is-never-the-size-it-looks.mp4` | 16:9 | **3840 × 2160** | 329.4s (5:29.4) | -14.35 LUFS / -1.20 dBTP | `ffprobe` + `loudnorm` |
| `2026-08-28-a-quantum-sphere-is-never-the-size-it-looks-short.mp4` | 9:16 | **2160 × 3840** | 114.1s (1:54.1) | -14.23 LUFS / -1.45 dBTP | `ffprobe` + `loudnorm` |

Both are **clean masters** — no slate, no review burn-ins. Masters are in the shared Google
Drive; this folder holds text and code only.

## Loudness

Mastered in **two stages**, because one is not enough. Kokoro's raw output measured around
−21 LUFS with peaks at the ceiling; YouTube targets ~−14 LUFS and only *attenuates* loud
uploads, so an un-mastered upload plays noticeably quiet.

1. **Per beat**, in `mp3/` — two-pass `loudnorm`. Done at this level so the Short inherits
   correct levels: it reuses the parent's beat audio.
2. **On the master** — every lossy generation after a limiter overshoots it.

Both cuts land inside −14.2 to −14.5 LUFS with true peak below −1.2 dBTP.

## Resolution

Every source clip is at or above its master's resolution — checked, not assumed. Mixed lanes
make this easy to get wrong: Remotion renders at the master's resolution by configuration,
Manim at whatever quality flag was typed. A film can be half native and half upscaled and
merely look "inconsistent".

The Short's beats were already 4K portrait and had been compiled down to 1080 × 1920; it
is now compiled at full resolution. The endcard was regenerated at 2160 × 3840 rather than
upscaled.

## Pacing and time-stretch

Every Manim beat renders **at or slightly longer than** its measured narration, so `compile.py`
applies no time-stretch anywhere. A scene shorter than its beat gets silently slowed, which
reads as a stylistic choice and is not one.

## Layout gates

`manim_layout_audit.py` run on every Manim scene: **0 errors, 0 warnings**. Remotion typecheck
exits 0. Frames for every claim were pulled from the **compiled master** — not from component
renders or intermediates — at the timestamp each claim is spoken.

## Reviews

See `PROOF-REVIEW-FINAL.md` for the full production-gate pass on the finished cut, and
`FACTCHECK.md` for every claim with what was checked and how.
