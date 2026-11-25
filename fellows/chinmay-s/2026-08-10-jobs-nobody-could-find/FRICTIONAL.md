# Frictional log — The Jobs Nobody Could Find

## 2026-08-10 — 6:08, 26 beats, Bella / Humanitarians AI

Evidence in this folder: `beat_sheet.json`, `PEDAGOGY.md`. Master MP4 held outside Git per repository policy. (YouTube: TBD.)

**What I was working on.** Porting the Brutalist toolkit to Windows and finishing a
deep-explainer that had been sitting at 4 of 26 beats filled since July.

**What I tried, and what I expected.** I expected `./setup --install` to work and the
remaining beats to be a content problem, not an environment one.

**Where it resisted, and what I did next.**
* 63 call sites invoke `python3`, which on Windows hits the Microsoft Store stub. Fixed
  with a shim on PATH rather than editing the toolkit.
* 47 unqualified `read_text()`/`write_text()` calls corrupted every em-dash on a
  read-modify-write, so Kokoro would have read the mangled text aloud. `PYTHONUTF8=1`
  fixed all of them with no code change.
* `requirements.txt` can never resolve on any platform: it pins `numpy>=1.26,<2` while
  `kokoro-onnx>=0.4` requires `numpy>=2.0.2`. Installed with numpy 2 instead.
* Changing the voice from Onyx to Bella changed every beat's duration, which forced a
  re-render of all 26 beats — audio durations *are* the timeline.

**What Claude contributed, and what I did with it.** Mine: the ship log, the topic, the
decision to keep the Teardown register when rebranding. Claude's: the Windows diagnosis
and fixes, the rebrand, the rebuild.

**What I understand now, and what I still do not.**
* Understood: the toolkit's "audio is the master clock" rule has a cost nobody states —
  a one-word narration change is a full re-render.
* Not resolved: 21 of 26 beats are still generic `SlateCard` previz on the VOX palette,
  which visibly clashes with the Claude-skin bookends. It is a watchable previz, not a
  finished piece.
