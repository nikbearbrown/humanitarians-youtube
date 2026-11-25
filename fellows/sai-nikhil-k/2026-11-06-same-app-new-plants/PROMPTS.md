# PROMPTS — Same App, New Plants

**No open generation slots.** Seven Remotion compositions and three plates of
real Gavia screenshots and iNaturalist photos. No image model, no paid API.

## B00 — the on-screen typed ask

> Gavia 0.5.0 adds Vegnet, a model for four invasive lake plants. How accurate is it, and does it mistake native look-alikes for invasives? Test it on natives.

## B08 — the handoff the viewer can paste

> Pick one invasive plant in my area. Name the native plants most often mistaken for it, and the field marks that tell them apart in a photo. Link an iNaturalist observation of each.

## Evidence commands

```bash
REEL=weekly_updates/2026-11-06-same-app-new-plants
# 1. the native look-alike sample (40 photos + sidecars, not committed)
python3 $REEL/evidence/lookalike_fetch.py $REEL/evidence/data/lookalikes --n 8 > $REEL/evidence/lookalike_fetch.out
# 2. Gavia's own code: clone github.com/nikhil-kunapareddy/gavia at v0.5.0, copy
#    evidence/lookalike_check.rs into desktop/src-tauri/examples/, then in desktop/src-tauri:
cargo run --release --example evaluate -- \
    --split ~/Documents/loonet/data/annotated/vegnet_v1/val.txt \
    --model resources/models/veg_v1.onnx                                  # -> evaluate_vegnet.out
cargo test --release --test plants
cargo run --release --example lookalike_check -- $REEL/evidence/data/lookalikes \
    --split ~/Documents/loonet/data/annotated/vegnet_v1/val.txt          # -> lookalike_check.out
```
