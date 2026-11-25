# How Do Websites Know I'm Not a Robot? — Script

**Fellow:** Keya G. · **Week 6** · **Voice:** Kokoro `af_bella` · **Pronounce:** Keya = kˈeɪjɛə ("Kay-yeah"); CAPTCHA to be checked by ear

Story plan, topic, research and decisions: Keya. Example script drafted with Claude from Keya's story plan and research notes; Keya approved and edited it.
Visuals: simple illustrative graphics only (a grid of drawn traffic-light squares, wavy letters, a checkbox, a 0-to-1 score dial, a stopwatch, a mouse path, a shield). No Google, reCAPTCHA, hCaptcha or Cloudflare logos, and no screenshots of real challenge pages.

## 1. Intro
Hi, I am Keya, and this video is about how websites know I'm not a robot. The voice you're hearing is an AI voice reading my script.

## 2. Hook
As an automation developer, my bots never ran into a CAPTCHA. But I do, all the time. Click every traffic light. Then every bike. Sometimes two in a row. Why does a website keep asking me to prove I'm human?
`[Keya's experience]`

## 3. Overview
On screen, typed then corrected: "Prove you can see traffic lights." → "Prove you behave like a person."

The traffic lights aren't the whole test. More and more, websites also check how you behave, often without you noticing. Let's see how, step by step.

## 4. What a CAPTCHA is
CAPTCHA stands for Completely Automated Public Turing test to tell Computers and Humans Apart. It's a test that checks whether you're a human or a bot. Early versions asked you to read wavy, distorted letters. Today, they come in three main types: text, images and audio.
`[Wikipedia: CAPTCHA; Merchant Risk Council blog]`

## 5. The checkbox
Then came the "I'm not a robot" checkbox. The click itself isn't the test. Behind it, the system looks at signals like your cookies, your browsing history and your mouse movements. If it's confident you're human, you go straight through. Only if it's unsure does it ask you to pick pictures.
`[Plesner et al., ETH Zurich, "Breaking reCAPTCHAv2"; Merchant Risk Council blog]`

## 6. No puzzle at all
The next version, reCAPTCHA v3, shows no puzzle at all. It watches how each visitor behaves and gives a score between zero and one. A score close to zero means you're more likely a bot.
`[Merchant Risk Council blog; IT Brew]`

## 7. Cloudflare's approach
Cloudflare moved away from puzzles too. Instead, your browser quietly solves small background challenges, and the system checks for signs of a real browser and human behaviour. Cloudflare reported that the CAPTCHAs it showed fell by ninety-one percent in a year, and the average check went from thirty-two seconds to about one.
`[Cloudflare blog: The end of the road for Cloudflare CAPTCHAs; IT Brew]`

## 8. Bots beat humans
And there's a twist. Researchers at UC Irvine had fourteen hundred people solve fourteen thousand CAPTCHAs. On distorted text, people took nine to fifteen seconds and were right fifty to eighty-four percent of the time. Bots, from earlier studies, took under a second, with ninety-nine point eight percent accuracy.
`[Searles et al., UC Irvine (participant counts); The Register (times and accuracy)]`

## 9. A hundred percent on the pictures
Image puzzles fell too. A team at ETH Zurich trained an AI image model that solved one hundred percent of Google's picture challenges, where earlier work solved sixty-eight to seventy-one percent. The same researchers found that the system relies heavily on cookies and browsing history to decide who's human. The picture alone was never the whole test.
`[Plesner et al., ETH Zurich]`

## 10. What happens now
So websites are changing what they check. They use scores instead of puzzles, and watch behaviour in the background. One Cloudflare leader argues for blocking bad behaviour rather than every bot. And companies are working on ways to verify which AI agents are allowed in.
`[IT Brew]`

## 11. Verdict
The traffic lights were never the whole test. A lot of it was how I moved. Puzzles are still around, but more and more, websites are moving from "prove you're human" to "show you behave like one."

## 12. Your turn
Your turn. This week, count how many times a website asks if you're human, and notice when it lets you through without asking. Then paste this into Claude: Explain why a website showed me a "Verify you are human" page, what it might have checked in the background, and how you would tell a person from a bot without traffic lights.

Prompt shown on screen: "Explain why a website showed me a 'Verify you are human' page, what it might have checked in the background, and how you would tell a person from a bot without traffic lights."

## 13. Outro
How Do Websites Know I'm Not a Robot? Built with Claude, for Humanitarians AI.

## Notes for the fact check
- Beat 2 is Keya's own experience.
- Beat 5: the ETH paper says reCAPTCHAv2 "usually only asks established users to check a box" and grants access "if enough evidence (browsing history, mouse movements, etc.) confirms that the user is indeed not a robot", and that it "is heavily based on cookie and browser history data."
- Beat 6: from the Merchant Risk Council member blog: v3 "is invisible for website visitors. There are no challenges to solve", "continuously monitors each visitor's behavior", and "produces a score between 0-1, 0 means higher likelihood of a bot attempt." IT Brew also says v3 "calculates a reliability score rather than presenting a CAPTCHA challenge." Use only these sources; don't add claims from elsewhere.
- Beat 4: the distorted letters come from Keya's sources ("deciphering the letters"). "Three main types: text, images and audio" is from the Merchant Risk Council blog ("Modern captchas fall into 3 main categories: text, image and audio"); check the exact wording there.
- Beat 7: the Cloudflare post is about its Managed Challenge, not Turnstile by name. It lists "proof-of-work, proof-of-space, probing for web APIs" and checks for browser quirks and human behaviour; CAPTCHAs served "fell 91%"; average challenge time from 32 seconds to about one second. Keep the narration to what the post says.
- Beat 8: human and bot figures are as reported by The Register for the UC Irvine study (1,400 participants, 14,000 CAPTCHAs). Bot figures come from earlier published studies the paper compares against, not from bots the team ran; the narration says "from earlier studies." Check against the paper's Table 3 if possible.
- Beat 9: the 100% and 68–71% figures, and "reCAPTCHAv2 is heavily based on cookie and browser history data", are from the ETH paper. The earlier line about faking human signals was removed because the paper doesn't say the system couldn't pass without them, and TechSpot couldn't be fetched. "The picture alone was never the whole test" is framing based on that finding.
- Beat 10: from IT Brew. "Blocking bad behaviour rather than every bot" is attributed to Cloudflare's Reid Tatoris, as one person's view. "Companies are working on ways to verify AI agents" follows IT Brew, which says HUMAN works with OpenAI and Cloudflare separately announced message signatures; the narration says only "companies".
- Beat 8: participant counts (1,400 people, 14,000 CAPTCHAs) are from the paper; The Register gives different counts, so cite the paper for counts and The Register only for the times and accuracy.
- Beat 3 and the verdict: worded to match the sources. CAPTCHAs are still widely used (Cloudflare post, Merchant Risk Council), so the verdict says "puzzles are still around" and "more and more", not that they're gone.
- Avoid years and dates in narration; source years stay in the Sources list only.
- Keya's rule: nothing goes in that isn't checked against these sources. If a line can't be supported by a source listed here, flag it and don't add new claims or sources without asking.

## Sources
- Wikipedia, "CAPTCHA" — https://en.wikipedia.org/wiki/CAPTCHA
- Merchant Risk Council, PayPal member blog on CAPTCHA evolution and effectiveness — https://merchantriskcouncil.org/learning/resource-center/member-news/blog/2024/paypal-captcha-evolution-and-effectiveness
- Cloudflare blog, "The end of the road for Cloudflare CAPTCHAs" — https://blog.cloudflare.com/end-cloudflare-captcha/
- Andrew Searles et al., "An Empirical Study & Evaluation of Modern CAPTCHAs", USENIX Security — https://arxiv.org/abs/2307.12108
- The Register, "So much for CAPTCHA then – bots can complete them quicker than humans" — https://www.theregister.com/2023/08/15/so_much_for_captcha_then/
- Andreas Plesner, Tobias Vontobel and Roger Wattenhofer, "Breaking reCAPTCHAv2", ETH Zurich — https://arxiv.org/abs/2409.08831
- IT Brew, "As AI solves CAPTCHAs, what's next?" — https://www.itbrew.com/stories/2025/09/30/as-ai-solves-captchas-what-s-next
