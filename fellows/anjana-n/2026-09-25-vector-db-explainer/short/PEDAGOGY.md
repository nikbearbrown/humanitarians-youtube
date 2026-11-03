# PEDAGOGY — What Vector Databases Do That SQL Cannot (9:16 derivative)

This is a derivative cut of `anjana-s/2026-09-25-vector-db-explainer`, produced
by `runtime/scripts/shorts.py` — same signed script, same evidence, reformatted
to 9:16. The parent's GATE P sign-off (`PEDAGOGY.md`, `VERDICT: PASS`) covers
every beat's content; nothing here re-argues that evidence.

## What's different from the parent

**Nothing was cut.** The parent runs 170.9s, inside the 3:00 Shorts cap, so this
is a full reformat rather than a shortened cut — same as the sibling
`embeddings-explainer`. Consequences:

- **No outro rewrite.** The rewriter exists to name the beats a short had to
  drop; with nothing dropped there is nothing to name, so it was suppressed with
  `--no-outro-rewrite` and B08's audio is reused untouched. (On every reel in
  this batch that *did* drop beats, that rewriter produced an unusable sentence
  and had to be hand-corrected.)
- **8 beats rewired to portrait `916` compositions** via the Onda check, with
  the reflow move logged per component:
  - B01 — R2 (restack): the two queries keep their vertical order and the
    "what hasn't arrived yet" box moves from the right half to the bottom of
    the frame, where a portrait viewer's eye ends up anyway. Each query wraps
    onto two lines so the monospace stays legible at phone width.
  - B02 — R1 (re-place): the space is re-laid out tall, green cluster high and
    red low, so the distance between them runs the long axis and reads *harder*
    than it does in landscape.
  - B03 — R2 (restack): queries the same portrait coordinates as B02, so the
    viewer recognises the space, and the ranked list moves from beside it to
    underneath.
  - B04 — R2 (restack): the split screen becomes a stack, brute force above and
    the graph walk below, so both counters stay legible.
  - B05 — R1 (re-place): the four use cases move from one row into a 2×2 grid,
    glowing in the same order.
- **Endcard generated with `--handle ""`** at cut time — the durable fix — and
  pre-built at 2160×3840, because `shorts.py`'s `endcard_png()` hardcodes
  1080×1920 and upscales badly against a 4K master.

## Evidence discipline

No new factual claims, and no beats dropped, so the parent's evidence table
applies in full and unchanged. The portrait B04 computes its own comparison
count from its own graph walk, exactly as the landscape version does — the two
layouts generate different point clouds, so the numbers differ, and each one is
true of the walk drawn beside it.

VERDICT: PASS
