# SHOTLIST — "SQL, Read Fewer Rows."

Reel: `fellows/supriya-k/2026-09-16-sql-query-optimization-for-analytics`
Typed work order, per the parent `explainer` slot contract. One beat = one visual
slot = one conformed per-beat mp4 named by beat id.

**Slot precedence at compile:** `media/<BID>.mp4` > `manim/<BID>.mp4` >
`media/<BID>.png` > **slate**. Every slot below is filled by Remotion, so this reel
has **no human-media slots and no slates** — nothing is waiting on a screen
recording, a download, or a purchase.

## The ten slots

| Beat | Act | Pattern | Origin | UI? | `content_type` | Est. |
|---|---|---|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | **library** | UI — cold open (exempt) | title | 23 s |
| B01 | SETUP | `AttritionChain` | **library** | illustration | data | 22 s |
| B02 | ASK | `ClaudeComposerAsk` | **library** | UI — ask micro-beat (exempt) | title | 14 s |
| B03 | EVIDENCE | `SqlPlanBeat` | **reel-local** | illustration (code/output) | mechanism | 21 s |
| B04 | MAGNITUDE | `ScaleComparison` | **library** | illustration | data | 20 s |
| B05 | PREDICT | `SqlPredictCard` | **reel-local** | illustration | title | 13 s |
| B06 | INSIGHT | `DivergentFates` | **library** | illustration | mechanism | 25 s |
| B07 | VERDICT | `ClaudeVerdictArtifact` | **library** | UI — verdict page (exempt) | mechanism | 28 s |
| B08 | HANDOFF | `ClaudeComposerAsk` | **library** | UI — handoff (exempt) | title | 37 s |
| B09 | OUTRO | `ClaudeTitleOutro` | **library** | UI — outro (exempt) | title | 6 s |

**8 of 10 slots are library compositions.** Two are reel-local, both for reasons
logged in `TEMPLATE-MISSES.md`.

## Scheme histogram (ILLUSTRATE LAW + the MOTION.md 40% cap)

| Scheme | Beats | Share |
|---|---|---|
| Claude UI (all five exempt slots) | B00 B02 B07 B08 B09 | 5/10 — but four are the mandated spine (cold open, verdict, handoff, outro) and one is a required ask micro-beat |
| Rhetorical pattern (deckPatterns) | B01 B04 B06 | 3/10 — three *different* patterns |
| Code / output card | B03 | 1/10 |
| Pedagogy device | B05 | 1/10 |

No single *body* scheme exceeds 40%. No two consecutive beats share a scheme:
`UI → attrition → UI → plan-card → log-scale → predict → divergence → UI → UI → UI`.
The B07–B09 UI run is the spine the laws require, and the three are distinct
compositions (artifact page / composer / title poster).

## Per-beat work order

### B00 — cold open (library: `ClaudeComposerAsk`, 1920×1080)
Props are authored in the beat sheet. Three RESULT `output` lines are **required**
by COLD OPEN LAW — the ask lands answered. Greeting `Hi, Supriya`. Typing is legal
here (one of only two typing beats).

### B01 — the funnel (library: `AttritionChain`, 1280×720)
`data.total: 400` with `slideMeta` declaring **1 DOT = 1,000 ROWS**. Survival
fractions are the real selectivities (0.028423, 0.392207).
**Do not raise `total` toward 400,000** — the component renders one SVG `<circle>`
per unit and would emit 400,000 nodes per frame.

### B02 — the ask micro-beat (library: `ClaudeComposerAsk`)
No `output` prop: this beat is the ASK, B03 is the RESULT. Greeting
`Watch, Supriya` — a one-word arc cue plus persona, which keeps inside the HAI
word budget (the two-word cues `The ask,` / `Watch this,` are Bear's only).

### B03 — the evidence (reel-local: `SqlPlanBeat`)
The executable-evidence beat. Both plan bodies are **verbatim** from
`demo/explain_a_non_sargable.txt` and `demo/explain_b_sargable.txt`. Terracotta
highlight moves `SCAN` → `SEARCH … USING INDEX` on the spoken words — one accent
at a time. Citation strip: "Captured from SQLite 3.45.3 — demo/RESULTS.md".
Never a screenshot; never retyped by hand — if the captures change, re-derive the
props from the files.

### B04 — the magnitude (library: `ScaleComparison`, 1280×720)
Log axis, decades 10³–10⁶, `unit: "rows"`. Band = 4,459–11,369 ("rows the answer
actually needs"). Plan A `hot: true` — the single accent. Axis draws at constant
velocity (MOTION.md §4: axis first, data after).

### B05 — the commit (reel-local: `SqlPredictCard`)
Thin wrapper over the library `PredictCard` + `IlluStage`. Props only; motion math
untouched, per the starter-template contract in `ILLUSTRATIONS.md`. Holds past the
narration on purpose — the silence is the pedagogy.

### B06 — the insight (library: `DivergentFates`, 1280×720)
One origin, two tracks, divergence on the spoken word "strftime". Labels kept
SHORT deliberately (`strftime(…) = '2026-01'`, `posted_at >= … AND < …`) because
the full SQL already lives in B03's card — see QC watch item Q2.

### B07 — the verdict (library: `ClaudeVerdictArtifact`)
`artifactLines` are **bare sentences with no leading numbers** — the component
numbers them itself and strips leading numerals defensively (`stripLeadNum`).
`lead_silence_s: 0.5` before "Let's recap with Claude." (your-turn SKILL: the
prior beat is Kokoro, not ElevenLabs, so it is "Let's recap with Claude.", **not**
"Thanks Bear, …").

### B08 — the handoff (library: `ClaudeComposerAsk`)
`greeting: "Your turn."` — fixed by HANDOFF LAW, the one persona-less greeting.
`props.command` is the suggested prompt; `narration_text` **opens with that prompt
word for word**, then discusses it. Second typing beat. Keep the prompt on screen,
completed and still, through the discussion so the frame is pausable.

### B09 — the outro (library: `ClaudeTitleOutro`)
Title restated poster-style with the terracotta period; `@HumanitariansAI` beneath.

## QC watch list — the things I could NOT verify without rendering

Rendering is out of scope for this scaffold, so these are named rather than
assumed clean. Each is a specific thing to look for in `_qc/` frames, per the
9-point rubric in `CLAUDE-CODE-VISUAL-QC-CHECK.md`.

| # | Risk | Rubric | Why it is a risk | What to do |
|---|---|---|---|---|
| Q1 | **B03 plan text overflow** | 1, 3, 6 | The inherited `ClaudeCodeBeat` layout uses `whiteSpace: 'pre'` with `overflow: hidden` — long lines **clip silently, without wrapping**. Its card is inset 7% L/R with ~26 px padding, so at `fontSize = height × 0.022` (≈23.8 px, mono) the usable budget is roughly **17 lines × ~100 chars**. `SqlPlanBeat` splits into two narrower columns, which halves the per-line budget. The `SEARCH … idx_postings_posted_at (posted_at>? AND posted_at<?)` line is the longest in the reel and is pre-wrapped in the props for exactly this reason. | Read the B03 frames first. If anything clips, shorten the wrap in `props.right.code` — **never** edit the captured plan's content. |
| Q2 | **B06 long track labels** | 3, 4 | `DivergentFates` track labels sit in fixed lanes; SQL fragments are longer than the pattern's design copy. | Labels are already abbreviated with `…`. If they still collide, shorten further — the full text is in B03. |
| Q3 | **Legibility floor** | 6 | `fontSize = height × 0.022` = **23.76 px** at 1080 — a hair under the rubric's 24 px floor. `remotion_scenes.py` renders at `--scale=2` so the master is crisp, but the *relative* size is what the rubric measures. | Judge from the frames. If it reads small, bump the multiplier in the reel-local `SqlPlanBeat` (it is ours to change) — do not patch the shared library scene for one reel. |
| Q4 | **B01 dot-field density** | 6 | `dotR` is derived from grid pitch and clamped to a 1.3 px floor. 400 dots should be comfortable; verify the first panel is not mush. | If mush, drop to `total: 200` at 1 dot = 2,000 rows and update `slideMeta`, `FACTCHECK.md` row 6, and `PEDAGOGY.md`. |
| Q5 | **LOGO LAW — unresolved** | 7 | The five body patterns have no logo-bug slot. This is a real gap, not an oversight. | See `TEMPLATE-MISSES.md` #3. Must be resolved before the master, not after. |
| Q6 | **1280×720 vs 1920×1080 mixing** | 8 | `AttritionChain`, `ScaleComparison`, `DivergentFates` are registered at 1280×720; the Claude scenes at 1920×1080. Same 16:9, so `compile.py` scales — but check for softness or unintended letterboxing on those three beats. | Compare a B04 frame against a B07 frame for sharpness. |
| Q7 | **`SqlPlanBeat` language chip** | — | `ClaudeCodeBeat` hard-codes the chip text `python`. Wrong on a SQL beat, and the direct cause of `SqlPlanBeat` existing. | Confirm the chip reads `sql`. `TEMPLATE-MISSES.md` #1 proposes the upstream fix. |

## Audio

One command, free, local, **only after GATE P is signed**:

```bash
python3 runtime/scripts/generate_audio_kokoro.py <REEL>   # af_bella
```

Per-beat MP3 durations become the master clock. `actual_duration_s` is `null` in
every beat right now — that is correct and deliberate. **Never hand-time a beat**;
regenerate audio and recompile.
