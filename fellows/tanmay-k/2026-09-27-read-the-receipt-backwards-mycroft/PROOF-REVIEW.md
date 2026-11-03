# PROOF review — Week 24 work video, *Read the Receipt Backwards* — pre-production (2026-09-28)

**Stage:** script signed at Gate P (2026-09-28); nothing generated yet: no audio, no scenes. This
review is deliberately placed here (Week 24 time lesson: checks before renders).

**Verdict: fix 4 wording points, then generate.** The structure, the claims and the framing all hold.
Four sentences overclaim or blur slightly. Each fix is a few words, and the changed sentences need your
quick re-read (a Gate P delta), not a full re-read.

## Teaching rubric

| Criterion | Score | Why |
|---|---:|---|
| Explicit framework | **2** | B03 states the move ("which step checked this, before it was written down?") before the first line is read |
| Reusable rubric | **2** | One question, one stamp per line, carried/earned; it transfers to any receipt, approval or log (B12) |
| Worked example | **2** | Six receipt lines, each answered live on the real build |
| Falsifiability / edge case | **2** | Three honest limits: synonyms (B07), the Gate's absent default (B09), and the merchant open box (B11). Plus the turn (B10): a sealed record can still carry an unearned line |
| Active task | **2** | B12: stamp every line of one record you own; add the check or mark the line unverified |
| Friction | **2** | B01's well-formed but false receipt; B06's "the receipt looked perfect"; B10 resolves it |

**12/12 on the script.** It's re-scored on the first compile, where the production checks apply.

## Findings

| # | Beat | Finding | Severity | Fix (exact new wording) |
|---|---|---|---|---|
| 1 | B05 | **"It went through" overstates it.** Before the fix, the Morgan purchase reached the Gate as a new category and completed because the demo's gate policy approved it (README #5: "if the Gate's supplied decision function happened to approve it"). The Gate isn't named until B09, so a viewer can't know that step existed | MAJOR (accuracy) | "…it looked like an ordinary new kind of purchase. **So it went to the gate that decides new cases, the demo's gate said yes,** and the receipt said Morgan approved it." |
| 2 | B06 | Same shape: "the purchase went through". The spelling variant reached the Gate, which approved it (the $70 is under the demo's cutoff) | MAJOR (accuracy) | "It treated it as a category Devon had never set, **sent it to that same gate, and the gate said yes.** The receipt looked perfect." |
| 3 | B02 | "At the end of every purchase, Mastercard describes a record…" can be heard as Verifiable Intent being live on every Mastercard purchase. Mastercard's page says integration into Agent Pay is "in the coming months" (FACTCHECK M4) | MAJOR (accuracy) | "**For purchases like these, Mastercard has described** a record called Verifiable Intent, 'a tamper-resistant record of what a user authorized.'" |
| 4 | B03 | "A line with an answer is **proven**" is stronger than the build shows: a check earns a line, it doesn't prove the world. The film elsewhere says "earned" (B04, B05) | MINOR (consistency) | "A line with an answer is **earned**. A line without one is just being carried along." |
| 5 | B01 / B05 | Devon first appears at B05 ("Devon's agent") with no introduction; B01 says only "somebody else" | MINOR (clarity) | B01: "The agent belonged to somebody else, **a cardholder called Devon.**" |

Checked and **not** findings:
- Every quote is verbatim (M1, M2, M3, M5).
- The reconstruction is labelled on screen (B01, B05).
- "I found this one while making this video" is true (round 3, 2026-09-28).
- "Plain Python" is true: standard library only, 3.10+.
- No gap/flaw/defect wording (scanned).
- No overlap with W15–W23 phrasing.
- 4:47 runtime.
- "Credentials just failed" (B04) refers to an agent's verification, not the build.

## Production plan checks (before anything is generated)

| Check | Plan |
|---|---|
| Sources on screen at the moment of assertion | Every quote appears with its source as it's spoken (B02 M1, B03 M3, B04 M5, B05 M2, B11 M8). Every code claim shows its live result row |
| Honesty labels | "RECONSTRUCTION: early version, before review round 2" on the Morgan receipt, whenever it's on screen |
| Timing | audio → **Whisper-align immediately** → every cue on the Whisper clock before the first render |
| New scene (ONE RECEIPT) | build the receipt component once, then **stills of B05 and B11 in both aspects** (16:9 + 9:16 Shorts zones, label sizes, GATE V fill) before rendering all beats |
| Compile | render once, compile once; full PROOF on the first compile (claims OCR, dense sweep, dark frames, sync vs Whisper, safe zones for the Short) |

## One dependency (not a script change)

B12 says "the build is linked below", and the description needs that link. **Where should it point?**
To the v2 zip, or to a repository you'll publish? Earlier weeks linked a repository.

## After the fixes

Re-run `script_to_sheet.py` → `gate_p_lint.py` → phonemize the changed lines → `make_read_sheet.py`,
then a Gate P delta read of B01, B02, B03, B05, B06 only.

## Fixes applied (2026-09-28, Tanmay: "go ahead and apply the fixes, link will go the repository")

All five are applied in SCRIPT.md (draft 2), plus B12 now says "the build's repository is linked below".
- Lint: no new BREATH or ECHO flags; +1 NAME (Devon in B01).
- The changed phrases were phonemized, and all are correct.
- 933 words, ~4:54.
- The repository link itself is added at the description stage.

**Gate P delta:** B01, B02, B03, B05, B06, B12, changed sentences only.

---

# PROOF review — the beat stills, before audio (2026-09-28)

Reviewed: the 13 end-state stills (`_preview/stills/`, rendered at 3840×2160) against FACTCHECK, the
script, GATE V's own analyser, and Tanmay's standing feedback from the topic video ("staring at the
same screen… viewers might become impatient").

**Verdict: fix before audio. 1 MAJOR (engagement), 2 MAJOR (accuracy/clarity), 3 MINOR.** None of it
touches the narration, so Gate P stands. All fixes are props or layout.

## Checks that passed

| Check | Result |
|---|---|
| GATE V analyser, full-res 4K stills | **13/13 clean** (no edge-bleed, underfill, low contrast) |
| Every quote on screen verbatim, with its source | B02 M1 ✓ · B03 M3 ✓ (the page's own dash) · B04 M5 ✓ · B05 M2 ✓ · B11 M8 ✓ |
| Every code result on screen is a live run | B05 (reconstruction labelled), B06, B07, B08, B11 ✓ |
| Reconstruction honesty | B01 badge **RECONSTRUCTION · EARLY VERSION**, source line "not the shipped code" ✓ |
| Receipt order matches "start at the bottom" | agent at the bottom; stamps fill upward, in narration order ✓ |
| Continuity | the same card, stamps accumulate beat to beat; B12's blank template keeps the same keys ✓ |
| Framing | boundaries read as design: "by design", "on purpose", "carried · not checked" ✓ |

## Findings

| # | Beat | Finding | Severity | Fix |
|---|---|---|---|---|
| 1 | all | **Same screen for 4:54.** Every beat is the same receipt-plus-panel layout. Stamps and panels change, but the frame never moves, which is exactly the pattern Tanmay flagged on the topic video | **MAJOR (attention)** | **(a) camera focus:** when a line comes into focus, the card eases in toward it (scale ≈1.12, the line centred), then settles back. **(b) live runs as a terminal:** in B05, B06, B08 and B11 the result rows *type in* as a real command and its output (the actual `python3` call and printed result, from the live runs), not a static table. **(c)** B03: a sweep runs bottom to top across the empty stamp column as "backwards" is said |
| 2 | B02 | Heading "Mastercard Agent Pay, **rebuilt** from public information" implies a replica; the README's own non-claims say it's an illustrative scaffold of its checks (and the narration says "a working version of its checks") | MAJOR (accuracy) | "**Agent Pay's checks, built from public information**" |
| 3 | B11 | The narration says "buy running shoes at a grocery store, and the receipt says the grocery store", but the card still shows the canonical receipt (`trailhead-running-co`); the grocery store is only in the side panel | MAJOR (clarity) | in B11, the card **becomes** that live receipt (`merchant: greenleaf-grocery`, `amount: 60.00`, the merchant line in focus with its open box) |
| 4 | B10 | "a tamper-resistant record **…** cryptographic proof of authorization" joins two separate sentences with an ellipsis | MINOR (quote hygiene) | two quoted fragments on two lines, one source |
| 5 | all | Smallest text: stamps, result reasons and the source line are ≈18px at 1080p (≈8pt on a phone in landscape). Fine on a TV; tight on a phone | MINOR (legibility) | stamps and reasons ×1.15; source line 0.019 |
| 6 | all | The card fills about two-thirds of the height, leaving an empty band above the source line | MINOR (layout) | absorbed by fix 1(a) and the ×1.15 type; recheck GATE V fill after |

**Order:** 1–6, then re-render the stills (end states, plus a mid-beat frame for the 1(a) and 1(b)
motion), then show Tanmay again, and only then audio.

## Stills fixes applied (2026-09-28, Tanmay: "go ahead and apply all six fixes")

| # | Fix | Verified |
|---|---|---|
| 1a | Camera focus: the card eases in toward the line under discussion (scale 1.07 about its left edge), holds, settles back, and again, more gently, when that line's stamp lands in a long beat. The panel gap is sized so it never reaches the panel | GATE V clean on every still; motion frames B05 @2s / @31.5s |
| 1b | Live runs as a terminal: B05, B06 (original build and v2), B08, B11 type a **real console transcript** (`live_runs.py`, `code.InteractiveConsole` inside each build copy), never hand-typed | transcripts match the live runs: `('REJECTED', 'agent_consumer_mismatch')`, `('COMPLETED', 'authorization_gate')`, `('ESCALATED', 'outside_timeframe')`, `('REJECTED', 'malformed_transaction_input')` ×2, `('COMPLETED', 'greenleaf-grocery')` |
| 1c | B03: a sweep runs bottom to top across the lines at "Backwards." | still |
| + | Found on the motion frames: B05 and B06 opened with an empty panel for 9–13s. They now open on "registered + verified ≠ yours" and on **Devon's rule** from the build's mock data (`household_staples`, limit 150.00, until 2026-12-31) | frames B05 @4s, B06 @4s |
| 2 | B02 heading: "Agent Pay's checks, built from public information" | still |
| 3 | B11: the card is the live grocery receipt (`greenleaf-grocery`, `60.00`), merchant line in focus | still |
| 4 | B10: two verbatim quote fragments (no ellipsis splice) | still |
| 5 | Stamps and reasons ×1.15, source 0.019, terminal 1.08u | — |
| 6 | The card's growth plus the larger type fill the frame more | GATE V fill: 13/13 clean |

---

# PROOF review — the 4K master (2026-09-28)

**File:** `read-the-receipt-backwards-final.mp4` · 3840×2160 · 24 fps · **4:31** (271.1s) · -15.0 LUFS /
-1.9 dBFS, LRA 3.0 · video = paced (MD5).

**Verdict: one batch fix, then clear-for-public.** The teaching and the evidence are complete (22/22).
The dense sweep found the one pattern the toolkit's own check can't see: four beats open with only the
receipt on screen, which fails the fill rule for their first few seconds. It's props only.

## Teaching rubric: **12/12**

| Criterion | Score | Evidence on the master |
|---|---:|---|
| Explicit framework | 2 | B03 states the move before any line is read; the sweep draws it |
| Reusable rubric | 2 | one question per line, earned vs carried; B12 hands it to the viewer |
| Worked example | 2 | six lines stamped live, each with its real run |
| Falsifiability / edge case | 2 | synonyms (B07), the gate's absent default (B09), the merchant open box (B11), the seal (B10) |
| Active task | 2 | B12: stamp every line of one record you own |
| Friction | 2 | B01's well-formed false receipt; B06 "the receipt looked perfect"; resolved in B10 |

## Production gate

| Check | Result |
|---|---|
| GATE V (compile, 26 frames) | 0 BLOCKER / 0 MAJOR |
| **Claims on screen at the moment of assertion** (`_qc/claims_at_assertion.py`, Whisper clock, OCR) | **22/22**: every quote, live result, stamp and label |
| **Dense sweep** (every 2% of every beat, 650 frames) | **52 underfill** in B01 (0–32%), B03 (0–42%), B09 (4–12%), B12 (4–26%): the right panel is still empty and the frame sits at exactly the 55% fill line. 1 low-contrast at B13 0.2s (the title's fade-in). 11 entrance frames |
| Dark frames (every frame) | 0 |
| Motion | the longest stretch with no visible change is 14.0s (B05, mid-story); the rest ≤11s. Frames with visible change: 19% of 0.5s samples |
| Audio | 11 gaps ≥0.6s, mean 0.92s, max 1.03s; per-beat loudness spread 1.0 LU |
| Words (Whisper) | no mispronunciations; the three TTS respellings are confirmed heard correctly |
| Framing / uniqueness | no gap/flaw/defect wording; no phrasing shared with W15–W23 |

## The fix (one batch, then recompile once)

Give each of the four beats an opening panel block from its first words:

| Beat | Opening block | Cue |
|---|---|---|
| B01 | note: "An early version of this build wrote this receipt." | "Here's a receipt" |
| B03 | note: "Start at the bottom. For every line: which step checked this?" | "So here's how I read it now" |
| B09 | the "two paths" chips, moved to the beat's first words | "The path line says" |
| B12 | chips: "a receipt · an approval · a line in a log" | "Take one record" |

Then re-render those 4 beats, recompile, re-run the dense sweep on those beats, and re-run the claims
check. B13's fade-in is the standard title entrance and is accepted.

## Fix applied (2026-09-28): **clear-for-public**

Opening blocks were added to B01, B03, B09 and B12 (B12 cued at "So try it", so it's on screen from 0s).
Only those four beats' props changed (diffed against the rendered sheet). They were re-rendered, then
recompiled once.
- **Dense sweep, the four beats:** 200 frames, **0 steady-state flags** (4 first-frame entrances,
  the fade-ins). Was 52.
- **GATE V:** 26 frames, 0/0. **Claims:** **22/22**. **Dark frames:** 0.
- **Master:** 4:31 · -15.0 LUFS / -1.9 dBFS · video = paced (MD5).

**Verdict: clear-for-public.** Teaching 12/12; production gate PASS.
