# Self-Assessment against PROOF.md — "How Facial Recognition Actually Works (And When It Shouldn't)"

Scored against **PROOF.md's** own two artifacts: **THE RUBRIC — Does this explainer
actually teach?** (six criteria, 0–2 each, /12) and **THE PRODUCTION GATE** (binary,
can veto publish regardless of teaching score). This is a self-review of the
2026-08-25 rebuilt master (12 beats, 3840x2160, 185.17s) — done by watching the
actual rendered frames (`_qc/REPORT.md`, direct `ffmpeg` frame extraction at each
beat's 50%/85% marks, and `qc-sheet.png`), not by re-reading the script. Per
PROOF's own core principle ("if you can't see it, ask for the frame — don't infer
a pass or a fail"), every score below cites the specific beat and what's actually
on screen, not what the beat sheet claims it shows.

This assessment is about the **teaching/production rubric only**. The video's
central factual claim (NIST FRVT demographic-effects data) is already verified
in `FACTCHECK.md`/`SOURCES.md` against NISTIR 8280 directly — that verification
is not repeated here.

## Rubric

| Criterion | Score /2 | Evidence |
|---|---|---|
| **Explicit framework** | **2** | B03 (`The lens`) shows the 3-question framework ("What's it used for? / What happens if it's wrong? / How confident is the claim, really?") as a numbered, on-screen structure, immediately after the B02 hook and *before* any example beat (B05 onward). This is the framework-first fix already logged in this reel's 2026-08-05 PROOF review (see PEDAGOGY.md) — confirmed still true in the rebuilt beat order (B03 sits at position 4 of 12, ahead of every example). |
| **Reusable rubric** | **2** | The same 3 questions recur verbatim in B03 (introduced), B04 (tagged "Q3: how confident?" on the mechanism beat), B09 (applied to the retail case), and B10 (handed to the viewer as a checklist). A viewer who watches once has the literal axes to score a fifth case — not just the topic. |
| **Worked example** | **2** | B09 (`One real case: retail loss prevention`) walks the three questions against a concrete case live, on screen, in sequence — "Used for? → Catching theft, scanning every shopper, no consent" / "If wrong? → Innocent shopper flagged, maybe banned, never told why" / "How confident? → Vendor claims '99% accurate' — the same fluency trap" — ending on a stated verdict ("Three high-stakes answers — needs real scrutiny"). This is the *reasoning step*, not just a conclusion card. |
| **Falsifiability / edge case** | **1** | Partial credit, not full. B07 (NIST evidence) does complicate a clean "facial recognition is biased" narrative — the same evidence shows a real gap for most algorithms AND a near-zero gap for the best-performing ones AND a named industry-aligned dissent (Security Industry Association) — so the video does resist an easy one-sided read. But that is friction *in the evidence*, not a stress-test *of the 3-question framework itself*. Nothing in this cut shows a case where the three axes disagree with each other, or a case that looks low-stakes on one axis and high-stakes on another (the PROOF definition of the real falsifiability test: "an example that fits more than one axis, or none"). B05/B06/B09 all resolve cleanly to one bucket each — the one-per-example tell PROOF explicitly warns about. **Gap, honestly named**: this framework has not been tested against a case that breaks it. |
| **Active task** | **2** | B10 (`YOUR TURN`) hands over the literal 3-question checklist as an on-screen template ("Pick one AI system you used this week" + the three boxed questions + the decision rule "Low-stakes on all three? Let it go. High-stakes on any? Scrutinize it."). This is a scaffold the viewer can run, not "ask an AI to explain it" — passes PROOF's explicit CTA test. |
| **Friction** | **1** | The industry dissent in B07 is real, kept-in friction (the fact-check discipline in FACTCHECK.md explicitly notes this was "kept... even though it complicates an otherwise-clean narrative"). But the video *narrates* that tension to the viewer rather than making the viewer *resolve* it — B10's task is "apply the 3 questions to your own case," not "decide whether NIST or the Security Industry Association has the better read of the same data." The ambiguity is shown; the viewer is not asked to do anything with that specific ambiguity. Partial credit only. |

**Total: 10/12** — clears PROOF's ship-bar teaching threshold (≥8/12).

## Production gate (binary)

| Check | Verdict | Evidence |
|---|---|---|
| **Evidence legible at the moment of assertion** | **PASS** (after one fix) | Direct frame extraction from the true clean master at every GATE V sample point (50%/85% of each beat) found one real failure: B04's caption ("A 98% match is a probability, not a certainty.") landed a `Write()` letter-trace animation exactly across the beat's native 50% mark — the frame at that instant showed a half-drawn, overlapping-looking glyph mess, i.e. the claim's own receipt was illegible at the moment it mattered. Fixed 2026-08-25 (swapped to a whole-string `FadeIn` and re-timed the build-up so the caption is fully settled ~0.2s before the halfway mark) and reconfirmed clean by re-extracting the same frame post-fix. All other beats' claim artifacts (the pipeline diagram, the low/high-stakes lists, the NIST bar chart, the fluency-trap panels, the worked-example rows) were legible at both sample points on direct inspection. |
| **Sources on screen, not just voiced** | **PASS** | B07 names the source directly on screen — "NIST FRVT — Demographic Effects (2019)" + "189 algorithms · 18.27 million images" in a citation line, plus the dissent explicitly attributed on screen to "Security Industry Association," not paraphrased as "some critics." B04's "98% match" is illustrative and explicitly *not* attributed to a vendor (FACTCHECK.md #2) — correctly not carrying a source card, since it isn't a sourced claim. |
| **Side-by-side at the moment of comparison** | **PASS** | B07 holds the "Most algorithms" (real gap) and "Best-performing algorithms" (near-zero gap) bars on screen together for the beat's full ~9s hold. B08 holds "a fluent paragraph" and "a match score" side by side for ~6s under the shared caption "Both are a probability — not a fact." Both satisfy PROOF's ≥2s side-by-side requirement. |

**Production gate: PASS.**

## GATE V (frame-level QC) findings, for context

0 BLOCKER, 12 MAJOR on the true clean master (`2026-07-27-how-facial-recognition-actually-works.mp4`, not the watermarked `-slate.mp4`, which carries a known false-positive edge-bleed from its timecode burn-in). All 12 were reviewed by eye against actual extracted frames, not accepted on the automated report alone:

- **B02_50/85, B04_50/85 — `low-contrast`**: the checker's whole-frame luminance-average heuristic flags these (0.17 and 0.22, threshold 0.30). Direct WCAG computation on the actual palette says otherwise: ink (#2F2A26) on cream (#F3EBDD) is **11.99:1** contrast — nearly 3x the AAA bar. This is the same documented false-positive class as the sibling reel's build (whole-frame average penalizes a mostly-cream canvas with a small area of dark text, not the text's own legibility). Confirmed legible by eye.
- **B01_50/85 (41%), B05_50/85 (34%), B06_50/85 (33%), B11_50/85 (6%) — `underfill`**: all four are beats designed to be sparse and centered by intent — B01 is a personal-intro card, B05/B06 are short 3-4 item lists with room to breathe, B11 is a deliberately compact brand outro (matching this fellow's other reels' outro style). None read as an accident or an unfinished frame on direct inspection.

**One real, new-to-this-rebuild defect was found and fixed** (the B04 mid-write glyph-trace above) — everything else in this list is cosmetic, matching the standard this fellow's other reels have shipped under.

## Verdict

Per PROOF's ship rule ("public requires teaching ≥ 8/12 AND the production gate PASS
AND the video passes its own standard"): **10/12 teaching, production gate PASS** —
this cut would clear PROOF's own bar for public.

That is **not** the same as this project's own publish authorization, which is a
separate, human fellowship sign-off — `beat_sheet.json` → `metadata.gates.publish`
remains **NOT AUTHORIZED**, unchanged by this rebuild, per README.md's production
state.

## Named gap for a future pass (not fixed in this rebuild — out of scope for a
resolution/beat-count program-feedback rebuild, logged honestly rather than
silently left out)

The framework has never been shown failing or straining. A real falsifiability
beat would need a case where the three questions don't cleanly agree — e.g. a
low-stakes *use* (unlocking your own phone) run through a high-stakes *deployment*
(a landlord requiring it for building access) — to prove the axes are doing real
work rather than three labels that happen to map one-per-example onto the cases
already chosen. [EDIT]-tier if added as a beat swap on the existing B05/B06 pair;
[RESHOOT/NEW SOURCE]-tier if it requires new evidence to source the edge case
honestly.
