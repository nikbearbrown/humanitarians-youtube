# BUILD-PROMPT — Mycroft "Multi-Month Trend Investigation"

Paste-ready prompt that rebuilds both cuts. Run from `/Users/adwaitchangan/Study/Brutalist/`.

---

Build the Humanitarians AI weekly **work** video at
`humanitarians-youtube/fellows/adwait-changan/2026-08-28-mycroft-trend-investigation/` with
the `brutalist.art` `ai-explainer` skill, in **both aspect ratios**.

```bash
source brutalist.art/.venv/bin/activate && cd brutalist.art
```

1. **Gates.** `PEDAGOGY.md` → `VERDICT: PASS`; `FACTCHECK.md` → `FACT GATE: CLEARED`.
2. **Re-verify against the artifacts, not the PR prose.** The source of truth is
   `nikbearbrown/mycroft` PR #17:
   - B05 against `inspect.getsource(trend._load_run)` — the tamper-check block, verbatim.
   - The "fifteen refusal paths" figure against
     `inspect.getsource(trend._load_run).count('raise TrendError')` → **15**. Scope the claim
     to the loader; the module has 30.
   - B03 and B07 against `reports/generated/mycroft-finance-investigator-trend-week35.md`.
   If a figure and the PR summary ever disagree, the generated report wins.
3. **Audio** → **render** → **compile `--height 2160`**.
4. **VISUAL QC.** Read the PNGs. Both `ClaudeWindow` beats carry financial tables and MUST
   render `numbered: false` with columns intact — a numbered financial table is a factual
   misrepresentation, not a style problem.
5. **Shorts.** `shorts.py <REEL> --drop B02 B04 B05 B06 B09 --handle "@HumanitariansAI"`,
   then audio → render → `compile.py <REEL>/short --height 3840`.
6. **Report** duration, beats, slates, defects.

**Do not publish, upload, or notify anyone.** The recipe is `DRAFT`, materiality is an
unapproved fixture, and the human gate is `OPEN` — all three must stay visible on screen.

## Rules that matter here

- **Never say or show an episode or week number.** Say "this week"; open with "Today we are
  going to learn about …"; the outro names the title only.
- **Protect B08 in the Short.** It carries the claim boundary — what the system refuses to
  say and who owns "why". On a finance tool a cut that keeps the mechanics and drops the
  boundary misrepresents the work. The auto-plan would drop BVDT and BHTF too; always pass
  explicit `--drop`.
- **`shorts.py` defaults the endcard handle to `@nikbearbrown`** — pass `--handle`.
- **Hand-write the Short's outro**; the auto-rewrite splices truncated fragments.
- **`short/` needs its own signed `PEDAGOGY.md`.**
- **Do not edit `beat_sheet.json` while a render process is running** — it re-dumps on exit
  and clobbers concurrent patches.

---

Expected: 13 beats 16:9 at 3840×2160, 8 beats 9:16 at 2160×3840, zero slates, $0.00.
