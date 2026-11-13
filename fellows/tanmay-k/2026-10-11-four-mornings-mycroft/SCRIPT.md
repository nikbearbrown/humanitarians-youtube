# SCRIPT: *Four Mornings* (Week 26 work video, Mycroft PR #64)

**Draft 2, 2026-10-10** (Gate P PASS on draft 1; B09's scaffold line added at Tanmay's request; B02 clause added after the PROOF read-through, needs a Gate P re-read). Angle A, approved by Tanmay 2026-10-10 (see `ANGLE.md`). Structure: FOUR MORNINGS. Every act
opens on the same illustrated dashboard, as its reader sees it over coffee; each morning, one hand-off behind it
slips. The question each time is what they would have seen, and what says so now. Then my own check's morning,
then the same dashboard again. About 720 words, roughly 4:30 at the voice's measured pace.

**Framing:** the zero-price and two-copies behaviours are described as how the workflow works, never as faults; the
recipe leaves them to the maintainers. The only mistake in this film is mine (B07), shown with its fix. Humble,
first person only on the genuine turns (B03, B05, B07). Every price is invented, said once in B02 and labelled on
screen. Committed files only (`FACTCHECK.md`).

**TTS spelling:** numbers in words in the narration; digits on screen only. "Mycroft" keeps its real spelling
everywhere; the audio step feeds Kokoro the override `mˈaɪkɹɔft` (MY-croft) in place of its own `mˈɪkɹɔft`
(MICK-roft), the same phoneme-override method as the topic video's names.

---

### B01 · COLD OPEN, the dashboard over coffee
> Here's a portfolio dashboard, the way its reader sees it over morning coffee. Five stocks. One total, sixty-five thousand and ninety-eight dollars, up twenty-one percent. It looks finished. But every number on this screen arrived through a few quiet hand-offs. Places where one part of the system takes another part's word for it. So let's spend four mornings with this dashboard, and on each one, let one of those hand-offs slip.

*On screen:* the illustrated dashboard (five rows, the total, the percentage), labelled "Illustration · invented prices". Under it, a strip of four hand-offs, unlit. *Refs:* W4.

### B02 · WHAT THIS IS
> Hi, this is Tanmay Kulkarni, in for Humanitarians AI. This week I contributed to Mycroft, which is both a book and a working repository for finance pipelines. It calls them recipes. Two of them sit behind this dashboard. One fetches the prices and does the math. The other calls it and draws the screen. My pull request, now merged, added checks to both, and rebuilt the math step so it runs on test data. Every price you'll see is invented, for testing. Morning one.

*On screen:* the README line quoted, "both a book and a working agentic repository" (Mycroft README); the two recipes as two boxes, "Portfolio Dashboard → calls → Portfolio Price Fetcher"; "PR #64 · merged"; "Every price in this video is invented." *Refs:* W1, W2, W3.

### B03 · MORNING ONE, a price of zero
> The quote for one stock comes back with a price of zero. The workflow reads the price with a JavaScript "or", and to JavaScript, zero counts as missing. So it quietly uses the previous close, five hundred and ninety, and the dashboard looks perfectly normal. The math is right. The reader just doesn't know which price they're looking at. I kept that behaviour exactly, because it's the workflow's choice, not mine, and the recipe now notes it for the maintainers. What changed is the record. For every stock, it now says which price was used.

*On screen:* the dashboard; the META row shows 590 with a small tag "previous close". Evidence panel: `clean/validated.json`, META `price_source: previousClose`; the code line `regularMarketPrice || previousClose`. Hand-off 1 lights. *Refs:* W5, W6, W7, W8.

### B04 · MORNING TWO, a stock the portfolio doesn't hold
> Morning two. A response comes back for a symbol the portfolio doesn't hold. In the original, the calculation looks up how many shares you own, finds nothing, and stops with an error. Now the check before it catches the response first, and sets it aside with a reason. And the calculation refuses to run on anything that check turned away. Nothing half finished reaches the screen.

*On screen:* a stray row "ZZZZ" slides toward the dashboard and is stopped at a gate labelled "step 3: set aside". Evidence panel: the original's two lines `const myStock = portfolio[ticker]; const shares = myStock.shares;` (source: the declared workflow, Calculate Metrics); `defective/validated.json`, reason "meta.symbol 'ZZZZ' is not in the workflow's portfolio"; "step 5: refuses (exit 1)". Hand-off 2 lights. *Refs:* W9, W10.

### B05 · MORNING THREE, one list, written twice
> Morning three, and this one surprised me. The portfolio, which stocks, how many shares, what you paid, is written out twice inside the same workflow. One copy decides which prices to fetch. The other one does the math. Edit the shares in the first, and the math keeps using the second. The total doesn't move, and nothing says why. So the first step now reads both copies, and stops if they disagree, naming the difference.

*On screen:* two small copies of the portfolio side by side ("Define Portfolio", "Calculate Metrics"); NVDA shares 50 in one becomes 55; the total stays put. Evidence panel: self-test A, "the two portfolio definitions disagree (NVDA shares 50 vs 55): exit 1". Hand-off 3 lights. *Refs:* W11, W12, W13.

### B06 · MORNING FOUR, the call by name
> Morning four. The dashboard doesn't hold any prices itself. It calls the price workflow, and it finds it by name. The ID that would pin it down is still a placeholder. So the dashboard's first step now checks that the name it calls is the price workflow's real name, and stops if it isn't.

*On screen:* the arrow "calls → Portfolio Price Fetcher"; the id field shows `YOUR_WORKFLOW_1_ID`. Evidence panel: the dashboard provenance record's note; self-test A, "dashboard calls a different workflow by name: exit 1". Hand-off 4 lights. *Refs:* W14, W15.

### B07 · THE MORNING IT WAS MY OWN CHECK
> And then there was the morning it was my own check. To make sure these checks could actually fail, I broke my own calculation on purpose, and ran the test that's meant to catch it. It passed. All green. But the broken version had never run at all. My test was grading a file left over from the good run. A check that can't fail is worse than no check, because it looks like one. Now the test won't grade anything unless the broken version really ran. And then it catches the break, down to a single cent.

*On screen:* a test result flipping from "pass" (struck through) to "broken port ran: true · original 11298.13 vs port 11298.12 · caught". Evidence panel: the self-test script's comment, quoted short; self-test D row. *Refs:* W16, W17.

### B08 · WHAT THE READER STILL SEES
> So here's the same dashboard, on any morning. Nothing on the screen changed. What changed is behind it. Four hand-offs that now speak up when they slip. And some that still run on trust. Fetching live prices. Three more steps in one recipe, and five in the other. Both recipes are still drafts, and they say so.

*On screen:* the dashboard as in B01; the four hand-offs lit; beyond them, greyed: "live prices", "price fetcher steps 2, 4, 6", "dashboard steps 2–6". Evidence: both recipes' frontmatter (`status: DRAFT`, `todos_open` 4 and 7). *Refs:* W18, W19.

### B09 · CLOSE
> Pick one number you look at every morning. What is it quietly taking on trust? And if that trust slipped, what would tell you? A good answer names the hand-off, and the thing that would say so. "It's always been right" doesn't count.

*On screen:* the dashboard, softly dimmed; the question; below it, "Good answer: names the hand-off, and what would say so · Not an answer: \"it's always been right\"". *Refs:* none.

### B10 · OUTRO
> Four mornings. Tanmay Kulkarni, in for Humanitarians AI, signing off.

*On screen:* title outro. *Refs:* none.
