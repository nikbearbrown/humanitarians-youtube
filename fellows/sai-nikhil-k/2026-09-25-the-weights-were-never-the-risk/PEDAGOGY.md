# PEDAGOGY — The Weights Were Never the Risk

**Reel** `weekly_updates/2026-09-25-the-weights-were-never-the-risk/` · **slug** `claude-sai-the-weights-were-never-the-risk`
**Subject** Gavia v0.2.0 — the Python-to-Rust port · **week of** 2026-09-25
**Host** Sai, in his own name (attribution override — see below)
**Voice** Kokoro `am_onyx`, free and local · **Chassis** all-Remotion, no Manim, no paid anything

---

## The ONE idea

> A rewrite that keeps the model file has not kept the model. The network was
> measured on particular pixels, so the port had to rebuild the pixels — and
> prove it by matching the old answers, not the old weights.

The week has an obvious headline: the Python backend is gone, Gavia runs in a
Rust core inside the app, the Mac download fell from 84 to 45 MB, and CI builds
installers for three operating systems. The reel treats that as the setting,
not the subject.

The subject is how the port knew it had changed nothing. The `.onnx` file is
byte-identical (same sha-256 before and after), which is exactly why it is
tempting to stop there. But the decoder, the JPEG reduction, the resampler and
the rounding all sit in front of the network. On 15 of the 26 validation photos
the Rust JPEG decoder's own shortcut would have fed the model a different
picture. So the port froze Python's answers into a fixture before deleting it,
rebuilt Pillow's behaviour, and made the Rust match all 32 boxes.

The same idea explains the one number that looks like progress but is not:
recall reads 0.879 this week against last week's 0.800. Same weights. Different
ruler.

## Act structure

| Beat | Act | Pattern | Why this pattern |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | Cold open; the week's ask typed on screen, three headline result lines. |
| B01 | THE SWAP | `ClaudeScienceChipGrid` | Six named things that left the app are a *set*. A grid is the honest shape for a set. |
| B02 | THE RISK | `BinaryBranch` | A real decision: trust the model file, or freeze the old answers. Two branches and a resolver. |
| B03 | THE PIXELS | `TypesetMath` | The JPEG draft rule is a formula. It is set as one — floored fractions, a set-builder max — then evaluated on a real validation photo. |
| B04 | THE PROOF | `ExecutedData` | Measured rows from runs actually made for this reel, not an illustration of them. |
| B05 | THE RULER | `DivergentFates` | One set of weights, two recalls, depending on who measures. A track that diverges is that argument's shape. |
| B06 | WHAT IT IS FOR | `ClaudeScienceChipGrid` | The six required features are a set; status is carried by the chip text. |
| B07 | VERDICT | `ClaudeVerdictArtifact` | One-page recap, four bare sentences. |
| B08 | HANDOFF | `ClaudeComposerAsk` | A prompt the viewer can paste, read aloud and discussed. |
| B09 | OUTRO | `LogoOutro` | `@HumanitariansAI` card. **Not** `ClaudeTitleOutro`, whose handle is hardcoded. |

## ILLUSTRATE LAW check

Claude UI appears at **B00**, **B08** and the verdict/outro only. Body beats run

`ChipGrid → BinaryBranch → TypesetMath → ExecutedData → DivergentFates → ChipGrid`

— six body beats, five distinct patterns, no two consecutive the same. ✓
(The two ChipGrids are four beats apart.)

Every body beat carries an ordered `show` block. None would survive as a static
slide with a voiceover: B02 forks and resolves, B03 reveals its algebra in three
stages timed to the narration, B04 fills a table row by row, B05 splits. ✓

## 9:16 constraint

Every pattern here has a registered portrait sibling in `Root.tsx` —
`ClaudeComposerAsk916`, `ClaudeScienceChipGrid916`, `BinaryBranch916`,
`TypesetMath916`, `ExecutedData916`, `DivergentFates916`,
`ClaudeVerdictArtifact916`, `LogoOutro916` — so the vertical cut rewires with no
new TSX. All strings were sized against the measured portrait budgets
(`build_beats.py --check`): BinaryBranch label ≤27 / detail ≤45 / fix ≤31,
ChipGrid sparkLine ≤22 / caption ≤40, DivergentFates notes ≤42.

B03's second and third rows are wide (aspect ≈ 14), so in portrait they render
smaller than in landscape. They are the first thing to inspect in the vertical
QC pass.

Narration carries no positional reference ("the top row", "on the left"),
because the same mp3 plays over both aspects.

## Evidence and honesty

Every number on screen was **re-run for this reel**, on this machine, on
2026-09-25. Nothing is quoted from the changelog on trust. See `FACTCHECK.md`
for each figure and `evidence/` for the scripts and their recorded output:

- `evaluate_python.out` — the deleted Python pipeline (`backend/scripts/evaluate.py`
  at `663feeb`, onnxruntime 1.29.0, Pillow 12.3.0) on the 26 validation photos.
- `evaluate_rust.out` — the shipped Rust pipeline (`examples/evaluate.rs` at `78b383e`).
- `parity_rust.out` — `tests/parity.rs`: Rust against the frozen Python fixture.
- `draft_factor.py` → `draft_factor.out` — Pillow's own `draft()` on every
  validation JPEG against the Rust formula: 26 of 26 agree.
- `scale_probe.rs` → `scale_probe.out` — jpeg-decoder's native `scale()` on the
  same photos: a different reduction on 15 of 26. (Scratch probe, not part of Gavia.)
- `model_sha256.out`, `release_and_ci.out` — the byte-identical weights, the
  release asset sizes and the CI job results, read from GitHub.

**Two places the repository's own prose was corrected, not repeated:**

- The README, CHANGELOG and ROADMAP say the Mac download "shrank from 84 MB to
  43 MB". The v0.2.0 release asset is 47,183,690 bytes = **45.0 MiB**. The reel
  says 45. (43 was plausibly measured before the icon and DMG artwork landed.)
- The shipped model card (`loon_v1.json`) still carries the Ultralytics
  validator's figures (P 0.930 / R 0.800), while the README quotes the app's own
  pipeline (P 0.906 / R 0.879). Both are real measurements of the same weights.
  B05 says so rather than letting 0.879 read as an improvement on last week.

**No adoption, speed or runtime claim appears.** The release has one recorded
download and no stars; neither is mentioned. No inference timing was measured.

## Attribution override

Established 2026-07-31 and carried through every weekly since: this series is
**hosted by Sai in his own name**, not by Liam-in-for-Bear. B00 says "This is
Sai"; B09 signs off "Sai." The IN-FOR-BEAR LAW of `WEEKLY-VIDEO-GUIDE.md` is
deliberately suspended here. The voice remains Kokoro `am_onyx`.

**One third party is named: Swara Joshi.** Two commits this week are hers
(`f7a9928` Windows run changes, `663feeb` the per-photo loon count), and the
Rust port's own commit message says it "brings in origin/swara's loon count".
Crediting her is the DOUBLE-CHECK LAW applied to people: the count feature is
not presented as Sai's. B06 and B07 name her. If you would rather not name a
collaborator in a public video, change those two lines — do not reassign the work.

## Expected build noise (not bugs)

- `./art run` prints a SKIN LINT line asking for `ClaudeTitleOutro` at B09.
  Wrong for this channel — its handle is hardcoded to `@NikBearBrown`.
- `./art scenes --check` may call a `*916` sibling NOT RENDERABLE. The
  `scenes.json` index lags `Root.tsx`; all eight are real registrations.
- B09's narration is held to seven words so it finishes inside the 4.0s logo
  card before its fade.
- `./art run vertical --height 3840` reports **20 BLOCKER edge-bleed** on the
  portrait *slate*: its own timecode burn-in. The clean candidate gated by
  `./art final` reports 0 / 0 (`vertical/_qc/REPORT.md`).

## Portrait-only edits (in `vertical/beat_sheet.json`, not the parent)

`shorts.py --vertical` regenerates `vertical/` and discards these — re-apply
them after any re-derive:

- **B06** `sparkLine` → `"WHAT GAVIA IS FOR"`. The landscape string wraps to two
  short lines in `ChipGrid916`, narrowing the ink box to 33% of the safe area at
  the 50% sample, and GATE V refused the final.
- **B03** `note` — no-break spaces inside "5568 × 3712" and "1392 × 928".

And one shared-toolkit fix, rendered into this reel: `DivergentFates916`'s split
label now sits on a patch of stage colour, because both arms leave the split
straight down through the centred label (`runtime/remotion/src/deckPatterns916.tsx`).
The same strike-through is visible in 09-18-2's shipped vertical ("ON WHAT?").

---

## Human review checklist

Work down this list before signing. Nothing below has been done by the
assistant.

- [ ] Read the full narration (below). Does it say what the week was?
- [ ] B00: is "This is Sai" in the right place and the greeting correct?
- [ ] B01/B07: are you happy saying **45 MB**, not the README's 43?
- [ ] B03: is the draft rule right, and is the Nikon frame the case you want shown?
- [ ] B05: is "same weights, different ruler" a fair account of 0.800 vs 0.879?
- [ ] B06/B07: are you happy naming Swara Joshi for the per-photo count?
- [ ] Is any figure on screen one you would not defend in public? (`FACTCHECK.md`)
- [ ] B08: is the handoff prompt one you would actually paste?
- [ ] Is anything here better left out of a public video?

After rendering, B03's equation frames must be inspected in both aspects at
each reveal and at 15/50/85%, with the result recorded in `FACTCHECK.md`.

---

## Full narration, as it will be spoken

<!-- NARRATION:BEGIN (generated from beat_sheet.json) -->

### B00 · ASK — `ClaudeComposerAsk` · 16.9s measured (59 words)

> Last week, Gavia was a Python server hiding inside a desktop app. This week
> the Python is gone. The detector was rewritten in Rust, the download shrank by
> almost half, and it installs on Mac, Windows and Linux. This is Sai. But a
> rewrite has one job first: find the same loons. Here is how you prove it did.

### B01 · THE SWAP — `ClaudeScienceChipGrid` · 17.8s measured (59 words)

> So what changed. The old app froze a Python server into the bundle and talked
> to it over a local port, with a token. All of that is gone. The detector runs
> inside the app, and the interface calls it directly. The Mac download went
> from eighty-four megabytes to forty-five, and every change builds installers
> for all three systems.

### B02 · THE RISK — `BinaryBranch` · 16.8s measured (62 words)

> Here is the trap. The model file is byte for byte the same, so it is tempting
> to call the answers the same. They are not guaranteed. The network only sees
> what the decoder and the resizer hand it. So before deleting the Python, the
> port wrote down every box it found on every validation photo, and made the
> Rust match them.

### B03 · THE PIXELS — `TypesetMath` · 19.7s measured (68 words)

> Here is one thing it had to rebuild. Before resizing, Pillow shrinks a JPEG
> inside the decoder, by the largest of one, two, four or eight that keeps both
> sides at least six hundred and forty pixels. A Nikon frame from the validation
> set gets four. The Rust decoder's own shortcut picks eight. On fifteen of the
> twenty-six photos, it would have handed the model a different picture.

### B04 · THE PROOF — `ExecutedData` · 21.2s measured (66 words)

> And it did. Both pipelines were re-run for this video on the same twenty-six
> photos. Python found thirty-two boxes above the shipped threshold; Rust finds
> all thirty-two, in the same places, confidences at most a point and a half
> apart. Precision and recall agree to four decimals. Average precision moved by
> a thousandth. It also scores the faintest guesses, where Rust has ninety to
> Python's eighty-nine.

### B05 · THE RULER — `DivergentFates` · 18.9s measured (60 words)

> One more number, because last week I said one loon in five goes unreported.
> This week's recall reads eighty-eight, not eighty. The model did not improve;
> the weights are byte-identical. The ruler changed. Last week's figure came
> from the training framework's own validator. This one is the app itself, at
> its shipped threshold. Twenty-nine of thirty-three loons found. Four missed.

### B06 · WHAT IT IS FOR — `ClaudeScienceChipGrid` · 19.9s measured (57 words)

> The README now also says what Gavia is for: six required features. Detection
> is shipped. Counting is partly there, as per-photo counts, which Swara Joshi
> contributed this week and which survived the rewrite. A call classifier,
> shoreline change, underwater habitat and invasive plants have not started.
> Next is survey counting: a whole folder, one total, one CSV.

### B07 · VERDICT — `ClaudeVerdictArtifact` · 13.1s measured (42 words)

> So: one page. The Python is gone, and the app runs on three systems. The
> weights were never the risk; the pixels were, and the port rebuilt them. All
> thirty-two boxes came back. And the recall moved only because the ruler did.

### B08 · HANDOFF — `ClaudeComposerAsk` · 17.5s measured (64 words)

> Your turn. If you are about to port a model to another language, paste this
> first. The weights will not change, so ask what to freeze before the old code
> goes: its outputs on real inputs, every step that touches pixels before the
> network does, and the one number you expect to move. If you cannot say why it
> moves, you are not done.

### B09 · OUTRO — `LogoOutro` · 2.7s measured (7 words)

> The weights were never the risk. Sai.

**Total: 544 words** → 164.5s measured (2:44). No 180s cap applies to the --vertical cut; audio remains the master clock.

<!-- NARRATION:END -->

---

VERDICT: PASS    — reviewer: SAI NIKHIL KUNAPAREDDY date: 09-25-2026
