# BUILD-LOG — financial-services--claude-liam-fixed-income-portfolio

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-fixed-income-portfolio/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `fixed-income-portfolio`
partner skill — reviews fixed income portfolios by pricing multiple bonds,
retrieving reference data, analyzing cashflows, and running scenario
analysis; triggered when computing portfolio duration and DV01, analyzing
cashflow waterfalls, stress testing rate scenarios, or assessing portfolio
composition — already fully built, no SCRIPT.md; source `beats[*].narration_text`
served as the locked script per REDO-CONTRACT). The `source_skill` path the
source metadata names does not exist on this machine (a different machine's
home directory), but the source beat_sheet.json's own narration already
stated the skill's function in enough detail to redo faithfully — no
reconstruction needed (see QUESTION.md). Built entirely fresh this
invocation — only SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: the skill
reads a written SKILL.md and executes a fixed procedure — price each bond
from reference data (coupon, maturity, current price), compute duration and
DV01 (the dollar change in a bond's price for a one basis point move in
rates), sum DV01 across the portfolio, and run whatever rate-shock scenario
it's told to. Register re-registered Teardown → Plain: the source's B03/BVDT
"what it gets right / what it bites" design-tell verdict was dropped;
Plain's structure instead required a new WRONG-GUESS beat (a newcomer
assumes Claude decides how risky the portfolio is, the way an analyst who
has studied it forms an opinion — falsified by "feed it a different price
and the numbers move without protest, it never argues that your bond is too
risky"), a new ANCHOR (DV01 summed across the portfolio, a rate shock in
basis points driving one portfolio P&L readout, planted at B02, paid off at
B03 via the scenario/sensitivity analysis), and a new BOTH-DIRECTIONS split
at B03 ("a portfolio that swings hard under one rate scenario isn't
necessarily poorly built — a large DV01 can be an intentional, hedged
position" / "a portfolio that holds steady under that one scenario doesn't
mean it's safe from rate risk generally — a bigger move, or a curve twist,
can still hurt it"). B00 replaced the source's `ClaudeComposerAsk` cold open
with `BrutalistHesitantWriter` per WRITER LAW ("judgment" → "the numbers").
Close re-skinned to `OutroCTA` / @HumanitariansAI with Liam's sign-off.

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01 anatomy
+ B02 pipeline + B03 design-tell + BVDT verdict + BHTF your-turn + BOUT
outro). This redo kept the same 7-beat shape: B00 carries the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat; B01 became the
wrong-guess/falsification beat (replacing "anatomy"); B02 became the
mechanism/anchor-planted beat (replacing "pipeline"); B03 became the
anchor-payoff/both-directions beat (replacing "design tell"); BVDT's verdict
facts were folded into BCRY per CARRY-OUT LAW; BHTF and BOUT kept. No source
beat was ai-video-prompt, pantry, or a human-drop slot — the source's final
build was already entirely REMOTION (`ClaudeComposerAsk` / `SkillTeardownAnatomy`
/ `SkillTeardownPipeline` / `SkillTeardownMechanism` / `ClaudeVerdictArtifact`),
so NO-GENAI/NO-PANTRY LAW required no substitution beyond B00's mandated
cold-open swap.

Built following the exact convention already established across the many
sibling `financial-services--claude-liam-*` hai-simple redos in this same
batch (e.g. `dcf-model`, `accrual-schedule`, `bond-relative-value`), all
sharing this identical source-template shape (anatomy/pipeline/design-tell/
verdict): a domain-appropriate wrong-guess ("Claude judges the risk, like an
analyst" — falsified by feeding it a different input and watching the
number move without protest) and a domain-appropriate anchor (here: DV01
summed across bonds, a basis-point shock driving one P&L readout, then
resized in a three-scenario grid). B00's Remotion settings (charMs 55,
mistakeRate 6, hesitateWithin 3, hesitateBetween 22, fontSize 64) copied
directly from the `dcf-model` sibling's proven-safe values rather than
guessed fresh (an earlier `claude-plugins-official--claude-liam-agent-development`
build in the same series hit exactly this failure mode with faster/looser
settings — writer never finished its correction before the clip ended — so
this build started from the value that avoided it).

All 3 GRAPHIC beats (B01–B03) built as bespoke Manim scenes (`scenes.py`,
classes `FIPB01Scene`/`FIPB02Scene`/`FIPB03Scene`), structurally copied
(card/dial/readout/grid mechanism, colors, GATE T exemption notes — no
Line() text-strikes, TERRA reserved for accents/borders, single scale-to-fit,
faint-fill cards instead of stroked borders) from the `dcf-model` sibling's
`scenes.py`, with fixed-income-portfolio-specific content: B01 = "analyst
judgment" (struck) vs. "the numbers" (coupon/maturity/current price →
DV01), one input changed, output moves without protest; B02 = THE ANCHOR —
five bond bars summing to one portfolio DV01 bar, a "RATE SHOCK (BPS)" dial
wired to a "PORTFOLIO P&L" readout, turned to +100bp → -$420K; B03 = THE
ANCHOR RETURNS — a three-scenario grid (-100bp/+100bp/+200bp), then splits
into "swinging is not broken" (large DV01, still hedged elsewhere) and
"steady is not safe" (100bp shock vs. curve-twist bars).

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`; B00 11.78s — well past the ≥9s WRITER LAW floor with
`lead_silence_s` 0.8). Frame-pulled B00 at t≈2s (typing "a portfolio'"),
t≈4s ("ju" of "judgment" doomed in terracotta), and the final frame
(settled: "What decides / a portfolio's risk — / the numbers?", fully
corrected and held) — correction confirmed on screen well inside the
11.8s clip.

B01–B03 rendered via `render_scenes.py` (Manim, foreground, all 3 succeeded
first attempt); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py`
(exceeded the tool's 120s timeout and was moved to background by the
harness automatically — blocked on it via `TaskOutput` before proceeding,
per the COMPLETION LAW's foreground-render rule, never treating a
backgrounded render as "handled" without waiting on its exit code). All 4
Remotion beats: exit 0, all `ok`.

`type_check.py` → **PASS, 0 FAILs, first attempt** (no GATE T defects to
fix — unlike several siblings in this batch that needed a border-color or
label-shortening fix).

Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR>
```

Result: `financial-services--claude-liam-fixed-income-portfolio.mp4`, 7/7
beats filled real (no slate), 110.2s, 3840×2160 (native 4K — compile.py's
4K LAW). B01–B03's Manim clips were time-stretched (setpts) 1.68x/2.47x/2.46x
to fill their audio-clocked beat durations — all under compile.py's own 3.0x
"extreme slow-mo" WARNING threshold, so accepted as normal audio-is-the-clock
behavior rather than a defect requiring re-timed `wait()` calls in scenes.py.

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs, first pass
- Gate V (visual): pulled 14 frames every ~8s across the full 110.2s
  runtime plus targeted checks of B00 (t≈2s, t≈4s "ju" doomed in
  terracotta, final frame fully corrected and held) — read every frame
  directly. B01's struck analyst-judgment card and lit "THE NUMBERS" card
  (coupon/maturity/current price → DV01) read cleanly, including the
  price-change/DV01-update transform. B02's five-bond-bar sum, rate-shock
  dial, and portfolio P&L readout (turned to -$420K) are legible at every
  step. B03's three-scenario grid and both-directions split ("swinging is
  not broken" / "steady is not safe") read cleanly with no label collision
  (the 100bp-shock/curve-twist bar labels stayed clear of each other per
  the wide-buff fix pattern copied from the dcf-model sibling). BCRY's
  carry-out quote and sparkline, BHTF's Your Turn composer card (correct
  topic/title/@HumanitariansAI handle, paste-ready prompt legible), and
  BOUT's title restate + subscribe CTA all render legibly with no overlap
  or clipping. No defects found.
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max
  -2.8 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 110.2s; mp4
  mtime (1788301007) newer than beat_sheet.json mtime (1788300846)

**Noted, not a defect introduced here:** `OutroCTA` renders on flat white
rather than the humanitarians cream ground — same shared-component
behavior already logged unremarked in sibling reels in this family (e.g.
`financial-services--claude-liam-accrual-schedule`,
`financial-services--claude-liam-dcf-model`).

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a defect:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) +
BOUT (outro) all REMOTION by skill contract, against 3 GRAPHIC body beats
for this 7-beat reel — same disposition as every other short hai-simple
reel in this family.

**Playlist resolution:** family `financial-services` does not match any
prefix key in `skills/make/hai-simple/loop/playlists.json`. Per the map's
documented fallback ("match SUBJECT.json's family, or the hai-simple
prefix"), fell through to matching the skill name itself: `hai-simple` is
a literal key in the map, resolving to **Claude Basics** — same resolution
as every other sibling in this family (`dcf-model`, `accrual-schedule`,
`bond-relative-value`, etc.).

Metadata file written:
`financial-services--claude-liam-fixed-income-portfolio.md` (channel
@HumanitariansAI, Playlist: **Claude Basics**, plus the direct code link
per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-09-01 — Phase 4, DELIVERED

Master is already native 3840×2160 (compile.py's 4K LAW forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects:

```
cp financial-services--claude-liam-fixed-income-portfolio.mp4 \
   financial-services--claude-liam-fixed-income-portfolio-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Outbox staged: `DELIVERY/financial-services--claude-liam-fixed-income-portfolio/`
(4K mp4 + description.md). Repo: committed + pushed to
`humanitarians-youtube/claude-bear/financial-services--claude-liam-fixed-income-portfolio/`
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no mp3/mp4).

**Status: DELIVERED.**
