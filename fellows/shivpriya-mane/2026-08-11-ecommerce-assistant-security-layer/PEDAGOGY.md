# PEDAGOGY — The Security Layer Behind My Smart E-Commerce Assistant (hai claude explainer)

Explains the real security architecture built into a Smart E-Commerce Assistant
(AI-powered listing analysis tool). The episode's thesis: no single check is
enough — the system layers structural validation, AI moderation, pattern
detection, structural isolation, and output validation, and fails closed
whenever it can't verify something.

## Act structure

- B00 cold open with RESULT lines (ASK→RESULT at B00) ✓
- B01 executive summary beat (required for submission review) ✓
- ILLUSTRATE LAW: Claude UI at B00/B11/B12 only. B02–B10 illustrate the
  project's actual mechanism (SourceFlow, ChipGrid, LayerStack, real code,
  real demo footage) — no UI wallpaper in the body ✓
- PROOF beats (B05, B07) carry real demo footage of the two threats being
  blocked live — not simulated or narrated only ✓
- Verdict card at B10 restates the three governing principles ✓ ·
  Handoff "Your turn." at B11 ✓ · Title-restate outro at B12 ✓

## Evidence discipline (source: user-provided project write-up, "Smart E-Commerce Assistant" security documentation)

| Claim | Source | Verdict |
|---|---|---|
| Image validation: 10MB limit, resolution/dimension caps, format whitelist, PIL verify | Project doc, "Stage 1: Structural validation" | OK |
| AI content moderation via GPT-4o-mini after structural checks pass | Project doc, "Stage 2: AI content moderation" | OK |
| Prompt injection defense: regex blocklists (6 categories) + XML-style isolation + secured system prompt + output validation | Project doc, "Threat #2: Prompt Injection"; `backend/security.py` CRITICAL_PATTERNS (verified directly in source) | OK |
| XML isolation lives in `build_review_prompt()` / `human_template`, `backend/reviews.py` | User-confirmed source location | OK |
| Code shown on screen (B09) is the real, unmodified `CRITICAL_PATTERNS` block | Copied verbatim via `sed` from `backend/security.py` lines 323–357 | OK — verbatim quote law satisfied |
| Demo footage (B05, B07) shows actual blocked attempts, not simulated/recreated | User-recorded project demo clips | OK |
| Three governing principles: defense in depth, fail closed, never trust input | Project doc, "The Core Security Philosophy" | OK |

## Friction protected

- Kept: both PROOF beats (B05, B07) — real evidence outweighs narrating the
  same claim a third time
- Compressed: threats #3 (bad input data), #4 (rate limiting), #5 (error
  leakage) from the source doc are not covered as standalone beats — the
  reel focuses on the two highest-severity, most visually demonstrable
  threats (image safety, prompt injection) to stay under the Shorts length
  limit; full detail remains in the project's own documentation
- Corrected during drafting: removed an early claim that better listings
  directly improve "search ranking" (unverifiable) in favor of "listing
  quality" and "reduced avoidable returns," per user correction

VERDICT: PASS
