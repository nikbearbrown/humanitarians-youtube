# PROMPTS — kavya-ai-junk-data-gate

There are no open media slots. This file records the prompts that shaped the film.

## P0 — the request (2026-10-29)

> Half the Data Is Fake: Catching AI Junk Before It Hits Your Pipeline. Create a video for this topic like
> you did for other topics; make sure about the submission requirements.

## B00 — cold-open composer prompt (on screen)

> Half of a rider-feedback batch is junk: copied comments, impossible values, rows with no source. Loaded
> straight in, the average rating looks great. What should check a batch before it reaches my pipeline?

## B03 / B04 — the commands actually run (on screen)

```bash
python junk_gate_demo.py ungated
python junk_gate_demo.py gated
```

## B07 — the viewer's Your Turn prompt (on screen and read aloud)

> Look at one batch my pipeline ingested this week. Which rows have no source, impossible values, or
> near-duplicate text? Draft the checks that should quarantine them before they load.

## AI generation in this film

| What | Tool |
|---|---|
| Narration audio | Kokoro TTS `am_onyx`, local (synthetic voice, disclosed in B00 and B08) |
| Script / beat sheet | Drafted by Kavya Mehta with help from Claude Code |
| Demo script `junk_gate_demo.py` | Written with Claude Code; the output is real execution |
| Visuals | Remotion compositions in this repo; no image or video generation model |
