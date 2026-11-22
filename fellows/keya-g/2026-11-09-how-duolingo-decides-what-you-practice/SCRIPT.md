# How Duolingo Decides What You Practice Next — Script

**Fellow:** Keya G. · **Week 5** · **Voice:** Kokoro `af_bella` · **Pronounce:** Keya = kˈeɪjɛə ("Kay-yeah"); shimasu and mimasu = option B from the test clips (final u dropped); Leitner = "LITE-ner"

Story plan, topic, research and decisions: Keya. Example script drafted with Claude from Keya's story plan and research notes; Keya approved and edited it.
Visuals: simple illustrative graphics only (a forgetting curve, flashcard boxes, a strength meter, a half-life curve, exercise difficulty). No Duolingo logos, owl mascot, app screenshots or other branding.

## 1. Intro
Hi, I am Keya, and this video is about how Duolingo decides what you should practice next. The voice you're hearing is an AI voice reading my script.

## 2. Hook
I've been learning Japanese on Duolingo for over a year. In my first days, I kept mixing up two words: shimasu, which means do, and mimasu, which means look. And Duolingo kept bringing them back, until I finally got them right. How did it decide when?
`[Keya's experience]`

## 3. Overview
On screen, typed then corrected: "Reviews are random." → "Duolingo predicts when you'll forget each word."

Duolingo doesn't review words at random. It predicts when you'll forget each word, and brings it back just in time. Let's see how, step by step.

## 4. The forgetting curve
First, how do we forget? In 1885, Hermann Ebbinghaus studied his own memory and described the forgetting curve: without any effort to keep it, what we learn fades away over time.
`[Wikipedia: Forgetting curve; Ebbinghaus, Memory (1885); Duolingo blog]`

## 5. Spaced repetition
But reviewing at the right moments slows that fading. Short practices spread out over time work better than cramming, and gradually increasing the gaps between practices works even better. The best time to review is just before you're likely to forget. This is called spaced repetition.
`[Duolingo blog: spacing effect, lag effect; BCU: spaced repetition]`

## 6. Leitner boxes
A simple version uses flashcards in boxes. This is the Leitner system. Get a card right, and it moves to a box you review less often. Get it wrong, and it moves to a box you review more often. But every card follows the same fixed rules.
`[University of York: Leitner system]`

## 7. Half-life
Duolingo goes further. It gives every word its own half-life: the time it takes for your memory strength to decrease by half. When the time since you last practiced a word equals its half-life, you have about a fifty-fifty chance of remembering it. And once a skill's strength meter slips to half-full, it's time to practice.
`[Duolingo blog; Settles & Meeder 2016]`

## 8. Half-life regression
To predict each word's half-life, Duolingo combined machine learning and data science into a new statistical model, called half-life regression. It looks at your history with each word: how many times you've seen it, and how often you got it right or wrong. From that, it predicts how long each word will last in your memory.
`[Duolingo blog; Settles & Meeder 2016]`

## 9. Did it work?
Did it work? Duolingo reported that its prediction error was nearly half that of the Leitner system. But tests with real learners were more mixed.
`[Duolingo blog; Settles & Meeder 2016, Table 4]`

## 10. Birdbrain
Later, Duolingo added another model, called Birdbrain. It makes an educated guess about whether you'll get an exercise right. Then it helps pick exercises at just the right difficulty: not so hard that you're frustrated, and not so easy that you've already mastered them.
`[Duolingo blog: Introducing Birdbrain]`

## 11. Where it falls short
But it has limits. In my view, the model only sees what I do inside the app. It doesn't know my interests, when I use Japanese somewhere else, or when I make a mistake while speaking.
`[Keya's view]`

## 12. Verdict
The idea behind spaced repetition is over a hundred years old. Duolingo's AI didn't invent it. It made it personal, one word at a time. The best review isn't more practice. It's the right word, just before I forget it. That's how shimasu and mimasu finally stuck.

## 13. Your turn
Your turn. Paste this into Claude: Explain Duolingo's half-life regression using one word I'm learning. Show what its half-life means, and when I should practice it next. Use example numbers. And next time an old word comes back in a lesson, ask: was I just about to forget it?

Prompt shown on screen: "Explain Duolingo's half-life regression using one word I'm learning. Show what its half-life means, and when I should practice it next. Use example numbers."

## 14. Outro
How Duolingo Decides What You Practice Next. Built with Claude, for Humanitarians AI.

## Notes for the fact check
- Beats 2 and 11 are Keya's own experience and view.
- Beat 7: the fifty-fifty line comes from the paper's formula, p = 2^(−Δ/h), which gives p = 0.5 when the time since practice equals the half-life.
- Beat 8: the paper lists the inputs as counts of times seen, correct and incorrect, plus word (lexeme) tags. The script names only the counts. The paper does not report whether right answers always lengthen a half-life, so the script doesn't say so.
- Beat 9: no engagement percentage is used. In the paper's Table 4, HLR against Leitner showed +0.3% overall activity and a 7.3% drop in practice sessions; the 12% (and 9.5%) came from a simpler HLR against the full HLR. "Mixed" summarizes this. "Nearly half" is the blog's wording (0.128 against 0.235 in the paper).
- Beat 7: the strength meter is per skill, so the script uses the blog's wording ("once the meter slips to half-full, it's time to practice"), not a per-word claim.
- Beat 10: the Birdbrain post does not say it replaced half-life regression; the script only says Duolingo "added another model."
- Beat 13: "Use example numbers" tells viewers the half-life Claude gives is illustrative.
- Beat 12: "over a hundred years old" rests on Ebbinghaus, 1885.
- Japanese: します (shimasu, "do") and みます (mimasu, "look/see").

## Sources
- Duolingo blog, "How we learn how you learn" — https://blog.duolingo.com/how-we-learn-how-you-learn/
- Burr Settles and Brendan Meeder, "A Trainable Spaced Repetition Model for Language Learning", ACL 2016 — https://aclanthology.org/P16-1174/
- Duolingo, half-life regression code and data (GitHub) — https://github.com/duolingo/halflife-regression
- Duolingo blog, "Learning how to help you learn: Introducing Birdbrain" — https://blog.duolingo.com/learning-how-to-help-you-learn-introducing-birdbrain
- Wikipedia, "Forgetting curve" — https://en.wikipedia.org/wiki/Forgetting_curve
- Hermann Ebbinghaus, Memory: A Contribution to Experimental Psychology (Classics in the History of Psychology) — https://psychclassics.yorku.ca/Ebbinghaus/index.htm
- Birmingham City University, "Spaced repetition" — https://www.bcu.ac.uk/exams-and-revision/best-ways-to-revise/spaced-repetition
- University of York, "Leitner system" — https://subjectguides.york.ac.uk/study-revision/leitner-system
