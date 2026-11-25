# FACTCHECK — Week 6 Progress

Narration is `SCRIPT.md` verbatim. Nothing in the script was changed by this check, and no claim or source was added.
Every claim was checked against your Week 6 explainer's own files (`README.md`, `FACTCHECK.md`, `FRICTIONAL.md`,
`beat_sheet.json`, `vertical/beat_sheet.json`, `scenes.py`, `vertical/scenes.py`, `TYPECHECK.md`, `vertical/TYPECHECK.md`)
and the toolkit's text-size gate (`runtime/scripts/type_check.py`, read only).

**Verdicts:** SUPPORTED (a file says it) · SIMPLIFIED (true in outline; the row says what is looser) ·
FLAG (the line says more or something different from the files; your decision) · EXEMPT (your own experience or view) ·
PROCESS (a statement about this video).

**Tally (25 claims):** 13 SUPPORTED · 6 SIMPLIFIED · 0 FLAG · 4 EXEMPT · 2 PROCESS.

## Decisions for you

Both earlier flags (beats 4 and 7) were resolved by your edits to `SCRIPT.md`; see rows 13 and 22. Nothing is flagged now.

Pronunciation (not a fact, but needs your ear): your explainer's `beat_sheet.json` sets only "Keya"; there is no CAPTCHA
entry to carry over, and its `SCRIPT.md` says "CAPTCHA to be checked by ear". In this script the word appears once,
plural ("CAPTCHAs", beat 2). Kokoro's phonemes for it are `kˈæpttʃə`, which drops the plural "s" and may add a "t" before
"ch". Listen to beat 2. If it is wrong, say what you want and the one beat is regenerated.

## Claims by beat

| # | Beat | Claim | Verdict | Evidence |
|---|---|---|---|---|
| 1 | 1 | "this is my week six progress update for the Brutalist project, where I'm learning film as code" | SUPPORTED | Explainer `README.md`: "Reporting period: Week 6". "Film as code" is the project's own name (your Week 3 log). |
| 2 | 1 | "The voice you're hearing is an AI voice reading my script." | PROCESS | True: Kokoro `af_bella`. Required disclosure. |
| 3 | 2 | The explainer is "How Do Websites Know I'm Not a Robot?" | SUPPORTED | Explainer `README.md` title and `beat_sheet.json`. |
| 4 | 2 | "I researched CAPTCHAs on websites and in two research studies" | SUPPORTED | Explainer `README.md`: research from Wikipedia, a Merchant Risk Council post, Cloudflare's blog, IT Brew, and "the UC Irvine and ETH Zurich studies". Explainer `FACTCHECK.md` reads the Searles et al. (UC Irvine) and Plesner et al. (ETH Zurich) papers in full. |
| 5 | 2 | "and built the video with Claude Code" | SUPPORTED | Explainer `README.md`: "Claude Code wrote the beat sheets, Manim scenes, fact check, shot list and prompts, and ran the builds". |
| 6 | 2 | "Everything in this update was new for me." | EXEMPT | Your own experience. |
| 7 | 3 | "I went deeper into film as code this week, especially how landscape and vertical videos are built." | SIMPLIFIED | The explainer has both a landscape and a vertical build with their own beat sheets and scenes. "Deeper" is your view: Week 3 also built both orientations. |
| 8 | 3 | "The narration is the same" | SUPPORTED | All 13 narration texts in the explainer's `beat_sheet.json` and `vertical/beat_sheet.json` are identical (compared line by line). |
| 9 | 3 | "but the checks are not" | SUPPORTED | The text-size floor differs (rows 10 and 11), and the vertical build also keeps all text above 86% of the frame height (`portrait_layout` in the vertical beat sheet). |
| 10 | 3 | "a landscape video needs at least forty-one pixels" | SIMPLIFIED | `type_check.py`: floor is 1.9% of frame height, `int(2160 x 1.9 / 100)` = 41. Explainer `TYPECHECK.md`: "floor 41px". The gate measures the height of the text's ink, not the font size, so "text size" is a plain-words short form. |
| 11 | 3 | "and a vertical video needs at least seventy-two" | SIMPLIFIED | Same rule at 3840 px: `int(3840 x 1.9 / 100)` = 72. Explainer `vertical/TYPECHECK.md`: "floor 72px". Same note on ink height versus font size. |
| 12 | 4 | "I set myself a rule: nothing goes in unless it's checked against a source" | SUPPORTED | Explainer `README.md`: "A rule for this video: nothing goes in that isn't checked against a listed source." |
| 13 | 4 | "the fact check flagged five things to fix, from lines that said more than the sources did to one source that couldn't be opened" | SUPPORTED | Explainer `FRICTIONAL.md` lists five fixes: counts from a news report that differed from the paper; "had to fake human signals" stronger than the paper; one person's opinion written as a trend; a verdict that sounded like puzzles were gone; "one article couldn't be opened at all". Explainer `FACTCHECK.md` decisions A to E match. "Five things to fix" covers all five; "lines that said more" covers the overstated lines; "one source that couldn't be opened" is the fifth. |
| 14 | 4 | "Because every line pointed to a source, each one was easy to fix." | SUPPORTED | Explainer `FRICTIONAL.md`: "every line pointed to a source I could compare against"; "The rule made the fixes easy". |
| 15 | 5 | "The text-size check surprised me." | EXEMPT | Your own reaction. |
| 16 | 5 | "It flagged tick marks on a dial, because it read them as tiny letters." | SIMPLIFIED | Explainer `FRICTIONAL.md`: Gate T "flagged three beats where drawn shapes (dial ticks and a fading outline) were read as small text". Dial ticks were one of two causes; "tiny letters" is a plain form of "small text". |
| 17 | 5 | "Making them a paler colour fixed it" | SIMPLIFIED | `FRICTIONAL.md`: "lightened or re-timed the flagged shapes". The explainer's dial calls pass a pale colour in some scenes (`dial(..., PALE)` in the landscape B10 and vertical B06); the fading outline was fixed by timing, not colour. |
| 18 | 5 | "without changing any words" | SUPPORTED | The narration is identical in both builds (row 8), and `FRICTIONAL.md` describes only shape and timing changes. |
| 19 | 6 | "My vertical verdict card was a numbered list" | SUPPORTED | Explainer `README.md` and `FRICTIONAL.md`. |
| 20 | 6 | "but one sentence was split across four numbers, so it read oddly" | SUPPORTED | `README.md`: "a numbered list had split one sentence across four items"; `FRICTIONAL.md`: "read oddly as a numbered list". |
| 21 | 6 | "I rewrote it as four complete thoughts." | SUPPORTED | Explainer `vertical/beat_sheet.json`, BVDT: four `artifactLines`, each a full sentence. |
| 22 | 7 | "More and more websites check how I behave" | SIMPLIFIED | Matches the explainer's own wording. Explainer `FACTCHECK.md` row 6: IT Brew says AI success "is forcing industry pros to explore new methods... including systems that analyze behavior"; row 37: no listed source counts how many websites have changed, so "more and more" is a trend claim without a number. Cookies, browsing history and mouse movement are the sourced signals (rows 13 and 39). |
| 23 | 7 | "and a check is only as good as what it measures" | EXEMPT | Your own view. No source states it. It fits the ETH finding that reCAPTCHA leans on cookies and history, but that is not claimed here. |
| 24 | 7 | "This week, I learned to check my videos the same way: every claim needs a source, and every frame needs a second look." | EXEMPT | Your own account; matches the rule (row 12) and `FRICTIONAL.md`: "watching every preview myself catches problems the gates don't". |
| 25 | 8 | "Week 6 Progress. Built with Claude, for Humanitarians AI." | PROCESS | Describes this video. |

## Visuals

- Drawn shapes only: a plain grid of squares for CAPTCHAs, drawn paper pages for the two studies, a drawn terminal for Claude Code, a film-frame outline, a dial, numbered bars, a video frame, an eye.
- No Google, reCAPTCHA or Cloudflare logos, no screenshots of real challenge pages, no real company or tool logos. "Claude Code" appears as plain text on a chip.
- The only figures on screen are "41 px" and "72 px" (rows 10 and 11) and the digits 1 to 4 on the numbered list.
- The opening composer's three lines ("Week 6 progress", "Film as code, deeper", "Checking every claim") are labels for what this video covers, not claims.
- No dates on screen or in these files.
