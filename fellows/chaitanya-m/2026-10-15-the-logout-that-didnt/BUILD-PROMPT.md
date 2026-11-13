# BUILD-PROMPT — The Logout That Didn't

Paste-ready prompt that rebuilds this reel end to end. Run from `~/dev/`.
Free, local, no keys. **Never publishes.**

---

Rebuild the reel at `research/youtube/claude-hai-the-logout-that-didnt/`. It is an
**ai-explainer** in war-story form on the default fidelity brand, **claude-hai**
channel, **@HumanitariansAI**, narrated by **Bella** (`af_bella`). Read
`brutalist/skills/make/ai-explainer/SKILL.md` in full first.

Environment: Remotion needs Node ≥ 20 — `export
PATH="$HOME/.nvm/versions/node/v20.20.2/bin:$PATH"`. Python deps live in
`brutalist/.venv`; call `brutalist/.venv/bin/python`, not system `python3`.

```bash
cd ~/dev
export PATH="$HOME/.nvm/versions/node/v20.20.2/bin:$PATH"
B=brutalist; R=research/youtube/claude-hai-the-logout-that-didnt

# 0. RE-CHECK THE OPEN ITEM FIRST. This reel asserts a branch's state on
#    screen, so the claim has a shelf life. Do this BEFORE anything else.
gh pr view 13 --repo Medhavy/medhavi-hub --json state,mergedAt,mergeStateStatus
gh api "repos/Medhavy/medhavi-hub/contents/components/LogoutButton.tsx?ref=development" \
  --jq '.content' | base64 -d | grep -c 'signOut('      # 0 ⇒ still unfixed
#    If #13 has MERGED, the caveat in B09 and B11 is now FALSE: re-record those
#    two beats and re-render them. Nothing else in the reel depends on #13.

# 1. GATE P
grep -q "VERDICT: PASS" $R/PEDAGOGY.md || { echo "GATE P unsigned"; exit 1; }

# 2. AUDIO — the master clock.
$B/.venv/bin/python $B/runtime/scripts/generate_audio_kokoro.py $R

# 3. CONFORM COMPOSITIONS. Each Root.tsx composition is registered at exactly
#    its beat's actual_duration_s * 30; update any that changed.
$B/.venv/bin/python -c "
import json;d=json.load(open('$R/beat_sheet.json'))
[print(b['beat_id'], b['shot']['remotion']['pattern'], round(b['actual_duration_s']*30)) for b in d['beats']]"

# 4. VISUALS — foreground only.
$B/.venv/bin/python $B/runtime/scripts/remotion_scenes.py $R --now "$(date -u +%FT%TZ)"

# 5. THE 4K MASTER.
$B/.venv/bin/python $B/runtime/scripts/compile.py $R --height 2160 --fps 30

# 6. SUBTITLES.
$B/.venv/bin/python $B/runtime/scripts/align.py $R
python3 $R/make_srt.py

# 7. VISUAL QC — see the sampling warning below. Sample t=0 for every beat.

# 8. THE 9:16 SHORT.
$B/.venv/bin/python $B/runtime/scripts/shorts.py $R --drop B05 B10 B11 B12 --keep B09 --handle @HumanitariansAI
$B/.venv/bin/python $B/runtime/scripts/generate_audio_kokoro.py $R/short
$B/.venv/bin/python $B/runtime/scripts/remotion_scenes.py $R/short --now "$(date -u +%FT%TZ)"
$B/.venv/bin/python $B/runtime/scripts/compile.py $R/short --height 1920 --fps 30
$B/.venv/bin/python $B/runtime/scripts/align.py $R/short
python3 $R/short/make_srt.py --out claude-hai-the-logout-that-didnt-short.srt
```

## QC SAMPLING — two traps, both hit on this reel

1. **`ffmpeg -ss T -i file` seeks on the input side** and snaps to the nearest
   keyframe — seconds of error on a 4K master.
2. **`select='eq(n\,A)+eq(n\,B)+…'` in one call does not reliably return frames in
   the order requested** (`n` is decode order). With many terms the outputs pair up
   with the wrong beat ids. This mislabelled the tail of both cuts here, twice — and
   both times the video was fine and the contact sheet was lying.

Use a batched `select` for a quick survey if you like, but **confirm anything
load-bearing with a single-frame, output-side extraction**:

```bash
ffmpeg -v error -i master.mp4 -ss 146.0 -frames:v 1 -vf scale=720:-1 -y out.png
```

That is how B09's caveat was verified in both cuts, and how it should be verified again.

## Things this reel will bite you on

1. **`--keep B09` is not optional.** B09 carries the PR #13 caveat on screen. Without
   it the short reads as claiming a complete fix.
2. **`--drop B05` is needed for the cap.** With only B10/B11/B12 dropped the short
   lands at 184.5s — over. B05 (the move) goes because B06 already carries the
   development/production contrast.
3. **B09's reveal timing is tuned to the narration.** Rows resolve at `0.52 + i·0.10`
   because "the fix is on main" is spoken at ≈0.53. If you re-record B09, re-check
   that the reveals still land on their words rather than before them.
4. **`shorts.py`'s auto-drafted outro** splices fragments of the dropped beats into
   an unreadable sentence. Replace it with written copy.
5. **`shorts.py` hardcodes a dark endcard** — regenerate with `dark=False`.
6. **SKIN LINT warns on B00/B13** — expected, they're `haiKit` wrappers.

## Hard constraints — re-verify every rebuild

- **Never imply `development` has the fix.** Extract every sentence containing
  "development" and read them individually; each must either describe the environment
  or state the branch lacks the fix.
- **Never hedge the three verified facts**: `signOut({ redirectUrl })` is live on
  `main`, raced against a 5s timeout with a fallback redirect, merged via PR #14 on
  2026-10-13; the stale "No Clerk signOut call" comment is gone from `main`.
- **Never claim logout is fully solved.** B11 must keep the line that textbook access
  was always revoked correctly and it was the hub's own session that survived —
  otherwise this reel contradicts "One Sign-In, Many Books", which is itself correct.
- **Keep the PR #13 caveat on screen, not only spoken**, and keep its
  "status checked <date>" footnote honest — re-run step 0 and update the date.

## Sources

Script: `the-logout-that-didnt-script.md`. Verified live against
`Medhavy/medhavi-hub`: `components/LogoutButton.tsx` on `main` and `development`,
PR #13 (open) and PR #14 (merged). Full ledger: `SOURCES.md`.

**Never publish.** The masters stay in this folder.
