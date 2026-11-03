# SOURCES — Works On My Machine

## Primary source

| Field | Value |
|---|---|
| Title | Week 1: Infrastructure & CI/CD — Video Script |
| Series | Provenance Gatekeeper Development Log |
| Structure | 5 scenes — HOOK / FRAMEWORK / WORKED EXAMPLE / FALSIFIABILITY / SCAFFOLDED TASK |
| Supplied | 2026-09-15 (revised: PR number corrected to **#44**, dual render added) |
| Author / narrator | Onkar Bhujbal (Humanitarians AI) |

## Beat ↔ scene map

| Scene | Beats |
|---|---|
| 1 — HOOK | B00 (+ B01, the mandatory BLUF the script does not carry) |
| 2 — THE FRAMEWORK | B02 |
| 3 — WORKED EXAMPLE | B03 (ask) → B04 (Dockerfile ∥ PR #44) |
| 4 — FALSIFIABILITY | B05 |
| 5 — SCAFFOLDED TASK & CLOSE | B06 · BHTF (handoff) · BOUT (close) |

## Claims taken from the source, verbatim or near-verbatim

| On screen / in narration | Source |
|---|---|
| "I am Onkar Bhujbal, a software engineer." | Scene 1 VO, verbatim |
| `ModuleNotFoundError: No module named 'yaml'` · `WORKS ON MY MACHINE` | Scene 1 visual |
| "'Works on my machine' is the death of microservices." | Scene 1 VO |
| Zero-Drift Matrix: `01 ISOLATION (DOCKER)` · `02 CANONICAL MANIFEST` · `03 CI/CD GATE` | Scene 2 visual + VO |
| The three axis questions, and "fail one of these axes → your deployment is a liability" | Scene 2 VO |
| FastAPI scaffolded inside Docker; Node build script aligning manifests | Scene 3 VO |
| **PR #44**, wired to GitHub Actions | Scene 3 visual + VO |
| **164 canonical checks** must pass before merge turns green | Scene 3 visual + VO |
| The bypass: local package added, `requirements.txt` not frozen, force push | Scene 4 VO |
| `git commit -m "quick fix" --no-verify` | Scene 4 visual, verbatim |
| "builds successfully locally but hard-crashes on the server" | Scene 4 VO |
| `node scripts/build-instructions.mjs --promote` · `0 un-synced manifests` | Scene 5 visual, verbatim |
| "If it returns anything other than zero un-synced manifests, your environment is drifting." | Scene 5 VO |

## The one thing NOT built — and why

**The FastAPI Dockerfile was never supplied.** The script calls for it on the left half
of Scene 3 and asks that both artifacts be "fully legible on screen", but the file itself
is not on disk and was not pasted in.

Writing a plausible Dockerfile and showing it as this project's file would be a
**DOUBLE-CHECK LAW violation** — it would put invented code on screen under the
authority of the author's own repo. So B04's left panel renders a **PIPELINE request**
naming exactly what is needed; the right half (PR #44, the 164-check counter, the merge
button arming) is fully built.

**To resolve:** set B04's `code` prop from the repo's real Dockerfile — trim to ~14 lines
(`FROM`, `WORKDIR`, the `requirements.txt` COPY + `pip install`, `CMD`) — and re-render
that one beat. `CiGateSplit` renders a listing instead of the slate as soon as `code` is
non-empty; no other change is needed, and the narration already fits the real file.

This mirrors how `ingest.py` was handled in Week 2 — see
`../claude-hai-gatekeeper-ground-truth/CHECKS-REPORT.md`.

## Corrections and additions under DOUBLE-CHECK LAW

1. **No timing, coverage or pass-rate metric is invented.** The script reports the check
   count (164) and the PR number (#44) and nothing else, so the reel claims nothing else
   — no build times, no coverage percentage, no "N minutes saved".
2. **Scene 4 is stated as a scenario, not as an incident.** The script describes what
   *would* happen if the gate were bypassed. The narration keeps it conditional ("what
   happens if we bypass the gate?") rather than implying this occurred on the project.
3. **B01 (the BLUF) is authored, not from the script.** The script carries no executive
   summary, but `EXECUTIVE-SUMMARY LAW` makes beat 2 mandatory. `features` →
   `guarantees` is the reel's actual misconception: week 1 looks like it shipped nothing.
4. **The `# ANYTHING ELSE` comment in B06 is the reel's addition** — it explains what a
   non-zero result *means* (manifests on disk and in the repo have diverged, and only one
   is what CI will build). The script gives the pass condition but not the diagnosis, and
   a scaffolded task the viewer cannot interpret is not scaffolding.
5. **"microservices" kept, "death of" kept** — the author's phrasing, and it is a claim
   about engineering practice rather than a factual assertion that could date.

## Palette decision

The script specifies the dark Brutalist palette with a red accent. A claude-explainer is
a FIDELITY brand that `CLAUDE-BRAND.md` forbids retinting, and it carries exactly ONE
accent. Terracotta `#D97757` carries every "red" the script asks for: the
`WORKS ON MY MACHINE` snap, the struck-through CI/CD axis in Scene 4, and the armed merge
button. Structural intent — visible grid, exposed labels, `border-radius: 0`, hard cuts —
is preserved.

## Narrator

First person, Onkar Bhujbal — matching the script's own Scene 1 VO. The Kokoro `am_onyx`
voice is a **synthetic read of the author's own script**, not a voice clone.

The script's Scene 5 sign-off still reads "Liam, for Onkar Bhujbal and Humanitarians AI",
carried over from the series template. Per the author's standing instruction, this reel
signs off **"Onkar Bhujbal, for Humanitarians AI."**

## Dual render (16:9 + 9:16)

Explicitly required by this revision, including *"keep core visual artifacts
center-framed for 9:16 safe zones."* Handled per `RENDER-TARGETS.md` §3:

- `CiGateSplit` puts its two panels **side by side in landscape and stacked in
  portrait**, and sizes the code listing from PANEL WIDTH against its longest line — not
  from canvas height, which is how code gets clipped mid-word in portrait.
- `ThreeStageBand` serializes the three axes top-to-bottom in portrait.
- Every bookend already has a `916` variant.
- Every beat therefore rewires; **no beat is flagged and none is centre-cut.**

## Components

**Built for this reel:** `CiGateSplit` + `…916` — the artifact beside the gate that
admits it: a file panel (with slate support), a PR check-run counter, and a merge button
that only arms once the count completes.

**Extended:** `ThreeStageBand` (= `GatekeeperIngestFlow`) gained a **failure mode** —
`failIndex` strikes one axis through in terracotta and stops the travelling token there,
`failLine` replaces the ready line with the bypass command. Both default to off, so the
Week 2 reels render byte-identically. Scene 4 reuses the *same* band rather than a second
matrix component, which is what makes the viewer read it as the same matrix returning.

**Reused:** `ClaudeComposerAsk`, `BrutalistHesitantWriter`, `ClaudeCodeBeat`,
`HaiTitleOutro`.
