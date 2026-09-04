# BUILD-LOG — Assisted, Not Automated.

## GATE DEVIATION — the beat-mix contract is not met, by machine constraint

`deep-explainer`'s reason for existing is its lane quota. Required, and what this build
actually has:

| Lane | Required share of body | This build | Why |
|---|---|---|---|
| VOX (pantry stills, machine-animated) | 20–25% (outside 10–35% = **FAIL**) | **0%** | Cannot source stills on this machine. `smithsonian_index.py` is not shipped, so `smithsonian_fetch.py` has no index to read; the `--s3` keyless flag its own error message recommends is not in its argument parser; `SI_API_KEY` is unset. The tier-0 local library (`svg/svg/images/`, `pantry_search.py`) is also not shipped, so the Gate D2 tier-0 pass cannot run either. |
| MANIM | 25–40% | **0%** | `manimpango` requires cairo's C headers, which come from Homebrew, which requires a password this agent will not enter. Verified again at build time: `ModuleNotFoundError: No module named 'manim'`. |
| REMOTION | 30–45% | **100%** | The only working lane. |

**This would FAIL the plan gate as written** ("vox share outside 10–35% is a FAIL"), and
hard rule 1 says so plainly: *"A 'deep-explainer' with 5% vox beats is an ai-explainer that
skipped its pantry. Fix the plan, not the label."*

The label is therefore not being defended. **This episode is the ai-explainer chassis run
at deep-explainer length and act structure — not a compliant deep-explainer.** The human
was shown the blocked lanes before authoring began and chose this path over (a) a
previz-plus-shopping-list two-stage build, or (b) obtaining a free Smithsonian API key.

What was kept from the genre: the act structure with segment cards, the 5–10 minute band,
the ~7–14s beat rhythm and 25–45 word body narration, the fixed spine (cold open →
acts → verdict → your turn → title outro), and the PROOF GATE.

What was dropped: the vox quota, vox runs and their handoff contracts, the pantry law, the
Gate D2 shopping list, and Gate D1's slate previz (there is nothing to shop for, so a
previz stage would be theatre).

### To make this a compliant deep-explainer later

1. Install Homebrew → `brew install cairo pango` → `pip install "manim<0.19"` — unblocks
   the MANIM lane.
2. Either ship `smithsonian_index.py` / repair the `--s3` path in `smithsonian_fetch.py`,
   or set a free `SI_API_KEY` from api.data.gov — unblocks VOX sourcing.
3. Re-plan the body to the quota and rebuild. The narration and stats carry over unchanged;
   only the lane assignment per beat changes.

## STATISTICS — provenance discipline

Seven figures were supplied by the human as verified, with sources. They are reproduced
**verbatim** and cited on screen at the beat where each appears, and again on a dedicated
SOURCES card near the end.

Enforced structurally: `SeoStat`, `SeoCompare`, `SeoDrop` and `SeoShare` all take a
**required** `source: string`. A stat scene cannot be authored without its citation. Values
are typed as strings and rendered verbatim — never parsed for display, never recomputed.
(Bar *lengths* derive a number from the string so two bars read as comparable, but the
printed figure is always the original string.)

No figure beyond the seven appears anywhere. Everything else in the episode is ordinal or
descriptive, per the human's instruction.

## Other constraints carried from previous reels in this series

- **GATE T cannot run** — `type_check.py` is not shipped in this toolkit, though the skill
  lists it as "ALWAYS RUN". Type checked by eye against the ~24px floor.
- **Gate V reports a blanket false-positive `edge-bleed`** on every reel: it inspects the
  `--review` cut and flags that cut's own burn-in, because `BURN_IN_EXCLUDE` masks only the
  bottom strip while the label sits top-right. Verification is therefore done against the
  clean master.
- **`OUTRO-LOCK.md`, `AUDIT-MODE.md`, `DESIGN-PRINCIPLES.md`** are referenced by the skill
  and none ship here.
- **No mascot** — `ClaudeMascotScene` is absent, so the outro card carries title + handle
  only. PIXEL-ART LAW is moot.
- **Channel** — `@Yatra`, `claude-yatra`, Kokoro `af_bella`. The skill's channels table has
  no row for this channel; it is this series' established convention, not a documented one.

## Format

16:9 master, plus a **full-length** 9:16 for TikTok. The vertical deliberately exceeds the
3:00 cap on YouTube Shorts and Instagram Reels — the human chose full-length over a
beat-cut short. `shorts.py` is therefore run with an explicit empty drop plan so it does
not auto-cut beats to fit a cap that does not apply to the target platform.
