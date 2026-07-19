# Chapter 3 — Storyboard-First

## Overview

The reels side of Unreal Reels — music videos, mini-bios, explainers — runs a six-stage engine, and the order is the lesson. You do not open an image generator and start making pretty frames. You start with the words, lock the audio, build a cast, and only then make pictures. Storyboard-first means the visuals serve a script and a clock that already exist.

The stages: **segment → audio → references → stills → video → overlay.**

1. **Segment.** A script, story, or set of lyrics is cut into beats — one narrated unit each — and written to `beat_sheet.json`. `python scripts/segment_story.py source.txt --slug my-film --title "My Film" -o reels/my-film/beat_sheet.json`.
2. **Audio (the clock).** `generate_audio.py` narrates each beat and measures its real duration. From this point, every beat has a true length. ✅ with a free local TTS; the durations are what matter, not the voice vendor.
3. **References.** `generate_references.sh` builds a small library of character/subject plates — the same face, the same look, that every scene will reuse. You generate several and *pick the keeper*. This is the first curation gate.
4. **Stills.** `generate_storyboard_flux.sh` makes the per-beat frames, drawing on the reference library so identity stays consistent across scenes. Typically several candidates per beat; you pick the best.
5. **Video.** Each chosen still becomes a short clip, trimmed to its beat's measured narration (the clock again).
6. **Overlay.** Remotion lays titles and captions on top, and assembles the final MP4.

Between each stage is a gate where you curate — pick the reference, pick the frame, approve the clip. Quality is controlled here, deliberately, not hoped for at the end.

## The one rule about prompts

An `image_prompt` describes a **visual scene only** — action and composition — never the narration or any caption text. If you put words in the prompt, the image model bakes them into the frame as gibberish, because diffusion models render text as noise. Identity comes from the *reference library*, not the prompt; the prompt carries what is happening and how it's framed. Any words the viewer should read are added later as crisp Remotion overlays, on top of the image, never inside it. This single rule prevents the most common and most embarrassing failure in AI video.

## Committed definition versus regenerable output

A reel's *definition* is small and worth keeping in version control: the `beat_sheet.json`, the source text, the chosen reference and storyboard picks, the prompts. The *output* is large and regenerable: full-resolution stills, audio, video. You commit the definition and let the heavy output stay local. This is what makes a reel reproducible — hand someone the definition and the pipeline rebuilds the video — without committing gigabytes.

## Free versus paid, honestly

The engine orchestrates external services (Higgsfield for references and video, ElevenLabs for voice) but does not depend on any one of them for the whole flow. A lyric/audiogram music video needs **no paid services at all** — you bring the track, and analysis, alignment, and the waveform render are free and local (Chapter 4). Explainer figures can be free SVGs instead of generated art (Chapter 6). Teach the seams, and you can swap any vendor — or run open models on your own GPUs — without the pipeline noticing.

## Worked example — segment a short story and lock the clock

Take a 150-word story. Run the segmenter; it returns a beat sheet of, say, eight beats, each with a `narration_text` and an empty duration. Run `generate_audio.py` on the folder; each beat now carries a measured `actual_duration_s`, and the total tells you the film's runtime before you have made a single picture. You have done stages 1–2. The clock is set; everything visual from here is trimmed to it.

## Exercises

**Exercise 3.1 — Segment and time.** Segment a short piece of your own text and generate its audio. Report the beat count and total runtime. (Artifact: a `beat_sheet.json` with measured durations.)

**Exercise 3.2 — Build a cast and pick a keeper.** Generate a reference plate set for one subject and choose the single best plate. Write one sentence on *why* you chose it (consistency of face/look matters more than prettiness). (Artifact: the chosen reference + your reason.)

**Exercise 3.3 — Catch a bad prompt.** Here is an `image_prompt`: *"Ada Lovelace at her desk with the caption 'The First Programmer' below her."* Rewrite it to obey the one rule. Where does the caption go instead? (Artifact: your corrected prompt + one line on the overlay.)
