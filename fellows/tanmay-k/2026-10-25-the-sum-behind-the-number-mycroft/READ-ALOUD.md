# READ-ALOUD — long film (16:9), draft 1.1

Narration only, in order, as the voice will say it. Read it aloud once, at your own pace, and mark anything that trips your tongue, rushes, or sounds unlike you. **For your read, not the Gate P sign-off.** Numbers are in words, as Kokoro will say them; digits appear only on screen.

**B01 · COLD OPEN, the number** (38 words)

Tech sector crash: minus seventy-eight percent. That is what one scenario did to a portfolio of three invented chip stocks, ten thousand dollars taken down to twenty-two hundred. Where does seventy-eight come from? Let me take it apart.

**B02 · WHAT THIS IS** (74 words)

Hi, this is Tanmay Kulkarni, in for Humanitarians AI. This week I contributed to Mycroft, a book and a working repository of finance pipelines, and it calls them recipes. One of them, the Scenario Stress Testing Agent, shocks a portfolio with a named scenario and reports what is left. The portfolios here are mine, invented. The tickers come from the workflow's own list. The numbers are scenario arithmetic, not predictions, and not investment advice.

**B03 · A SCENARIO IS A LIST** (73 words)

A scenario is a short list of named shocks. Tech Sector Crash names five. Four are price shocks: market, minus fifteen percent; technology sector, minus thirty; semiconductors, minus thirty-five; and AI stocks, minus forty. The fifth is a volatility number. The engine's rule is simple: for each holding, add up the shocks that belong to it. Hold a guess: if the market alone falls fifteen percent, how far does the biggest holding fall?

**B04 · ONE HOLDING, ONE BLOCK AT A TIME** (85 words)

Take the biggest holding, a chip designer. Everything belongs to the market, so a block of minus fifteen. It is a semiconductor stock, so minus thirty-five. And it is on the AI list, so minus forty. The engine adds them: minus ninety. The workflow's own README prints this exact sum as its worked example, which is a big part of why it is so easy to check. It even names a different way to combine them, so the rule is a choice you can see.

**B05 · THE SAME CRASH, DIFFERENT HOLDINGS** (63 words)

The third holding is a chip maker that is not on the AI list. A block of minus fifteen for the market, minus thirty-five for semiconductors. That is minus fifty, not ninety. The second chip stock takes minus ninety, like the first. Now give each its share: forty percent, thirty, thirty. Thirty-six, plus twenty-seven, plus fifteen makes seventy-eight, and there is the number.

**B06 · A MILDER SCENARIO, THE SAME RULE** (73 words)

A smaller scenario shows the same rule. An aggressive rate hike: market, minus ten percent; growth stocks, minus twenty; technology sector, minus fifteen. Four growth names, equal shares. Three of them take minus thirty. One is also filed under the technology sector, so a third block lands on it, and it takes minus forty-five. The book loses thirty-three point seven five percent, which the workflow labels critical, its word for losses above thirty.

**B07 · THE TURN, MY ADDER** (71 words)

Here is the part I wanted to be sure of. To check the original, I wrote a second adder, a Python copy of the engine and its first steps, and ran both on the same portfolios. The original code comes straight out of the workflow file. On twenty-four requests, every number, every label and every message matched. Then I added twelve deliberate breaks to my checks, and each one was caught.

**B08 · WHAT THE CHECKS PROTECT** (82 words)

Before any adding, a validator reads each portfolio, with the workflow's own rules and one addition of mine, and it protects the sum. Portfolios whose shares total six tenths, or one point two, are accepted, because the workflow rescales them to one. A holding with no ticker, a share that is not a number, an empty list: each is stopped, with its reason written down. Ten out of ten of my deliberately flawed portfolios. A sum of nothing never reaches the screen.

**B09 · A GOOD LIST FOR NEXT TIME** (49 words)

Nothing here calls the outside world. The call to a model, the market-data request and the reply to a caller are written down as hand-offs, not approved. Five items in the recipe are still open, and it says draft, on purpose. That leaves a good list for next time.

**B10 · CLOSE** (34 words)

So next time a stress test gives you one number, ask what was added: which shocks, from which lists, and has anyone run the adder beside the original? A good answer names the terms.

**B11 · OUTRO** (17 words)

This was Tanmay Kulkarni, for Humanitarians AI. The contribution is pull request seventy-four on the Mycroft repository.

---
11 lines · 659 words
