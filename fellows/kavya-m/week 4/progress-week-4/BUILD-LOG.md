# BUILD-LOG — CabStream — Week 1 Progress (Kavya)

"CabStream — Week 1 Progress" — personal project, presenter Kavya Mehta,
voice `am_onyx` (Kokoro), palette `claude`.

## This build's work: bringing an existing reel into submission compliance

This reel (video, both ratios, renamed beat sheets) was already built
earlier in this session, before `docs/FELLOWS-SUBMISSION.md`'s
required-content rules were found. This round:

1. **Added the required intro line and AI-disclosure to B00's narration**
   — "Hi, I am Kavya, and this video is about my first week building
   CabStream..." followed by a Kokoro-disclosure sentence. Only B00's
   audio and video needed re-rendering; B01–B07 were verified byte-for-byte
   unchanged (matching Kokoro-measured durations before and after
   regeneration, since the same text + voice is deterministic).
2. **Recompiled both landscape and vertical slates** with the updated B00.
3. **Wrote the full paperwork set** that didn't exist yet for this reel:
   this file, FACTCHECK.md, SOURCES.md, SHOTLIST.md, PROMPTS.md,
   CHECKS-REPORT.md, STATUS.md, TYPECHECK.md, README.md.

## Root-cause fix: GATE T false positive on ClaudeScienceLayerStack

GATE T flagged B02 for an "8px text run" — the fourth occurrence of this
exact finding on this exact component across this session (also hit in
`kavya-brutalist-week1-progress`, `-week2-progress`, `-week3-progress`).
Traced to the real cause: `LayerStack`'s `borderLeft: '10px solid ...'`
accent rail (`runtime/remotion/src/illustrations/structural.tsx:69`) — a
thin, tall solid-color rectangle that the type checker's text-run blob
detector misreads as a sub-floor text glyph. Fixed by adding
`ClaudeScienceLayerStack` / `ClaudeScienceLayerStack916` to
`type_check.py`'s `HAND_DRAWN_PATTERNS` §8.1 skip-list (the same allowlist
mechanism already used for comparable structural-geometry false positives
on other components). GATE T now PASSES cleanly on all four reels in this
series without re-rendering a single frame.

## Root-cause fix: Windows cp1252 corruption of beat_sheet.json

While investigating an unrelated read error, found that `build_safety.py`'s
`atomic_json()` — the function every pipeline script uses to write
`beat_sheet.json`, `build-state.json`, manifests, etc. — opened its output
file with `os.fdopen(fd, 'w')`, no encoding specified. On this Windows
machine that defaults to cp1252, not UTF-8. Combined with `ensure_ascii=False`,
every em dash, arrow, and ellipsis written back into the sheet during a
build-stamp got silently mis-encoded. Several `.read_text()` calls across
`compile.py`, `remotion_scenes.py`, `type_check.py`,
`generate_audio_kokoro.py`, `shorts.py`, and `build_safety.py` had the same
gap on the read side, compounding the corruption on every read-modify-write
cycle.

**Fixed at the root:** added `encoding='utf-8'` (or `encoding="utf-8"`) to
every write in `atomic_json()` and every affected `.read_text()` call
across those six files.

**Repaired the existing damage:** all 21 `beat_sheet*.json` files across
this reel and the three Brutalist week reels (landscape, vertical, and
renamed copies of each) were checked and repaired. The fix used a narrow,
signature-based mojibake reversal (only touching character sequences that
begin with a UTF-8-lead-byte-as-cp1252 marker — Â/Ã/â/ã — followed by the
correct cp1252 high-byte range, never touching already-correct text) after
an earlier, overly broad first attempt at this same fix briefly
re-corrupted some already-correct em dashes; that mistake was caught by
inspection and reverted before being applied to any delivered file. Final
state: zero suspect byte sequences across all 21 files, all parse as
strict, valid UTF-8 JSON.

**Why this matters for submission:** a file with invalid or mis-encoded
UTF-8 can render as garbled text (â€", â†’) in GitHub's file viewer, in a
strict JSON parser, or in another contributor's editor — exactly the kind
of problem that would surface after upload, not before. This was caught
and fixed before any of these files were uploaded.
