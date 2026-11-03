# Explainer — KV Cache

**Week:** 31 Aug – 4 Sep 2026
**Type:** STEM / AI explainer

- **Video:** not uploaded
- **Drive:** https://drive.google.com/drive/folders/1-H-vE7c3x-pJmIU_Jw5rjhPBydSJfA8q

## What it covers

Why a transformer caches the key and value tensors it has already computed, and
what that cache costs in memory as a conversation grows.

## Why this topic, this week

The same week's project work measured live model calls for the first time and
found that cost follows **how much a model chooses to say**, not the rate card.
The KV cache is the mechanism underneath that: output tokens are expensive
because each one is generated sequentially against a growing cache, while input
tokens are processed in one pass.

