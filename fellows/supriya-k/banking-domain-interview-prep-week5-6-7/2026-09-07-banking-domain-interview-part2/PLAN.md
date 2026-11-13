# PLAN — banking-sql-running-total-bug (CLI-explainer, technical deep-dive)

**Status: DRAFT — awaiting user gate approval. Nothing past this file is generated yet.**

## Pattern being followed — and why it's heavier than the trailer

This is a **different toolkit checkout** from the whole-book trailer: it lives in
`brutalist.art/` (not `brutalist-art/`), which is a separate, "pared-down free-only" sibling
build with its own `skills/`, `runtime/`, and `projects/<book>/<reel-slug>/` convention (not
`reels/<slug>/`). The structural reference you named,
`projects/data-analyst-book/hai-sql-window-functions-tie-bug/`, is built with the **`cli-explainer`
skill** (`skills/make/cli-explainer/SKILL.md`) — a materially different, heavier pipeline than the
trailer's previz-only Manim path:

- **Mixed rendering**: some beats are Manim (`manim/<BID>.mp4`), others are **Remotion**
  (`media/<BID>.mp4`, via `runtime/remotion/` — a real Node/React project, already has
  `node_modules/` installed here, needs a headless-Chrome at render time — should work on this
  Mac by default).
- **Mandatory 12-beat spine** (not a free-form beat count): `INTRO → PROBLEM → MECHANISM →
  [CLI→CODE→OUTPUT] → [CLI→CODE→OUTPUT revision, required] → SUMMARY → NEXT STEPS → OUTRO`.
- **A full paperwork set is required before anything renders** — `SHOTLIST.md`, `FACTCHECK.md`,
  `PROMPTS.md` (hard-gated by **GATE F** in `run.sh`) and `PEDAGOGY.md` (hard-gated by **GATE P** in
  `generate_audio_kokoro.py`, before a single second of narration is generated) — plus
  `NARRATION-SCRIPT.md`, `RESEARCH-SUMMARY.md`, `VISUAL-PLAN.md`, `STATUS.md`, `ToDo.md`, which
  the reference always produces even though no script hard-checks them.
- **Target resolution is 4K** (3840×2160) — the reference package's own render note says so, and
  `run.sh` in this checkout defaults to `HEIGHT=2160` / `manim -qk`.

Your ask was 4 steps (plan → beat_sheet.json → scenes.py → wait for render gate). To genuinely not
deviate from the reference pattern, "planning" here has to expand to include the paperwork set
above — those files are load-bearing (GATE F/P will hard-refuse to render without them), not
optional documentation. I'm flagging this expansion explicitly rather than silently doing 9 files
when you asked for a plan file: **section "Paperwork set" below lists exactly what I'll write, and
none of it gets written until you approve this plan.**

## Source

- **Bug**: `books/banking-data-analyst-interview-prep/factchecks/MASTER_REPORT.md`, Critical
  Finding #3: the Ch. 8 worked example's `running` CTE filtered to the Jan–Jun 2026 reporting
  window *before* computing the cumulative `SUM() OVER`, silently truncating balance history for
  any account with pre-2026 activity. Fixed by moving the date filter downstream, into
  `last_posting_per_month`, so `SUM() OVER` sees the entire ledger first.
- **Worked example**: `chapters/08-sql-i-balances-cohorts-window-functions.md`, lines 141–197 —
  the fixed query (already correct in the shipped book) plus the book's own prose explaining why
  the ordering matters. I'll show the *reconstructed buggy version* (WHERE inside `running`) as
  the "before," and the book's actual shipped query as the "after" — both are real, both are
  quoted/derived directly from the manuscript, nothing invented except illustrative sample ledger
  rows (same license the reference project used for its own sample data).

## Output location

`brutalist.art/projects/banking-data-analyst-interview-prep/banking-sql-running-total-bug/`
(mirrors the reference's `projects/<book>/<reel-slug>/` convention; the reference's `<book>` folder
name `data-analyst-book` is a short alias for `books/data-analyst-interview-prep`, so I'm using the
full book slug here for clarity — flag if you'd rather I shorten it to match that alias style.)

## Persona / compliance — open decisions I'm flagging, not deciding unilaterally

This toolkit copy only wires up two named personas: **`liam`** (default — Kokoro `am_onyx`,
`claude-liam` channel, `@NikBearBrown`, "IN-FOR-BEAR LAW": *"Liam, in for Bear"*) and **`hai`**
(Kokoro `af_bella`, `claude-hai` channel, `@HumanitariansAI` — confirmed from
`projects/data-analyst-book/OVERVIEW.md`: that package's narrator says *"Supriya for Humanitarians
AI"* in every cold open — a coincidental name match to you, not a description of you). Your
instruction is explicit: **neither named persona, no channel branding — just "in for Supriya,"**
matching exactly what the whole-book trailer already did. Recommended plan (same as the trailer,
for series consistency):

- **No persona name.** B00 and the outro (B11) say "in for Supriya" directly — no "Liam," no
  "Bear," no channel handle standing in for you.
- **Tool skin: `claude`** (the default skin — cream/ink/terracotta `ClaudeComposerAsk`/
  `ClaudeCodeBeat`/`ClaudeTitleOutro`). No reason to pick `onda` (dark terminal) or `codex` unless
  you'd prefer the terminal look for a SQL-heavy piece — flagging as a real alternative.
- **Voice: Kokoro `af_heart`** (same voice as the whole-book trailer, for series continuity) —
  deliberately *not* `am_onyx`/`af_bella`, since those are the Onyx/Bella named identities tied to
  the other two channels.
- **Corner brand mark (LOGO LAW):** the skill requires a channel bug on every beat. With no real
  channel, I'll use a plain text mark — the book's short title — instead of an `@handle`. Flag if
  you'd rather drop the corner mark entirely (a deliberate, documented deviation) or use something
  else.

**Please confirm or override these four bullets** along with the plan.

## Beat arc (12 beats, matching the reference's exact spine shape)

| Beat | Role | Renders via | Content |
|---|---|---|---|
| B00 | INTRO (cold open) | Remotion `ClaudeComposerAsk` | "in for Supriya" line + the one-sentence hook: a correct-looking query can still be wrong |
| B01 | PROBLEM | Manim | Why care: "balance as of date X" = "sum every posting up to X" — get one clause out of order and the query still runs, still returns numbers, all wrong, no error. Corrected from my first draft below: SHOW-DON'T-TELL LAW requires this beat to move, not sit as a static card — matches the reference's own B01, which is Manim |
| B02 | MECHANISM | Manim | The ordering rule: a `WHERE` in an earlier CTE runs before a `SUM() OVER` two CTEs later — filter early and the running total never sees what got cut. Split visual: filter-then-sum (wrong) vs sum-then-filter (right) |
| B03 | CLI (ask) | Remotion `ClaudeComposerAsk` | Ask Claude to review the Ch. 8 running-balance query before it ships |
| B04 | CODE | Remotion `ClaudeCodeBeat` | The actual buggy SQL — `WHERE posted_at >= '2026-01-01' AND < '2026-07-01'` inside the `running` CTE |
| B05 | OUTPUT (run) | Manim | Animated result table: an account with real 2025 history shows a balance that resets near zero in January — wrong, and it doesn't error |
| B06 | CLI (revision, required) | Remotion `ClaudeComposerAsk` | "That's a bug, not a feature" — the fix: move the date filter out of `running`, into `last_posting_per_month` |
| B07 | CODE (revised) | Remotion `ClaudeCodeBeat` | The actual fixed SQL — the book's real shipped query |
| B08 | OUTPUT (revised) | Manim | Mirrored table: the true prior balance now carries forward correctly; the wrong number fades, the right one lands |
| B09 | SUMMARY | Manim | The lesson: the bug was never the window function — compute the running total over the whole ledger, narrow to the reporting window only after. Also corrected to Manim (animated checklist + checkmarks), matching the reference's B09 |
| B10 | NEXT STEPS (handoff) | Remotion `ClaudeComposerAsk` | "Your turn" — suggested prompt: check your own running-balance CTE for a `WHERE` living one CTE too early |
| B11 | OUTRO | Remotion `ClaudeTitleOutro` | Title restate + "in for Supriya" sign-off |

Target runtime ~4–5 min (260–300s), matching the reference package's own stated 4–6 min range for
this format (not the shorter ~2 min canonical example in the skill's own docs) — B02 (MECHANISM) is
the one beat beyond the skill's *minimum* required spine, included because the reference project
also added it and because this bug is genuinely about an ordering *rule*, which earns a dedicated
beat.

Register: **Teardown** (spare, no fabrication, forbidden-phrase list in `voices/teardown/VOICE.md`)
— same voice doctrine the reference used, independent of which persona/channel speaks it.

## Paperwork set (required — GATE F / GATE P — written before beat_sheet.json)

| File | Purpose | Gates it satisfies |
|---|---|---|
| `SHOTLIST.md` | Minimal pattern (like the reference): no archive/AI-image slots exist here — every beat resolves via Remotion or Manim — so this documents that explicitly, satisfying GATE F's paperwork check without inventing shot prompts that don't apply | GATE F |
| `PROMPTS.md` | Same minimal pattern — no open AI-image slots | GATE F |
| `FACTCHECK.md` | Claim-by-claim trace: every on-screen/spoken claim → the exact chapter/factcheck line it's sourced to, verdict column, plus the "what's new/illustrative and why it's not fabricated" section for sample ledger rows | GATE F |
| `PEDAGOGY.md` | Checklist against the skill's required elements (spine present, Revision Law, Actual-Code Law, moving-output law, no fabrication, handoff quality) + `VERDICT: PENDING` — **only you sign this to PASS**, same as the reference (its own `PEDAGOGY.md` carries `VERDICT: PENDING` awaiting sign-off) | GATE P |
| `NARRATION-SCRIPT.md` | Human-readable script: one block per beat, narration text + act label, footer with word count/pace/estimated duration | none (documentation) |
| `RESEARCH-SUMMARY.md` | Source citation, the book's own mechanism explanation quoted, the exact bug/fix text quoted verbatim, "what this adds that is not a new fact" | none (documentation) |
| `VISUAL-PLAN.md` | Sample ledger data table, hand-traced buggy vs. fixed query results (row by row), per-beat visual plan table, resolution checklist | none (documentation) |
| `STATUS.md` | `0/12 beats filled` + per-beat status table — mirrors the reference's own tracking format | none (documentation) |
| `ToDo.md` | Outstanding-work tracker (starts as "12 slots need audio + render," updates as we go) | none (documentation) |

## Schema notes (beat_sheet.json / scenes.py — next gate, not this one)

- `metadata` will follow the reference's fuller schema (title, slug, channel/brand fields left
  neutral per the persona decision above, `skill:"cli-explainer"`, `tool:"claude"`,
  `voice_kokoro:"af_heart"`, `register:"Teardown"`, `narrator_identity` override, `source[]`
  pointing at the exact book/chapter/factcheck lines, `aspect:"16:9"`, `resolution:"3840x2160"`,
  `no_paid_services:true`, `gate_p:"PENDING"`).
- Manim beats (B01, B02, B05, B08, B09 — 5 total, matching the reference's exact split) get
  `shot.type:"GRAPHIC"`, `shot.source:"manim"`, `shot.manim:{scene_class, file:"scenes.py"}`.
  Remotion beats (B00, B03, B04, B06, B07, B10, B11 — 7 total) get `shot.type:"GRAPHIC"`,
  `shot.source:"remotion"`, `shot.remotion:{pattern, props{...}}`.
- `scenes.py` classes will be named `B0X_DescriptiveName(Scene)` (e.g. `B02_FilterOrderSplit`,
  `B05_TruncatedBalance`, `B08_CorrectedBalance`) — **not** the trailer's `B01(BeatScene)` shape —
  because this naming *is* what makes `run.sh`'s scene-detection regex actually work for this
  project (confirmed against the reference's own `scenes.py`). This also means I'll write
  `weight="BOLD"` as a **string**, not the bare `BOLD` constant, since Gate A's static-check stub
  doesn't define that name — the reference's own scenes.py does it this way too.

## Environment status (checked, no action needed yet)

- `manim`, `kokoro-onnx`, `mutagen` already installed (carried over from the earlier trailer
  session's global Python env). `cairosvg` still lacks system `libcairo` — not needed by this
  skill (no PNG-still fallback in the cli-explainer path).
- `node`/`npm` present; `runtime/remotion/node_modules/` already installed in this checkout.
  Remotion render needs a headless Chrome at render time — untested here yet, will confirm at the
  render gate.

## Gates (in order)

1. **This plan** (incl. the 4 flagged persona/branding decisions) — you review and mark it passed.
   *(current gate)*
2. **Paperwork set + `beat_sheet.json`** — written together (the paperwork *is* what GATE F/P
   check against the beat sheet); you review narration, the buggy/fixed SQL shown on screen, and
   sign `PEDAGOGY.md`'s `VERDICT: PASS` yourself (P1 — that gate is never mine to sign).
3. **`scenes.py`** — the 3 Manim scene classes (B02, B05, B08); you review before anything renders.
4. **Render gate** — `generate_audio_kokoro.py` (blocked until you've signed `PEDAGOGY.md`) →
   `run.sh` (GATE F paperwork check → GATE A static pre-flight → GATE W WCAG → GATE L beat-mix
   lint → Manim render → GATE B pixel audit → Remotion render for the 7 non-Manim beats → GATE V
   final-frame check → compile review cut, then clean cut). Nothing here happens before you
   approve stages 1–3, in order.
