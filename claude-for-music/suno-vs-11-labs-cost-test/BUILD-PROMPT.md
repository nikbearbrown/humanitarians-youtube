# BUILD-PROMPT — Suno vs 11 Labs Cost Test

Video for the "Brutalist — Claude for Video Production" playlist on @HumanitariansAI.
Meta, like the rest: THE VIDEO IS THE EXPERIMENT. Its own narration gets voiced
BOTH ways — once through ElevenLabs (`generate_audio.py`), once through the Suno
path (`./art suno` → human generates in Suno with Bear's uploaded voice → vocal-only
stem into pantry/ → `./art suno-slice`) — and the honest numbers become the video.

Standing rules #1–#4 (EXAMPLES-CAMPAIGN.md) apply. Read the docstrings of
runtime/scripts/suno_export.py and runtime/scripts/suno_slice.py first — they ARE
the spec for the Suno path.

## Phase A — the experiment (before any script writing)

1. `./art keys` (free) — record ElevenLabs credit balance BEFORE.
2. Write the beat sheet for THIS video (script → beats per the house flow; the
   narrative arc is the comparison itself: the itch — 11 Labs is getting
   expensive; the two paths; the numbers; the verdict).
3. GATE P, then voice the sheet BOTH ways:
   a. ElevenLabs: python3 runtime/scripts/generate_audio.py <this reel>
      → record credits consumed (./art keys AFTER), wall time, # of API calls.
   b. Suno: ./art suno <this reel> → the HUMAN pastes each .suno.N.txt into Suno
      (style "spoken word", Bear's voice), downloads the VOCAL-ONLY stems into
      pantry/ → ./art suno-slice <this reel>
      → record Suno credits used, wall time, # of human steps, and any
      segmentation retries (--silence-db / --min-gap values that worked).
4. Log EVERYTHING in COST-LOG.md: cost per finished narration minute for each
   engine, quality notes (Suno's speak-sing tendency vs clarity; ElevenLabs
   consistency), where each engine wins. Honest record — no thumb on the scale.

## Phase B — the video

5. Author docs/suno-vs-11-labs-cost-test.md FROM COST-LOG.md (the honest record,
   same voice as docs/posting-to-youtube.md).
6. Choose the take that ships (human decides which voice narrates the final cut —
   that choice is itself content for the verdict beat).
7. Build per the house flow: manim cost-table graphic (real numbers), Onda
   terminal beats showing both command flows, hero beat on the split (the machine
   voices every beat; you choose whose voice ships). Render, ./art run, QC by
   looking, ./art final (master staged AFTER final — symlink convention).
8. Captions (<slug>.srt from the sheet), publish unlisted to the Brutalist
   playlist with chapter_number = next in sequence. Log to PUBLISH-LOG.md.
