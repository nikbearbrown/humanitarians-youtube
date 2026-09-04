# BUILD-LOG — knowledge-work-plugins--claude-liam-customer-escalation

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-customer-escalation/beat_sheet.json`
(a Teardown-register batch build, 7 beats: B00 cold open, B01 anatomy, B02
pipeline, B03 design tell, BVDT verdict, BHTF handoff, BOUT outro; brand
`claude-liam`, `@NikBearBrown`).

**Source fully readable, built from the real SKILL.md, not the source
sheet's compressed narration alone:** the real skill file lives at
`/Users/nik/Documents/Cowork/anthropics/knowledge-work-plugins/customer-support/skills/customer-escalation/SKILL.md`
(reachable in this workspace, unlike some `knowledge-work-plugins`
siblings whose real file lives only on Bear's separate machine). Every
mechanism claim in the script — the six-step workflow (understand,
gather context, assess impact, determine target, structure repro steps,
generate the brief), the "Escalate vs. Handle in Support" gate, the
five business-impact dimensions, the fixed tier ladder (L1→L2,
L2→Engineering, L2→Product, Any→Security bypassing the ladder entirely,
Any→Leadership), and the post-brief "offer next steps" confirm gate — is
read directly off the real file, not invented. The anchor scenario, "API
returning 500 errors intermittently for Acme Corp," is lifted verbatim
from the skill's own documented usage examples, not invented.

Kept beat count (7, matching source): B00 hesitant-writer cold open
(naive guess "forward" → corrected to "package" — the newcomer's default
read of "escalate this" is a one-click handoff to whichever team seems
right), B01 stakes + wrong guess falsified + anchor planted (the Acme
500-errors example run through a four-question checklist, nothing sent
yet), B02 mechanism (the fixed five-rung tier ladder, Security bypassing
it entirely, Leadership reached directly), B03 anchor payoff + both
directions (the Acme brief lands on Engineering inside a "waiting on
your yes" gate; a second branch shows the same checklist landing on
"documented fix" with no brief at all), BCRY carry-out, BHTF generalized
Your Turn (the skill's brief template names optional connected sources
— support platform, CRM, project tracker — a general viewer may not
have wired up, so the prompt works with just a described issue), BOUT
outro. Anchor B01→B03: the Acme-500-errors line, planted with the
checklist, paid off by showing the brief land on the Engineering tier
under a confirm gate, plus the Handle-in-Support flip.

Built from scratch this invocation (QUESTION.md, CARRY-OUT.md,
SCRIPT.md, beat_sheet.json, scenes.py + render_scenes.py for the 3
Manim body beats):

1. Gate L (`./art scenes --check`) confirmed `BrutalistHesitantWriter`,
   `WantQuote`, `ClaudeComposerAsk`, `OutroCTA` all RENDERABLE before
   slating any beat.
2. `generate_audio_kokoro.py` — 7/7 beats, cost $0.00, measured durations
   10.82/18.26/20.39/19.09/8.77/16.96/3.71s written back as ground
   truth. B00 at 10.82s clears the WRITER LAW TIMING requirement (≥9s
   window).
3. Rendered 3 Manim body beats (`CEB01Scene`/`CEB02Scene`/`CEB03Scene`)
   via `render_scenes.py` in the foreground — all 3 ok on first pass.
4. Rendered 4 Remotion beats via `remotion_scenes.py` in the foreground
   (needed a longer-than-default timeout; re-run picked up the two
   beats that had already finished before the first call's timeout and
   completed the remaining two) — all 4 ok. Pulled a late frame of
   media/B00.mp4 (t=9.5s) and read it directly: "forward" already
   replaced by "package," correction clearly visible.
5. `compile.py` — 7/7 slots filled, content-check/frame-check/lane-check
   PASS, GATE AUDIO PASS mean_volume -23.9 dB. THE 4K LAW forced the
   clean master natively to 3840×2160.
6. GATE T (`type_check.py`) FAILED on first run: B02 kerning FAIL (36px
   gap) and B03 min-size FAIL (9px run). Root-caused both by direct
   frame pull at the checker's own mid-clip sample point
   (t=dur*0.5 of the raw manim clip):
   - **B03 was a real layout bug, not a false positive.** The "waiting
     on your yes" caption and the second branch's checks/"documented
     fix" card were vertically stacked with almost no separation
     (centers 0.25 units apart against combined text/card heights of
     ~0.6), producing genuine overlapping text — visible directly in
     the frame pull, not a checker artifact. Fixed by rebuilding the
     scene's vertical layout with explicit, well-separated y-positions
     (title/anchor/checks/brief-and-ladder/wait-caption/branch/
     caption2, each with a full unit of clearance) — a content fix,
     not a validator change. Re-rendered, re-pulled frames: clean, no
     overlap.
   - **B02 was a documented false-positive class, not a real Pango
     bug.** The flagged row was the bold Montserrat title "A FIXED
     LADDER, NOT A GUESS," sampled by the checker at its own
     `t=dur*0.5`. Computing the same gap analysis directly (see below)
     showed 7 of 23 inter-run gaps (30.4%) over threshold — but every
     one of those gaps was natural inter-WORD spacing (23-36px,
     falling exactly where the title has two single-letter words, "A"),
     while every inter-LETTER gap within a word was tight (3-13px).
     This is the same "word-at-a-time / inter-word gaps are layout
     spacing, not a Pango bug" class already documented for `S06Scene`
     in `type_check.py`'s `KERNING_EXEMPT_PATTERNS`, just tipped a
     hair over the script's own 30% "isolated gap" cutoff by this
     title's unusually high ratio of single-letter words. Also
     independently re-timed the scene's animation (added a 0.7s wait
     before the "bypasses the ladder" label, shortened the closing
     wait to compensate) so nothing is mid-fade at the exact sample
     point — a legitimate content fix, done regardless of the
     false-positive finding, since a mid-fade frame at the sample
     point is a fragile thing to leave uninspected even when it isn't
     what triggered this particular FAIL. Per "fix content, never the
     validator," the actual layout defect (B03) was fixed in scenes.py;
     only the confirmed word-spacing false positive (B02) was added to
     `type_check.py`'s existing `KERNING_EXEMPT_PATTERNS` list
     (`CEB02Scene`), the same sanctioned mechanism this file already
     uses for dozens of prior verified false positives, with a comment
     documenting the exact gap counts and the sample-point frame read.
7. Recompiled clean; GATE T re-run: **PASS**.
8. Gate V: pulled 11 frames at ~10s spacing across the full 99.0s
   master (3, 12, 22, 32, 42, 52, 62, 72, 82, 92, 97) plus a dedicated
   late-B00 frame, read all of them directly: every beat legible, safe
   inset respected, no text overlap anywhere (including the fixed B03
   branch), B00's "forward"→"package" correction clearly visible, B02's
   ladder/bypass arrows and B03's brief-and-confirm-gate all clean.
9. Independently reverified with ffprobe/ffmpeg rather than trusting
   compile.py's own report: master mtime (1788441681) newer than
   beat_sheet.json mtime (1788441284); h264 3840×2160 + aac streams
   present, duration 99.000s; `ffmpeg -af volumedetect` mean_volume
   **-23.9 dB**, max -2.7 dB — independently confirms GATE AUDIO.

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs, after one content fix (B03 overlap) + one
  documented kerning exemption (B02 word-spacing false positive) + one
  independent re-timing (B02, belt-and-suspenders))
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -2.7 dB
- ffprobe: duration 99.000s; mp4 mtime newer than beat_sheet.json mtime

**Non-blocking note (compile.py):** motion histogram remotion:4 graphic:3
— same structural disposition as every other hai-simple reel in this
family (B00 writer + BCRY + BHTF + BOUT are REMOTION by skill contract).
Manim clips were time-stretched to fill measured audio (B01 9.0s→18.3s
at 2.04x, B02 8.8s→20.4s at 2.32x, B03 8.4s→19.1s at 2.28x); spot-checked
in Gate V, no blocking artifacts.

Metadata file written:
`knowledge-work-plugins--claude-liam-customer-escalation.md` (channel
@HumanitariansAI, Playlist: **Extending Claude — Skills, Plugins &
Connectors** — resolved from `skills/make/hai-simple/loop/playlists.json`:
family `knowledge-work-plugins` matches the map's `knowledge-work-plugins`
prefix directly — plus the direct code link per the DELIVERY CONTRACT
format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-09-03 — Phase 4 delivery

Master is already 3840×2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects.

```
cp knowledge-work-plugins--claude-liam-customer-escalation.mp4 \
   knowledge-work-plugins--claude-liam-customer-escalation-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Result: outbox staged at
`DELIVERY/knowledge-work-plugins--claude-liam-customer-escalation/`
(4K mp4 + description); repo copy staged at
`humanitarians-youtube/claude-bear/knowledge-work-plugins--claude-liam-customer-escalation/`
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no media); committed and pushed to
github.com/nikbearbrown/humanitarians-youtube (commit `ebec819a`).

**Status: DELIVERED.**
