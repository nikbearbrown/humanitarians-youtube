# QC REPORT — Morgan Stanley's AI Drafts One Thing and Files Another

Week 20 work video · Humanitarians AI · Tanmay Kulkarni · 2026-08-30

---

## Deliverables

| File | Aspect | Resolution | Duration | Loudness | Verified |
|---|---|---|---|---|---|
| `2026-08-30-drafts-one-thing-files-another.mp4` | 16:9 | **3840 × 2160** | 378.4s (6:18.4) | -14.36 LUFS / -1.34 dBTP | `ffprobe` + `loudnorm` |
| `2026-08-30-drafts-one-thing-files-another-short.mp4` | 9:16 | **2160 × 3840** | 159.8s (2:39.8) | -14.43 LUFS / -1.36 dBTP | `ffprobe` + `loudnorm` |

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

One thing the compiled-cut check earned its place on, worth recording. B07 existed twice in
the Short:
`media/B07.mp4` (shorts.py's automatic centre-cut, 1214 × 2160) and `media/B07-916.mp4` (the
hand-built portrait scene). `compile.py` reads the first. The portrait scene was verified in
isolation, and an early build therefore picked up the centre-cut. A resolution sweep *passed*
at that point, because both files were dimensionally fine — it had no way to see which one was
wired in. **Pulling the frame from the compiled master is what showed it**, and the fix is
`pantry/B07-916.mp4`, the override slot that survives a re-run. Every frame in this report was
verified the same way afterwards.

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
