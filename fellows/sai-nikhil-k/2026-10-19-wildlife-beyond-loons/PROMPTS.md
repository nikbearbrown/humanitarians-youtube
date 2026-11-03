# PROMPTS — Seals Pass, Seabirds Wait

**There are no open generation slots.** Nine beats are registered Remotion
compositions; two are plates of real, freely licensed photographs. No image
model, no stock purchase, no Higgsfield clip, no paid API.

## B00 — the on-screen typed ask (typed, not spoken)

> Gavia finds loons in photos, offline, for a person to review. Which wildlife should the next Gavia count? Check who counts it by hand today, whether a dataset lets us ship trained weights, and whether an offline app already exists.

## B09 — the handoff the viewer can paste

> Pick one animal I care about and run four checks with me: who counts it by hand today, is there a labelled dataset whose licence lets me ship trained weights, does an offline tool already exist, and does it fit photos → boxes? Link every source.

## The evidence commands (B05)

```bash
python3 weekly_updates/2026-10-19-wildlife-beyond-loons/evidence/maine_labels.py \
  > weekly_updates/2026-10-19-wildlife-beyond-loons/evidence/maine_labels.out
python3 weekly_updates/2026-10-19-wildlife-beyond-loons/evidence/seal_labels.py \
  > weekly_updates/2026-10-19-wildlife-beyond-loons/evidence/seal_labels.out
```

Both download their public files into `evidence/data/` if missing (no account,
no key) and count them with the standard library.
