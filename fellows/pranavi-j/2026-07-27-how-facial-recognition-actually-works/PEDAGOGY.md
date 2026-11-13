# PEDAGOGY — How Facial Recognition Actually Works (And When It Shouldn't)

Single-topic `ai-explainer` reel (3-minute cap, not deep-explainer — content
was scoped down from an original 5-minute deep-explainer brief to fit the
tighter format). Audience: general public interested in AI policy and
technology, not a technical audience. Thesis: facial recognition is neither
good nor bad — it's a probability estimate, and the scrutiny it deserves
should scale with what's at stake in the decision it feeds.

## Act structure

Renumbered 2026-08-25 per program feedback (4K rebuild + 2 new opening beats).
All 10 beats below are unchanged in content from the 2026-08-05 restructure —
only their `B0N` IDs shifted by 2 to make room for B00/B01.

- B00 TITLE (NEW) — silent title card: video title + @HumanitariansAI, no narration
- B01 INTRO (NEW) — spoken personal-intro card: fellow's name + one-line thesis summary
- B02 HOOK — frames the topic as current and actively debated, not settled ✓
- B03 FRAMEWORK — the reusable lens (3 questions), shown before any example ✓
- B04 MECHANISM — the actual pipeline (detect -> embed -> compare -> score), correcting the "yes/no match" misconception before taking any side ✓
- B05 BENEFITS — legitimate uses, stated plainly and first ✓
- B06 HARMS — harmful uses, stated with equal directness, right after ✓
- B07 EVIDENCE — the NIST FRVT data: real gap for most systems, near-zero gap for the best, an industry-aligned dissenting view named directly — all three in one beat, not spread out to bury any of them ✓
- B08 FRAMEWORK-CALLBACK — connects to the fellow's "fluency trap" framing: a precise number isn't a certainty ✓
- B09 WORKED-EXAMPLE — the lens applied live to a retail loss-prevention case ✓
- B10 CTA — a real scaffolded viewer task, not a vague pointer ✓
- B11 SIGN-OFF — channel/fellow credit ✓

## Self-assessment against PROOF.md (2026-08-25/26 rebuild)

A full scoring of this rebuilt master against **PROOF.md's** own six-criterion
teaching rubric (/12) and its binary Production Gate lives in
`SELF-ASSESSMENT.md`, not duplicated here — short version: **10/12** teaching
(explicit framework 2, reusable rubric 2, worked example 2, falsifiability/
edge case 1, active task 2, friction 1) and Production Gate **PASS** (one real
legibility defect found by direct frame inspection — B04's caption animation
straddling a QC sample point — and fixed before this score was taken). The
named gap: the 3-question framework has never been tested against a case that
breaks it (every example resolves cleanly to one stakes-bucket) — logged as a
future punch-list item, not fixed in this rebuild.

One thesis, evidence for both the harm and the benefit sides, one non-partisan
takeaway — matches the "balanced and explanatory, not advocating a single
policy position" brief.

## Evidence discipline (source: FACTCHECK.md, verified 2026-08-03 against NISTIR 8280 directly, BEFORE narration was locked)
| Claim | Verdict |
|---|---|
| 189 algorithms / 18M+ images | PASS |
| Real demographic gap for most algorithms | PASS |
| Near-zero gap for best-performing algorithms | PASS |
| Industry-aligned dissent named and cited | PASS |
| No policy verdict asserted | PASS (by design) |

## Compliance
Narration is first-person ("I"), attributed to the fellow by name in the
sign-off beat (B07: "in for Sai Pranavi J.") — per the fellowship's
explicit requirement that reports demonstrably come from the volunteer, not
a generic persona.

## Friction protected
- Kept: the industry-dissent sentence in B04, even though it complicates a
  otherwise-clean "NIST found bias" narrative — cutting it would have made
  the video less balanced than the brief required.
- Deliberately excluded: naming any specific vendor/product, and any
  numeric claim not directly traceable to NISTIR 8280.

VERDICT: PASS
