# PEDAGOGY — The Tools I Built for Marley (hai claude explainer)

Explains three small business AI tools built for the Marley platform (Payment
Reminder Letter Generator, Business Email Writer, Product Description Writer),
the product problem they solve, and the shared architecture behind all three.
The episode's thesis: the AI writes, the person only decides — one structured
form, one tone choice, one output, never a chat-style refinement loop.

## Act structure

- B00 cold open with RESULT lines (ASK\u2192RESULT at B00) \u2713
- B01 executive summary beat (required for submission review) \u2713
- ILLUSTRATE LAW: Claude UI at B00/B16/B17 only. B02\u2013B14 illustrate the
  actual product (real screenshots of all three tools, real architecture
  diagram) \u2014 no UI wallpaper in the body \u2713
- Real screenshots (B04\u2013B13) show the actual live tools, not simulated or
  recreated interfaces \u2713
- Verdict card at B15 restates the four governing principles \u2713 \u00b7
  Handoff at B16 (architecture blueprint, not a Claude prompt \u2014
  a deliberate departure from the standard HANDOFF LAW composer pattern,
  made at the fellow's request since the takeaway here is the build pattern
  itself) \u00b7 Title-restate outro at B17 \u2713

## Evidence discipline (source: "Payment Reminder Letter Generator — Software Design Document," Shivpriya Amarsinh Mane, April 22, 2026)

| Claim | Source | Verdict |
|---|---|---|
| Sarah scenario: freelance designer, $2,000 logo project, 45 days overdue, 30 minutes agonizing over tone | SDD Section 1, Problem Summary | OK — verbatim scenario from source |
| "One Decision, One Output" / "Prompt is the Product" / "Zero Friction to Copy-Paste" / "Graceful Failure Over Silent Failure" \u2014 four named architecture principles | SDD Section 2, Architecture Principles | OK — exact principle names preserved |
| Payment Reminder Generator: seven fields, three tones (Polite/Firm/Final Notice) | SDD Section 5, Component 1 / Evidence A | OK |
| Business Email Writer: six email types, four tones (Professional/Friendly/Direct/Formal) | SDD Evidence B, Section 5 | OK |
| Product Description Writer: six platforms (Website/Amazon/Etsy/Instagram/Shopify/eBay), three writing styles | SDD Evidence C, Section 5 | OK |
| Architecture: Next.js API route (`/api/generate`), API key never enters client bundle, locked/versioned prompt instruction sets per tone | SDD Section 3 (Integration Flow), Section 5 (Component 3, Component 4) | OK |
| Screenshots (B04\u2013B13) are the fellow's own tool interface, demo input, and generated output, as submitted in SDD Part 3 (Live Tool Evidence) | SDD Part 3 | OK — real, unedited screenshots |

## Friction protected

- Kept: all three tools shown with real intro/demo/output screenshots each —
  proportional coverage since the source treats them as equally-weighted
  deliverables
- Excluded: SDD Part 4 (Future Scope / roadmap) and Part 5 (post-submission
  meeting notes) — out of scope per fellow's instruction; this episode covers
  only the three tools as built and evidenced, not planned future work
- Handoff (B16) deliberately departs from the standard Claude-prompt HANDOFF
  LAW pattern — shows the architecture blueprint instead, since the episode's
  takeaway is a reusable build pattern rather than a single prompt to try

VERDICT: PASS
