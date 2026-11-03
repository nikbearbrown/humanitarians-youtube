# BUILD-LOG — claude-plugins-official--claude-liam-example-command

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-plugins-official/youtube/claude-liam-example-command/beat_sheet.json`
(a 7-beat Teardown skill-teardown of the Anthropic `example-command` reference
plugin skill — B00 composer-ask, B01 anatomy, B02 design, B05 teardown,
BVDT verdict, BHTF your-turn, BOUT outro). Picked up mid-build: QUESTION.md,
CARRY-OUT.md, SCRIPT.md, the 17-beat `beat_sheet.json`, all 17 mp3s, all 13
manim GRAPHIC renders, and 3 of 4 REMOTION renders (B00/BCRY/BOUT) already
existed on pickup, with no BUILD-LOG — verified each artifact rather than
trusting it before continuing.

Question, facts, and body argument carried over unchanged from the source:
five frontmatter fields (name, description, argument-hint, allowed-tools,
model); `$ARGUMENTS` as the verbatim injection point; the parse/perform/report
body pattern (described, not carried out, in the reference file); the
`skills/<name>/SKILL.md` vs. legacy `commands/<name>.md` load-path
equivalence. Register re-registered Teardown→Plain per SCRIPT.md's
"Beat-count note (redo)": the source's B01/B02/B05 (three dense 35-65s beats)
were decomposed into 13 one-idea GRAPHIC beats (B01-B13, ≤150 words each);
BVDT's verdict recap was dropped per CARRY-OUT LAW (folded into BCRY); the
source's design-judgment "gaps" list (model-choice guidance, Bash blast
radius, /help description limits) was dropped as Teardown judgment, not
carried into Plain — replaced with WRONG-GUESS/BREAK-IT (B02-B03) and
BOTH-DIRECTIONS (B12-B13) beats framing the same material as newcomer-useful
facts instead of a verdict on the template's design. No source beat was
ai-video-prompt, pantry, or a human-drop slot.

**Completed this invocation:**
- Copied the 13 already-rendered `manim/B*.mp4` GRAPHIC beats into `media/`
  (the render step had finished; the copy into the compile-visible slot had
  not).
- Rendered the one missing REMOTION beat, BHTF (`ClaudeComposerAsk`), via
  `remotion_scenes.py --only BHTF` — foreground; the call exceeded the
  tool's 120s timeout and was moved to background by the harness
  automatically, blocked on via `TaskOutput` before proceeding, per the
  COMPLETION LAW's foreground-render rule.

**B00 TIMING LAW defect caught and fixed, not a QC-sampling trap.** The
picked-up B00 render (`triggerWords: "just work"`, a two-word phrase) never
displayed its correction at all — confirmed by pulling frames at t=8.5,
9.7, 10.2, 10.3, 10.4s of the 10.47s clip, which showed the writer typing
straight through "just work, right?" with no accent/deletion of the intended
phrase, ending mid-typo-correction of an unrelated stray character. Root
cause, found by reading `BrutalistHesitantWriter.tsx`: `triggerWords` is
split only on commas, so a trigger containing an internal space (`"just
work"`) can never equal a single whitespace-split token's core (`"just"` or
`"work"` individually) — the intended correction was mechanically incapable
of firing, regardless of timing. (First attempted fix — retuning
`charMs`/`jitter`/`hesitateWithin`/`hesitateBetween` to speed up the
animation — was the wrong diagnosis: it produced a clean but *uncorrected*
render, proving the trigger match itself was the defect, not the pacing.)
Fixed by rewriting the on-screen text's last line to end on a single-word
trigger the component can actually match: `"...slash command / already
works, right?"` with `triggerWords: "works"` → `replacementWords: "runs a
template"`, settling to "already runs a template, right?" — preserving the
exact wrong-guess semantics from CARRY-OUT.md ("already works" → "runs a
template") more literally than the original broken props did. Re-rendered
B00 only; frame-verified: "works" sits doomed in terracotta at t≈4.8s,
deletion/retype visible through t≈6.5s, and "...already runs a template,
right?" settles legible by t≈8.0s of the 10.4s clip (TIMING LAW's ≥8s floor
met with margin).

Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --review
```

Result: `claude-plugins-official--claude-liam-example-command-slate.mp4`,
17/17 beats filled real (no slate), 184.0s, 3840×2160 (native 4K —
compile.py's 4K LAW).

**Gates:**
- content-check: PASS (17 beats, no violations)
- frame-check: PASS (3840×2160, 17 beats, no violations)
- lane-check: PASS (no lane violations, cut=review)
- GATE T (`type_check.py`): PASS, 0 FAILs
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: video 3840×2160, audio present, duration 183.98s; mp4 mtime
  (Aug 31 01:24:22) newer than beat_sheet.json mtime (Aug 31 01:23:33)
- Gate V (visual): read the full QC contact sheet (all 17 beats) plus
  targeted frame pulls on B00 (t=4.8/6.5/8.0/9.0/10.0/10.3s — hesitation,
  deletion, retype, and settled correction all confirmed legible) — no
  overlap, safe inset held, one terracotta accent per beat, BCRY/BHTF/BOUT
  carry the Humanitarians AI skin correctly.
- Non-blocking WARNING: motion histogram graphic:13/17 (76%) over the
  ~40% pantry-cap heuristic — expected and intentional under hai-simple's
  spine (B00 REMOTION + 13 one-idea GRAPHIC body beats + 3 REMOTION close
  beats is the prescribed shape per SKILL.md, not an imbalance to fix).

Metadata file written: `claude-plugins-official--claude-liam-example-command.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`claude-plugins-official`) matches the map's `"claude-plugins"` prefix,
consistent with every other `claude-plugins-official` sibling. Direct code
link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-08-31 — Phase 4, DELIVERED

Compiled the final (non-`--review`) cut — compile.py's 4K LAW forced the
master from the review cut's 720p to native 2160p automatically:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `claude-plugins-official--claude-liam-example-command.mp4`, 17/17
beats real, 184.0s, 3840×2160, mean_volume -23.9 dB (re-verified). Copied
to `claude-plugins-official--claude-liam-example-command-4k.mp4`.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/claude-plugins-official--claude-liam-example-command/`
(4K master + description) for the Drive sync. Committed to
`claude-bear/claude-plugins-official--claude-liam-example-command/`
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, CARRY-OUT.md,
QUESTION.md, BUILD-LOG.md — no mp3/mp4) as commit `1c76a323`, pushed clean
(no rebase conflicts).

**Status: DELIVERED.**
