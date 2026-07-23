# Chapter 2 — The Beat Sheet

## Overview

If the two laws are the constitution, `beat_sheet.json` is the country they govern. It is a single JSON file that describes a video as an ordered list of **beats**, where the rule — memorize it — is that **one beat = one narrated unit = one visual.** One line of narration, one thing on screen while it's spoken. A reel of forty scenes is forty beats; a lecture of forty-seven slides is forty-seven beats.

Every tool in the system speaks this file. The segmenter writes it; the audio generator adds measured durations to it; the caption aligner reads its narration and writes timing back; the renderer consumes the whole thing. This is not an accident of convenience — it is *why the parts compose*. Because there is one schema, a text-to-speech script written for sketch videos narrates a lecture with no adapter, and lyric-alignment code written for music videos aligns lecture captions with no adapter. Learn this file and you can read any Unreal Reels project.

## The fields that carry the whole pipeline

A beat from a real lecture (Chapter 7's fairness lecture, forty-seven beats) looks like this, trimmed:

```json
{
  "beat_id": "S01",
  "label": "Title",
  "speaker_notes": "Chapter 7. Three reasonable definitions of fairness…",
  "on_slide_text": "AI Engineering · Chapter 07 · Fairness metrics…",
  "visual_mode": "doodle",
  "narration_text": "Welcome to Chapter 7. Today is about a problem that…",
  "tts_normalized_text": "Welcome to Chapter 7. Today is about a problem that…",
  "actual_duration_s": "24.08",
  "audio_file": "mp3/beat-S01.mp3"
}
```

Two fields carry the entire pipeline and are never placeholders. **`beat_id`** is the beat's identity — the handle you use to say "re-record S07" or "the figure on S12 overflows." **`narration_text`** is the spoken line: the seed from which audio, captions, and timing all grow. A blank `narration_text` is a silent beat; it is the one field you can never leave empty.

The rest earn their place:

- **`speaker_notes`** — the source seed the narration was *expanded from* (for lectures, the slide's own notes). It is the raw material; `narration_text` is the finished spoken voice.
- **`on_slide_text`** — what is literally printed on screen. It exists so the pipeline can check that the narration *discusses* the slide rather than *reading* it aloud (Chapter 7).
- **`visual_mode`** — how this beat is shown: a live chart, a progressive figure, a drawn doodle, animated bullets, a video clip. This is the beat's picture decision.
- **`actual_duration_s`** — the measured length of the spoken audio. This is Law 1 made concrete: written by the audio step, read by everything after. It is *measured*, not estimated.
- **`audio_file`** — the path to this beat's rendered narration.
- **`tts_normalized_text`** — a subtle but important one. It holds the narration with pronunciation fixes applied ("muh-LYE-nuh-thun" for a hard surname) so the voice model says it correctly. The captions still display the correctly-*spelled* `narration_text`; only the speech engine sees the respelling. Display text and spoken text are kept separate on purpose.

At the top of the file, a `metadata` block holds project-wide settings — the voice id, frames per second, tail padding between beats, the source deck. One place, not scattered per beat.

## Why measured, not estimated

Notice `actual_duration_s` is a real number with two decimals, not a round guess. That is the master clock. The audio step measures each clip and writes the true duration back; the renderer turns it into an exact frame count. If you ever see durations that look estimated — every beat suspiciously round — something has bypassed the clock, and the video will drift.

## Worked example — add a beat, re-derive timing

Say a lecture's beat sheet has S06 and S07, and you want a new transitional beat between them. You insert a beat object with `beat_id: "S06b"`, a `label`, a `visual_mode`, and — the one field that matters — a real `narration_text`. You leave `actual_duration_s` and `audio_file` empty. You run the audio step for just that beat; it generates the clip, measures it (say 7.3 seconds), and writes both fields back. The renderer now slots a 7.3-second beat between S06 and S07 and pushes everything after it later by 7.3 seconds. You wrote one line of narration and one small JSON object; the clock did the rest.

## Exercises

**Exercise 2.1 — Read a real beat sheet.** Open any project's `beat_sheet.json` and answer: how many beats, what is the total measured runtime (sum the `actual_duration_s`), and which beat is longest? (Artifact: three numbers. You are now fluent in the file.)

**Exercise 2.2 — Hand-edit a beat.** Pick one beat and rewrite its `narration_text` to be one sentence tighter, without changing its meaning. Do *not* touch `actual_duration_s`. Explain what must happen next before the video is correct again. (Artifact: the edited beat + your one-sentence explanation — it should name the audio step.)

**Exercise 2.3 — Spot the silent slide.** Given a beat sheet, find any beat whose `narration_text` is empty or still equals its `speaker_notes` verbatim. Why is each a problem? (Artifact: the offending `beat_id`s. The first is silent; the second is "reading the slide," which Chapter 7 forbids.)
