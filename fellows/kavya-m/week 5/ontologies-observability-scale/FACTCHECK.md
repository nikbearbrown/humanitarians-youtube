# FACTCHECK — Ontologies for Observability at Scale (Kavya)

Every claim mapped to its evidence, with an honest status on each.

## What kind of reel this is

An **original-argument explainer**, not a fact-check of a published source.
Adapted from `claude-liam-ontologies-observability-scale`, built earlier
this session under the house persona; content is identical, only the
on-screen presenter and branding changed.

## B00 — Cold open

- **"At ten services, everyone just knows what 'payment service' means. At
  a thousand, three teams tag three different things 'payments'"** — a
  framing claim about the general pattern of naming drift at scale, not a
  measured statistic from a specific system. Defensible as a widely
  observed pattern in distributed-systems practice, not a citation-backed
  number.

## B01 — BLUF

- No factual claim; states the reel's thesis.

## B02 — Framework

- **"Entity types, relationships, stable identifiers, a shared
  vocabulary"** — a standard decomposition of what an ontology/data model
  provides, consistent with documented patterns like OpenTelemetry's
  semantic conventions and resource/entity modeling. General industry
  knowledge, not tied to one citation.

## B03/B04 — Worked example (bad/good)

- **"payment-svc / PaymentService / payments" naming collision across
  three teams** — an AUTHORED ILLUSTRATIVE SCENARIO, not measured from an
  executed system. Clearly a worked example illustrating the mechanism,
  not a claimed real incident.
- **"svc_payment_core" canonical entity, resolving the graph to 3 of 3"**
  — same illustrative scenario, continued.

## B05 — Verdict

- Restates B02's framework and the illustrative example's outcome. The
  closing boundary line ("an ontology can't reason about a span that was
  never emitted") is the reel's own falsifiability statement — an honest
  limit on the claim, not an overclaim.

## B06 — Handoff

- No factual claim; a prompt for the viewer to apply the same method to
  their own telemetry.

## B07 — Outro

- No factual claim; "Made by — Kavya Mehta, narration: AI voice (Kokoro)"
  credit and disclosure card.

## Corrections & caveats applied during this build

- This reel's content is unchanged from the original `claude-liam-`
  version — only the presenter, branding, and the required
  intro/disclosure line were added. No new factual claims were introduced
  in the adaptation.
- GATE T: PASS, 8/8, on first run.
- This reel's landscape and vertical masters were recompiled at native 4K
  (`--height 2160` / `--height 3840`) after discovering that the default
  `compile.py --height` (720) had been silently used for every reel built
  earlier this session — see BUILD-LOG.md for the full account.
