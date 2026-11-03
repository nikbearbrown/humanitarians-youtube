# BUILD-LOG — llm-function-calling

Deviations and findings that need an explicit author justification rather than a
silent pass, per the PROOF GATE and VISUAL QC LAW.

## 1. Outro is `FnCallTitleOutro`, not `ClaudeTitleOutro` — deliberate

SKIN LINT warns: *"BOUT: palette=claude but the outro is 'FnCallTitleOutro' —
OUTRO LAW wants ClaudeTitleOutro."*

Justified. `ClaudeTitleOutro` hardcodes `const HANDLE = '@NikBearBrown'` and
always renders one of the 18 mascots. Both are locked by `OUTRO-LOCK.md`, whose
Scope section reads: *"Only claude-liam / @NikBearBrown reels … Other channels —
hai, medhavy, musinique … have their OWN outros and NEVER get this card, handle,
or mascot."* This reel is `@HumanitariansAI`, so using that card would violate
the lock, not satisfy it.

`FnCallTitleOutro` keeps everything OUTRO LAW actually requires — exact title
restate, poster serif, terracotta terminal period, handle beneath, no subline,
slug-seeded deterministic polarity — and drops only the two elements the lock
reserves for the other channel. The lint checks the component name rather than
the channel scope, so it cannot see this distinction.

## 2. Motion histogram is 100% Remotion — accepted

Warning: *"'remotion' carries 14/14 beats (100%) — over the ~40% pantry cap."*

Accepted for this reel. The cap in `MOTION.md` exists to stop a reel from
becoming a single-language slideshow, and the mix it wants assumes Manim
fragments or human-supplied media. This subject has no equations to animate and
no archival footage to source: it is a mechanism explainer whose every figure is
a deterministic diagram. Every beat is a distinct visual scheme (composer,
hesitant writer, predict card, chip grid, loop figure, source flow, code block,
layer stack, binary branch, verdict artifact, title card), so the failure the cap
guards against — visual monotony — does not occur. Introducing Manim purely to
satisfy a ratio would be padding.

## 3. Duration mismatch — a pipeline bug found and fixed during this build

The first compiled cut passed BLOCKER=0 but GATE V reported 14 `underfill`
MAJORs. Inspecting the frames showed those were a **symptom, not a layout
problem**: every beat was truncated mid-animation.

`remotion_scenes.py` renders each composition at its *registered*
`durationInFrames`, then the clip is cut to the beat's measured audio length.
Every illustration is a pure function of `useP() = frame / durationInFrames`, so
it is paced to the registered length. With 30s compositions against 14–21s
beats, only 48–71% of each animation was ever seen:

| Beat | Scene | Registered | Shown | Consequence |
|---|---|---|---|---|
| B01 | `BrutalistHesitantWriter` | 20.2s | 50% | the BLUF correction never landed |
| B03 | `ClaudeScienceChipGrid` | 30s | 48% | 2–3 of 5 chips appeared |
| B04 | `FnCallLoop` | 30s | 52% | 2 of 4 framework stages |
| B05 | `ClaudeScienceSourceFlow` | 30s | 61% | settle line never landed |
| B07 | `FnCallLoop` | 30s | 58% | 3 of 4 stages in the worked example |
| B08B | `ClaudeScienceLayerStack` | 30s | 54% | 2 of 3 rounds |
| B09 | `BinaryBranch` | 30s | 56% | the resolver card never appeared |
| BVDT | `ClaudeVerdictArtifact` | 34s | 49% | artifact lines incomplete |

B01 was the worst: its final frame read *"Function calling is how a model **runs a
tool by itself** and then uses what comes back"* — the uncorrected misconception —
while the narration spoke the corrected version. The mandatory executive summary
was asserting the exact claim the reel exists to dismantle.

**Root cause is a doctrine conflict, not an authoring mistake.** SHOW-DON'T-TELL
LAW sets a 45–70 word body-beat budget; at `am_onyx`'s measured ~3.35 words/sec
that yields 13–21s beats. The shared illustration components are registered at
30s. The exemplar reel `claude-liam-algorithmic-art` does not hit this because
its beats run 68–97 words (≈22–29s), *above* the stated budget, which nearly
fills its 30s compositions.

**Fix applied.** The repo already documents the correct pattern at
`Root.tsx` (LogoMotion): length is a prop, and `calculateMetadata` converts it to
`durationInFrames` so *"the animation re-times instead of truncating."* That
pattern was extended to every composition this reel uses:

- New components (`FnCallLoop`, `FnCallPredictCard`, `FnCallTitleOutro`).
- Shared components (`BrutalistHesitantWriter` ×3 aspects, `ClaudeComposerAsk`
  ×2, `ClaudeVerdictArtifact`, `ClaudeScienceLayerStack/SourceFlow/ChipGrid`,
  `BinaryBranch`).

**Backwards-compatible by construction:** each `durationInSeconds` defaults to
that composition's previously-registered length, and `calculateMetadata` reads
`props.durationInSeconds ?? <old default>`. A beat sheet that omits the prop
renders exactly as before, so no existing reel changes.

`ClaudeCodeBeat` was deliberately left alone: at 300f/10s it already completes
within its beat and then freeze-holds, so re-timing it to a longer beat would
only slow its line stagger.

## 4. Windows environment bugs worked around

This build ran on Windows and needed `ART_NO_DRAWTEXT=1 PYTHONUTF8=1`. A fourth
bug blocked rendering entirely and was patched: `remotion_scenes.py` called a
bare `"npx"`, which `subprocess`/`CreateProcess` cannot resolve on Windows
(no PATHEXT lookup), and `shutil.which("npx")` returns the extensionless MSYS
shell script under Git Bash, which also cannot be executed. Now resolved via an
`npx.cmd`/`npx.exe`-first lookup with an `ART_NPX` override. See the upstream
issue draft covering all of these.

## 5. Render scale

This pass was rendered with `ART_SCALE=1` (a new env override; the default stays
`2`) for a fast pacing-review cut. **Text is not supersampled in this cut** — do
not judge type quality from it, and do not ship it as a master. Re-render without
`ART_SCALE` for the real thing.

## 6. `triggerWords` only matches SINGLE tokens — SKILL.md documents otherwise

This is the bug that actually broke B01, and the duration fix in §3 did not touch it.

`buildActs()` in `scenes/BrutalistHesitantWriter.tsx` splits the text on
whitespace (`p.text.split(/(\s+)/)`) and then tests each token with
`triggers.indexOf(core.toLowerCase())`. A trigger is therefore only ever matched
against **one whitespace-delimited word**. A multi-word trigger silently matches
nothing — no error, no warning, and the beat renders the *uncorrected* text.

ai-explainer's SKILL.md instructs the opposite, under EXECUTIVE-SUMMARY LAW:
*"when the misconception lives in a phrase, put the whole phrase in
`triggerWords`"* — and its own worked example is a three-word phrase,
`list of topics` → `sequence of distinctions`. That documented example cannot
work against this implementation.

B01 was originally authored to the doctrine with
`triggerWords: "runs a tool by itself"`. It never fired, so the reel's mandatory
executive summary rendered the misconception and held it through the cut while
the narration spoke the corrected version.

**Fix:** put the swap on one token and let the *replacement* carry the phrase —
only the trigger is token-matched, the replacement can be any length:

    text:        "Function calling is how a model\nruns a tool\nand then uses what comes back."
    trigger:     "runs"
    replacement: "asks your program to run"
    result:      "Function calling is how a model asks your program to run a tool
                  and then uses what comes back."

Verified by sampling the beat's final frame: the corrected sentence is on screen
and matches the narration verbatim.

**Also fixed:** the writer's performance is paced in absolute milliseconds
(`charMs`), not as a fraction of the composition, so it cannot be re-timed by
`durationInSeconds` — shortening the composition only truncates the typing. Its
`calculateMetadata` now uses the module's own exported `hesitantWriterFrames()`
helper, whose comment says *"Use it to size the composition"*, and the typing was
tuned (`charMs: 38`, `mistakeRate: 0`, `hesitateBetween: 12`) to fit the 10.05s
audio window with room to hold the corrected sentence.

## 7. Final QC state — BLOCKER 0, MAJOR 7, all `underfill`

GATE V went 14 → 10 → 7 MAJOR across the fixes. Every remaining flag is the same
`underfill` class (content below 55% of the safe area). No BLOCKER at any point.

| Frame | Fill | Assessment |
|---|---|---|
| B01_50 / B01_85 | 17% / 28% | 3-line centred text beat. Type raised 76→96px (a real improvement); a 3-line serif block cannot reach 55% without redesigning the component. |
| B02_50 | 54% | One point under the threshold. `PredictCard` exposes no size prop. |
| B03_50 | 39% | **Transient** — sampled mid-stagger while chips are still arriving. Clean by 85%. |
| B08B_50 | 33% | **Transient** — same, cards still stacking. Clean by 85%. |
| BVDT_50 / BVDT_85 | 51% | `ClaudeVerdictArtifact` geometry. Four points under. |

Two distinct things are left, and neither is a correctness defect:

1. **Transient mid-stagger samples** (B03_50, B08B_50). Inherent to staggered
   reveals: GATE V samples at 50% of the beat, when by design not every element
   has landed. Clearing these would mean front-loading every reveal, which
   fights the signalling principle (reveals land ON the spoken word).
2. **Shared-component geometry** (B01, B02, BVDT). These components are used by
   other reels, and raising their fill means changing their layout for everyone.
   Not done here.

All *substantive* defects found by inspecting frames are fixed: every animation
now completes within its beat, the BLUF corrects itself, the framework and worked
example both show all four stages with the return leg, and B09's resolver lands.
