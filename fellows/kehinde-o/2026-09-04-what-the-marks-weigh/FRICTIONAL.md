# Frictional log — Explainer: What the Marks Weigh

## 2026-09-04 — first reel, and most of the week went on the toolkit

- **Video:** not yet published
- **Drive:** https://drive.google.com/drive/folders/1V-BZnGQ8a2soQqO7zD2N_atkRd7OYYPp (`Medhavy_Kehinde/STEM Topic/what-the-marks-weigh/`)
- **Report:** [REPORT.md](REPORT.md)
- **Source project:** https://github.com/Kenny0bi/ami
- **Paired report:** [Chapter One, Reviewed](../2026-09-04-chapter-1-review/)

**What I was working on.** My first Humanitarians AI explainer, on Yoruba
diacritics: how much information a tone mark actually carries, and why measuring
that decides whether restoring them needs a model or a lookup table. Built on my
own `ami` repo, a 1.29M-parameter BiLSTM.

**What I tried, and what I expected.**
- I expected the video to be the work and the toolkit to be a detail. It was the
  other way round: most of this week went on getting Brutalist to run at all.
- I expected to narrate the entropy result as a headline number and move on.

**Where it resisted, and what I did next.**
- **The install would not resolve.** `kokoro-onnx` requires onnxruntime 1.20.1 or
  newer; there is no x86_64 macOS wheel above 1.19.2, and this is an Intel Mac.
  Pip gave ResolutionImpossible. Resolved by pinning `onnxruntime==1.19.2` and
  installing `kokoro-onnx==0.4.9 --no-deps` with its dependencies by hand.
- **The voice model never downloaded**, because the pip failure aborted the step
  that fetches it. Pulled it manually with curl.
- **Renders produced no video and said nothing.** Remotion's bundled ffmpeg
  aborts on macOS 12: its `libavdevice` links a symbol that only exists on macOS
  13 and later. Every frame rendered correctly and the encode died silently, so
  the failure looked like success. Fixed by probing the bundled binary at startup
  and, when it is unusable, rendering a PNG sequence and stitching it with the
  system ffmpeg instead. Without that patch nothing on this machine renders.
- **Audio-first was a genuinely different way to think about production.** I had
  assumed you cut visuals and then fit narration to them. It is the reverse: the
  narration is generated and measured first, and every visual is conformed to it.
  Some of my beats ran long and had to be split rather than trimmed, because the
  fix for a long beat is less script, not a faster animation.
- **The output was not actually 4K.** The pipeline passed a flat `--scale=2`,
  which only reaches 4K if the composition is 1920 wide. Several are not. Replaced
  with a per-composition factor computed from each composition's real dimensions.
- **Animations were being cut off before their payoff**, because clips longer than
  their narration were truncated rather than retimed.
- **A number was rendered wrong on screen.** The verdict card strips a leading
  numeral, so "1.64 bits" displayed as "64 bits". The rule I now follow is never to
  start one of those lines with a digit.
- **The outro carried the wrong channel.** The stock outro hardcodes
  @NikBearBrown, and the shorts tool appends an endcard with that handle by
  default. It shipped on a short and I caught it on playback. I had a dedicated
  HAI outro component built, and the endcard stripped.

**What Claude contributed, and what I did with it.**
- Mine: the topic, the `ami` model and its measurements, and the decision about
  what the video should argue.
- Claude's: the beat sheet in the toolkit's conventions, the diagnosis of the
  ffmpeg and scaling failures, and the patches for both.
- Accepted: the PNG-sequence fallback, the per-composition 4K scaling, and a
  separate HAI outro component rather than bending the stock one.
- Rejected/changed: the first outro carried a Humanitarians AI monogram that
  looked wrong at the end of a cream page. I asked for it removed; it is now
  off by default.
- Evidence: rendered masters on the Drive folder above; beat sheet in this folder.

**What I understand now, and what I still do not.**
- Understood: audio-first is not a style preference. Narration length is the clock
  every visual is conformed to, so fixing timing by hand is always wrong.
- Understood: a render that produces no file is easier to catch than a render that
  produces a wrong one. The silent encode failure cost hours; the "64 bits" bug
  shipped because I checked the file existed rather than watching it.
- Not resolved: the video is not published yet, so I have no view numbers or
  comments to learn from.
