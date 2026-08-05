<!-- BEGIN BRUTALIST REBUILD GUIDE -->

# Cage, Rules, Belts — MMA vs Boxing

## What this video is about

**Topic:** COMBAT SPORTS — MMA vs BOXING

Host: **Param Madan**. Voice: Kokoro `af_bella`.

The plan contains **11 beats** with a runtime of **210 seconds** (3:30), rendered
at **3840×2160**. Sources are recorded in `SOURCES.md` with retrieval dates.

An explainer for viewers who follow neither sport. It answers three questions —
what the floor looks like, what a fighter may legally do, and how many belts are
on the line — and argues one claim: **MMA's top tier is a single organization
while boxing's is four**, which is why "world champion" means one name in MMA and
up to four in boxing. Every term (octagon, submission, sanctioning body, interim
title, undisputed) is defined the first time it appears.

## Beats

| Beat | Act | Pattern | Seconds |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | 20.8 |
| B00B | PROMISE | `MvbPromise` | 18.9 |
| B01 | BLUF | `MvbFloorPlan` | 16.2 |
| B02 | EVIDENCE | `MvbWeapons` | 24.4 |
| B03 | EVIDENCE | `MvbOneOrg` | 27.1 |
| B04 | TURN | `MvbFourOrgs` | 20.3 |
| B05 | CONSEQUENCE | `MvbSplitBelts` | 22.3 |
| B06 | PAYOFF | `MvbUndisputed` | 17.1 |
| B07 | VERDICT | `MvbTest` | 19.9 |
| B08 | HANDOFF | `ClaudeComposerAsk` | 19.6 |
| B09 | OUTRO | `MvbOutro` | 3.4 |

`B00B` is the executive-summary beat: it states what the video is and why to
keep watching before any evidence lands.

## Files

| Path | What it is |
|---|---|
| `beat_sheet.json` | Source of truth — narration, shot list, per-beat props, measured audio durations. |
| `src/MmaVsBoxing.tsx` | The nine Remotion scenes written for this reel. |
| `src/Root.registration.tsx` | The exact lines `Root.tsx` needs so those scenes render. |
| `description.txt` | YouTube description with chapter timestamps. |
| `SOURCES.md` | Every on-screen figure, ledgered with retrieval dates. |
| `PEDAGOGY.md` | GATE P — does the explainer actually teach? |
| `BUILD-LOG.md` | What was built, what deviated from house law, and why. |

MP3 and MP4 are excluded by the repository's root `.gitignore`.

## Make your own version

Download the free local toolkit:

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./setup
```

Then, with this folder as `<REEL>`:

```bash
cp src/MmaVsBoxing.tsx runtime/remotion/src/scenes/
# apply src/Root.registration.tsx to runtime/remotion/src/Root.tsx

python3 runtime/scripts/generate_audio_kokoro.py <REEL>
python3 runtime/scripts/remotion_scenes.py <REEL>
./art final <REEL>          # 3840x2160 master
```

`./art final` is the 4K path. `./art run` compiles a 1080p review cut — the
per-beat renders in `media/` are already native 4K because `remotion_scenes.py`
renders at `--scale=2`, so `./art run` discards resolution that already exists.

Recommended builder: **`ai-explainer`**.

## These facts expire

Belt holders change every few months. This project handles that three ways:
every holder is a scene **prop** rather than a hardcoded string, `B05` carries a
visible "as of 3 August 2026" date, and `B07` tells the viewer outright that the
names change while the structure does not. **Re-verify the `SOURCES.md` ledger
before any re-cut.**

This reel is itself a rebuild of a July 2026 version whose central claim had
already expired — the UFC heavyweight division now carries an interim champion
alongside the undisputed one, which broke the old "exactly one champion per
division" contrast. Four claims were corrected; see the corrections section of
`SOURCES.md`.

## Research prompt

> Research **MMA versus boxing — governance, rules, and world titles** for an
> educational explainer aimed at viewers who follow neither sport. Locate primary
> sources: sanctioning-body champion listings (WBC, WBA, IBF, WBO), official UFC
> athlete and division pages, and unified rules documents. Identify the central
> question, the mechanism that resolves it, important terminology, and every
> dated or version-sensitive claim. Return a claim table with claim, exact source
> URL, retrieval date, pinpoint evidence, confidence, and what must still be
> verified. Do not invent statistics, names, or results.

## Fact-check prompt

> Audit `beat_sheet.json` beat by beat. Extract every factual, numerical, and
> governance claim. Check each against the strongest available primary source —
> prefer the sanctioning body's own site over aggregators. Produce a table with
> beat ID, claim, verdict (SUPPORTED / QUALIFY / UNSUPPORTED / OUTDATED),
> evidence, source, and required correction. Pay particular attention to claims
> that were true when written and have since expired: title holders, vacancies,
> interim champions, and division counts. Do not silently repair the script —
> list every proposed change for human review.

## Build and review loop

You are the conductor; the machine performs the build. GATE P in `PEDAGOGY.md`
requires a human signature before a master ships, and rendered frames must be
read rather than inferred from an `ffprobe` output — two layout collisions and
one dead-canvas defect in this reel were caught only by looking at the PNGs.

<!-- END BRUTALIST REBUILD GUIDE -->
