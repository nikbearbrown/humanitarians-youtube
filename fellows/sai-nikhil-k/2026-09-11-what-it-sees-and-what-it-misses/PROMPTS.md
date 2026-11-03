# PROMPTS — What It Sees, And What It Misses

**There are no open generation slots in this reel.** Every beat is either a
registered Remotion composition rendered from props in `beat_sheet.json`, or a
still composed locally by `make_plates.py` from the author's own images. Nothing
is pending an image model, a stock purchase, a Higgsfield clip or any other
external generation.

This file exists because GATE F requires it, and because two beats do carry
prompts that matter — just not generation prompts.

---

## B00 — the on-screen typed ask

This is the `command` prop of `ClaudeComposerAsk`. It is **typed on screen and
not spoken**; the spoken words are `narration_text`, which differs.

> LoonNet, first iteration. 106 images trained, 26 held back and never seen.
> Here are its predictions. Don't tell me it looks promising — go frame by frame,
> tell me what it gets wrong, how often, and which of those are the same mistake
> wearing two names.

---

## B08 — the handoff prompt the viewer can paste

This is the `command` prop of the second `ClaudeComposerAsk`. It is both typed on
screen **and** discussed in narration, as the handoff beat requires. It is
written to be useful to someone who has a first detector of their own and has
not yet looked past the metrics.

> Take a detection model I just trained and its validation prediction sheet.
> Ignore the metrics. Go frame by frame, list every wrong box, and group them by
> CAUSE — duplicate, false positive, miss. Then tell me how many distinct
> problems I have, and which of them more training data will not fix.

---

## Still composition — not a prompt, a script

`media/B02.png`, `media/B04.png`, `pantry/B02-916.png` and `pantry/B04-916.png`
are composed deterministically by `make_plates.py` from:

- `images/B02-source.jpg` — the author's `val_batch0_pred.jpg`, 1920×1280
- `images/B02b-source.jpg` — the author's `val_batch1_pred.jpg`, 1920×1920

No model generated any pixel of these plates. Every bounding box, label and
confidence value on them is the author's own YOLO output, reproduced unaltered;
the script only crops, scales, and sets the frames on the reel's cream ground
with captions. Re-run `python3 make_plates.py` to rebuild all four, and
`python3 make_plates.py --audit` to re-check cell selection if either source
sheet is regenerated.
