# PEDAGOGY — "What MP3 Throws Away"

Narration sign-off. Audience: a smart non-technical viewer who uses audio tools
but has no signal-processing background. The reel fails if they leave thinking
"compression makes files smaller" and nothing else.

## The one thing this reel has to land

**An MP3 is edited, not compressed.** The word "compressed" is the whole
problem — it implies a zip file, something folded up and recoverable. The reel
replaces that model with deletion: the encoder decides what you cannot hear and
removes it, permanently. Every beat either builds toward that sentence or
unpacks a consequence of it.

## Act structure

| | |
|---|---|
| B00 ASK | ✓ Channel attribution in the first breath. States the thesis immediately — "a different song" — so the viewer knows the frame being replaced |
| B01 BLUF — the cut | ✓ Shows the deletion before explaining it. Constraint before mechanism, per the register |
| B02 MECHANISM — masking | ✓ Answers the question B01 provokes ("why 16 kHz?"). The answer is about ears, not files, which is the reframe that makes the rest make sense |
| B03 COMPARISON — bitrates | ✓ Makes the abstract number on an export dialog concrete: this is what 128 vs 320 actually buys |
| B04 LIMIT — generation loss | ✓ The practical trap. Also the strongest proof of the thesis: if it were compression, repeating it would be free |
| B05 APPLY — when | ✓ Two lists, both concrete. Not "use your judgement" |
| B06 outro | ✓ Restates the thesis in one line, then the standard sign-off |

## Register — Pragmatist, per `brands/hai.md`

- Leads with the constraint. ✓
- States where it fails, specifically: B04 quantifies the failure, B05 names
  four situations where lossy is wrong. ✓
- No marketing language, no academic hedging, no personality tax. ✓
- Every jargon term defined on first use. ✓

## Deliberate decisions

**The experiment came first.** The measurements were run before the script was
written, so the narration describes what happened rather than the numbers being
chosen to fit a story. This also meant one planned line got cut: an early draft
said 320 kbps "keeps everything", which the measurement contradicted — 20 kHz is
3.5 dB down. The line became "survives intact all the way to nineteen," which is
what was actually observed.

**"Not quieter — gone" is rhetoric, and the graphic tells the truth.** 25 dB
down is not literally zero. The narration uses the absolute phrasing because for
any practical purpose the content is unrecoverable, and the spectrogram shows a
steep cliff rather than a wall at negative infinity. FACTCHECK flags this
explicitly rather than letting it pass.

**The masking curve carries no numbers.** It is drawn qualitatively, because
this build measured lowpass behaviour, not masking thresholds. Putting an axis
on it would imply a measurement that was not made.

**Encoder dependence is stated on screen, not buried.** The B03 footnote says
the exact cliff is encoder-dependent. Without it, the reel would be teaching
"16 kHz" as a fact about MP3 rather than a fact about this encoder.

## Vocabulary discipline

| Term | How it is handled |
|---|---|
| lossy / lossless | never used before B03, and by then the concept has been shown twice |
| masking | defined by consequence first — "you physically cannot hear the quiet one" — then named |
| bitrate | introduced as "how much the algorithm was allowed to discard", not as a data rate |
| kilohertz | used as a location on a visible axis, never as a bare number |
| decibel | always shown as a change against a visible reference line, never as an absolute |
| psychoacoustic | **cut entirely** — the idea is delivered without the word |
| transparent | used once in B05 in its audio sense, immediately glossed by context |

## Length

139.77s (2:19) against the ~2:20 sibling explainer. Narration was written to a
per-beat word budget from `af_bella`'s measured rate and landed on the first
pass; no beat was re-cut. The 9:16 Short is the same length.

## Name pronunciation

`narration_text` spells the presenter phonetically — `Row-Haan VeeJayKooMaar` —
so Kokoro says it correctly. Every on-screen string keeps the correct spelling.

VERDICT: **PASS**
