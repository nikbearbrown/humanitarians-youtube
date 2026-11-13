# PROMPTS — Refuse, Don't Guess

**There are no open generation slots in this reel.** Eight beats are registered
Remotion compositions; two are screen recordings of the real app. No image model,
no stock purchase, no Higgsfield clip, no generated picture. No key is required
and nothing cost money — a Fellow Tier build end to end.

This file exists because GATE F requires it, and because two beats carry prompts
that matter — they are just not generation prompts.

---

## B00 — the on-screen typed ask

The `command` prop of `ClaudeComposerAsk`. **Typed on screen, not spoken**; the
spoken words are `narration_text`, which differs.

> Gavia 0.3.1 checks up to 25 photos at once, or a zip of them. Before you call that progress: what happens to the 26th photo, and to a file it can't read? Show me in the app, then in the code.

---

## B08 — the handoff prompt

The `command` prop of the second `ClaudeComposerAsk`. **Typed on screen and
discussed in narration** — the thing the viewer is meant to paste.

> My tool has a limit. Before I ship, walk me through the limit plus one. Does anything get dropped without the user being told? If so, who would notice, and when? Make the case for refusing the whole input instead, and tell me where refusing would be worse.

---

## The executed scripts and recordings

Not prompts, but they are the reel's only generated content. All are preserved
with their recorded output.

| Script / command | Produces | Deps |
|---|---|---|
| `evidence/fetch_photos.py` (+ `commons_search.py`, `commons_fetch.py`) | `images/src/` — 26 Commons photos + licence sidecars | Python 3, network |
| `evidence/make_survey.py` | `ui/survey.zip`, `ui/extra/photo-26.jpg`, `evidence/batch_manifest.json` | Python 3 |
| `evidence/batch_rules.test.ts` in a clone at `760e465` | `evidence/batch_rules.out` → B04, B03 checks | Node 26, the repo's `npm ci` |
| `npx vitest run`, `cargo test --release` at `760e465` | `evidence/vitest.out`, `evidence/cargo_test.out` | Node, Rust 1.97.1 |
| `evidence/release_and_ci.sh` | `evidence/release_and_ci.out` | `gh` |
| `ui/rec/take_batch.sh`, `ui/rec/take_updates.sh` (+ `rec2.sh`, Swift helpers) | `ui/takes/*.mp4`, `ui/rec/*.timeline`, `ui/rec/take_net.log` → `evidence/ui_batch.out`, `evidence/ui_network.out` | macOS, Screen Recording for Terminal, Accessibility, ffmpeg |
| `make_ui.py` | `media/B01.mp4`, `media/B05.mp4`, `pantry/B01-916.mp4`, `pantry/B05-916.mp4` | Pillow, numpy, ffmpeg |
