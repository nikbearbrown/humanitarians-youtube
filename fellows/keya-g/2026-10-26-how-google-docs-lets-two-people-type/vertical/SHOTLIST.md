# SHOTLIST — How Google Docs Lets Two People Type in the Same Sentence

Typed work order. Thirteen beats. Narration is `SCRIPT.md` verbatim. Beat IDs B01–B10 match script sections 1–10, so
"beat 4" and "beat 9" mean the same thing here as in the script. BVDT, BHTF and BOUT are sections 11, 12 and 13.

**Status: audio approved. Scenes written: `scenes.py` (16:9) and `vertical/scenes.py` (9:16, native layouts). Gates A, W
and B pass on both. Low-quality previews with audio are in `_preview/`. No finals are rendered. Nothing is published.**

## Rules for every visual

- Simple illustrative graphics only: two plain browser windows, the letters a b c, operations moving to a server, a
  revision log, cursors, two copies that change on their own and end up the same.
- **No Google logo, no Google Docs interface or screenshots, no Google colour scheme used as branding, no other
  branding.** The word "Google Docs" may appear as plain text only where the narration says it. The windows are drawn
  rectangles holding a line of text, not a copy of any product's interface. No toolbar, no share button, no avatars.
- Every example, packet, tag and log is an illustration, not data. The only numbers on screen are slot numbers 1 2 3
  under the a-b-c tiles and the numbers 1 and 2 in the revision log; they label an example and are not measurements.
  No percentages.
- The blog's example editors are not used. The two people are "me" and "teammate".
- **Portrait (9:16):** all text sits above 86% of the frame height (y < 0.86 × H); the bottom 14% stays empty. 9:16
  gets its own native layouts, not a crop of 16:9: one idea at a time, stacked, bigger type. Portrait text is never
  scaled. Font sizes are set directly with a 32 pt floor, which is an x-height of about 87 px at 2160 px wide, above your
  72 px rule.
- Palette `humanitarians`: ink `#2F2A26`, terracotta `#E4572E` (one accent per beat; in the two-person beats it marks
  "me"), teal `#1F4E5F` (marks "my teammate" and the kept, merged result), ground `#F3EBDD`.
- No dates on screen or in files.
- Un-highlighted elements never fade below about 40% opacity.
- On-screen text shows **Ctrl+Z**; the narration says "Control Z". The verdict page keeps "Control Z" to match the spoken
  line.
- Math: none. The example is a row of letters; no formula is shown.

## Library check

`./art scenes` was searched first for: two browser windows sharing a document, operations sent to a server and
acknowledged, revision log history list, the typed-then-corrected overview, text cursors of two collaborators, characters
with ID tags (an earlier idea, since dropped), letters a b c insert and delete shift, two copies client and server sync, a keyboard key press Ctrl Z undo,
packets travelling between client and server, two versions merge in any order without a central server, a slow connection
and delayed text, and two edits side by side.

| Need | Result |
|---|---|
| Typed and corrected overview | **Hit:** `BrutalistHesitantWriter` and `BrutalistHesitantWriter916` |
| Cold open, Your Turn | **Hit:** `ClaudeComposerAsk` and `ClaudeComposerAsk916` |
| Verdict page | **Hit:** `ClaudeVerdictArtifact` and `ClaudeVerdictArtifact916` |
| Outro | **Hit:** `LogoOutro` and `LogoOutro916` (same as Keya's earlier films) |
| Two windows with overlapping typing and Ctrl+Z | **Miss.** Lead read and rejected: `BrowserCapture` shows a real captured web page, which is not allowed here. Custom Manim. |
| a-b-c insert and delete shift | **Miss.** Nothing close among the results. Custom Manim. |
| Client and server change flow, acknowledgements | **Miss.** Leads read and rejected: the `BuildMcpServer*` and `McpIntAnatomy` figures (MCP deployment diagrams). Custom Manim. |
| Revision log | **Miss.** Lead read and rejected: `HaiBrutalistE10Revise` (a video revision loop). Custom Manim. |
| Cursors, per-author colour, delayed text | **Miss.** Custom Manim. |
| Two copies changing on their own and ending up the same | **Miss.** The earlier "characters with ID tags" search was a PUNT; the tool's `TEMPLATE-MISSES.md` line for it was reverted at your request. Not re-searched. Custom Manim. |
| Slow connection, two rewrites side by side | **Miss.** Custom Manim. |

A genuine miss is a design card, not a licence to slate. The misses are custom scenes in this reel's own `scenes.py`,
which is still to be written. `./art scene-index` is not needed because no component is added to the library.

## Audio (the master clock)

Kokoro `af_bella`, generated. Pronounce: `Keya` only (`kˈeɪjɛə`); see `PROMPTS.md`. Seconds are from the generated files.
Total about 3 minutes 28 seconds. B03, B06, B07 and B09 were regenerated after the script edits.

| Beat | s | Beat | s |
|---|---|---|---|
| B01 | 10.33 | B08 | 16.17 |
| B02 | 18.07 | B09 | 15.83 |
| B03 | 9.51 | B10 | 17.45 |
| B04 | 19.80 | BVDT | 17.39 |
| B05 | 15.13 | BHTF | 16.28 |
| B06 | 21.76 | BOUT | 6.76 |
| B07 | 23.47 | | |

The `go()` times inside each Manim scene must come from word timings measured on these files, not from estimates.

## Beats

### B01 · INTRO · 10.33 s · Remotion `ClaudeComposerAsk`
Greeting "Hi, Keya", topic "Irreducibly Human", segment is the title, folder chip `@HumanitariansAI`.

| At | Event |
|---|---|
| 10% | The ask types in: "Explain how Google Docs lets two people type in the same sentence." |
| 55% | Three result lines land: Your change goes to a server · Other people's changes are shifted to fit · Every copy ends up the same |
| 85% | The answered composer holds while the AI-voice disclosure is spoken |

### B02 · HOOK · 18.07 s · Manim `B02_Hook`
Your own experience and test. Two plain windows, side by side, each with the same line of text. A terracotta cursor for
you, a teal cursor for your teammate.

| At | Event |
|---|---|
| 5% | Two windows draw in; "shared document" reads small above them |
| 30% | Two cursors type into the same line and the two bits of text overlap for a moment |
| 55% | A Ctrl+Z key chip presses in the left window; a question mark floats up: "my teammate's work too?" |
| 75% | Only the left window's (terracotta) words disappear; the right window's (teal) words stay |
| 92% | "How does it keep track?" lands between the windows |

### B03 · OVERVIEW · 9.51 s · Remotion `BrutalistHesitantWriter`
No lead silence, as in the week 5 film. The audio is now 9.51 s, over the 9 s minimum for the typed overview. Check after
rendering that the correction is fully on screen before the cut.

| At | Event |
|---|---|
| 10% | "The last person to type wins." types in terracotta |
| 40% | It pauses, then deletes the whole sentence |
| 55% | "Every keystroke gets merged." types in ink |
| 90% | The corrected sentence holds while the voice says "Let's see how, step by step" |

### B04 · THE PROBLEM · 19.80 s · Manim `B04_TheProblem`
Tiles a, b, c with slot numbers 1 2 3. Labelled "illustrative example".

| At | Event |
|---|---|
| 5% | "Why this is hard" lands; three tiles draw in with slot numbers beneath |
| 30% | Two labels appear at once: "me: add x at the start" and "teammate: delete the third letter", with an arrow on c |
| 55% | The x tile drops in at the front and a, b, c slide one place right; the slot numbers stay put, so slot 3 now sits under b |
| 80% | The teammate's delete arrow, unchanged, lands on b and crosses it out in terracotta: "wrong letter"; c is left standing |

### B05 · TWO COPIES · 15.13 s · Manim `B05_TwoCopies`
Only changes travel; the page never moves.

| At | Event |
|---|---|
| 5% | Two boxes draw in, "your browser" and "the server", each holding a small page; "runs in two places" lands |
| 35% | One small packet, "insert x", leaves the browser for the server; the page stays |
| 65% | A packet from someone else travels back and lands on the browser's page |
| 88% | Small lists settle under each box: the browser's "changes not yet sent" and "sent, not yet acknowledged"; the server's "changes received", "revision log", "current document" |

### B06 · OPERATIONAL TRANSFORMATION · 21.76 s · Manim `B06_Transformation`
Same tiles as B04, so the viewer sees the problem solved. The narration now opens "Google's engineers explained that Docs
solves this with…"; no visual change.

| At | Event |
|---|---|
| 5% | "operational transformation" lands; the a, b, c tiles return |
| 30% | Two operation chips appear: "insert x at the start" and "delete the third letter" |
| 55% | The chips clash; a diamond labelled "transform" opens and the delete chip is rewritten to fit the insert |
| 80% | The delete arrow slides from slot 3 to slot 4, lands on c, and c is removed: x a b |

### B07 · THE COLLABORATION PROTOCOL · 23.47 s · Manim `B07_Protocol`
The longest beat. Acknowledgement goes to the sender; the change goes to the other editor.

| At | Event |
|---|---|
| 5% | "transforming isn't enough" lands; a server column draws between "me" and "teammate" |
| 30% | Two packets arrive at the server; the first is numbered 1, the second 2 |
| 55% | For each packet the sender gets a check, "acknowledged", and the other editor receives the change |
| 85% | Both changes sit stacked in the server's "revision log: the complete history of the document" |

### B08 · CURSORS AND DELAY · 16.17 s · Manim `B08_CursorsDelay`
Your own test. The "who made each change" layer is marked "my guess", because it is your inference.

| At | Event |
|---|---|
| 5% | "In my test" lands; a window draws in with a typed line, each letter underlined in the colour of who typed it |
| 30% | Ctrl+Z presses and only the terracotta letters vanish; a tag, "who made each change?", appears, marked "my guess" |
| 60% | A teal cursor with a "teammate" tag slides into the line |
| 85% | A teal letter travels to a small server box and back and lands a beat after the cursor: "a moment late" |

### B09 · ANOTHER WAY: CRDTS · 15.83 s · Manim `B09_Crdts`
New visual: copies changing on their own and ending up the same. No ID tags, no server, no "any order" claim. Labelled
"simplified", with "I'm just starting to learn" small at the top. Listen to how "CRDTs" is spoken before building this
scene.

| At | Event |
|---|---|
| 5% | "CRDT: conflict-free replicated data type" lands; "I'm just starting to learn" appears small |
| 35% | Two copies of the same short line draw in side by side. Each is changed on its own, at the same time: a terracotta letter appears in the left copy and a teal letter in the right, with no message passing first |
| 65% | A dashed "no coordination" gap holds between the copies on "without coordinating with the others" |
| 90% | The two changes cross over and both copies end on the identical line: "the copies still end up the same"; "simplified" appears small |

### B10 · WHERE IT GETS MESSY · 17.45 s · Manim `B10_Messy`
Your own experience on the left, your framing on the right (labelled "framing, not a measurement").

| At | Event |
|---|---|
| 5% | "In my experience" lands; a long dotted path to a server box draws in, and a letter crawls along it |
| 30% | The late letter overlaps the line for a moment, then settles |
| 60% | The right panel opens: one sentence rewritten two ways, a terracotta version and a teal version |
| 85% | Both rewrites stay merged in the line side by side; a question mark lands: "which wording did the team want?" |

### BVDT · VERDICT · 17.39 s · Remotion `ClaudeVerdictArtifact`
Heading "Shifted, ordered and shared". Three lines, each matching the narration word for word.

### BHTF · YOUR TURN · 16.28 s · Remotion `ClaudeComposerAsk`
Greeting "Your turn." The prompt types in and holds while the voice reads and discusses it. The spoken ending, "And next
time you edit a shared document, ask: whose change just moved my text?", is narration only, not on screen, as in
`SCRIPT.md`.

### BOUT · OUTRO · 6.76 s · Remotion `LogoOutro`
Humanitarians AI mark, `@HumanitariansAI` beneath it. No subline. Sparse by design.

## For the build, later

- Vertical (9:16) is a separate beat sheet with its own native layouts, as in the week 5 folder.
- Before a render, run the toolkit's gates in order and do not skip any. After a render, look at the frames
  (`_qc/` and the qc sheet); the file check alone is not a review.
- The pantry is empty: no photographs, screenshots or stills are needed.
