# Explainer — Semantic Normalization & Regex Parsing

**Week:** 05 Oct – 11 Oct 2026
**Type:** Work update

- **Drive:** https://drive.google.com/drive/folders/1VfQRD7kWi1mjLO2n1G0dck0f-RBlQaNv

## What it covers
How the Provenance Gatekeeper was upgraded from brittle strict-string matching to robust mathematical evaluation by implementing a regex parsing layer to extract floats from probabilistic AI text.

## Why this topic, this week
Strict string matching causes false positives. If the ground truth is `5000000` and the model outputs `$5.0M`, the system previously failed it as a hallucination. This week solved that by teaching the application to deterministically sanitize and convert stylistic formatting into standardized floats before performing magnitude checks.

## Limits
- Source files for the video: see the Drive folder.