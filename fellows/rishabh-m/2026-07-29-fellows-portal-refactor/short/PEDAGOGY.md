# PEDAGOGY — Fellows Portal, Refactored. (9:16 SHORT)
# Auditor: Claude Opus 5 | 2026-08-14
# GATE P — quality gate, not a cost gate (Kokoro audio is free).
# Human sign-off required below before generate_audio_kokoro.py runs.

## What this is
The 9:16 Shorts cut derived from `claude-hai-fellows-portal-refactor` (16:9,
283.4s). A Short is a **derivative cut, not a re-edit** (SHORTS LAW): beats were
cut, never re-authored, and every surviving beat reuses the parent's existing
MP3. **Exactly one line of new narration exists** — the rewritten outro, below.

## Cap check
Parent 283.4s → Shorts hard cap is 180s. Cut to **5 beats, ~76.5s (1:16)**,
comfortably inside the cap with headroom for the real outro duration.

## The cut
Kept: **B00** (intro) → **B02** (the ask) → **B03** (the code) → **B14** (outro,
rewritten) → silent endcard 4.5s.

Dropped (12): B01, B04, B05, B06, B07, B08, B09, B10, B11, B12, B12F, B13.

Rationale: cli-explainer doctrine says the 9:16 ships a **single cycle** and
points at the 16:9 for the complete example. The auto-plan kept three cycles and
still came in at 184.1s — over the cap — so it was overridden with an explicit
`--drop`. The kept cycle is the video's hero: the two-boolean schema change.

## ⚠ Deviation the signer must accept: no OUTPUT beat
The documented single-cycle spine is CLI → CODE → OUTPUT. **This cut has no
OUTPUT beat.** The only OUTPUT candidates are the four screen captures, which are
1280×720; a 9:16 centre-cut takes a 404×720 slice and upscales it 2.7× to
1080×1920, chopping the dashboard layout mid-component. That would be the
weakest-looking beat on the channel.

The trade taken: an all-generated Short where every beat is a native portrait
render, with the result deferred to the long ("the full video shows what actually
enforced it"). The funnel still works — arguably better, since the payoff is the
reason to click. **If you would rather honour the spine literally, say so and
B04 goes back in at 404×720.**

## The one new line (the reason this gate exists)
`shorts.py` auto-rewrites the outro to name what was cut. Its generated text was
defective — it stitched truncated fragments of dropped beats into a sentence:

> *"That's the short version. The full video also covers Before: fellow login
> worked fine,…, Log in once, as yourself.… and fellows portal, refactored. —
> watch Fellows Portal, Refactored. for the whole story."*

Unreadable aloud, and it mangles the title to lowercase. Replaced by hand with:

> "That's the schema change. The full video shows what actually enforced it —
> the profile split, and nav-level gating that gives an admin and a super-admin
> different dashboards from one component. Watch Fellows Portal, Refactored.
> The link is right below."

Verified accurate against the parent: the profile split is B05–B07, nav-level
gating is B08–B11, and B10/B11 are the same `DashboardNav` component rendered for
two accounts. Nothing claimed here is absent from the long.

## Portrait handling — no centre cuts
All four content beats are REMOTION renders, so the ONDA CHECK rewired them to
portrait compositions rather than cropping them (a centre cut chops code
mid-word):
- B00, B02 → `ClaudeComposerAsk916` (existed)
- B14 → `ClaudeTitleOutro916` (existed)
- B03 → **`ClaudeCodeBeat916` — newly added** to `Root.tsx` for this cut

Zero centre-cut media is used. The stale `media/B04-916.mp4`, `B07-916`,
`B10-916`, `B11-916` written by the first auto-plan are unused and should be
deleted.

## Toolkit change made for this cut
`ClaudeCodeBeat916` did not exist, which blocked every code beat from going
portrait. Added as a **registration only** — same component, same zod schema
(standing rule #4), registered 1080×1920.

One real fix was needed alongside it: `ClaudeCodeBeat` sets
`fontSize: height*0.022` with `whiteSpace:'pre'` and `overflow:'hidden'`, so in
portrait the type grows (1920×0.022 ≈ 42px) while the card narrows — long lines
would be **clipped, not wrapped**. B03's longest line is 76 chars; roughly 35
would have fitted. The component now shrinks the type to fit the longest line
**in portrait only**; the `isPortrait` guard leaves every existing 16:9 render
byte-identical. This also unblocks the video-2 Short, which has four code beats.

**Unverified until render:** the fit-shrink is a calculation, not yet an
inspected frame. The QC pass after compiling must confirm B03's code is fully
visible and still above the legibility floor — if the shrink overshoots, the fix
is fewer lines in the short's B03, not a smaller font.

## Estimated runtime
~76.5s across 5 beats (+4.5s silent endcard) — an output of the cut, not a target.

---

**VERDICT: PASS**