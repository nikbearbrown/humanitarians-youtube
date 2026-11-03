# READ-ALOUD: Gate P sheet (work video)

*Four Mornings* (working title) · structure: FOUR MORNINGS · voice `am_onyx`

Generated from `SCRIPT.md` by `make_read_sheet.py`. Read each beat aloud at speaking pace, top to bottom, in one
sitting; tick or note; skim the *on screen* line too. Reply **"Gate P PASS"** or list the beats that tripped you.

## Say-it-right checklist (Kokoro's phonemes, checked 2026-10-10)

| Word | Should sound like | Kokoro alone | Override | Where |
|---|---|---|---|---|
| Mycroft | MY-croft | `mˈɪkɹɔft ✗ (MICK-roft)` | `mˈaɪkɹɔft` | B02 |
| Tanmay Kulkarni | TAN-may kul-KAR-nee | `tˈænmeɪ kˈʌlkɑːɹni ✓` | `—` | B02, B10 |
| a JavaScript "or" | jah-vuh-script OR | `dʒˈɑːvə skɹˈɪpt "ɔːɹ" ✓` | `—` | B03 |

## Where to listen hardest

- **B01**: the cold open has to sound like a normal morning, then turn on "But every number…"
- **B03**: "The math is right. The reader just doesn't know": calm, not alarmed; it is the workflow's choice
- **B05**: **"this one surprised me"**: a genuine turn, said lightly
- **B07**: **the turn.** "It passed. All green." then the drop: "But the broken version had never run at all."
- **B08**: the cool-down: plain and honest; "and they say so" without a flourish
- **B09**: a real question to the viewer, unhurried

## The script

### [0:00] B01 · COLD OPEN, the dashboard over coffee

Here's a portfolio dashboard, the way its reader sees it over morning coffee. Five stocks. One total, sixty-five thousand and ninety-eight dollars, up twenty-one percent. It looks finished. But every number on this screen arrived through a few quiet hand-offs. Places where one part of the system takes another part's word for it. So let's spend four mornings with this dashboard, and on each one, let one of those hand-offs slip.

<sub>**On screen:** the illustrated dashboard (five rows, the total, the percentage), labelled "Illustration · invented prices". Under it, a strip of four hand-offs, unlit. *Refs:* W4.</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [0:21] B02 · WHAT THIS IS

Hi, this is Tanmay Kulkarni, in for Humanitarians AI. This week I contributed to Mycroft, which is both a book and a working repository for finance pipelines. It calls them recipes. Two of them sit behind this dashboard. One fetches the prices and does the math. The other calls it and draws the screen. My pull request, now merged, added checks to both, and rebuilt the math step so it runs on test data. Every price you'll see is invented, for testing. Morning one.

<sub>**On screen:** the README line quoted, "both a book and a working agentic repository" (Mycroft README); the two recipes as two boxes, "Portfolio Dashboard → calls → Portfolio Price Fetcher"; "PR #64 · merged"; "Every price in this video is invented." *Refs:* W1, W2, W3.</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [0:46] B03 · MORNING ONE, a price of zero

The quote for one stock comes back with a price of zero. The workflow reads the price with a JavaScript "or", and to JavaScript, zero counts as missing. So it quietly uses the previous close, five hundred and ninety, and the dashboard looks perfectly normal. The math is right. The reader just doesn't know which price they're looking at. I kept that behaviour exactly, because it's the workflow's choice, not mine, and the recipe now notes it for the maintainers. What changed is the record. For every stock, it now says which price was used.

<sub>**On screen:** the dashboard; the META row shows 590 with a small tag "previous close". Evidence panel: `clean/validated.json`, META `price_source: previousClose`; the code line `regularMarketPrice || previousClose`. Hand-off 1 lights. *Refs:* W5, W6, W7, W8.</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [1:15] B04 · MORNING TWO, a stock the portfolio doesn't hold

Morning two. A response comes back for a symbol the portfolio doesn't hold. In the original, the calculation looks up how many shares you own, finds nothing, and stops with an error. Now the check before it catches the response first, and sets it aside with a reason. And the calculation refuses to run on anything that check turned away. Nothing half finished reaches the screen.

<sub>**On screen:** a stray row "ZZZZ" slides toward the dashboard and is stopped at a gate labelled "step 3: set aside". Evidence panel: the original's two lines `const myStock = portfolio[ticker]; const shares = myStock.shares;` (source: the declared workflow, Calculate Metrics); `defective/validated.json`, reason "meta.symbol 'ZZZZ' is not in the workflow's portfolio"; "step 5: refuses (exit 1)". Hand-off 2 lights. *Refs:* W9, W10.</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [1:35] B05 · MORNING THREE, one list, written twice

Morning three, and this one surprised me. The portfolio, which stocks, how many shares, what you paid, is written out twice inside the same workflow. One copy decides which prices to fetch. The other one does the math. Edit the shares in the first, and the math keeps using the second. The total doesn't move, and nothing says why. So the first step now reads both copies, and stops if they disagree, naming the difference.

<sub>**On screen:** two small copies of the portfolio side by side ("Define Portfolio", "Calculate Metrics"); NVDA shares 50 in one becomes 55; the total stays put. Evidence panel: self-test A, "the two portfolio definitions disagree (NVDA shares 50 vs 55): exit 1". Hand-off 3 lights. *Refs:* W11, W12, W13.</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [1:58] B06 · MORNING FOUR, the call by name

Morning four. The dashboard doesn't hold any prices itself. It calls the price workflow, and it finds it by name. The ID that would pin it down is still a placeholder. So the dashboard's first step now checks that the name it calls is the price workflow's real name, and stops if it isn't.

<sub>**On screen:** the arrow "calls → Portfolio Price Fetcher"; the id field shows `YOUR_WORKFLOW_1_ID`. Evidence panel: the dashboard provenance record's note; self-test A, "dashboard calls a different workflow by name: exit 1". Hand-off 4 lights. *Refs:* W14, W15.</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [2:14] B07 · THE MORNING IT WAS MY OWN CHECK

And then there was the morning it was my own check. To make sure these checks could actually fail, I broke my own calculation on purpose, and ran the test that's meant to catch it. It passed. All green. But the broken version had never run at all. My test was grading a file left over from the good run. A check that can't fail is worse than no check, because it looks like one. Now the test won't grade anything unless the broken version really ran. And then it catches the break, down to a single cent.

<sub>**On screen:** a test result flipping from "pass" (struck through) to "broken port ran: true · original 11298.13 vs port 11298.12 · caught". Evidence panel: the self-test script's comment, quoted short; self-test D row. *Refs:* W16, W17.</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [2:44] B08 · WHAT THE READER STILL SEES

So here's the same dashboard, on any morning. Nothing on the screen changed. What changed is behind it. Four hand-offs that now speak up when they slip. And some that still run on trust. Fetching live prices. Three more steps in one recipe, and five in the other. Both recipes are still drafts, and they say so.

<sub>**On screen:** the dashboard as in B01; the four hand-offs lit; beyond them, greyed: "live prices", "price fetcher steps 2, 4, 6", "dashboard steps 2–6". Evidence: both recipes' frontmatter (`status: DRAFT`, `todos_open` 4 and 7). *Refs:* W18, W19.</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [3:01] B09 · CLOSE

Pick one number you look at every morning. What is it quietly taking on trust? And if that trust slipped, what would tell you? A good answer names the hand-off, and the thing that would say so. "It's always been right" doesn't count.

<sub>**On screen:** the dashboard, softly dimmed; the question; below it, "Good answer: names the hand-off, and what would say so · Not an answer: \"it's always been right\"". *Refs:* none.</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [3:14] B10 · OUTRO

Four mornings. Tanmay Kulkarni, in for Humanitarians AI, signing off.

<sub>**On screen:** title outro. *Refs:* none.</sub>

> ☐ reads cleanly   ☐ note: ______________________

_10 beats · 653 words · about 3:17 at 3.3 words/s, before holds._
