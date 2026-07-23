# Chapter 5 — Bios

## Overview

A bio is the smallest complete documentary: a narrated mini-biography over B-roll, one figure and one life, told in the time it takes to walk across a room. It is the same six-stage engine you met in Chapter 3, pointed at a single question — *who was this person, why did they matter, and what did they leave behind?* If you can answer those three in order, and trim each answer to about ten seconds, you have a bio.

The discipline of the form is subtraction. A life has thousands of facts; a bio keeps the handful that make the arc legible. You are not writing a Wikipedia entry read aloud. You are choosing the one line that defines them, the one idea that changed something, the one year that turned. Everything else is cut, and the cut is the craft. A simple figure with a single clean idea might run thirty seconds; a layered life a few minutes. Length is an *output* of the beats the story needs, never a target you write to.

What makes bios distinct from the music videos of Chapter 4 is the presence of a real subject — or a real-enough one. When your figure lived and was photographed, the pictures carry weight and responsibility at once. Most of this chapter is the pipeline you already know, applied to one person. But the part worth reading slowly is the ethics of showing a face that belonged to someone.

## The three-beat arc

Every bio, however long, answers the same three questions in order, and the visual track alternates as it goes — a photoreal beat, then a clean card, then photoreal again.

**Who.** Open on the figure and establish them: a title card with the name in caps and the dates, `1815 — 1852`. The viewer meets a person.

**Why they mattered.** The work, the world it lived in, the line or equation that defines them, the turning point. This is the body of the bio and where most beats sit. For Ada Lovelace it is the Analytical Engine and the note that a machine might weave algebra as a loom weaves flowers.

**Legacy.** What endures — the technology a discovery enabled, the field it founded, the way we still say the name — and then you close, deliberately, back on the figure. A bio opens and closes on the person so the arc returns home.

Each beat is one narrated unit, one idea, roughly ten seconds or less, and the beats alternate between full-frame footage and dark cards so the two read as one documentary piece. If a draft doesn't clearly answer all three questions, it isn't finished — it's a list of facts.

## The single reference plate

In Chapter 3 you built a cast and picked a keeper. A bio has a cast of one, which makes the reference step both simpler and higher-stakes. You generate one reference plate for the figure — a Higgsfield SoulID, a consistent invented likeness — and reuse it across every beat where the figure appears. Generate several candidates, then pick the single great one; that plate becomes the face the whole film returns to.

Not every beat shows the figure. Bios divide their footage into three kinds. **Figure beats** reuse the reference plate — the same face opening, recurring through the body, and closing. **World beats** show the milieu the story lived in: a Victorian drawing room, punched cards, a gathering storm — no character, just the world. **Legacy beats** show what endures: rows of servers, a monument, a shelf of worn books — again, no character. Only the figure beats depend on the reference; world and legacy beats are scenes with no person in them, so they need no plate at all. This is why the single reference goes far: you are not asking it to appear in every frame, only in the ones that are *about the person.*

## The ethics rule

Here is the part to read twice. When your figure is a real person, photographs of them are governed by a single rule, and there is no clever way around it.

**A real photograph is used as-is if it is freely licensed, or it is omitted.** If a public-domain or openly licensed photograph of the person exists, you may place it in the film unchanged. If no such photograph is free, you leave the photograph out. You do not run a copyrighted or unlicensed photo through an image model to "reimagine" it, restyle it, upscale it, or vectorize it into something you can claim as new. Never fake or vectorize a real photograph. The SoulID likeness you generate is explicitly an *invented* face — copyright-safe precisely because it is not a real photo of the person — and that is the point: it lets you show "a woman at a desk in 1843" without laundering someone's actual portrait.

Line diagrams are the one thing you may redraw. A schematic — the plan of a machine, a diagram from a paper — can be honestly re-drawn as a clean original figure, because a diagram communicates a structure, not a likeness. But a redrawn diagram still gets human sign-off before it ships. The rule is not "diagrams are free"; it is "diagrams may be redrawn, *and a human still checks the result.*" When in doubt, the safe defaults are: invented SoulID for the face, freely licensed photo used untouched or not at all, redrawn diagram with a human's eyes on it.

And the prompt rule from Chapter 3 holds without exception here: the `image_prompt` is a **visual scene only** — the woman at her writing desk, lamplight, papers — never the narration text baked into the frame. Words the viewer reads are Remotion overlays, added last, on top of the picture, never inside it.

## Audio is the master clock

As everywhere in this engine, narration is generated and measured first, and its real durations set the timing. Every beat's on-screen time equals its narration length exactly; the scene budgets the hold to absorb the remainder, and clips are trimmed to the measured narration. You never write to a clock — the clock writes itself from the words. Watch the placeholder cut (cards plus audio, no footage yet) to judge the rhythm before you spend anything on video.

## Worked example — Ada Lovelace, from source to reference

Start with a short prose source and segment it into beats:

```
python scripts/segment_story.py examples/bios-demo/source.txt \
  --slug ada-lovelace --title "Ada Lovelace" \
  -o reels/ada-lovelace/beat_sheet.json
```

You get a `beat_sheet.json` — the who/why/legacy arc as narrated units. Now author the `image_prompt` for each beat: visual scenes only, tagged by kind. The opening and closing figure beats describe Ada at her desk (they will reuse the reference plate); a world beat describes the Analytical Engine's brass and punched cards with no person present; a legacy beat shows modern computing. Set the metadata `voice_id` and the `character`, then lock the audio:

```
python scripts/generate_audio.py reels/ada-lovelace
```

✅ With a local TTS this stage is free; the durations are what matter, and they are now measured. Build the one reference plate for the figure and pick the great one:

```
bash scripts/generate_references.sh reels/ada-lovelace
```

Then the storyboard stills, where figure beats reuse that reference and the world/legacy beats generate as no-character scenes:

```
bash scripts/generate_storyboard_flux.sh reels/ada-lovelace
```

From here it is video (each still trimmed to its beat's measured narration) and the Remotion overlay for the title and captions — the same last two stages as any reel. You have made a mini-bio: one figure, one life, three beats of arc, one honest face.

## Exercises

**Exercise 5.1 — Segment a life into three beats.** Take a real or fictional figure and write a three-beat arc — one narrated line each for *who*, *why they mattered*, and *legacy* — then segment it into a `beat_sheet.json`. Keep each narration under about ten seconds when read aloud. (Artifact: a `beat_sheet.json` with three beats covering the full arc.)

**Exercise 5.2 — Make an ethics call.** Pick your figure and find whether a freely licensed photograph of them exists. Write down what you'll use for the *who* beat — a freely licensed photo used as-is, or an invented SoulID likeness because no free photo exists — and one sentence on why the other option is off the table. (Artifact: your sourcing decision + the license or absence you verified.)

**Exercise 5.3 — Author a clean prompt and place the words.** Write the `image_prompt` for your opening figure beat as a visual scene only, with no narration or caption text in it, and note where the figure's name and dates go instead. State plainly whether this beat reuses your single reference plate. (Artifact: your corrected prompt + one line on the title-card overlay.)
