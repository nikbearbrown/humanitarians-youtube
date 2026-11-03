# BUILD-LOG — knowledge-work-plugins--claude-liam-call-summary

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-call-summary/beat_sheet.json`
— a fully-built Teardown reel (7 beats, `claude-liam` / @NikBearBrown)
examining the Anthropic `call-summary` skill (folder:
`sales/skills/call-summary/`). No SCRIPT.md existed on the source; its
`beats[*].narration_text` served as the locked narration per the redo
contract. Never touched the source reel's folder.

**Facts kept unchanged:** a skill is a folder Claude reads before it acts;
`call-summary`'s whole instruction set lives in one file, SKILL.md, plain
language; its job is to process call notes or a transcript into action
items, a follow-up email, and an internal summary; the pipeline runs five
fixed steps in order (read notes, action items, follow-up email, internal
summary, result) with no branching unless a step says so; because the steps
are fixed, the same notes get the same treatment every run, and a request
outside the file's steps (e.g. booking the follow-up meeting) has no
instruction to follow.

**Beat count kept exactly:** source is 7 beats (B00 composer-ask cold open,
B01 anatomy, B02 pipeline, B03 design-tell, BVDT verdict, BHTF your-turn,
BOUT outro). Redo shape: B00 → `BrutalistHesitantWriter` (hai-simple's
mandatory swap), B01/B02 kept as GRAPHIC beats with facts unchanged, B03's
Teardown "what it gets right / what it bites" judgment rewritten as a plain
behavioral fact (consistency + an unstated case, no ruling on the trade-off),
BVDT → BCRY (carry-out, judgment stripped), BHTF/BOUT kept with the
Humanitarians AI skin. Total: 7 beats — no expansion, matching the source's
already-compact scope (unlike deeper sibling redos that had to compress a
20+ beat source).

**B00 WRITER LAW:** newcomer misconception — that a Claude "skill" for call
notes means Claude can listen to or transcribe the call itself, rather than
process text you already have. Typed text: "Claude hears my calls. / How
does that work?", trigger "hears" → replacement "reads notes from".
**First two render attempts failed the TIMING LAW's own verification step**
(discovered only by pulling late frames and reading them, not by trusting
the "rendered OK" exit code): `lead_silence_s` in this reel's beat_sheet.json
is NOT consumed anywhere in `generate_audio_kokoro.py`, `remotion_scenes.py`,
or `compile.py` (grepped all three; only `repair_b00_audio.py`, a different
Seedance-audio-baking fix, reads it) — so it adds no actual render time, and
the SKILL.md's "≥9s window via narration + lead_silence_s" promise does not
hold in this toolkit version as written. With the original 3-line/21-char-
replacement text, the typing needed ~9.3–9.6s but the beat's real (audio-
driven) duration was only 8.79s, so the final line never appeared in either
of the first two renders. **Fixed by shortening the on-screen text** (3
lines → 2, replacement "reads the notes from" → "reads notes from") rather
than relying on lead_silence: final render's correction resolves by t≈4s
and the full corrected question completes by t≈6s of 8.8s, leaving ~2.8s to
hold on the finished text — reverified against 3 explicit frame pulls
(t=3, t=6, t=8.5). Logging this as a toolkit gap, not just a per-reel fix:
any future hai-simple B00 that leans on `lead_silence_s` alone for its ≥9s
window will hit the same failure until the render scripts actually consume
that field.

**Body beats:** B01–B03 built as Manim GRAPHIC scenes via one shared generic
"chip row" renderer in `scenes.py` (title + up to 5 labeled chips, optional
arrows, optional terracotta accent or dimmed/struck chip, caption) — the
same reusable pattern as the `books--claude-liam-building-plugins` sibling,
scaled down to 3 beats since the source itself was compact. No anchor pair
was needed at this scale (one file, SKILL.md, carries the through-line named
in B01, traced in B02, edged in B03). Close: BCRY `WantQuote` (carry-out),
BHTF `ClaudeComposerAsk` (source's Your-Turn prompt re-registered to Plain,
explicit `folderLabel: "@HumanitariansAI"` per the known
ClaudeComposerAsk-defaults-to-@NikBearBrown behavior), BOUT `OutroCTA`
(@HumanitariansAI).

Built end to end this invocation: QUESTION.md, CARRY-OUT.md, SCRIPT.md,
beat_sheet.json (7 beats), `scenes.py` (generic chip-row Manim generator +
3-beat content table), `render_scenes.py`. Ran `generate_audio_kokoro.py`
(7/7 beats, am_onyx, $0.00) — measured durations became the clock. Rendered
3 Manim beats and 4 Remotion beats via `remotion_scenes.py` (foreground,
waited on exit code every time — no orphaned background renders); B00 was
re-rendered twice in the foreground (`--only B00 --force`) to fix the
typing-completion defect above, each time waited on exit code before
pulling verification frames.

**GATE T (type_check.py): PASS**, 0 FAILs on first pass (all §8.10 checks
SKIPPED per the checker's own report — no pixel-level defects flagged).

Compiled with `compile.py .`: 7/7 beats real (no slate), master born
natively 4K (3840×2160, compile.py's 4K LAW), 86.1s. `content-check`/
`frame-check`/`lane-check` all PASS. Motion histogram `remotion:4 graphic:3`
— fixed by hai-simple's mandated shape (B00/BCRY/BHTF/BOUT REMOTION,
B01–B03 GRAPHIC) at this beat count, same disposition as sibling redos.

**Gate V:** pulled 14 frames at 6s spacing across the full 86.1s runtime
(private `/tmp/gv_cs/` dir, isolated from other concurrent sessions' shared
`/tmp/gatev/` clutter discovered mid-review) plus a dedicated late-runtime
pull for BOUT; read every one directly. B00's correction and full question
both land with margin (see WRITER LAW note above). B01/B02/B03 chip
diagrams are legible, correctly labeled, safe-inset, matching narration.
BCRY carries the carry-out sentence alone, serif, large. BHTF shows the
correct `@HumanitariansAI` folder label (not the ClaudeComposerAsk Root.tsx
default `@NikBearBrown`) and the verbatim Your-Turn prompt. BOUT restates
the title with the Humanitarians AI skin (title + SUBSCRIBE + handle). No
remaining blockers.

**Audio:** independently verified (not just trusting compile.py's own GATE
AUDIO line) via `ffprobe`: AAC stream present, master mtime (1788392451)
newer than beat_sheet.json mtime (1788392341); `ffmpeg -af volumedetect`:
mean_volume **-24.0 dB**, max -2.9 dB — comfortably above the -40 dB floor.
Resolution confirmed 3840×2160.

Metadata file written: `knowledge-work-plugins--claude-liam-call-summary.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors** — direct map hit on SUBJECT.json's `family:
"knowledge-work-plugins"` key in playlists.json, no fallback needed). Per
the DELIVERY CONTRACT format, the description also carries the direct code
link.

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
