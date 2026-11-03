# BUILD-PROMPT — One Sign-In, Many Books

Paste-ready prompt that rebuilds this reel end to end. Run from `~/dev/`.
Free, local, no keys. **Never publishes.**

---

Rebuild the reel at `research/youtube/claude-hai-one-sign-in-many-books/`.
It is an **ai-explainer** on the default fidelity brand (claude palette),
**claude-hai** channel, **@HumanitariansAI**, narrated by **Bella** (`af_bella`),
Pragmatist register. Read `brutalist/skills/make/ai-explainer/SKILL.md` in full
before touching anything; it inherits from `skills/make/explainer/`,
`skills/make/your-turn/` and `skills/make/duration-planner/`.

Environment (this machine): Remotion needs Node ≥ 20 — `export
PATH="$HOME/.nvm/versions/node/v20.20.2/bin:$PATH"`. Python deps live in
`brutalist/.venv`, so call `brutalist/.venv/bin/python`, not system `python3`
(`./art doctor` reports blocked against system python; that is the venv, not a
missing dep).

```bash
cd ~/dev
export PATH="$HOME/.nvm/versions/node/v20.20.2/bin:$PATH"
B=brutalist; R=research/youtube/claude-hai-one-sign-in-many-books

# 0. GATE P — must already read "VERDICT: PASS". Do not bypass with --no-gate.
grep -q "VERDICT: PASS" $R/PEDAGOGY.md || { echo "GATE P unsigned"; exit 1; }

# 1. AUDIO — the master clock. Free; durations are ground truth.
$B/.venv/bin/python $B/runtime/scripts/generate_audio_kokoro.py $R

# 2. CONFORM THE COMPOSITIONS TO THE CLOCK.
#    Each composition in Root.tsx is registered at exactly its beat's
#    actual_duration_s * 30. If any mp3 changed length, update the matching
#    durationInFrames before rendering, or compile.py will freeze-hold or
#    tail-trim that beat's animation.
$B/.venv/bin/python -c "
import json;d=json.load(open('$R/beat_sheet.json'))
[print(b['beat_id'], b['shot']['remotion']['pattern'], round(b['actual_duration_s']*30)) for b in d['beats']]"

# 3. VISUALS — foreground only, never hand-rolled npx remotion render.
$B/.venv/bin/python $B/runtime/scripts/remotion_scenes.py $R --now "$(date -u +%FT%TZ)"

# 4. THE 4K MASTER.
$B/.venv/bin/python $B/runtime/scripts/compile.py $R --height 2160 --fps 30

# 5. SUBTITLES — word clock, then cues.
$B/.venv/bin/python $B/runtime/scripts/align.py $R
python3 $R/make_srt.py

# 6. VISUAL QC — mandatory, and the ffprobe numbers do not count.
#    Sample ≥2fps plus 15/50/85% of each beat, READ the PNGs, audit the
#    9-point rubric, log to _qc/REPORT.md. Zero BLOCKER, zero MAJOR to pass.

# 7. THE 9:16 SHORT — derivative cut, cap 180s.
$B/.venv/bin/python $B/runtime/scripts/shorts.py $R --keep B07 B08 B09 --handle @HumanitariansAI
#   then, in $R/short/: rewrite the auto-drafted outro line (it splices fragments),
#   regenerate its audio, bump ClaudeHaiTicketOutro916's durationInFrames to match,
#   re-render portrait, and regenerate the cream endcard:
$B/.venv/bin/python $B/runtime/scripts/generate_audio_kokoro.py $R/short
$B/.venv/bin/python $B/runtime/scripts/remotion_scenes.py $R/short --now "$(date -u +%FT%TZ)"
$B/.venv/bin/python $B/runtime/scripts/compile.py $R/short --height 1920 --fps 30
$B/.venv/bin/python $B/runtime/scripts/align.py $R/short
python3 $R/short/make_srt.py --out claude-hai-one-sign-in-many-books-short.srt
# then QC the portrait frames too — they re-band, so they are a different layout.
```

## Things this reel will bite you on

1. **`--keep B07 B08 B09` is not optional.** Scene 4 (the logout timestamp) is
   the author's designated payoff. If the short needs more headroom, cut Scene 2
   (B03/B04) — the author's own release valve — never Scene 4.
2. **`shorts.py`'s auto-drafted outro splices raw fragments** of the dropped
   beats into an unreadable sentence. Replace it with written copy that restates
   the title and points at the long, then regenerate only that beat's audio.
3. **`shorts.py` hardcodes a dark endcard.** This is a fidelity brand on a cream
   page; call `endcard_png(..., dark=False)` and verify the ground pixel is
   `(243,235,221)`. Do not patch `shorts.py` — dark is right for the teardown brands.
4. **SKIN LINT will warn on B00 and B13.** Expected. `ClaudeHaiTicketAsk` and
   `ClaudeHaiTicketOutro` are wrappers that render the shared `ClaudeComposerAsk`
   / `ClaudeTitleOutro` plus the LOGO LAW bug. Not a defect; see `_qc/REPORT.md`.
5. **Two compositions per beat, not per component.** B00/B12 both wanted
   `ClaudeComposerAsk` and B01/B10 both wanted `ClaudeHaiHubAndBooks`, but their
   audio lengths differ, so they are registered separately
   (`…TicketAsk` / `…TicketHandoff`, `…HubAndBooks` / `…HubConverge`).

## Hard constraints — re-verify every rebuild

- **Never speak or show the three-letter token acronym.** "Ticket" carries the reel.
- **One metaphor.** No unlocking device, travel document, or festival band. The
  script's "secret" and the visual "seal" belong to the stub and are fine.
- **Never render a real token string,** expired or not — it carries a real user id
  and email. The only identifier on screen is B04's invented
  `TCKT-EXAMPLE-0000` / `TCKT-EXAMPLF-0000`, captioned "example — not a real ticket".
- **Never open, display, or reference `auth-debug.txt`** (in the `medhavi-hub`
  repo root). The verify route appends real access decisions to it. B06's six-check
  list comes from `DEVELOPER.md` §4.2, not from that log.
- Re-run the constraint sweep in `_qc/REPORT.md` over both compiled beat sheets
  before calling the build done.

## Sources

Script: the author's `one-sign-in-many-books-script.md`. Verified against
`medhavi-hub`: `app/api/access/generate-token/route.ts`,
`app/api/access/verify/route.ts`, `DEVELOPER.md` §4.1–§4.4.
Full claim ledger and declared simplifications: `SOURCES.md`.

**Never publish.** The masters stay in this folder.
