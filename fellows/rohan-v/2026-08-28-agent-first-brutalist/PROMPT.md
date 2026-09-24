# PROMPT — "Your Weekly Video, Handled."

## The brief

Build a 3–5 minute `ai-explainer` reel that teaches a Humanitarians AI fellow the
**entire** weekly video pipeline — from a machine with nothing installed, through
to four files delivered to the two correct destinations.

Audience: fellows who are **not** necessarily programmers. The reel must be
followable by someone who has never opened a terminal, and it must be explicit
about which steps the agent performs and which stay human.

## Constraints given

| Constraint | Resolution |
|---|---|
| Opens "Hi, I'm Rohan" | B00, first line of narration. |
| Signs off with the full name | B12: "I'm Rohan V., for Humanitarians AI." Outro subline carries it on screen. |
| Voice `af_bella` | `metadata.voice_kokoro`; every beat generated with it. |
| 3–5 minutes | Measured **4 min 14 s**. |
| Fellows never type commands | The whole spine. B02 shows approval, not typing; B08 shows the agent choosing the Git route; B10 states "Not one of them requires a command line." |
| Fellows interact via the **Claude desktop app** | B02 and B11 are fidelity mocks of the desktop app specifically (sidebar, thread, permission card). |
| Recreate Claude / GitHub / other windows | Three product surfaces rebuilt natively: Claude desktop (B02, B11), GitHub dark (B07, B08), Google Drive (B09). |
| Fluid animation | Spring-driven throughout: type-on, cursor travel with smoothstep easing and a click ring, stroke-dashoffset git-graph edges, a proportional reflow ghost for the 16:9→9:16 derivation, staggered progress fills. |
| Exact links on screen | All three, verbatim — see FACTCHECK.md §Links. |
| Four files: 2 topics × 2 formats, 4K | B01 establishes it, B06 shows the derivation, B09 shows all four uploading. |
| Manual vs automated made explicit | Every step beat carries a `STEP N · AUTOMATED` or `· THIS ONE IS YOURS` eyebrow, and B10 is a dedicated 7-vs-3 ledger. |
| Fork+PR for new fellows, branch+PR for those with access | B08, as two lanes of one git-graph converging on `main`. |
| Docs (<25 MB) → GitHub; videos → Drive | B07 (what commits, what does not) and B09 (what is uploaded by hand). |
| No mention of any third party by name | No personal name in any narration line or on-screen string except the presenter's. See FACTCHECK.md §Deliberate omissions for the one unavoidable case: the repository URLs. |

## Structure

Standard Claude bookends, pragmatist middle:

```
B00  ASK          composer cold open — the problem, stated by the presenter
B01  REQUIREMENT  what is due, and when
B02  SETUP        one-time install, by approval
B03–B06  THE LOOP plan → voice → your review → the two formats
B07–B09  SUBMIT   docs to GitHub · the access question · videos to Drive
B10  RECAP        7 automated vs 3 yours
B11  YOUR TURN    the paste-ready prompt
B12  OUTRO        title restate + sign-off
```

## Build order actually used

1. `./setup --install` — verified every dependency live (one Windows fix, below).
2. `./art scenes "…"` per beat — **library-first**. Reused `ClaudeComposerAsk`,
   `ClaudeTitleOutro`, `GitHubRepoHero`'s `OctoMark`, and the `github`/`claude`
   token sets. Ten genuine gaps were built as new components rather than slated.
3. `./art scene-index` — registered all ten under `hai-weekly-submission`.
4. Still-frame QC on all ten before any audio spend; fixed title-safe bleed on
   eight spark lines, a missing-glyph branch icon, and three underfilled canvases.
5. `generate_audio_kokoro.py` — audio measured first; composition durations then
   set from those measurements.
6. `remotion_scenes.py` → `compile.py` → Gate V frame check.

## Toolkit changes made during the build

Both are genuine cross-platform defects in the clone, not workarounds:

| File | Change | Why |
|---|---|---|
| `runtime/scripts/remotion_scenes.py` | Resolve `npx` via `shutil.which`, falling back to `npx.cmd` | On Windows npm ships `npx.cmd`; `subprocess.run` without `shell=True` raises `FileNotFoundError` on the bare name. Rendering was impossible on Windows before this. |
| `runtime/remotion/src/Root.tsx` | Added the `hai-weekly-submission` folder and 10 compositions | Required by GATE L — a component not in the index cannot be found by the next fellow. |

Note for anyone re-running `./setup` on Windows: `python3` resolves to the
Microsoft Store stub unless the real Python directory precedes `WindowsApps` on
`PATH`. Prepend it before running, or the readiness table reports false misses.

## What this reel deliberately does not do

- **It does not publish.** No YouTube machinery is invoked; the master stays in
  this folder. Uploading is a human decision.
- **It does not upload to Drive.** The agent cannot and should not; B09 says so.
- **It carries no slates.** Nothing is owed by a human before it compiles clean.
