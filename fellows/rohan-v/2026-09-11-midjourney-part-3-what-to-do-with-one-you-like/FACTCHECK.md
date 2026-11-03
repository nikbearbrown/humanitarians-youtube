# MIDJOURNEY PART 3 — fact check

Every claim this video makes, on screen or in the voice, with its source.

**Source of record:** `../MIDJOURNEY-UI-SPEC.md` §3, built by reading
`Image opened.png`, `Image opened 2.png`, `Image opened 3 (more options).png`,
`video opened.png`, `video opened 2.png` and `video opened 3 (more
options).png` first-hand.

**Nothing in this video comes from web research.** Unlike Part 2 — whose
subject was prompt craft and whose authority was the vendor's documentation —
this part is pure UI, so the capture rule applies without exception.

---

## 1. The rail, row by row

| Claim | Source |
|---|---|
| Opening an image gives: image centred, action rail right, siblings far right | `Image opened.png` — all three regions visible |
| The heading is `Creation Actions` | Same |
| Six labelled rows, in order: Vary · Upscale · More · HD · Use · Edit | Same, read top to bottom |
| Vary offers `Subtle` and `Strong` | Same |
| Upscale offers `Subtle` and `Creative` | Same |
| More offers `Rerun`, full width | Same |
| HD offers `Run batch as HD`, full width | Same |
| Use offers `Style` and `Prompt` | Same |
| Edit offers `Quick Edit` and `Open Editor` | Same |
| Buttons are pale grey pills with dark text, no accent fill | Same |

**Verified by script.** `check_beats.py` reads `MJ_RAIL_ROWS` out of
`midjourneyRail.tsx` and fails the build if the order drifts from the captured
order, if the count is not six, or if the narration references a button label
that is not in the data.

### What the buttons DO — and how far the claim goes

The captures show the controls, not their output. So the narration describes
**what each control is for**, in the plainest reading of its own label, and
stops there:

- "Vary gives you a new set of four built from this image" — Vary is labelled
  Vary and offers a degree (Subtle/Strong). Safe.
- "Upscale adds pixels. Subtle keeps the detail honest, Creative invents some
  to fill the gaps." — the *distinction between the two buttons* is the claim,
  and it follows from their labels. **Not claimed: that either improves the
  image.**
- "Rerun sends the same prompt again from scratch. Four fresh results, not
  variations." — follows from Part 1's captured fact that one job returns a row
  of four.

---

## 2. `More Options` — the checklist

| Claim | Source |
|---|---|
| It opens a checklist, not a list of actions | `Image opened 3 (more options).png` |
| Seven entries | Same — counted, one per line, in `MJ_MENU` |
| Four carry accent ticks: Vary · Upscale · More actions · Use in prompt | Same |
| Three arrive unchecked: **Pan · Zoom · Remix** | Same |
| It controls which rows the rail displays | Same — the checked entries correspond to the rows visible in `Image opened.png` |

**Verified by script.** The three names the narration speaks are checked
against the entries whose `on` flag is `false`. If a flag flips in the data and
the narration is not updated, the build fails. This check exists because Suno
shipped "four submenus" against a five-item menu.

**Pan, Zoom and Remix are named and described, never depicted in use.** There
is no capture of any of them working. Our one-line descriptions say what each
control *is* — not what it returns — and `check_beats.py` blocks phrasings that
would overstep ("pan gives you…", "zoom produces…").

---

## 3. `Animate Image`

| Claim | Source |
|---|---|
| It is a separate collapsible below the six rows, not a seventh row | `Image opened.png` (collapsed) and `Image opened 2.png` (open) |
| Open, it holds two rows: `Auto` and `Loop` | `Image opened 2.png` |
| Each offers `Low Motion` and `High Motion` | Same |
| An `Animate Manually` link sits on the header row | Same |
| On a video the rail is shorter: no Vary, Upscale, HD or Edit | `video opened.png` |
| On a video, `Use` offers `Start Frame` instead of `Style` | Same |
| On a video, `Extend Video` replaces `Animate Image` | Same |

"Auto lets Midjourney decide what moves; Loop builds a clip that runs back into
itself" is the plainest reading of the two labels. **Not claimed: what either
clip looks like.** No captured video output exists.

---

## 4. Deliberately NOT claimed

| Not claimed | Why |
|---|---|
| What the four rail-header icons do | Their glyphs and order are captured (`list`, download, pin, heart); **no capture shows any opened**. Only the download arrow's function is unambiguous. A whole beat was considered and cut over this — see `PLAN.md`. |
| Where a downloaded file goes, or what formats are offered | The download dialog is not captured. Part 6 owns "getting files out". |
| What Pan, Zoom or Remix produce | No capture of any in use. |
| That Upscale makes an image better | It adds pixels. The captured fact is the Subtle/Creative distinction, not a quality verdict. |
| That Vary is cheaper or faster than Rerun | Nothing captured supports a cost or speed comparison. The narration says only that both spend another job. |
| Any model version number | The real rail carries a `Help us improve V8` row between the prompt and the folder icon. **It is omitted from every mockup in this series** — `VIDEO-PIPELINE.md` §7 forbids a version number on screen, and it is a feedback prompt, not a control. |
| Any pricing, plan, credit or GPU-hour figure | Register rule, checked by script. "Spend another job" is about job count, not money. |
| The number of videos in the series | Suno Part 1 said "the first of three" and it forced a cramped Part 3. |
| The Studio page, or anything under `Organize` | Not this part. Part 6. |

---

## 5. On-screen text that is NOT a product string

Product strings are reproduced verbatim; everything else is this series' own
voice, typographically distinct:

- Every commentary card body in the third column
- All section titles and spark lines
- B01's closing card, B05's "this menu does not *do* anything" card
- B06's `Gone / Changed / Replaced` summary of the video rail
- The word `hidden` badged onto the three unchecked entries

Product strings reproduced verbatim: `Imagine` · `Creation Actions` ·
`More Options` · `Vary` · `Upscale` · `More` · `HD` · `Use` · `Edit` ·
`Subtle` · `Strong` · `Creative` · `Rerun` · `Run batch as HD` · `Style` ·
`Prompt` · `Quick Edit` · `Open Editor` · `Animate Image` ·
`Animate Manually` · `Auto` · `Loop` · `Low Motion` · `High Motion` · `Pan` ·
`Zoom` · `Remix` · `More actions` · `Use in prompt` · `Start Frame` ·
`Extend Video`

**No screenshot is composited into any frame.** Every surface is a native
Remotion recreation (REBUILD LAW). Tile imagery is deterministic seeded
geometry — an abstract stand-in, never a claim about what Midjourney produced.

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
| Kicker on every scene | `LYRICAL LITERACY · MIDJOURNEY TUTORIAL PART 3` — checked |

**`check_beats.py`: 0 blockers, 0 warnings.**

### Heteronyms removed before audio lock

| Was | Now | Why |
|---|---|---|
| "another **separate** section" | "**another** section" | adjective /ˈsɛpərət/ vs verb /ˈsɛpəreɪt/ |
| "**Use** carries something forward" | "**The Use row** carries something forward" | noun /juːs/ vs verb /juːz/ |

---

## 7. Outstanding — needs the author's ears

1. **`Rohaan`** in BOUT.
2. **`Use`** wherever spoken — it is a product row label and cannot be reworded
   away, only cushioned ("the Use row").
