# Frictional log — Backpropagation, One Error at a Time

## 2026-11-22 — the chain rule on real numbers, and an accent the contrast gate misread

- **Drive:** https://drive.google.com/drive/folders/1zudlUZG4n6vUShgp1M1VU1pwPly0YjMR
- **Video:** `exports/landscape/claude-liam-backpropagation.mp4` (3:17)

**What I was working on.** The second film in the STEM series, the sequel to *Gradient Descent, One Step at a Time*. I chose backpropagation from the topics Claude proposed, because film 1 named it in its scale beat. It was built in the ai-explainer format from the start, with the greeting "Hola, Liam". I directed the work in Claude Code; Claude wrote and built the film with the brutalist.art toolkit.

**What I tried, and what I expected.**

- I expected film 1's lessons to carry over, so Claude planned the scenes around them before writing any code: stub-safe code for GATE A's isolated pre-flight, a clock counted in frames (ceil(run_time·fps)), box spotlights instead of underlines, at least 55% canvas fill for GATE V, and text kept within ±6.0 x / ±3.2 y.
- I expected about 3.0 min of narration, estimated at the film-1 Kokoro rate of 3.5 words/s.
- I expected the toolkit's `lead_silence_s`/`tail_silence_s` fields to add the pauses at the start and end of beats.
- I expected Kokoro to say "tanh" and "backpropagation" correctly.

**Where it resisted, and what I did next.**

- **Kokoro read "tanh" as "tan".** Claude pinned it to /tæntʃ/ in `metadata.pronounce`.
- **Whisper heard "backpropagation" as "back repugation".** Claude pinned it to /bˌækpɹˌɑːpəɡˈeɪʃən/ and regenerated the affected beats.
- **The toolkit ignores** `lead_silence_s`**/**`tail_silence_s`**.** Claude padded the audio directly with `stem-films/tools/pad_silence.py` (B01 +0.8 s lead, BVDT +0.5 s lead, BOUT +1.0 s tail), then ran `align.py`.
- **GATE V still flagged underfill**, despite the plan. Claude shortened B01's on-screen correction to "tests every weight" → "sends the error backward" at type 160, with the narration unchanged; made B02 ghost its full layout from t = 0.2; and made B06 show its cost-row labels early.
- **GATE T §8.3 read terracotta arrow tips in B05 as low-contrast accent text.** It was a false positive. Claude changed the accent, not the gate: arrows and labels are now ink, and terracotta stays only on box outlines, B02's frame, B03's brace and the filled bars in B06/B07.

**What Claude contributed, and what I did with it.**

- **Script and evidence:** Claude wrote the 11-beat narration and `demo/bp_demo.py`, ran it, and read every on-screen number from `demo/evidence.json`. Its fact check marked two claims "minor" and kept the wording honest.
- **Build and QC:** Claude wrote the six Manim scenes, generated the Kokoro audio, rendered, fixed the gate failures above and ran the checks: GATE V clean, GATE T PASS, `check_no_labels` PASS (98 samples, no footer strip), `master_check` PASS, loudness −24.63 LUFS / −3.12 dBTP.
- **My part:** I chose the topic, approved the narration, set the rule that no delivered video carries a "B0x REMOTION" footer or bottom strip, and reviewed the result.
- Accepted:
    - **The narration as drafted, all 11 beats.** I approved it at GATE P in chat with "Approve, build it".
    - **The two "minor" qualifiers** (FACTCHECK #9 and #12): "Backprop needs one" pass is a simplification of a backward pass's cost, and vanishing gradients are "one reason", not "the reason", deep nets moved to ReLU.
- Rejected: none recorded.

**What I understand now, and what I still do not.**

- Understood:
    - Backprop multiplies local slopes along the path: 1.4485 × 2 × 0.7864 × 1 = 2.2783. Central differences agree to |Δ| = 2.68e-10, but cost 2 passes per weight.
    - Ten sigmoid layers each multiply the gradient by about 0.22, so it reaches the first layer at 3.483e-7.
    - A gate can fire for the wrong reason. Here the honest fix was to change the colour choices, not to loosen the gate.
    - Planning from film 1's lessons did not remove GATE V underfill; fill was still fixed beat by beat.
- Not understood / not verified:
    - The locked `ClaudeTitleOutro` still wraps the title as "…at a / Time.", as in film 1. Not fixed.
    - `master_check` skipped its clock check because `clock_check.py` is missing from the toolkit.
    - GATE T's §8.10 advisory (BVDT narration recites the card, 0.91) was left as is; it does not block the cut.
    - Not published. The Drive copy is still the labelled review cut.
