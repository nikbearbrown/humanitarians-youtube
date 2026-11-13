# Frictional Log — Why AWS Bedrock Exists

> Append dated entries as you go; never rewrite an earlier one.

## 2026-10-03 — Build a 60-second explainer on why Amazon Bedrock exists, in 16:9 and 9:16

*Drafted with Claude Code from the build record and reviewed by me.*

- **What I tried, and what I expected:**
  I expected the story to be "a model from AWS". I wanted the API calls on screen to be real, so the SDK was run offline to show the actual call shape without spending anything.

- **Where it resisted, and what I did next:**
  The first draft ran about 71 seconds and was trimmed twice. The docs corrected a few of my assumptions: "one API" still has model-specific parameters, and "no servers" doesn't mean free. The outro voice slurred "A I", so it was changed to "AI".

- **What Claude or another person contributed — and what I accepted, changed, or rejected:**
  Claude Code drafted the beat sheet, wrote the scenes, checked the claims against the AWS docs, ran the SDK for the evidence, and fixed layout issues. I accepted softening the "one API" and "no servers" claims, and kept "AWS Bedrock" in the narration because that's what people search for.

- **What I understand now, and what I still do not:**
  I understand Bedrock is a managed layer over many models, not a model itself. I haven't run real requests through it yet.

- **Evidence:** [beat sheet](beat_sheet.json) · [vertical beat sheet](vertical/beat_sheet.json) · [build log](BUILD-LOG.md) · [fact-check](FACTCHECK.md) · [evidence](evidence/)
