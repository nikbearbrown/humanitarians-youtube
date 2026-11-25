# FACTCHECK — How Do Websites Know I'm Not a Robot?

Narration is `SCRIPT.md` verbatim. Nothing in the script was changed by this check. Where a claim is weaker than the
sentence that carries it, the row says so and suggests a wording for you to decide on. No source outside the list in
`SCRIPT.md` was used, and no claim or source was added.

## How this was checked

Each source listed in `SCRIPT.md` was fetched and read. A claim is SUPPORTED only where a fetched page says it.

| Source (as listed in `SCRIPT.md`) | What was actually read |
|---|---|
| Wikipedia, "CAPTCHA" | Whole page text. |
| Merchant Risk Council, PayPal member blog | Whole post. |
| Cloudflare blog, "The end of the road for Cloudflare CAPTCHAs" | Whole post. |
| Searles et al., "An Empirical Study & Evaluation of Modern CAPTCHAs" (arXiv) | Abstract page, plus the arXiv HTML version of the full paper (Tables 2, 3 and 4 included). No PDF reader was available here; the HTML is the same paper. |
| The Register, "So much for CAPTCHA then…" | Whole article. |
| Plesner, Vontobel and Wattenhofer, "Breaking reCAPTCHAv2" (arXiv) | arXiv HTML version of the full paper: abstract, introduction, methodology, results, Tables I to III. |
| TechSpot | Removed from your script and source list. It had refused automated fetches earlier and is not used. |
| IT Brew, "As AI solves CAPTCHAs, what's next?" | Whole article. |
| Your own experience | Not checkable. Taken as you describe it. |

**Verdicts:** SUPPORTED (a fetched source says it) · PARTLY (some of it, or it joins things the source keeps apart, or the
source is weaker than the sentence) · SIMPLIFIED (true in outline) · NOT STATED (no listed source says it) · EXEMPT (your
own experience or view, so not a sourced claim) · PROCESS (a statement about this video).

**Tally (49 claims):** 26 SUPPORTED · 16 SIMPLIFIED · 0 PARTLY · 2 EXEMPT · 5 PROCESS · 0 NOT STATED.

Your edits resolved all five earlier decision items (A to E); see "Your five decisions, resolved" below. No new decision is needed. Nothing in `SCRIPT.md` was changed by this check.

## Claims by beat

| # | Beat | Claim | Verdict | Evidence |
|---|---|---|---|---|
| 1 | 1 | "Hi, I am Keya, and this video is about…" opens the video. | PROCESS | Matches the required opening line in `docs/FELLOWS-SUBMISSION.md`. |
| 2 | 1 | "The voice you're hearing is an AI voice reading my script." | PROCESS | True: Kokoro `af_bella`. Required disclosure in `docs/FELLOWS-SUBMISSION.md`. |
| 3 | 2 | "As an automation developer, my bots never ran into a CAPTCHA." | EXEMPT | Your own experience (tagged in `SCRIPT.md`). |
| 4 | 2 | "But I do, all the time. Click every traffic light. Then every bike. Sometimes two in a row." | EXEMPT | Your own experience. The sources describe picking out traffic lights (Merchant Risk Council: "pick out all the traffic lights in an image"), but nothing in them says bikes or "two in a row". |
| 5 | 3 | "The traffic lights aren't the whole test." | SUPPORTED | The ETH paper says the checkbox version "usually only asks established users to check a box" and that "only in a case where reCAPTCHAv2 is insecure do the image recognition tests come into play"; the Cloudflare post still shows "a visual puzzle" when "the signal is weak". So pictures are a fallback, not the whole test. Wording changed from "really the test" to "the whole test", which the sources support. |
| 6 | 3 | "More and more, websites also check how you behave, often without you noticing." | SIMPLIFIED | IT Brew: the success of AI "is forcing industry pros to explore new methods…, including systems that analyze behavior like mouse movements, typing speed, and IP reputation". "Without you noticing": Merchant Risk Council says v3 "is invisible for website visitors"; The Register says reCAPTCHA moved "to make the browser identify low-risk human users in the background". No listed source counts how many websites do this, so "more and more" is a trend claim without a number (your notes accept it). |
| 7 | 3 (on screen) | "Prove you can see traffic lights." → "Prove you behave like a person." | SIMPLIFIED | On screen only, not narrated. The first line is the viewer's likely misconception, not a claim. The second is the same framing as row 6. |
| 8 | 4 | "CAPTCHA stands for Completely Automated Public Turing test to tell Computers and Humans Apart." | SUPPORTED | Wikipedia, Merchant Risk Council, The Register and IT Brew all spell out the same name. |
| 9 | 4 | "It's a test that checks whether you're a human or a bot." | SUPPORTED | Merchant Risk Council: "to differentiate if a human or a bot is accessing…". IT Brew: a task "that's easy for a human and difficult for a bot". |
| 10 | 4 | "Early versions asked you to read wavy, distorted letters." | SIMPLIFIED | Wikipedia: the "historically common type… requires interpreting a sequence of letters or numbers from a distorted image". The Register: "the technology starting out as a distorted series of letters and/or numbers". "Wavy" is a plain word for the Merchant Risk Council's "squiggly lines" (which that post says of CAPTCHAs in general, not specifically early ones). As your notes say, the script makes no claim about why computers could not read them. |
| 10a | 4 | "Today, they come in three main types: text, images and audio." | SUPPORTED | Merchant Risk Council: "Modern CAPTCHAs fall into three main categories—text-based, image-based, and audio." The post's exact words differ a little from the quote in your notes ("3 main categories: text, image and audio"): it spells out "three", says "categories", and hyphenates "text-based, image-based". The narration's "types" and "images" are plain paraphrase of the same list. "Today" stands for the post's "Modern"; the post is an older blog post, so it is not evidence about what is true now. |
| 11 | 5 | "Then came the 'I'm not a robot' checkbox." | SUPPORTED | Merchant Risk Council: the second version "was depicted on a merchant's website as a simple rectangle with a check box". ETH paper: reCAPTCHAv2 asks users to check a box that they are "not a robot". The narration does not say whose checkbox. |
| 12 | 5 | "The click itself isn't the test." | SUPPORTED | Merchant Risk Council: "Although this box may look simple, there is a very sophisticated process behind it." ETH paper: access is granted "if enough evidence… confirms that the user is indeed not a robot". |
| 13 | 5 | "Behind it, the system looks at signals like your cookies, your browsing history and your mouse movements." | SUPPORTED | ETH paper, quoted in your notes: "(browsing history, mouse movements, etc.)", and the system "is heavily based on cookie and browser history data". Merchant Risk Council adds cookies: "It assigns trust based on cookies and multiple user and site interactions." Your notes' quotes were checked and are accurate. |
| 14 | 5 | "If it's confident you're human, you go straight through." | SUPPORTED | ETH paper: "If enough evidence… confirms that the user is indeed not a robot, reCAPTCHAv2 will grant access directly." |
| 15 | 5 | "Only if it's unsure does it ask you to pick pictures." | SUPPORTED | Merchant Risk Council: "if the user seemed suspect, or if there was not sufficient information, he/she was then asked to identify pictures." The ETH paper says "Only in a case where reCAPTCHAv2 is insecure do the image recognition tests come into play"; that wording reads as a slip for "unsure", so the Merchant Risk Council sentence is the one relied on. |
| 16 | 6 | "The next version, reCAPTCHA v3, shows no puzzle at all." | SUPPORTED | Merchant Risk Council: v3 "is invisible for website visitors. There are no challenges to solve." IT Brew: v3 "calculates a reliability score rather than presenting a CAPTCHA challenge." |
| 17 | 6 | "It watches how each visitor behaves…" | SUPPORTED | Merchant Risk Council: v3 "continuously monitors each visitor's behavior". |
| 18 | 6 | "…and gives a score between zero and one." | SUPPORTED | Merchant Risk Council: "It produces a score between 0-1". |
| 19 | 6 | "A score close to zero means you're more likely a bot." | SIMPLIFIED | Merchant Risk Council: "0 means higher likelihood of a bot attempt." The post says what 0 means; "close to zero" is the natural reading, not its wording. |
| 20 | 7 | "Cloudflare moved away from puzzles too." | SIMPLIFIED | Cloudflare: "we're going to stop using CAPTCHAs" and it "reduced the number of CAPTCHAs we serve by 91%". It still shows "a visual puzzle" when "the signal is weak", and plans to get below 1%, not zero. "Moved away" is fair; "stopped" would not be. |
| 21 | 7 | "Instead, your browser quietly solves small background challenges…" | SUPPORTED | Cloudflare: "a series of small non-interactive JavaScript challenges" run "in-browser", including "proof-of-work, proof-of-space, probing for web APIs". "Quietly" stands for "non-interactive"; the post says it "almost always require[s] no interaction". |
| 22 | 7 | "…and the system checks for signs of a real browser and human behaviour." | SIMPLIFIED | Cloudflare: "various challenges for detecting browser-quirks and human behavior". "Signs of a real browser" paraphrases "browser-quirks". |
| 23 | 7 | "Cloudflare reported that the CAPTCHAs it showed fell by ninety-one percent in a year." | SUPPORTED | Cloudflare: "reduced the number of CAPTCHAs we serve by 91% over the past year." Your notes quote "fell 91%"; the post's own words are "reduced… by 91%". Same figure. |
| 24 | 7 | "…and the average check went from thirty-two seconds to about one." | SIMPLIFIED | Cloudflare: "reduce the visitor time spent in a challenge from an average of 32 seconds to an average of just one second to run our non-interactive challenges", by "skipping the visual puzzle step for almost all visitors". The one second is the time for visitors who never see a puzzle. "Average check" is a fair short form. |
| 25 | 7 | Scope: the Cloudflare figures are about its Managed Challenge. | SUPPORTED | The post is about Managed Challenge and never says Turnstile. Neither does the narration or the scene plan. IT Brew's Turnstile description is not used. |
| 26 | 8 | "Researchers at UC Irvine…" | SUPPORTED | Paper: authors' affiliation "UC Irvine" (some co-authors list other institutions). The Register: "team lead Gene Tsudik of the University of California, Irvine". |
| 27 | 8 | "…had fourteen hundred people solve fourteen thousand CAPTCHAs." | SUPPORTED | Paper abstract: "1,400 participants collectively solved 14,000 CAPTCHAs"; Table 2 "the 1,400 participants of the main user study". The Register gives different counts (1,000 people, 10 tests each), so it is no longer cited for counts; the script now tags the paper for counts and The Register for times and accuracy. Resolves decision A. |
| 28 | 8 | "On distorted text, people took nine to fifteen seconds…" | SUPPORTED | Paper, Table 3 (distorted text): human time "9-15.3". The Register: "humans took 9-15 seconds". |
| 29 | 8 | "…and were right fifty to eighty-four percent of the time." | SUPPORTED | Paper, Table 3: human accuracy "50-84%". The Register: "an accuracy of just 50-84 percent". |
| 30 | 8 | "Bots, from earlier studies, took under a second, with ninety-nine point eight percent accuracy." | SUPPORTED | Paper, Table 3 (distorted text): bot "<1" second and "99.8%", each marked with a citation to earlier work. The Register: bots "coded by researchers and published in journals" took "less than a second with 99.8 percent accuracy". As your notes say, these are not bots the team ran. The figures are for distorted text only, which the narration says. For other types in the same table the gap is smaller (for example reCAPTCHA image: humans 15-26 s and 81%, the bot figure 17.5 s and 85%). The narration does not claim otherwise. |
| 31 | 8 | "And there's a twist." | SIMPLIFIED | Framing for rows 28 to 30. |
| 32 | 9 | "Image puzzles fell too." | SIMPLIFIED | Framing, and a lab result: the ETH paper's footnote says the system was evaluated on Google's reCAPTCHAv2 "demo site". The narration does not say real websites. |
| 33 | 9 | "A team at ETH Zurich trained an AI image model…" | SIMPLIFIED | ETH paper: all three authors list ETH Zurich; "a fine-tuned YOLOv8 model for image segmentation and classification". "Trained" stands for "fine-tuned". |
| 34 | 9 | "…that solved one hundred percent of Google's picture challenges, where earlier work solved sixty-eight to seventy-one percent." | SUPPORTED | ETH paper abstract: "we can solve 100% of the captchas, while previous work only solved 68-71%." It is about Google's reCAPTCHAv2 (see row 32 for the demo-site note). |
| 35 | 9 | "The same researchers found that the system relies heavily on cookies and browsing history to decide who's human." | SUPPORTED | ETH paper abstract: "we… find evidence that reCAPTCHAv2 is heavily based on cookie and browser history data when evaluating whether a user is human or not." Table III supports it: with a real user's history and cookies the median number of challenges fell from 5 to 2. The paper says "find evidence"; "found" is a fair short form. "The system" is reCAPTCHAv2. Replaces the removed "fake human signals" line. Resolves decision B. |
| 36 | 9 | "The picture alone was never the whole test." | SIMPLIFIED | Framing, as your notes say. It matches the paper's finding that cookies and history matter heavily. |
| 37 | 10 | "So websites are changing what they check." | SIMPLIFIED | IT Brew's overall theme. No listed source says how many websites have changed. |
| 38 | 10 | "They use scores instead of puzzles…" | SIMPLIFIED | IT Brew: v3 "calculates a reliability score rather than presenting a CAPTCHA challenge". That describes one product, so "they" is a generalisation. |
| 39 | 10 | "…and watch behaviour in the background." | SUPPORTED | IT Brew: systems that "analyze behavior like mouse movements, typing speed, and IP reputation"; HUMAN's Precheck "uses behavioral analysis (and no CAPTCHA challenge)" with "'invisible' device challenges". |
| 40 | 10 | "One Cloudflare leader argues for blocking bad behaviour rather than every bot." | SUPPORTED | IT Brew quotes Cloudflare's senior director of product: "The idea of classifying behaviors and helping customers block a behavior, rather than just blocking automation, I think, is where security needs to move." The narration now presents it as one person's view, which is what the article gives. "Leader" is a plain word for "senior director of product". Resolves decision C. |
| 41 | 10 | "And companies are working on ways to verify which AI agents are allowed in." | SIMPLIFIED | IT Brew: HUMAN is "partnering with OpenAI to integrate a protocol for cryptographically verifying ChatGPT-agent interactions"; "Cloudflare also in July announced the integration of message signatures to verify bots and their origins". Your notes say Cloudflare and OpenAI work together; the article says HUMAN with OpenAI and Cloudflare separately. The narration says only "companies", so it is unaffected. "Which agents are allowed in" is a plain paraphrase, and both examples are vendors describing their own products. |
| 42 | 11 | "The traffic lights were never the whole test." | SUPPORTED | Same as row 5. "Never the whole test" matches beat 9 and the sources. Resolves the first half of decision D. |
| 43 | 11 | "A lot of it was how I moved." | SIMPLIFIED | Framing in your voice. Mouse movement is one signal in the sources, alongside cookies and browsing history (row 13), and no source says what any site judged about you, so "a lot" is unquantified. Softened from "The test was how I moved", which overstated it. |
| 44 | 11 | "Puzzles are still around…" | SUPPORTED | Cloudflare: CAPTCHA "remains an effective tool" that "many sites choose", and it still shows "a visual puzzle" when signals are weak. Merchant Risk Council: "more than one-third of the top 100,000 websites use CAPTCHAs". |
| 44a | 11 | "…but more and more, websites are moving from 'prove you're human' to 'show you behave like one.'" | SIMPLIFIED | Supported for some sites and vendors (IT Brew, the Cloudflare post, The Register's expert quote), and now limited to "websites" with "more and more" instead of "the internet is moving". The two quoted phrases are your framing, not a source's words. Resolves the second half of decision D. |
| 45 | 12 | "This week, count how many times a website asks if you're human, and notice when it lets you through without asking." | PROCESS | An instruction to the viewer, not a claim. |
| 46 | 12 | The prompt: explain why a website showed me a "Verify you are human" page, what it might have checked in the background, and how you would tell a person from a bot without traffic lights. | PROCESS | A prompt for the viewer. No listed source quotes a "Verify you are human" page, and the video does not claim it exists; it is the viewer's own prompt. It must not be illustrated with a copy of any real page. |
| 47 | 13 | "Built with Claude, for Humanitarians AI." | PROCESS | Describes this video. Matches the `SCRIPT.md` header ("drafted with Claude from Keya's story plan and research notes; Keya approved and edited it"). |

Also checked: no years or dates appear anywhere in the narration (`SCRIPT.md` rule). The `Sources` list in `SCRIPT.md`
is not touched.

## Your five decisions, resolved

| Item | What you did | Result |
|---|---|---|
| A. Participant counts | Beat 8 tag now cites the paper for counts and The Register for times and accuracy. | Row 27 SUPPORTED by the paper. |
| B. "Had to fake" | Line removed; replaced by the paper's finding about cookies and browsing history. | Row 35 SUPPORTED. |
| C. Blocking bad behaviour | Now "One Cloudflare leader argues…". | Row 40 SUPPORTED. |
| D. Verdict | Now "never the whole test", "A lot of it was how I moved", "Puzzles are still around, but more and more…". | Rows 42, 43, 44, 44a. None is PARTLY now. |
| E. TechSpot | Removed. | Nothing depends on it. |

## Other changes since the first check

| Beat | What changed | Result |
|---|---|---|
| 3 | Lengthened: "…aren't the whole test. More and more, websites also check how you behave, often without you noticing." | Rows 5 and 6. |
| 4 | New line: "Today, they come in three main types: text, images and audio." | Row 10a, checked against the Merchant Risk Council post. |

## Notes for the fact check: your list, answered

- **Beat 2 (your own experience):** EXEMPT, rows 3 and 4.
- **Beat 3 and the verdict:** worded to match the sources, as your note says: "puzzles are still around" and "more and more", not that they are gone. Rows 5, 6, 42 to 44a.
- **Beat 4:** the exact Merchant Risk Council wording is "Modern CAPTCHAs fall into three main categories—text-based, image-based, and audio." Your notes quote it slightly differently; the content matches. Row 10a. The distorted-letters line is row 10; the script claims nothing about why computers could not read them.
- **Beat 5:** the three ETH quotes in your notes are accurate (rows 13 and 14); the cookie claim is also in the Merchant Risk Council post.
- **Beat 6:** every quote in your notes is accurate, and only those two sources were used. Rows 16 to 19.
- **Beat 7:** the post is about Managed Challenge, not Turnstile by name; narration stays within what it says. Your notes' "fell 91%" is the post's "reduced… by 91%"; the figure matches. Rows 20 to 25.
- **Beat 8:** bot figures come from earlier studies, and the narration says so. Checked against Table 3. Counts are from the paper. Rows 26 to 31.
- **Beat 9:** 100% and 68 to 71% are the paper's, and so is the cookies-and-history finding. Rows 32 to 36.
- **Beat 10:** from IT Brew only. Rows 37 to 41.
- **Years and dates:** none in the narration.
- **Your rule, "nothing goes in that isn't checked":** no row is NOT STATED or PARTLY. No new claims or sources were added.

## Visuals

- Drawn shapes only, as in `SCRIPT.md`: a grid of traffic-light squares, wavy letters, a checkbox, a 0-to-1 score dial, a stopwatch, a mouse path, a shield.
- No Google, reCAPTCHA, hCaptcha or Cloudflare logos, no screenshots of real challenge pages, and no copy of any product's widget or colours. Company and product names appear only as plain text where the narration says them.
- Every example is an illustration. The only figures on screen are the ones in `SCRIPT.md` (91%, 32 s to about 1 s, 1,400 and 14,000, 9 to 15 s, 50 to 84%, under 1 s, 99.8%, 100%, 68 to 71%) and the 0 and 1 on the dial.
- No dates on screen or in these files.
