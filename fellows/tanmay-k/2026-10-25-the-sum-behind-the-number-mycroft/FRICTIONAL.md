# Frictional Log — the-sum-behind-the-number (Week 28 work video)

**Record provenance:** drafted 2026-10-25 with Claude from this folder's own records (`ANGLE.md`, `FACTCHECK.md`, the proof
reviews, `GATE-P-LINT.md`, the video gates), after the work was done rather than while it happened. **Awaiting Tanmay's
review.** Every entry points at the record it comes from.

## 2026-10-25 — An angle that is new

- **Work and expectation:** an angle that does not repeat the earlier Mycroft contribution films (parity and rounding, hand-offs
  taken on trust, weighted votes and the AI's briefing), and shows nothing negatively.
- **Where it resisted:** three earlier films sit close to anything about a pipeline's parts and checks.
- **What was done:** every work-video narration file for Weeks 17–27 (70 files) was searched for the idea's words; none had it.
  The angle, a stress-test number as a sum that can be taken apart, was chosen with a standing instruction to reframe
  anything that could read negatively. The workflow's own README, which prints the same sum as its worked example, is credited
  on screen.
- **Decided by:** Tanmay chose the angle and set the framing rule.
- **Record:** `ANGLE.md`.

## 2026-10-25 — A Short that needed more context

- **Work and expectation:** a Short that carries its context and does not feel rushed.
- **Where it resisted:** the first draft used terms it had not defined ("Mycroft", "named shocks", "the AI list") and packed the
  shares and the arithmetic into one line.
- **What was done:** rewritten as 8 lines, one idea each, with the arithmetic spread over three lines; the narration was then
  measured and a 0.85–1.0 s dead-air gap between lines was trimmed to 0.4 s.
- **Record:** `PROOF-REVIEW-SHORT*.md`, `SHORT-SCRIPT.md`.

## 2026-10-25 — Checks that found what a read could not

- **Work and expectation:** each check catches what the one before cannot see.
- **Where it resisted, and what caught it:**
  - 21 sentences under five words and the word "weight" (heard as "wait") were caught by the Gate P lint.
  - Chips running into a bar outline in the Short were spotted by Tanmay; an overlap check now covers both formats and found
    21 more collisions in the moving parts, all fixed.
  - Block numbers overlapping blocks still growing, a disclaimer static for 7 s, and labels arriving before their words were
    found at low resolution before the full-size render.
- **What was done:** each was fixed and the gate re-run; the Short passes 11/11 and the long film's measured gate passes.
- **Record:** `GATE-P-LINT.md`, `PROOF-REVIEW-RENDERED.md`, `VIDEO-GATE-LONG.md`, `VIDEO-GATE-SHORT.md`.

## 2026-10-25 — Rendering without saturating the machine

- **Work and expectation:** two 4K renders.
- **Where it resisted:** the last renders ran two jobs at 8 workers each on a 6-core machine and needed re-renders.
- **What was done:** both films were checked at quarter size first and rendered at full size once, at 3 workers each. A
  leftover diagnostic process from an earlier build was found and closed.
- **Record:** this entry.
