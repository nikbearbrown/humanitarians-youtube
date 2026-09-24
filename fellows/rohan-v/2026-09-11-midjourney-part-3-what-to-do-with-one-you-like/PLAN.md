# MIDJOURNEY PART 3 — "What To Do With One You Like"

**Runtime 2:39, 10 beats.** Part 1 shipped 3:19, Part 2 3:16.

This is the part Part 1 originally promised as Part 2, before prompt-writing
was inserted ahead of it. Part 1's tease was re-cut and re-rendered to point
here instead — see `../midjourney-part-2/PLAN.md`.

---

## The spine

The **opened-image action rail**, in the product's own row order, from
`MIDJOURNEY-UI-SPEC.md` §3 — built by reading `Image opened.png`,
`Image opened 2.png` and `Image opened 3 (more options).png` first-hand.

```
Imagine   19h              [list] [download] [pin] [heart]
<prompt>
Creation Actions                            More Options
Vary        [ Subtle ]      [ Strong ]
Upscale     [ Subtle ]      [ Creative ]
More        [ Rerun                      ]
HD          [ Run batch as HD            ]
Use         [ Style ]       [ Prompt ]
Edit        [ Quick Edit ]  [ Open Editor ]
Animate Image  ⌄                            Animate Manually
  Auto      [ Low Motion ]  [ High Motion ]
  Loop      [ Low Motion ]  [ High Motion ]
```

**Six labelled rows**, then `Animate Image` as a **separate collapsible** —
not a seventh row. Every count on screen derives from `MJ_RAIL_ROWS` and
`MJ_MENU`; `check_beats.py` fails the build if a spoken number disagrees.

---

## Beat table

| Beat | Act | Scene | Actual |
|---|---|---|---|
| B00 | Cold open | `ClaudeComposerAsk` | 15.6s |
| B01 | BLUF — the panel, six rows | `MjL3Bluf` | 19.2s |
| B02 | Vary and Upscale — the two pairs | `MjL3Pair1` | 19.4s |
| B03 | Rerun and Run batch as HD | `MjL3Pair2` | 17.5s |
| B04 | Use and Edit | `MjL3Pair3` | 17.1s |
| B05 | More Options is a **visibility checklist** | `MjL3Menu` | 17.1s |
| B06 | Animate Image, and the shorter video rail | `MjL3Animate` | 18.6s |
| BVDT | Verdict | `ClaudeVerdictArtifact` | 18.7s |
| BHTF | Part 4 tease | `ClaudeComposerAsk` | 13.0s |
| BOUT | Outro | `ClaudeTitleOutro` | 2.9s |

---

## Scenes — three components, six compositions

`MjL3Rail` serves **four beats** (B01–B04), differing only by `focus`. Each
still needs its own `<Composition>` because `durationInFrames` must equal that
beat's audio length and every cue is a fraction of it.

- **`MjL3Rail`** — three columns: the opened image and its siblings, the rail,
  our commentary. Widths derived from `CONTENT`, so the right edge lands on the
  safe edge by construction. Unfocused rows **desaturate rather than fade** —
  a translucent surface over cream composites to a grey slab.
- **`MjL3Menu`** — the seven-entry checklist beside the three entries it hides.
- **`MjL3Animate`** — the rail with the collapsible open, plus what changes once
  the thing is a video.

**Annotation never crosses into the rail.** It lives in the third column. The
Suno "red datum line" defect was a mark drawn over recreated UI from outside
its container.

---

## The best fact in this part

`More Options` is **not an action menu**. It is a checklist controlling *which
rows the rail shows you*, and **three of its seven entries arrive switched
off** — Pan, Zoom and Remix. They exist; they are simply not on screen until a
volunteer turns them on. Nobody discovers that by poking around, which is
exactly what makes it worth a beat.

Pan, Zoom and Remix are **named and described, never depicted in use**. There
is no capture of any of them working, and `VIDEO-PIPELINE.md` §8 forbids
depicting an uncaptured surface. `check_beats.py` blocks phrasing that would
overstep.

---

## What the cue pass caught before rendering

| Beat | Problem | Fix |
|---|---|---|
| B01 | `first` at **0.965** — closing card with 0.7s left | re-anchored to "same question" → 0.839 |
| B05 | `why` at **0.923**, and the two late movements in the wrong order | thesis card moved onto "which rows the panel shows" (0.339); the three names now land after it (0.652) |
| B04 | `second` at **0.836** | re-anchored to "two doors" → 0.587 |

B05's fix was not just timing. The payoff card — *this menu decides which rows
you see* — was resolving after the narration had already moved on. Anchoring it
to the line that states it put the claim and its evidence on screen together.

---

## Why 2:39 and not ~3:15

The content is complete: six rows, the checklist, the collapsible, the video
difference. Kokoro simply reads it faster than the estimate.

**One beat was considered and rejected.** The rail header carries four icons —
list, download, pin, heart. Their glyphs and order are captured, but **no
capture shows any of them opened**, and only the download arrow's function is
unambiguous from its glyph. Naming the others' functions would be inference
presented as observation. Logged as a capture request in
`../MIDJOURNEY-UI-SPEC.md`; it is worth ~20s once captured, because "how do I
get the file out" is the most practical question a volunteer has.

Padding a training video to match its siblings' length would be the wrong
trade.

---

## Register applied

- Host opens "Hi, I'm Rohaan from Humanitarians AI"; full name **once**, in BOUT.
- The series count is never stated.
- **The `Help us improve V8` row is omitted from every mockup** — §7 forbids a
  version number on screen, and it is a feedback prompt, not a control.
- No pricing. "Both of them spend another job" is the only cost language, and
  it is about job count, not money.
- Heteronyms handled at draft: "a separate section" → "another section";
  "Use carries" → "**The Use row** carries".

---

## What this part deliberately does NOT claim

| Not claimed | Why |
|---|---|
| What the four header icons do | Their glyphs are captured; their behaviour is not. |
| What Pan, Zoom or Remix produce | Named and described only. No capture of any in use. |
| Where a downloaded file lands, or in what formats | The download dialog is not captured. Part 6 owns it. |
| That Upscale improves an image | It adds pixels. Subtle keeps detail honest, Creative invents some — that is the captured distinction, not a quality judgment. |
| Any model version number, price or plan | Register rules, checked by script. |
