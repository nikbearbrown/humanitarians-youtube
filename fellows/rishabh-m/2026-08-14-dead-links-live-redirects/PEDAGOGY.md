# PEDAGOGY — Dead Links, Live Redirects. (claude-hai cli-explainer)
# Auditor: Claude Opus 5 | 2026-08-14
# GATE P — this is a QUALITY gate, not a cost gate (Kokoro audio is free).
# Human sign-off required below before generate_audio_kokoro.py runs.

## What this reel is
The sequel to `claude-hai-fellows-portal-refactor`, scoped to the 11 commits
dated 2026-08-10 on branch `dev` of `humanitarians_html` (`0e125f1`..`b952855`).
A site-wide link and route cleanup that turns into a lesson about the router:
consolidating five duplicate artifact files deletes the destinations of live
redirects in `next.config.mjs`, producing a 404 on a file nothing linked to.

It is deliberately a **corrections reel** — what was broken, what fixed it — not
a feature tour. It carries no demonstration footage and requires nothing from the
human: all 15 beats are machine-rendered. Commit list and diffs verified in
SOURCES.md.

## The 15 beats

| beat | act | pattern |
|---|---|---|
| B00 | INTRO — cold open, ask shown answered | ClaudeComposerAsk |
| B01 | PROBLEM — three kinds of rot | FellowsPortalLayerStack |
| B02 | ASK 1 — the crawler | ClaudeComposerAsk |
| B03 | CODE 1 — `check-links.mjs` | ClaudeCodeBeat |
| B05 | ASK 2 — consolidate the duplicates | ClaudeComposerAsk |
| B06 | CODE 2 — the delete | ClaudeCodeBeat |
| B07 | **OUTPUT — the 404** | FellowsPortalLayerStack |
| B08 | CHANGE — the revision | ClaudeComposerAsk |
| B09 | CODE 3 — `html-meta.ts` | ClaudeCodeBeat |
| B11 | ASK 4 — subdomains | ClaudeComposerAsk |
| B12 | CODE 4 — `middleware.ts` | ClaudeCodeBeat |
| B14 | SUMMARY | ClaudeVerdictArtifact |
| B14F | FUTURE WORK | FellowsPortalLayerStack |
| B15 | NEXT STEPS — handoff | ClaudeComposerAsk |
| B16 | OUTRO — title restate | ClaudeTitleOutro |

## Spine check (cli-explainer required spine)
Mandatory elements all present:
- **PROBLEM before any prompt** — B01 names three kinds of rot and tells the
  viewer one of them bites back ✓
- **At least one revision** — cycle 3 (B08→B09) is a genuine check-and-change:
  cycle 2's output is *wrong*, and cycle 3 changes the approach rather than
  refining it ✓
- **SUMMARY · NEXT STEPS · OUTRO** — B14, B15, B16 ✓

**⚠ Accepted deviation — OUTPUT beats.** Doctrine gives each cycle CLI → CODE →
OUTPUT. This reel has one OUTPUT beat, not four:

| cycle | ASK/CHANGE | CODE | OUTPUT |
|---|---|---|---|
| 1 — the crawler | B02 | B03 | folded into B05's narration |
| 2 — the delete | B05 | B06 | **B07** ✓ |
| 3 — the revision | B08 | B09 | folded into B09's narration |
| 4 — subdomains | B11 | B12 | folded into B12's narration |

The three folded results were "here it is, working" demonstrations of claims no
viewer would dispute — the crawl's findings, the redirect resolving, the
subdomain loading. Stating them is enough; showing them was ceremony. B07 is the
exception and is non-negotiable: it is the only evidence for the reel's central
claim, and without it B08 repairs a problem the viewer never saw.

## THE ACTUAL-CODE LAW
Four CODE beats, all real source or real command output — no pseudocode:
- **B03** → `scripts/check-links.mjs` (`MIN_TEXT`, `TEMPLATE_MARKERS`) plus the
  `package.json` script entry added in `13c3370`
- **B06** → literal `git show --stat c89299f` output (5 files, 2,612 deletions)
- **B09** → `lib/html-meta.ts` as changed by `4af984f` — the comment and the
  `SUPERSEDED_ARTIFACT_FILES` filter, quoted verbatim
- **B12** → `middleware.ts` as created by `b952855`, trimmed to map + rewrite

Each ASK plausibly generates the CODE shown; each CODE plausibly produces the
result described. **SCORE: PASS**

## The pedagogical claim, and why it holds
The load-bearing idea is *a redirect is a reference*. It is verifiable, not
rhetorical: `next.config.mjs` maps `rootFilesMovedToArtifacts` — eight filenames
including all five that `c89299f` deleted — to `/artifacts/:file`. Nothing in any
page links to `gru.html`, which is exactly why deleting it looked safe; the only
pointer lives in the router config, where a link crawler and a `git grep` for
hrefs both miss it. The recovery commit `4af984f` is evidence the trap was real
and was hit in the actual history, six minutes after the delete — not staged for
the video.

## B07 — rebuilt, not captured (REBUILD LAW)
B07 is a native Remotion animation of the causal chain, not a screen recording.
The **REBUILD LAW** prefers this: "any source figure is rebuilt as native
animation, never a screenshot." Three cards reveal in sequence:

1. `next.config.mjs` — `/gru.html → /artifacts/gru.html · permanent: true`
2. `c89299f` — deleted `public/artifacts/gru.html`, nothing linked to it
3. `GET /gru.html` — `301 → 404` *(accent)*
   caption: *"The redirect outlived its destination."*

Every line traces to SOURCES.md. **No fabricated HTTP output appears on screen** —
a mocked-up `curl` trace would have been invention dressed as evidence, so the
beat is presented plainly as a diagram of facts.

## DOUBLE-CHECK LAW — verification notes (full detail: SOURCES.md)
| Claim on screen | How it was verified |
|---|---|
| "5 files changed, 2612 deletions" | Literal `git show --stat c89299f` output |
| "/tools … still shipping 288 lines" | `143df5f` diffstat: 79 + 88 + 121 = 288 |
| "gru.html and gru-tool.html — the same tool, listed twice" | `SUPERSEDED_ARTIFACT_FILES` comment states the superseding relationship |
| Three subdomains | `SUBDOMAIN_PROJECTS` — exactly mycroft / medhavy / dayhoff |
| "a redirect is a reference" | `rootFilesMovedToArtifacts` contains all five deleted filenames |
No model version numbers, no drifting counts, no dated claims. Every number
shown is structural and re-derivable from the repo at any time.

## Provenance — stated on air
`rootFilesMovedToArtifacts` was authored in `2073715` (2026-07-15) by
`nikbearbrown`, four weeks before the delete, in a commit about the AI+1 hub.
B08 names this ("four weeks earlier, a different author … inherited config is
still your config"). It is the actual reason the delete looked safe; omitting it
would portray the mistake as more careless than it was.

## Scope gap — chosen, not overlooked
Scoped to work done after video 1 was *built*, not after video 1's *content*
ends. 26 commits sit between the two reels, covered by neither: 6 by `RishabhHM`
(2026-07-01, course/donate/sorting) and 20 by `nikbearbrown` / `Nik Bear Brown`
(2026-07-15–21, the AI+1 hub and a prior site-wide broken-link pass). Excluded as
off-spine. Note: `9d59ca1` was an earlier *manual* broken-link pass, so the
narration claims only that this crawler is the first **automated** one. Full
table in SOURCES.md.

## Pragmatist register check (required when-NOT-to diagnostic)
B14 states the method (hide the row, keep the file) AND names when the opposite
applies — deleting is fine when nothing references the file, which is precisely
the condition that was assumed and not checked. B14F is blunter still: the
guardrails do *not* exist, so the same failure is currently unguarded. The hai
channel's mandatory "when NOT to" is present. **SCORE: PASS**

## HANDOFF LAW
B15's prompt is read aloud in full and then justified ("run it even if you have
never deleted anything, because redirects outlive the moves that created them").
It extends the lesson into the viewer's own repo rather than restating it.
**SCORE: PASS**

## Brand/channel check
`claude-hai`: Kokoro `af_bella`, Pragmatist register, `@HumanitariansAI` footer
chip, greeting `"Hi, HAI"` ✓. Visual skin stays the shared `claude` fidelity
palette per house law ✓. Continuity with video 1: same topic (`Irreducibly
Human`), same spoken sign-on ("Hi! This is RM, for Humanitarians AI."), same
title grammar (`<Noun>, <Past-participle>.`).

## Render notes
- **B01, B07, B14F use `FellowsPortalLayerStack`**, registered 1280×720 — render
  with `--scale 3` to reach 3840×2160. `--scale 2` silently yields 2560×1440;
  that bug was found and fixed during video 1's 4K pass.
- **Each carries its own `durationInFrames`.** The component's reveal is authored
  in fractional progress (caption fades over p 0.72→0.82), so a beat shorter than
  the registered 737 frames was truncated mid-curve and its caption left
  part-opaque — B01 rendered at 17% and B14F at 33% before this was caught by
  inspecting frames. The composition now takes the beat's own frame count.
  Verified fixed on rendered frames, not assumed.

## Runtime
15 beats. 210.7s of audio already generated across 12 beats; B05, B09 and B12
regenerate (their narration absorbed the folded results). Expect roughly
**4:40** — an output of the script, never a target.

---

**VERDICT: PASS**
