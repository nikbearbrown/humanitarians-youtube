# MIDJOURNEY PART 2 — fact check

Every claim this video makes, on screen or in the voice, with its source.

**This part is different from the rest of the series.** Its subject — how to
write a prompt — cannot be verified by a screenshot. So it runs two evidence
standards side by side, and says which is which on screen.

| Claim type | Standard | Where |
|---|---|---|
| Product UI | captures only, first-hand | `../Midjourney Screenshots/` |
| Prompt craft | Midjourney's own documentation | cited below, per claim |
| Our commentary | marked as ours, typographically separate | the note cards |

---

## 1. The seven elements — the spine

**Source: Midjourney, Prompt Basics** (docs.midjourney.com, fetched
2026-09-07). The list, its order, the questions and the example strings are all
the vendor's. Reproduced verbatim in `MJ_SEVEN`.

| # | Element | Question | Vendor's examples |
|---|---|---|---|
| 1 | Subject | Who or what? | person, animal, character, location, object |
| 2 | Medium | In what form? | photo, painting, illustration, sculpture, doodle, tapestry |
| 3 | Environment | Where? | indoors, outdoors, on the moon, underwater, in the city |
| 4 | Lighting | What kind? | soft, ambient, overcast, neon, studio lights |
| 5 | Color | In what shades? | vibrant, muted, bright, monochromatic, colorful, black and white, pastel |
| 6 | Mood | Feelings to evoke? | playful, calm, gloomy, energetic |
| 7 | Composition | How is it framed? | portrait, headshot, closeup, birds-eye view |

**Verified by script.** `check_beats.py` reads `MJ_SEVEN` out of
`midjourneyPrompt.tsx` and fails the build if the count is not 7, if the order
drifts from the documented list, or if any element is never spoken.

**Also documented and used:** "While single-word prompts can yield stunning
images, the true magic happens when you mix in different concepts" — the basis
for B01's line that a one-word prompt still works. *(Paraphrased in narration,
not quoted on screen.)*

---

## 2. Exclusions — the correction in B07

| Claim | Source |
|---|---|
| Describe what you want, not what you don't; "no cake" may still produce a cake | **Prompt Basics**, quoted on screen and attributed |
| There is a `--no` parameter; comma-separate the items | **No** article |
| Every word after `--no` is read independently — "`--no modern clothing`" reads as "no modern" AND "no clothing" | **No** article |
| Using `--no` equals weighting that phrase to −0.5 | **No** article |

**The workspace prompt does it the documented-unreliable way.** Its tail reads
`no gore, no exposed organs, no armor, no scenery, no text, no motion blur` —
six exclusions in plain text. That is quoted, transcribed from
`Create Tab.png`, and named as the one thing the prompt gets wrong.

**What B07 does NOT say:** that the images failed. The four wolf images in that
capture plainly worked. The claim is bounded to "the docs call this pattern
unreliable", which is checkable. `check_beats.py` fails the build on phrases
that overreach ("the exclusions were ignored", "that is why it looks…").

---

## 3. The worked example

**Source: `../Midjourney Screenshots/Create Tab.png`**, read first-hand and
transcribed character-for-character into `PROMPT_WOLF`. The rail shows the
prompt complete, ending at "no motion blur", followed by an `ar 3:2` chip.

**Verified by script.** For each of the seven, `check_beats.py` asserts that the
substring `MJ_SEVEN` claims is in the prompt actually appears in `PROMPT_WOLF`.
If the quotation and the mapping ever drift apart, the build fails rather than
shipping a highlight over the wrong words.

### Three prompts deliberately NOT used as evidence

`grid of 4 finished.png` and `In progress creation.png` show three more prompts
— vampire mother, vampire boy, graveyard zombie — but **all three are truncated
by the product's rail**. Only their opening is legible. They are therefore not
used to support the seven-element claim, and no beat depicts their full text.

An earlier draft of this part built a whole beat on "all four share one
skeleton". That claim is **not verifiable from the captures** and was cut.

---

## 4. Deliberately NOT claimed

| Not claimed | Why |
|---|---|
| An eleven-slot prompt structure | That was **my own segmentation** of the workspace prompt, written before the vendor's list surfaced. Plausible, unauthoritative, replaced. |
| That the four prompts share all seven elements | Three of the four are cut off by their rails. |
| That the wolf images failed | Inference. The images worked. |
| Anything about how the prompt was authored | An earlier draft claimed "nobody was ticking boxes" and "an earlier attempt cut the paws off". Both invented. Both now blocked by script. |
| Any dial or parameter beyond `--no` | Stylize, chaos, weird and aspect ratio are the **settings panel**, which is Part 4. This part is the words you type. |
| A specific stylize / chaos / weird value as "good" | The panel shows no numeric readouts at all. Naming a number would be inventing product behaviour. |
| Any model version number | `8.2` appears in the settings dropdown and `Help us improve V8` in every image rail. `VIDEO-PIPELINE.md` §7 forbids both. |
| Any pricing, plan or credit figure | Register rule. `check_beats.py` fails on a term list. |
| The number of videos in the series | Suno Part 1 said "the first of three" and it forced a cramped Part 3. |

---

## 5. On-screen text that is NOT a product string

The vendor's words are quoted; everything else is this series' own voice, set
in a different type treatment so no viewer mistakes it for Midjourney UI:

- Every note card body (the commentary beneath each element)
- All section titles and spark lines
- B01's closing line, B06's closing card
- The column tags in B07 ("The prompt we just read", "What the docs say",
  "What to do instead")

Product / documentation strings reproduced verbatim: the seven element names ·
their seven questions · their example strings · the `--no` syntax example ·
the "no cake" guidance · the −0.5 weighting note · and `PROMPT_WOLF` in full.

**No screenshot is composited into any frame.** Every surface is a native
Remotion recreation (REBUILD LAW).

---

## 6. Register compliance

| Rule | Status |
|---|---|
| Host opens "Hi, I'm Rohaan from Humanitarians AI" | B00 — checked by script |
| Full name spoken exactly once, in BOUT | 1 occurrence — checked by script |
| Phonetic spellings preserved (`Rohaan`) | Deliberate for Kokoro G2P |
| No promotion, no pricing, no plan names | checked by script |
| Series count never stated | checked by script |
| No model version number | checked by script |
| Kicker on every scene | `LYRICAL LITERACY · MIDJOURNEY TUTORIAL PART 2` — checked by script |

**`check_beats.py`: 0 blockers, 0 warnings.**

### Heteronyms removed before audio lock

| Was | Now | Why |
|---|---|---|
| "an object" | "a location" | verb stress /əbˈdʒɛkt/ risk; the vendor's full list is on screen anyway |
| "read in a minute" | "coming up" | two gambles in one phrase |
| "Read it against the seven" | "Check it against the seven" | /rɛd/ risk in a key line |
| "is read on its own" | "is taken on its own" | the passive needs /rɛd/; Kokoro defaults the other way |

`subject` remains — it is one of the seven element names and cannot be reworded.

---

## 7. Outstanding — needs the author's ears

The build cannot listen back. Two checks remain:

1. **`Rohaan`** in BOUT.
2. **`subject`** wherever it is spoken as a noun — the one heteronym that could
   not be removed.
