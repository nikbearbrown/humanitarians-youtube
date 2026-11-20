# SHOTLIST — How Do Websites Know I'm Not a Robot?

Typed work order. Thirteen beats. Narration is `SCRIPT.md` verbatim. Beat IDs B01–B10 match script sections 1–10, so "beat 5" and "beat 9" mean the same thing here as in the script. BVDT, BHTF and BOUT are sections 11, 12 and 13.

**Status: audio approved. `scenes.py` and `vertical/scenes.py` are written (eight Manim scenes each, portrait laid out natively). Gates A, W and B are clean on both. Low-quality previews with audio exist for all 13 beats in both orientations under `_preview/with-audio/`. No final renders. Nothing is published.**

## Rules for every visual

- Simple illustrative graphics only: a grid of drawn traffic-light squares, wavy letters, a checkbox, a 0-to-1 score dial, a stopwatch, a mouse path, a shield, three small cards for text, images and audio.
- **No Google, reCAPTCHA, hCaptcha or Cloudflare logos, and no screenshots of real challenge pages.** No copy of any product's widget (the real checkbox, the real picture grid) or its colour scheme. Company and product names (CAPTCHA, reCAPTCHA v3, Cloudflare, UC Irvine, ETH Zurich) appear as plain text only, where the narration says them. The checkbox is a drawn box with the plain words "I'm not a robot". The letters in the wavy-text example are a made-up string, not a real challenge.
- **No person icons.** "Me" is a cursor; bots are a drawn robot (a square head, two dots, an antenna). No avatars, no portraits. The shield, gate, eye, stopwatch and dial are plain geometric shapes.
- Every example is an illustration, not data. The only figures on screen are those in `SCRIPT.md`: 91%, 32 s to about 1 s, 1,400 people, 14,000 CAPTCHAs, 9 to 15 s, 50 to 84%, under 1 s, 99.8%, 100%, 68 to 71%. The dial shows only 0 and 1; its needle position is an example, labelled "illustrative". Ranges are drawn as ranges, not as single bars.
- On-screen-only text from `SCRIPT.md` is shown but not narrated: the typed-then-corrected overview (beat 3) and the prompt (beat 12).
- **Portrait (9:16):** all text sits above 86% of the frame height (y < 0.86 × H); the bottom 14% stays empty. 9:16 gets its own native layouts, not a crop of 16:9: one idea at a time, stacked, bigger type. Portrait text is never scaled. Font sizes are set directly with a 32 pt floor.
- Palette `humanitarians`: ink `#2F2A26`, terracotta `#E4572E` (one accent per beat; it marks the thing being questioned or struck), teal `#1F4E5F` (marks the kept, passing or correct thing), ground `#F3EBDD`.
- No dates on screen or in files.
- Un-highlighted elements never fade below about 40% opacity.
- Math: none. Figures are drawn as bars, bands, a dial and a stopwatch; no formula is shown.

## Library check

`./art scenes` was searched first for: a grid of traffic-light picture squares to select; wavy distorted letters; the "I'm not a robot" checkbox; a checkbox that gets ticked; a 0-to-1 score dial; a stopwatch (twice); a mouse-cursor path; a shield protecting a website from bots; traffic light; a typed-then-corrected overview sentence; two readings of one sentence old versus new; humans versus bots bars; humans versus bots race; background signals (cookies, history, mouse); a before-and-after drop of 91 percent. `./art scenes --check` confirmed the four bookend compositions and their 9:16 variants are renderable.

| Need | Result |
|---|---|
| Typed and corrected overview | **Hit:** `BrutalistHesitantWriter` and `BrutalistHesitantWriter916` |
| Cold open, Your Turn | **Hit:** `ClaudeComposerAsk` and `ClaudeComposerAsk916` |
| Verdict page | **Hit:** `ClaudeVerdictArtifact` and `ClaudeVerdictArtifact916` |
| Outro | **Hit:** `LogoOutro` and `LogoOutro916` (same as Keya's earlier films) |
| Traffic-light picture grid, wavy letters | **Miss.** Leads judged from their search descriptions only (files not opened) and rejected: `AlgArtSeedGrid` (a generative-art seed grid), `K12Fig03TextScaffold` (a text-support split from another film). Custom Manim. |
| "I'm not a robot" checkbox, ticked | **Miss (PUNT).** The search said no scene matches; nothing close among the weak hits. Custom Manim. |
| 0-to-1 score dial | **Miss.** Lead judged from its description and rejected: `BrandBoondoggleScore` (a 0 to 100 gauge tied to another film's score table). Custom Manim. |
| Stopwatch, 32 s to 1 s | **Miss (PUNT).** The search said no scene matches. Custom Manim. |
| Mouse path and behaviour signals | **Miss.** Lead judged from its description and rejected: `CursorLayer` (a macOS pointer overlay that must sit inside a real app shell, which is not allowed here). Custom Manim. |
| Shield, gate, bot stopped or verified | **Weak match only** (`WalkerGodotSetup`, a game-setup figure). Custom Manim. |
| Humans versus bots, ranges | **Miss.** Lead judged from its description and rejected: `BarChart` (single-value bars; beat 8 needs ranges and an under-1-second sliver). Custom Manim. |

A genuine miss is a design card, not a licence to slate. The misses are custom scenes in this reel's own `scenes.py` and `vertical/scenes.py`. The tool logged the checkbox and stopwatch PUNTs to the toolkit's `TEMPLATE-MISSES.md`; that line was reverted at your request, so those two misses are recorded here only. `./art scene-index` is not needed because no component is added to the library.

## Audio (the master clock)

Kokoro `af_bella`, generated. Pronounce: `Keya` only (`kˈeɪjɛə`); see `PROMPTS.md`. Seconds are from the generated files. Total about 3 minutes 15 seconds. B03, B04, B09, B10 and BVDT were regenerated after the script edits.

Waiting for your listen-check: **CAPTCHA** (B02, B04, B06, B07, B08), **reCAPTCHA v3** (B06), **Cloudflare** (B07), **UC Irvine** (B08), **ETH Zurich** (B09).

**B03 timing:** now 9.34 s after the narration was lengthened, in line with the earlier films' overview beat (about 9.5 s). Still check after rendering that the correction finishes typing before the 50% frame.

| Beat | s | Beat | s |
|---|---|---|---|
| B01 | 8.75 | B08 | 19.95 |
| B02 | 13.48 | B09 | 22.51 |
| B03 | 9.34 | B10 | 16.83 |
| B04 | 17.96 | BVDT | 11.46 |
| B05 | 17.75 | BHTF | 19.24 |
| B06 | 12.59 | BOUT | 5.42 |
| B07 | 20.03 |  | |

The `go()` times inside each Manim scene must come from word timings measured on these files, not from estimates.

## Beats

### B01 · INTRO · 8.75 s · Remotion `ClaudeComposerAsk`
Greeting "Hi, Keya", topic "Irreducibly Human", segment is the title, folder chip `@HumanitariansAI`. Typed ask: "Explain how websites know I'm not a robot."

| At | Event |
|---|---|
| 10% | The ask types in under 'Hi, Keya' |
| 55% | Three result lines land: websites check how you behave, a score instead of a puzzle, traffic lights aren't the whole test |
| 85% | The AI-voice disclosure is spoken while the answered composer holds |

### B02 · HOOK · 13.48 s · Manim `B02_Hook`
A plain 3x3 grid of drawn squares, some holding a simple drawn traffic light (three stacked circles in a rounded box), others a plain shape. A cursor ticks the traffic-light squares one by one on 'Click every traffic light'; the grid refills with bicycle outlines (two circles and a frame) on 'Then every bike'; it refills once more on 'Sometimes two in a row'. A small drawn robot (a square head, two dots, an antenna) glides past a dashed gate without stopping on 'my bots never ran into a CAPTCHA'. The question 'Why does it keep asking me to prove I'm human?' lands last. Everything is a drawn illustration; no logo, no real challenge page.

*Note:* Keya's own experience (tagged in SCRIPT.md). The grid is a drawn illustration, not a copy of any real challenge page. No person icon: 'me' is a cursor.

| At | Event |
|---|---|
| 5% | A small drawn robot glides straight through a dashed gate on 'my bots never ran into a CAPTCHA'; 'automation developer' reads small above it |
| 30% | The cursor stops at the same gate; a 3x3 grid of drawn squares opens and the cursor ticks every traffic-light square, on 'Click every traffic light' |
| 55% | The grid refills with bicycle outlines and the cursor ticks those, on 'Then every bike'; it refills again on 'Sometimes two in a row' |
| 90% | The question 'Why does a website keep asking me to prove I'm human?' lands under the grid |

### B03 · OVERVIEW · 9.34 s · Remotion `BrutalistHesitantWriter`
Typed text on screen, not narrated. Narration lengthened to 9.34 s. Check after rendering that the correction is fully on screen before the 50% frame.

*Note:* Typed 'Prove you can see traffic lights.' then corrected to 'Prove you behave like a person.' as in SCRIPT.md (on screen only; not narrated). The whole sentence is the trigger phrase so the correction replaces the sentence, not one word. 'Prove you can see traffic lights' is the viewer's likely misconception. Narration lengthened to give the typing room; no lead silence. Verify after render that the correction finishes typing before the 50% frame, and shorten the lines if not.

| At | Event |
|---|---|
| 10% | The writer types 'Prove you can see traffic lights.' in terracotta, finishing before the 50% point |
| 40% | It pauses, then deletes the whole sentence |
| 55% | 'Prove you behave like a person.' types in ink |
| 90% | The corrected sentence holds while the voice says 'Let's see how, step by step' |

### B04 · WHAT A CAPTCHA IS · 17.96 s · Manim `B04_WhatIsCaptcha`
The word CAPTCHA draws in large; its letters unfold into the long name, one word per letter (Completely Automated Public Turing test to tell Computers and Humans Apart), word by word as spoken. Under it, a plain question card: 'human or bot?'. Then a short row of drawn wavy, distorted letters (a made-up string, not a real challenge) appears with a cursor typing under it, on 'wavy, distorted letters'. Last, three plain drawn cards, 'text', 'images', 'audio' (a letters card, a small picture-grid card and a sound-wave card), land one by one on 'three main types'. Labelled 'illustrative'.

*Note:* Listen-check CAPTCHA. The letter string is invented for the picture and is not a real challenge. 'Three main types: text, images and audio' is from the Merchant Risk Council post; see FACTCHECK.md. The word 'Today' is the script's own.

| At | Event |
|---|---|
| 5% | 'CAPTCHA' lands large; it unfolds letter by letter into the full name as it is spoken |
| 40% | A plain 'human or bot?' card settles under the name on 'checks whether you're a human or a bot' |
| 60% | A row of drawn wavy, distorted letters (made-up, labelled 'illustrative') appears with a text box under it, on 'wavy, distorted letters' |
| 85% | Three plain cards land one by one: text, images, audio, on 'text, images and audio' |

### B05 · THE CHECKBOX · 17.75 s · Manim `B05_Checkbox`
A plain drawn checkbox with the words 'I'm not a robot' beside it (plain text, no logo). A cursor ticks it. The click is shown as small, then pushed aside: behind the box three signal chips slide in, 'cookies', 'browsing history', 'mouse movements', feeding a small gate labelled 'confident?'. Two branches leave the gate: 'confident you're human' goes straight through; 'unsure' opens a small grid of drawn picture squares. 'The click itself isn't the test' sits small at the top.

*Note:* Simple drawn checkbox. No reCAPTCHA branding, no real widget.

| At | Event |
|---|---|
| 5% | A drawn checkbox with 'I'm not a robot' draws in; the cursor ticks it on 'the "I'm not a robot" checkbox' |
| 30% | The click shrinks and three chips slide in behind it: cookies, browsing history, mouse movements, on 'signals like your cookies, your browsing history and your mouse movements' |
| 60% | The chips feed a gate 'confident?'; the 'confident' branch goes straight through, on 'you go straight through' |
| 88% | The 'unsure' branch opens a small grid of picture squares, on 'only if it's unsure does it ask you to pick pictures' |

### B06 · NO PUZZLE AT ALL · 12.59 s · Manim `B06_NoPuzzle`
A visitor's path (a short drawn line of a cursor moving across a plain page) is watched by a small eye shape; no puzzle appears. The eye feeds a semicircular dial marked 0 at the left end and 1 at the right end. The needle settles at an example spot near the 0 end; a tag 'closer to 0: more likely a bot' sits there. 'Illustrative score' reads small. The only numbers on screen are 0 and 1.

*Note:* Listen-check 'reCAPTCHA v3'. The needle position is an example, labelled illustrative; it is not a measured score.

| At | Event |
|---|---|
| 5% | 'reCAPTCHA v3' lands as plain text; a plain page with a moving cursor path draws in and no puzzle appears, on 'shows no puzzle at all' |
| 30% | A small eye shape follows the cursor path on 'watches how each visitor behaves' |
| 55% | A dial marked 0 and 1 draws in and the needle swings to an example spot on 'gives a score between zero and one' |
| 85% | The needle settles near 0 and the tag 'closer to 0: more likely a bot' lands, on 'more likely a bot' |

### B07 · CLOUDFLARE'S APPROACH · 20.03 s · Manim `B07_Cloudflare`
Left: a plain browser box quietly running three small background tasks (small gear shapes labelled 'small background challenges') while a tick for 'real browser?' and a tick for 'human behaviour?' appear beside it; no puzzle appears. Right: two plain figures. First a bar labelled 'CAPTCHAs shown' shrinks by 91%; then a stopwatch face whose hand drops from 32 seconds to about 1 second, with 'average check' beneath. No Cloudflare logo, no Cloudflare colours as branding; 'Cloudflare' appears as plain text only where it is spoken.

*Note:* Listen-check Cloudflare. The 91% and 32 s to about 1 s figures are the Cloudflare post's own (about its Managed Challenge, not Turnstile by name); the narration does not say Turnstile and neither does the scene.

| At | Event |
|---|---|
| 5% | 'Cloudflare' appears as plain text; the plain browser box draws in with no puzzle |
| 30% | Three small gears turn quietly inside the box on 'your browser quietly solves small background challenges'; two ticks follow, 'real browser?' and 'human behaviour?' |
| 60% | A bar of 'CAPTCHAs shown' shrinks by 91% on 'fell by ninety-one percent in a year' |
| 85% | A stopwatch hand drops from 32 seconds to about 1 second on 'from thirty-two seconds to about one' |

### B08 · BOTS BEAT HUMANS · 19.95 s · Manim `B08_BotsBeatHumans`
Plain header: '1,400 people, 14,000 CAPTCHAs' above a drawn distorted-text sample. Two rows, 'people' and 'bots (from earlier studies)'. Row 1, time: people 9 to 15 seconds as a long bar, bots under 1 second as a sliver. Row 2, accuracy: people 50 to 84 percent as a range band, bots 99.8 percent as a near-full bar. 'distorted text' labels the whole panel. The ranges are drawn as ranges, not single bars.

*Note:* Listen-check UC Irvine. Figures are the paper's own (Table 3), drawn as ranges where the paper gives ranges.

| At | Event |
|---|---|
| 5% | 'UC Irvine' appears as plain text; the header '1,400 people, 14,000 CAPTCHAs' lands on 'fourteen hundred people solve fourteen thousand CAPTCHAs' |
| 35% | The time row draws: people 9 to 15 seconds as a long bar, on 'nine to fifteen seconds' |
| 60% | The accuracy row draws: people as a band from 50 to 84 percent, on 'fifty to eighty-four percent of the time' |
| 85% | The bots' sliver under 1 second and the near-full 99.8 percent bar land, with 'from earlier studies' small beneath |

### B09 · A HUNDRED PERCENT ON THE PICTURES · 22.51 s · Manim `B09_HundredPercent`
Left: a drawn picture grid with a bar below it that fills to 100 percent beside a shorter earlier bar marked 68 to 71 percent (as a band). Right: the same grid with two chips, 'cookies' and 'browsing history', feeding a small gate labelled 'who's human?', the chips drawn heavier than the grid. 'The picture alone was never the whole test' lands last as framing. ETH Zurich appears as plain text only. No mouse path, no claim that the system faked anything.

*Note:* Listen-check ETH Zurich. The earlier 'fake human signals' line was removed from the script; the scene shows the paper's finding about cookies and browsing history instead. See FACTCHECK.md.

| At | Event |
|---|---|
| 5% | 'ETH Zurich' appears as plain text; a picture grid draws in and a bar fills to 100 percent, with an earlier band at 68 to 71 percent beside it, on 'one hundred percent' and 'sixty-eight to seventy-one' |
| 55% | Two chips, cookies and browsing history, feed a gate 'who's human?' beside the grid, on 'relies heavily on cookies and browsing history' |
| 90% | The line 'The picture alone was never the whole test' lands |

### B10 · WHAT HAPPENS NOW · 16.83 s · Manim `B10_WhatNow`
Four plain steps. A puzzle grid is replaced by a score dial; a small eye over a cursor path stays in the background; a shield at a gate stops a drawn robot labelled 'bad behaviour', with a small tag 'one Cloudflare leader argues' (plain text); a second drawn robot with a small tag 'verified' is checked at the gate, tagged 'companies are working on it'.

*Note:* Drawn shapes only. The blocking-behaviour line is shown as one person's view, as the script now says; see FACTCHECK.md.

| At | Event |
|---|---|
| 5% | A puzzle grid slides away and a score dial takes its place on 'scores instead of puzzles' |
| 30% | A small eye follows a cursor path in the background on 'watch behaviour in the background' |
| 55% | A shield at a gate stops the robot labelled 'bad behaviour' under the small tag 'one Cloudflare leader argues', on 'blocking bad behaviour rather than every bot' |
| 85% | A second robot with a 'verified' tag is checked at the gate on 'verify which AI agents are allowed in' |

### BVDT · VERDICT · 11.46 s · Remotion `ClaudeVerdictArtifact`
Artifact page. Heading "Show you behave like one". Lines are the spoken verdict, word for word.

| At | Event |
|---|---|
| 10% | The artifact page opens on the title |
| 45% | The heading lands: show you behave like one |
| 80% | The closing line lands: from 'prove you're human' to 'show you behave like one' |

### BHTF · YOUR TURN · 19.24 s · Remotion `ClaudeComposerAsk`
Greeting "Your turn.", the prompt is typed and held while the voice reads it.

| At | Event |
|---|---|
| 20% | The suggested prompt types into the composer |
| 70% | The prompt holds on screen while the voice discusses it |

### BOUT · OUTRO · 5.42 s · Remotion `LogoOutro`
Humanitarians AI mark and `@HumanitariansAI` handle. Card length set to the measured 5.42 s.

| At | Event |
|---|---|
| 15% | The Humanitarians AI mark springs in |
| 60% | The @HumanitariansAI handle settles beneath it |

## Not yet done

- Scenes: `scenes.py` (16:9) and `vertical/scenes.py` (9:16, native layouts) for B02 and B04–B10.
- Gates, previews, renders, QC frames, 4K exports, README, SHA-256 records.
- Your listen-check of the regenerated beats and the five words above.
