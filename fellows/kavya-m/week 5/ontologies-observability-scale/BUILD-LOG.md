# BUILD-LOG — Ontologies for Observability at Scale (Kavya)

"Ontologies for Observability at Scale" — personal project, presenter
Kavya Mehta, voice `am_onyx` (Kokoro), palette `claude`. Adapted from
`claude-liam-ontologies-observability-scale`, built earlier this session.

## Structural decisions

- Content (narration, framework, worked example) reused verbatim from the
  original claude-liam reel. Only presenter, branding, folder chip,
  terminal `host`/`path`, and outro pattern changed.
- Outro: `ClaudeVerdictArtifact`, "Made by" / Kavya Mehta /
  narration-disclosure line — matching the established pattern from
  `kavya-semantic-layers-ai-context` (a topic-explainer outro, distinct
  from the "Built by" pattern used on the Brutalist/CabStream progress
  reels).

## CRITICAL FIX: every prior video this session was the wrong resolution

While resending corrected beat sheets for the Brutalist week reels, a
README file changed unexpectedly on disk for `kavya-cabstream-week2-progress`
with claims that the delivered videos were 1280×720 review previews, not
native 4K masters. Verified directly with `ffprobe`:

```
kavya-cabstream-week2-progress-slate.mp4            → 1280x720
kavya-cabstream-week2-progress-vertical-slate.mp4   → 1080x1920
```

**Root cause:** `runtime/scripts/compile.py`'s `--height` argument
defaults to `720` (`ap.add_argument("--height", type=int, default=720)`).
Every landscape compile this session was run without an explicit
`--height`, silently producing 1280×720 output instead of 3840×2160.
Every vertical compile was run with `--height 1920` (copied from the
example command `./art vertical` itself prints as its suggested "next
step"), producing 1080×1920 instead of the true portrait 4K, 2160×3840.
The correct flags — `--height 2160` for landscape, `--height 3840` for
vertical — are stated explicitly in `skills/make/fellows/SKILL.md`
("use height 2160 for landscape and height 3840 for the 9:16 master") but
were not applied to any reel built this session before this one.

**Scope of impact:** every video delivered this session before this reel —
`kavya-brutalist-week1/2/3-progress`, `kavya-cabstream-week1/2-progress` —
is at the wrong (review) resolution and needs recompiling, rehashing, and
redelivering. This reel (`kavya-ontologies-observability-scale`) is the
first one built correctly from the start — its landscape master was
recompiled once (from 1280×720 to 3840×2160) after the bug was found, and
its vertical master was compiled once, correctly, at `--height 3840`
directly.

**Why this wasn't caught earlier:** every QC spot-check this session
inspected *per-beat* render frames (`media/B0X.mp4`), which Remotion always
renders at full native resolution (`scale: 2` on a 1920×1080 or 1080×1920
composition = 3840×2160 / 2160×3840) regardless of the compile step's
`--height`. The screenshots genuinely were 3840×2160 — it was only the
*compiled, concatenated* master that `compile.py` silently downscaled.
Checking a per-beat frame's resolution was not sufficient evidence for the
final master's resolution; this was the actual gap in the verification
method.

**Fix going forward:** always pass `--height 2160` on every landscape
`compile.py` call and `--height 3840` on every vertical one, and verify
the *final compiled master* (not a per-beat frame) with `ffprobe` before
reporting a build as done.
