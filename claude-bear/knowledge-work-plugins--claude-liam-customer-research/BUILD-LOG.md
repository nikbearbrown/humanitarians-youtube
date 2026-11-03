# BUILD-LOG — knowledge-work-plugins--claude-liam-customer-research

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-customer-research/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `customer-research`
skill: multi-source research on a customer question or topic with source
attribution — triggered when a customer asks something you need to look
up, checking whether a bug's been reported before, checking what an
account was previously told, or gathering background before drafting a
response; 7 beats, already fully built as REMOTION). Picked up mid-build:
QUESTION.md, CARRY-OUT.md, SCRIPT.md, beat_sheet.json, all 7 mp3s +
timings.json, manim/B01-B03.mp4, and media/B00.mp4 already existed from a
prior invocation; only the three remaining Remotion beats (BCRY, BHTF,
BOUT) and the compile/gate/deliver phases were outstanding. Verified the
existing artifacts rather than rebuilding: audio durations in
mp3/timings.json matched beat_sheet.json's `actual_duration_s`, and
manim/B0{1,2,3}.mp4 durations were within compile.py's per-beat conform
tolerance.

Question, facts, and beat count kept from the source: a skill is a folder
Claude reads before acting; `customer-research`'s SKILL.md is one file
written in plain language; Claude reads it, executes its steps in order
(no branching unless a step says so), and returns the output; because the
steps are fixed, the same customer question gets the same treatment every
run (sources pulled, attributed, findings returned), and a request outside
the steps (e.g., skip sourcing and guess) has no instruction backing it.
Register re-registered Teardown -> Plain: the source's BVDT verdict
("what it gets right... what it bites") was folded into BCRY as a
behavioral fact (consistent output; an unstated case) with the design
judgment stripped, per the redo contract. B00 replaced the source's
`ClaudeComposerAsk` cold open with `BrutalistHesitantWriter` per WRITER
LAW: "knows" -> "checks sources for" (the newcomer's wrong guess that
Claude already knows/remembers things about a customer, corrected to it
looking up and attributing sources it's given). B00 audio measured 9.11s
(narration + `lead_silence_s: 0.8`), clearing the >=9s TIMING LAW floor;
frame-verified at t=2s (mid-typing, pre-correction: "Claude checks sources
for my customer." already settled, second line "How does that work?" not
yet started) and t=8.5s (both lines settled and legible, cursor active) —
the correction lands well inside the beat's window.

No source beat was ai-video-prompt, pantry, or a human-drop slot; NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's mandated cold-open
swap. B01-B03 use the shared generic "chip row" Manim template
(`scenes.py`/`render_scenes.py`, `CRB01Scene`/`CRB02Scene`/`CRB03Scene`)
with customer-research-specific labels.

This invocation rendered the three outstanding Remotion beats:

```
python3 runtime/scripts/remotion_scenes.py <REEL_DIR>
```

(exceeded the tool's 120s default timeout and was moved to background by
the harness automatically; blocked on it via `TaskOutput` before
proceeding, per the COMPLETION LAW foreground-render rule — never treated
the backgrounded run as handled without waiting on its exit code.) Result:
`BCRY: WantQuote -> media/BCRY.mp4 (10.2s)`, `BHTF: ClaudeComposerAsk ->
media/BHTF.mp4 (18.8s)`; B00/BOUT were already filled from the prior
invocation and skipped.

Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR>
```

Result: `knowledge-work-plugins--claude-liam-customer-research.mp4`, 7/7
beats filled real (no slate: B00/BCRY/BHTF/BOUT VIDEO, B01/B02/B03 MANIM),
82.6s, 3840x2160 native (compile.py's 4K LAW forced 720p source components
to a 2160p clean master — no separate upscale needed for delivery).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE AUDIO (compile.py): PASS, mean_volume -24.0 dB
- ffprobe re-verification: video 3840x2160 h264, audio aac present,
  duration 82.6s; mp4 mtime (1788445643) newer than beat_sheet.json mtime
  (1788445564)
- Audio presence (ffmpeg volumedetect, independent of compile.py's gate):
  mean_volume -24.0 dB, max_volume -2.7 dB — well above the -40 dB floor
- Gate V (visual): 7-frame sweep across the full runtime (B00 typing
  mid-correction, B01 "A SKILL IS A FOLDER", B02 "READ, EXECUTE, RETURN",
  B03 "SAME EVERY RUN, NOT EVERYTHING" with "GUESS THE ANSWER" dimmed/
  struck, BCRY carry-out quote card, BHTF "Your turn." composer-ask with
  paste-ready prompt, BOUT outro "Claude, Customer Research. Liam, in for
  Bear." + Subscribe/@HumanitariansAI) — all legible, safe inset clean, no
  text overlap, no blockers.

Metadata file written: `knowledge-work-plugins--claude-liam-customer-research.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) matches the map's `"knowledge-work-plugins"`
key directly (exact match, not a prefix fallback) -> "Extending Claude —
Skills, Plugins & Connectors". Direct code link per DELIVERY CONTRACT
format included.

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-09-03 — Phase 4, DELIVERED

Master was already born native 3840x2160 (compile.py's 4K LAW), so copied
directly to `knowledge-work-plugins--claude-liam-customer-research-4k.mp4`
rather than re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/knowledge-work-plugins--claude-liam-customer-research/`
(4K master + description) for the Drive sync. Committed text artifacts
(README.md = description, beat_sheet.json, SCRIPT.md, SUBJECT.json,
CARRY-OUT.md, QUESTION.md, BUILD-LOG.md — no mp3/mp4) to
`claude-bear/knowledge-work-plugins--claude-liam-customer-research/` in
the humanitarians-youtube clone, pushed clean.

**Status: DELIVERED.**
