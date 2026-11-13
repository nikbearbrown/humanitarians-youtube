# PROMPTS — The Weights Were Never the Risk

**There are no open generation slots in this reel.** All ten beats are
registered Remotion compositions rendered from props in `beat_sheet.json`. No
image model, no stock purchase, no Higgsfield clip, no pantry still. No key is
required and nothing costs money — a Fellow Tier build end to end.

This file exists because GATE F requires it, and because two beats carry prompts
that matter — they are just not generation prompts.

---

## B00 — the on-screen typed ask

The `command` prop of `ClaudeComposerAsk`. **Typed on screen, not spoken**; the
spoken words are `narration_text`, which differs.

> Gavia 0.2.0 swapped its Python backend for a Rust core and ships on three systems. Before you congratulate me, tell me how I know it still finds the same loons. “Same weights” is not an answer.

---

## B08 — the handoff prompt

The `command` prop of the second `ClaudeComposerAsk`. **Both typed on screen and
discussed in narration** — it is the thing the viewer is meant to paste.

> I'm porting a model's inference code to another language. The weights will not change. Before I delete the old code, tell me what to freeze: its outputs on real inputs, every step that touches pixels before the network does, and the one metric I expect to move — and why it moves.

---

## The executed scripts

Not prompts, but they are the reel's only generated content. All are preserved
with their recorded output under `evidence/`.

| Script / command | Produces | Deps |
|---|---|---|
| `cargo test --release --test parity` @ `78b383e` | B04 rows 1–3 | Rust 1.97.1, the local `loonnet_v1` split |
| `cargo run --release --example evaluate` @ `78b383e` | B04 row 4, B05 upper track | same |
| `backend/scripts/evaluate.py` @ `663feeb` | B04 row 4 (Python side) | onnxruntime 1.29.0, numpy 2.4.6, Pillow 12.3.0 |
| `evidence/draft_factor.py` | B03 conditions line (26 of 26) | Pillow 12.3.0 |
| `evidence/scale_probe.rs` | B03 narration + conditions (15 of 26) | jpeg-decoder 0.3.2 via Gavia's crate |

None needs a network or a key once the crates and wheels are installed.

---

## Why there is no Higgsfield beat

**No beat was authored as a candidate.** The reel's argument is that the same
file can produce different answers depending on what is fed to it; every frame
is therefore a typeset rule, a recorded measurement, or text the author wrote.
A generated clip would be the one thing in it that stands for nothing.
