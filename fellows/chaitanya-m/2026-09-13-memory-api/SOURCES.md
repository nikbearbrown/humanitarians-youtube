# SOURCES — Memory API (Medhavy Hub)

## Narration

Every spoken line is **verbatim** from `../memory-api-script-2min.md`. Nothing
paraphrased, added, or cut, with two mechanical exceptions:

1. Markdown backticks were stripped from `chat_memory_turns`,
   `learner_profiles`, `memory_subject` and `hub:` so the TTS does not vocalise
   them. The words are unchanged.
2. Kokoro's standing symbol map renders `—` as a comma pause.

**Scene 5 uses the PRIMARY narration.** The alternate ("ONE STUDENT, MANY
BOOKS") was deliberately not substituted — see PEDAGOGY.md. The script flags
the underlying claim as possibly stale and the operator has not confirmed it.
The build agent did not attempt to resolve it and has no access to the book
repositories.

Beat mapping: B01–B06 = deck scenes 1–6 in order, unsplit.

## Visuals

**Nothing was invented and nothing was re-implemented.** Every frame of B01–B06
is `../memory-api-deck.html` rendered as-is by Chrome at a 3840×2160 viewport.
The deck sizes everything in container-query units (`cqw`), so at that viewport
the stage is exactly 3840×2160 and all type is vector-crisp — this is native 4K,
not an upscale.

Capture method, for reproducibility:

- Each scene is emitted as a standalone HTML copy with that `<section>` already
  carrying `.on` and the deck's controller script removed, so nothing can reset
  the active scene.
- All CSS animations are frozen (`animation-play-state:paused`) from the first
  frame, then seeked to an exact time by rewriting each element's
  `animation-delay` to `(original − t)`. The deck declares its `.d1`–`.d7`
  delays with `!important`, so the seek uses `setProperty(..., 'important')`.
  This makes each frame a pure function of `t` — deterministic and re-runnable.
- The entrance animations are sampled at true 24 fps until they settle (per
  scene, 1.3 s–3.3 s), after which the deck is static, so the settled frame is
  captured once and held.
- The deck's progress rail is **not** captured — it advances across the whole
  scene. It is composited afterwards by ffmpeg across each beat's real measured
  duration, so it still reaches 100% exactly at the scene end.

Fonts are the deck's own — **Archivo Black** and **IBM Plex Mono**, loaded from
Google Fonts by the deck itself. No substitutions.

## The one added visual

`B00` has no counterpart in the deck: it carries the requested spoken sign-in
line. Its card was generated **from the deck's own file** — the deck's CSS,
rail, and markup classes, with the six scenes stripped and one section inserted.
It is not a separate design. On-screen lede matches the spoken line verbatim.

Rail reads `SIGN-IN` / `00 / 06` to mark it as pre-roll rather than renumbering
the deck's six scenes.

## Claims spoken on camera

| Claim | Source | Verified by this build? |
|---|---|---|
| Two tables: `chat_memory_turns`, `learner_profiles` | Script + deck | No |
| Both key on `memory_subject` | Script + deck | No |
| `hub:` prefix sliced off; Clerk user ID stored separately | Script + deck | No |
| Keeps 24 turns / 48 rows, prunes older | Script + deck | No |
| Two endpoints, shared-secret auth | Deck scene 5 | No |
| "I read the code, it works" | Script — the **script author's** first-person claim | No |
| At least one book uses local SQLite, scoped to that book | Script, **self-flagged as partly stale** | No |

**None independently verified.** The build agent has no access to the Medhavy
hub or the textbook repositories. Everything is reproduced on the authority of
the script and deck. The stale-flagged Scene 5 claim is the one to resolve
before publishing: `grep -r 'x-memory-api-secret'` in a book repo, or ask
Prarthana.

## Toolchain

| Component | Source |
|---|---|
| Narration | Kokoro-82M via `kokoro-onnx`, voice `af_bella` ("Bella", hai persona) |
| Visuals | Google Chrome headless, `--virtual-time-budget`, 3840×2160 viewport |
| Progress rail | ffmpeg `drawbox` with a time expression |
| Assembly | brutalist `compile.py` via `./art final` (read-only) |
| 9:16 derivation | brutalist `shorts.py` (read-only) |

No paid service, no API key. The only network access is the deck's own Google
Fonts request.
