# NARRATION — "Visual Question Answering, Blind?"

Reviewed at GATE P (`PEDAGOGY.md`). Kokoro `am_onyx`, speed 1.0. Durations below are
MEASURED from the generated mp3s — they are the master clock every visual conforms to,
and they are identical in the 16:9 and 9:16 cuts because both reels use the same files.

| Beat | Act | Words | Measured | Pattern (16:9) |
|---|---|---|---|---|
| B00 | ASK | 24 | 7.34s | `ClaudeComposerAsk` |
| B01 | SUMMARY | 34 | 10.20s | `VqaExecSummary` |
| B02 | FRAMEWORK | 35 | 11.43s | `VqaFourMoves` |
| B03 | MECHANISM | 37 | 13.03s | `VqaTokenize` |
| B04 | WORKED-EXAMPLE | 37 | 13.48s | `VqaAttend` |
| B05 | MECHANISM | 24 | 8.19s | `VqaDecide` |
| B06 | FALSIFIABILITY | 38 | 12.99s | `VqaBlindTest` |
| B07 | EDGE-CASE | 38 | 12.20s | `VqaPairs` |
| B08 | VERDICT | 32 | 9.00s | `ClaudeVerdictArtifact` |
| B09 | HANDOFF | 46 | 13.82s | `ClaudeComposerAsk` |
| B10 | OUTRO | 7 | 4.01s | `ClaudeTitleOutro` |
| **total** | | **352** | **115.69s** = 1:55.7 | |

## The spoken track

### B00 · ASK · 7.34s

A model answers questions about a picture. I want the real path from pixels to answer — and whether it even needs the picture.

> **On screen (typed, not spoken):** Visual question answering with transformers: show me the exact path from pixels and words to an answer, tell me how much accuracy survives if I hide the image, and give me one test I can run on any VQA model.

### B01 · SUMMARY · 10.20s

I'm Ritik. Give a model an image and a question, it returns an answer. I'll show you the four moves a transformer makes — and the experiment proving most answers never needed the image.

### B02 · FRAMEWORK · 11.43s

Four moves. Tokenize both inputs into one currency. Fuse them with attention. Pool, then decide. Then audit — because the first three can be flawless and still answer from memory. Move four is the rubric.

### B03 · MECHANISM · 13.03s

Move one. Transformers only eat sequences. So the image is sliced into sixteen-pixel patches — a hundred ninety-six vectors. The question splits into subwords at the same width. Pixels and words become the same kind of thing.

### B04 · WORKED-EXAMPLE · 13.48s

Move two — the worked example. The token for color becomes a query. It scores every patch; softmax sharpens those scores onto the umbrella. Concatenate into one stack, that's ViLT. Keep two towers and cross-attend, that's LXMERT.

### B05 · MECHANISM · 8.19s

Move three. Pool to one vector, score it with a linear head, pick from a fixed answer list. Most VQA is classification, not generation.

### B06 · FALSIFIABILITY · 12.99s

Move four. In the original VQA paper, a model that never sees the image lands within nine points of the model that does. On yes-or-no questions, the blind one clears seventy-eight percent. The picture was worth almost nothing.

### B07 · EDGE-CASE · 12.20s

The fix is a test you can steal. For every question, find a second image where the honest answer flips. Balanced that way, the language-only baseline drops five points, and the best model of the day drops six.

### B08 · VERDICT · 9.00s

The verdict. The four moves are real. The architecture is honest. The benchmark was not. Show me a blind score and a paired score, or I don't know what your model sees.

### B09 · HANDOFF · 13.82s

Your turn. Paste this. Take any VQA model and report four numbers: with the image, with the image replaced by noise, on ten pairs you build yourself, and where the attention lands. If the noise number is close, you have a language model wearing a camera.

> **On screen (typed, not spoken):** Take a VQA model I can run locally. Report four numbers: accuracy with the image, accuracy with the image replaced by Gaussian noise, accuracy on ten complementary pairs I build by hand, and the fraction of cross-attention mass landing inside the region my question names. Then tell me which of the four moves is actually doing the work.

### B10 · OUTRO · 4.01s

Visual Question Answering, Blind? Humanitarians A I.

> **On screen (typed, not spoken):** Visual Question Answering, Blind?

## Why the voice and the screen say different things

Every published figure is spoken loosely and shown exactly. B06 says "within nine points"
and "clears seventy-eight percent"; the frame shows 48.76, 57.75, +8.99 and 78.20 with the
citation beneath them. That split is the whole point of the show-don't-tell rule here —
the voice carries the judgment, the screen carries the digits, and a viewer who wants to
check a number can read it rather than rewind for it.

B00 and B09 carry a `narration_text` that differs from `narration`: those beats type a long
prompt into the Claude composer while the voice says something shorter. The audio script
reads `narration` when present, so the spoken line is the short one.
