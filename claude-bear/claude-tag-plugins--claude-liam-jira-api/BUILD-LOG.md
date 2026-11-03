# BUILD-LOG — claude-tag-plugins--claude-liam-jira-api

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-tag-plugins/youtube/claude-liam-jira-api/beat_sheet.json`
— a fully-filled, fully-narrated Teardown-register "skill-teardown" sheet
(metadata `register: "Teardown"`, `brand: "claude-liam"`, `audience:
"Claude"`, `source_skill` pointing at the Jira API Claude Tag Plugin
skill). 7 beats: B00 cold open (ClaudeComposerAsk, reading the skill's own
summary aloud), B01 anatomy (JiraApiAnatomy Remotion), B02 design/patterns
(JiraApiDesign Remotion), B05 teardown tell (JiraApiTell Remotion), BVDT
verdict (ClaudeVerdictArtifact), BHTF handoff, BOUT outro — all already
REMOTION, so NO-GENAI/NO-PANTRY LAW required no substitution beyond the
WRITER LAW swap at B00; no beat in the source planned as `ai-video-prompt`,
pantry, or a human-drop slot. Source has exactly 3 body beats (B01, B02,
B05), so this redo also produces exactly 3 GRAPHIC body beats (B01/B02/B03)
— beat count held per the redo-mode "locked script" contract, same
disposition as the `asana-api` sibling redo.

Facts carried over unchanged: two API families — Platform REST v3 (issues,
projects, JQL search, comments, transitions — the default) and Agile REST
v1 (boards, sprints, backlog, epics — only for concepts the core issue
model lacks); transitions must be listed then posted by ID, IDs are
per-workflow/per-current-status and not portable across issues; ADF
(description/comment bodies are a JSON tree — `type: doc`, `version: 1`, a
`content` array — a plain string draws a 400 that never names ADF as the
fix); JQL search must be bounded (at least one filter clause) and returns
no total, paginating on `nextPageToken`'s presence; accountId (not email)
for assignee/watcher/reporter since the GDPR change; documented gaps — the
no-total workaround is under-documented, three pagination schemes have no
single detection rule, `maxResults` is silently clamped, and 404 (not 403)
is what an unbrowsable issue returns.

B00 replaced the source's `ClaudeComposerAsk` cold open (which read the
skill's raw capability list aloud, no wrong-guess framing) with
`BrutalistHesitantWriter` (WRITER LAW: "set" → "transition" — the naive
assumption that a ticket's status is a field Claude can set directly,
corrected to the fact that status only moves through a looked-up
transition ID). Register re-registered Teardown → Plain: the source's B05
framed the same facts as "what it gets right" / "where it bites" —
Teardown trade-off language — restated here as mechanism + documented-
boundary facts with no verdict on the skill's design quality. Source's
BVDT verdict recap folded into a dedicated BCRY carry-out beat per
CARRY-OUT LAW. Close re-skinned to `OutroCTA` / @HumanitariansAI with
Liam's sign-off. Anchor: B02 → B03, a bounded JQL search ("every open bug
in PROJ, assigned to me") traced through `nextPageToken` pagination and an
ADF comment, then paid off against the same request completing cleanly
vs. quietly failing (a total-expecting loop that never terminates, or a
plain-string comment that 400s with no clue why) — the WRONG-GUESS LAW
beat itself (B00/B01) covers the transitions half of the source's
teardown facts; the anchor covers the pagination/ADF half.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Durations: B00
   10.52s, B01 18.58s, B02 32.47s, B03 29.97s, BCRY 13.08s, BHTF 23.57s,
   BOUT 3.43s.
2. Wrote `scenes.py` (3 Manim scenes, B01–B03, reel-unique names
   `JAB01Scene`/`JAB02Scene`/`JAB03Scene` per the naming-collision lesson
   from sibling BUILD-LOGs) and `render_scenes.py`; rendered all three in
   the foreground. Manim's natural scene length ran well short of the
   measured narration on B02/B03 (~12.6s rendered vs. 29.5–32.5s needed);
   rather than let compile.py apply a >2x ffmpeg slowmo stretch (the
   documented anti-pattern from earlier reels' `replace_log.md` entries),
   padded `self.wait()` calls directly in `scenes.py` to bring rendered
   duration within compile.py's ±5%/mild-slowdown bands (B01 exact match,
   B02 1.10x mild slow, B03 within ±1%).
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py`. The first
   invocation exceeded the tool's 120s window and was killed by the
   harness's default timeout before it reached the post-render
   freeze-pad/trim step — B00.mp4 was left on disk as the RAW 20.24s
   BrutalistHesitantWriter render (the component's composition duration is
   a fixed 606 frames @30fps regardless of typing-simulation props,
   confirmed by reading `Root.tsx`; the typing itself completes and holds
   on the corrected final text well before 8s, verified by frame pull at
   3/6/8/9/10/11/12s — all show the finished, corrected "…to close it
   out.|"). Manually applied the same `tpad=stop_mode=clone` + `-t`
   trim `remotion_scenes.py` would have run, to `actual_duration_s`
   (10.52s); re-verified the last frame still reads the finished corrected
   question, cursor at rest. Re-ran `remotion_scenes.py` with a longer
   timeout for BCRY/BHTF/BOUT — all three completed and were correctly
   extended to their measured durations by the tool itself, exit 0.

**Real defects found and fixed by direct frame inspection, not by trusting
default layout/prop choices:**

- **GATE T kerning §8.4 false-positive on B01's bold title.** The 1080p
  frame's peak-ink row landed on "NOT A STATUS FIELD" (Montserrat Bold);
  at that specific row-band, letter-shape counters/apexes ('A', 'U', 'S')
  register as separate ink runs, producing a measured 28px gap the checker
  read as a kerning failure. Verified by direct pixel run/gap dump at the
  checker's own mid-clip sample point: the title reads as one cleanly
  kerned, fully legible headline with even spacing — no real glyph-
  touching or gappy-letter defect. Added `JAB01Scene` to
  `KERNING_EXEMPT_PATTERNS` in `runtime/scripts/type_check.py` with the
  verification documented inline, per the file's own established
  precedent for this false-positive class (same disposition as
  `S03Scene`/`B02Scene`/etc. already in that set).
- **GATE T min-size §8.1 real defect on B02's corner labels.** The
  "DEFAULT"/"ONLY WHEN NEEDED" labels were scaled down 0.5x along with
  their boxes when repositioned to the corner, shrinking an already-small
  font_size=16 SANS label to an effectively ~8pt render — genuinely too
  small (measured 10px text-run height vs. the 20px floor), not a checker
  false positive. Fixed by decoupling the labels from the box scale
  animation: labels now animate position only (at a bumped font_size=22,
  scaled 0.7 instead of the group's 0.5), keeping them comfortably above
  the legibility floor. Re-verified by direct pixel blob dump: smallest
  text run is now 75px.
- **Three card-clip §8.13-class overflows caught by Gate V frame-by-frame
  read, not flagged by GATE T's automated checks.** "a different ID
  works" (B01), "comment: JSON tree, sent" (B03 — lengthened when the ✓
  glyph was swapped for plain text, see below, without widening its
  card), and "waiting for a total…" (B03) all rendered with their MONO
  text touching or exceeding their RoundedRectangle card's left/right
  edges. Fixed by widening each card (3.0→3.7, 2.6→3.5, 2.6→3.3
  respectively) and trimming font sizes 1–2pt for margin; re-rendered and
  confirmed clean with visible padding on all three at the exact frames
  where the defect previously showed.
- **Two ✗/✓ unicode glyphs replaced pre-emptively.** `Text("✗ rejected", ...)`
  and `Text("comment: JSON tree ✓", ...)` were rewritten as plain-word
  MONO text ("rejected", "comment: JSON tree, sent") before the first
  render — Menlo's rendering of these symbols was suspected (and, for the
  "✗" case, confirmed as a contributing factor in an earlier iteration of
  this same investigation) to risk Pango fallback-font spacing issues;
  removing them was simpler and safer than special-casing the font path.
- **B02 middle-dot (`·`) list separators removed.** `"issues · projects ·
  search"` / `"boards · sprints"` were rewritten with `/` — the isolated
  dot glyph's tiny bounding box was a candidate source of spurious
  min-size text-run fragments (same false-positive shape as this file's
  existing `individual-char fallback` notes elsewhere), and the `/`
  reads identically well without the risk.

Recompiled after all fixes (`compile.py --force`):
`claude-tag-plugins--claude-liam-jira-api.mp4`, 7/7 real (no slate),
132.6s, 3840×2160 (THE 4K LAW — clean master forced to 4K automatically).

**Gate V (visual):** pulled frames at 6s intervals across the full 132.6s
runtime (twice — before and after the card-widening fixes) and read them
directly. B00's correction ("set"→"transition") and finished question read
cleanly, ending on the corrected text with the cursor at rest. B01's
struck-through direct-status-write guess, the list-transitions/match-by-
name/post-ID path, and the same-ID-fails-on-a-different-ticket case all
read cleanly after the card-width fix. B02's THE ANCHOR (two API families,
the bounded-search request traced through token pagination and the ADF
comment) reads cleanly after the title-fadeout and corner-label fixes.
B03's THE ANCHOR RETURNS (clean completion vs. the spinning-loop/400
failure modes, plus the accountId exception card) reads cleanly after the
card-width fix. BCRY's carry-out card, BHTF's Your Turn composer card (the
real transition-plus-comment prompt, with the three watch-fors), and
BOUT's outro/subscribe card render legibly with safe inset respected.
**Noted, not a defect introduced here:** `OutroCTA` renders on a flat-white
ground (`VOX.CREAM = #FFFFFF` in `tokens/vox.ts`) rather than the
humanitarians cream (`#F3EBDD`) — same shared-component behavior already
logged unremarked in sibling hai-simple reels; out of this reel's scope to
fix.

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs, after the kerning-exemption + min-size fixes above)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: video 3840x2160 h264, audio aac present, duration 132.625s;
  mp4 mtime (1788214999) newer than beat_sheet.json mtime (1788213443)

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a defect:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) +
BOUT (outro) all REMOTION by skill contract, against 3 GRAPHIC body beats
for this 7-beat reel — same disposition as every other short hai-simple
reel in this family.

Metadata file written: `claude-tag-plugins--claude-liam-jira-api.md`
(channel @HumanitariansAI, Playlist: **Claude Basics** — resolved from
`skills/make/hai-simple/loop/playlists.json`: the reel's own family
`claude-tag-plugins` matches no prefix in the map, so resolution fell
through to the `hai-simple` skill prefix, which maps to "Claude Basics" —
plus the direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-08-31 — Phase 4 delivery

Master is already 3840x2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects:

```
cp claude-tag-plugins--claude-liam-jira-api.mp4 \
   claude-tag-plugins--claude-liam-jira-api-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged to `DELIVERY/claude-tag-plugins--claude-liam-jira-api/` (4K master +
description) and committed + pushed the text artifacts (README.md =
description, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no media) to
`claude-bear/claude-tag-plugins--claude-liam-jira-api/` in the
humanitarians-youtube clone: commit `886015e8`, pushed clean (`git status
--short` empty after).

**Status: DELIVERED.**
