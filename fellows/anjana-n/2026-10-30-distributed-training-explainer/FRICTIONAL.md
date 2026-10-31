# Friction Log: What Distributed Training Actually Looks Like

**Type:** STEM Educational Video
**Week:** Week 18, October 25 – 31, 2026

---

## 1. Date and focus

This week's video explains how large AI models are trained across many GPUs. The build finished on October 28, with all nine scenes rendered.

The video covers:
- why one GPU doesn't have enough memory
- copying the model across GPUs, and keeping the copies in sync
- the "ring" method of sharing results between GPUs
- splitting the model itself across GPUs, and the idle time that causes
- how real training setups combine all of these

## 2. What was tried, and what was expected

- **Colors:** the brief's colors were expected to cover everything the video needed.
- **Memory numbers:** the numbers in the narration were expected to add up on screen.
- **Example models:** the two example models, one in the model-splitting section and one in the final section, were expected to read clearly as separate examples.
- **Ending:** the brief ended with a fade to black. This was expected to give a clean finish.
- **Length:** the narration was to stay exactly as written, within the 45 to 70 word target.

## 3. Where things got stuck, and what was done next

**The memory chart had to add up.**
This is the scene the whole video depends on. If a viewer checks the math and it doesn't work, they stop trusting the rest.

| Part | Memory |
|---|---|
| model weights | 28 GB |
| optimizer memory | 56 GB |
| gradients | 28 GB |
| **total** | **112 GB** |

That total is more than an 80 GB GPU can hold. 
This also showed something unexpected. The model weights, which most people think of first, are only a quarter of the total.

**The two example models looked like one model changing.**
The model-splitting section uses a 48-layer model on four GPUs. The final section uses a 72-layer model on three machines. Back to back, they looked like the same model with different numbers.

Both were kept, and each scene now states its own setup on screen. The layer ranges are calculated so they fit together with no gaps.

**"Nearly linear" speed-up.**
The narration says training gets nearly linearly faster with more GPUs. That can leave viewers thinking four GPUs means four times faster.

The wording was kept. Right after it, though, the video shows the syncing step that has to happen every round, and it ends on the communication limit rather than on the speed-up.

**Idle time in the pipeline.**
The simplest animation would show the idle time disappearing once small batches are used. In reality it shrinks but doesn't go away, so a small gap stays visible.

**Colors.**
The brief was missing two shades, one for the inside of boxes and one for borders. Two dark shades that match the background were added.

**Ending.**
A fade to black would have ended on an empty screen, because the final frame is held for a few seconds. The video ends on the title card instead.

**Length.**
Four of the five main sections ran over the 45 to 70 word target. They were kept, because something new is always appearing on screen. The closing summary written by Claude was the longest section in the video, about eight seconds over its plan.

## 4. What Claude contributed, and what was kept or changed

**Who did what:**
- **Original work:** the concept, the brief, and the narration for the five main sections.
- **Claude:**
  - assembled the video using the video generation tool created by Humanitarians AI
  - wrote the opening, the closing summary, the viewer prompt and the outro

**Accepted:**
- the calculated memory chart
- labelling each example model on screen
- showing the syncing cost next to the speed-up
- keeping the idle time visible
- a female voice instead of the default male one, to match the first-person narration

**Changed from the brief:**
- the ending
- two added colors

**Kept as written:**
- all of the original narration
- both example models

## 5. What is understood now, and what is still open

**Understood now:**
- **If a viewer can check a number, calculate it.** If the model size changed, every bar would update together.
- **The picture can add context without changing the narration.**
- **Training across many GPUs is limited more by moving data between them than by computing power.**

**Still open:**
- None