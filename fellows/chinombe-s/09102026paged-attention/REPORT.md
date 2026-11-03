# Explainer — Paged Attention

**Week:** 14–18 Sep 2026
**Type:** STEM / AI explainer

- **Video:** https://www.youtube.com/watch?v=0rRC3kx5Jd8&t=4s
- **Drive:** https://drive.google.com/drive/folders/1CY_suzRRK4f05C5OeNKXm-5Bw6Ynhv1H?usp=sharing
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)

## What it covers

How vLLM borrows virtual-memory paging from operating systems to stop the KV
cache wasting GPU memory on reserved-but-unused space, and why that raises how
many requests a server can hold at once.

## Why this topic, this week

The same week's project work hit a hard ceiling that comes from exactly this
constraint: the strong tier's account cap of 1000 output tokens per minute made
every call fail until the token budget was lowered. Serving limits are not
arbitrary  they follow from how memory is allocated per request, which is what
paged attention addresses.

