# NARRATION GATE P — Madison Weekly — Nov 27.

Collective Madison voice. No teammate names (brief named people; the cut does not).
Kokoro `am_onyx` · Liam as one word via `liam.json` (no `metadata.pronounce`).
Greeting `Namaste` → nah mah stay. This is Madison's weekly update.

## B00 · COLD OPEN
Namaste — this is Liam, in for Komal. This is Madison's weekly update. Madison is building a new Intelligence Agents layer: detect inauthentic Instagram engagement. Bots, fake followers, fake likes, fake comments. Two questions, not one.

## B01 · BLUF
Here is the whole idea. A score on the account is not a score on the comments. Rules are not a trained model. Building is not shipped. Those distinctions are the week.

## B02 · WHO CAN CHECK
The problem they named. A brand deciding whether to invest in an influencer has no easy way to check if that audience is real. Large companies can buy proprietary vetting. Smaller brands, independent creators, and nonprofits — the groups Humanitarians AI exists to support — cannot. Spend can go to a partnership built on fake engagement, with no way to catch it beforehand.

## B03 · TWO QUESTIONS
So they are building an explainable trust signal. Not a black-box verdict. A risk score with visible reasoning. It takes an account's profile and engagement data, and it answers two things: how likely the account itself is fake, and separately, how likely the likes and comments on a given post are fake. That sits next to the scraping they already have for social research.

## B04 · HOW IT DIFFERS
How it differs from desks they reviewed. HypeAuditor, Modash, CreatorIQ: fraud at the account level. One score from account-wide stats. Rule-based thresholds, not a trained, validated model. Madison's first difference: train a classifier on TwiBot-20, a labeled benchmark with known real versus bot, so they can measure performance instead of guessing a cutoff.

## B05 · SECOND LAYER
Second difference: the post. They separately ask whether the likes and comments look authentic, even if the account posting looks authentic. In their competitive reading, none of those tools appear to offer that second layer. Appear is not a census of every product.

## B06 · VERDICT
Let's recap with Claude. Intelligence Agents: two questions — the account, and the comments on a post. Trained on TwiBot-20, not a hand-set rule. Built for people who cannot buy the enterprise desk. Design judgment: a trust signal is not a verdict. Building is not shipped.

## B07 · HANDOFF
Your turn. Madison is building two layers on Instagram engagement. Explain (1) why an account score is not an engagement score, (2) what TwiBot-20 can and cannot prove for Instagram, and (3) what must be true before this is a product in someone's hands. Take this prompt, run it on your own first dataset.

## B08 · OUTRO
Madison Weekly. Liam, in for Komal.

---
**Locks:** Liam in for Komal · Madison's weekly update · collective team voice · no teammate names · greeting `Namaste, Liam` · TTS: nah mah stay; Liam one word never Lay-um (`liam.json` after-stop + IPA); Hype Auditor; Modash; Creator I Q; Twai bot twenty; AI without periods · no GitHub URL · no invented accuracy · TwiBot-20 is not Instagram ground truth · 4K 16:9 + 4K 9:16
