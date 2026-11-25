# SCRIPT — Bayes' Theorem: The Positive That's Usually Wrong

Narration as built, from `beat_sheet.json`. On 2026-11-24 the film was converted from the tldr format to ai-explainer, and Anant approved the new narration. Durations are the measured audio, lead silence included. The pre-conversion script is in `_superseded/format-tldr/docs/SCRIPT.md`.

## B00 · ASK · ClaudeComposerAsk

*33 words · 10.5 s*

Hello, this is Liam, in for Bear. The ask: a test that catches ninety-nine percent of cases says I'm positive. How likely is it that I'm actually sick? Show me with real numbers.

*On screen:* composer card fades in on cream → greeting 'Hello, Liam' types above the composer → the ask types in → runningText 'working through the math…' appears → three result lines cascade in

## B01 · BLUF · BrutalistHesitantWriter

*35 words · 11.8 s*

A positive test can still be a false alarm. When a disease is rare, false alarms from the healthy outnumber the real cases. What decides it is the base rate: how common the disease is.

*On screen:* cream page holds; caret blinks → types "A positive test / means you're probably sick." → 'means you're probably sick' turns terracotta, hesitates, backspaces → types 'can still be a false alarm' → final lines settle

## B10 · LEARN 1 · B10_YouArePositive

*37 words · 10.3 s*

You take a test for a rare disease. It catches ninety-nine percent of the people who have it. Your result: positive. So how worried should you be? Hold on to your first answer. We're going to count.

*On screen:* one ink square 'you' draws on, centre stage → test chip 'catches 99% of cases' slides across the square → result stamp 'positive' lands beside the square — the beat's terracotta → MathTex P(sick) = \, ? writes beside it, the '?' large → the square and stamp shrink toward the top-left corner (the grid's first cell)

## B11 · LEARN 1 · B11_TenThousand

*40 words · 12.7 s*

Make it people. Ten thousand of them, one square each. One percent have the disease: one hundred squares. Run the test on them. It catches ninety-nine. One slips through. So far, the ninety-nine percent is doing exactly what it promised.

*On screen:* 125 × 80 isotype grid (pitch 0.068 u, 8.5 × 5.44 u, left of a counter column; IsotypeGrid pattern from explainer/manim/animated_graphics.py) counts up in reading order, dim; 'you' sits in it as an outline ring → a 10 × 10 block of 100 cells, top left, turns ink on 'one hundred squares'; label 'sick: 100' → a scan bar sweeps the sick cells on 'Run the test' → 99 stay ink, counter 'positive: 99' → 1 square fades to ghost — terracotta ring on it for the sentence 'One slips through'

## B12 · LEARN 1 · B12_FalseAlarms

*46 words · 14.8 s*

Now the other nine thousand nine hundred, the healthy ones. The test clears ninety-five percent of them. But five percent light up anyway. Five percent of nine thousand nine hundred is four hundred ninety-five false alarms. Five times as many as the sick people it caught.

*On screen:* scan bar returns to row 2 and sweeps down the remaining healthy cells → 9,405 cleared squares fade to ghost as the bar passes → 495 squares stay lit, scattered — they flash terracotta on 'light up anyway' → counter 'false alarms: 495' beside 'positive: 99' → the 495 settle to dim; two counters held side by side

## B13 · LEARN 1 · B13_WrongCrowd

*47 words · 14.0 s*

The natural answer is ninety-nine percent. It's the number on the box. And it's true, for this block: ninety-nine of the one hundred who are sick tested positive. But that fraction is about people already known to be sick. All you know is that you tested positive.

*On screen:* rectangle draws round the sick block; label 'out of the sick' → MathTex \frac{99}{100} writes beside the box → the 495 lit squares outside the box pulse once — terracotta → dim caption: 'but you only know you're positive'

## B14 · LEARN 1 · B14_OnlyThePositives

*41 words · 12.2 s*

So change the crowd. Keep everyone who tested positive, and let everyone else go. Here they are: ninety-nine who are sick, four hundred ninety-five who aren't. Before we count, commit to a guess. Of these lit squares, what share are sick?

*On screen:* all ghost (negative) squares fade out → the 594 positives fly into one 27 × 22 block, larger squares, sick first → 'you' ring lands on the block's edge: you're one of these → HOLD ≥ 3 s — nothing moves on 'commit to a guess'

## B15 · LEARN 1 · B15_OneInSix

*23 words · 8.1 s*

Ninety-nine have the disease. Five hundred ninety-four in all. Watch the fraction shrink. One in six. Five out of six positives are healthy.

*On screen:* the 99 ink squares slide up and stack above a growing fraction bar → all 594 squares stream under the bar → the stacks morph into MathTex \frac{99}{594} → the fraction transforms to \frac{1}{6} — the terracotta lands on it → dim chip '≈ 16.67%' under it; held

## B16 · LEARN 1 · B16_BuildBayes

*51 words · 17.0 s*

This thing deserves a name. Divide every count by ten thousand and the counts become chances. Ninety-nine becomes the sensitivity times the base rate. Five hundred ninety-four becomes the chance of any positive. What's left is Bayes' theorem. It flips a conditional chance by weighing in how common each side is.

*On screen:* the \frac{99}{594} from B15 slides left; '÷ 10,000' writes under each number → 99 → \frac{99}{10\,000} → 0.99 \times 0.01 → P(+\mid D)\,P(D) (MathTex, staged) → 594 → P(+) (MathTex) → assembles P(D\mid +) = \frac{P(+\mid D)\,P(D)}{P(+)} → D, + morph to A, B: P(A\mid B) = \frac{P(B\mid A)\,P(A)}{P(B)}; serif label 'Bayes' theorem' — terracotta

## B17 · LEARN 1 · B17_ReadTheLine

*75 words · 21.8 s*

Read it piece by piece. On the left: the chance of disease, given a positive. On the right: the chance of a positive, given disease, the ninety-nine percent, times the base rate, one percent, divided by the share of everyone who tests positive. Zero point nine nine times zero point zero one, over zero point zero five nine four. One sixth. The bar has a direction. Swap its sides, and you get a different number.

*On screen:* LHS P(A|B) boxed (box spotlight, not underline); sentence 'chance of A once you know B' → P(B|A) boxed; glossary row 'P(B|A) · sensitivity · 0.99' → P(A) boxed; row 'P(A) · base rate · 0.01' → P(B) boxed; row 'P(B) · all positives · 0.0594' → worked value: 0.99 × 0.01 / 0.0594 = 1/6 (MathTex) → values claim: P(B|A) ≠ P(A|B) — the '≠' gets the box spotlight, terracotta

## B18 · LEARN 1 · B18_BackToYou

*51 words · 14.6 s*

Back to you. You are one of these five hundred ninety-four; one in six is sick. A positive moved you from one in a hundred to one in six: a real jump, nowhere near ninety-nine percent. The sick are outnumbered ninety-nine to one, so a small false-alarm rate makes a crowd.

*On screen:* the B10 'you' square + stamp return (same objects) and settle into the 594 block → MathTex \frac{1}{100} → \frac{1}{6} arrow beside the square → the 99:1 ratio: sick row vs the healthy mass flash once, terracotta on the healthy side → held: you, the block, 1/6

## B19 · LEARN 1 · B19_BaseRateDial

*46 words · 13.8 s*

One number did most of that work: the base rate. Same test, rarer disease, one in a thousand: a positive means about two percent. One in ten: about sixty-nine percent. One in two: ninety-five. What this film didn't do is test you twice. That's your turn.

*On screen:* the 1/6 slides onto axes: base rate (log) vs chance sick given positive → marker slides left to 0.1%: reads 1.94% → slides right through 1% (1/6) to 10%: 68.75% → to 50%: 95.19%; the full curve traced in ink, marker terracotta → dim captions: 'same test: 99% sensitive, 95% specific' · 'not taught here: a second positive'

## BVDT · VERDICT · ClaudeVerdictArtifact

*64 words · 20.6 s*

Let's recap with Claude. The ninety-nine percent is about the sick: ninety-nine of every hundred sick people test positive. Your question is about the positives, and only ninety-nine of five hundred ninety-four are sick: one in six. The healthy outnumber the sick ninety-nine to one, so five percent false alarms make a crowd. Bayes' theorem flips the question by weighing in the base rate.

*On screen:* artifact page opens → four verdict lines land in narration order

## BHTF · YOUR TURN · ClaudeComposerAsk

*122 words · 35.7 s*

Your turn. Paste this into Claude: A test catches ninety-nine percent of people who have a disease and wrongly flags five percent of healthy people. One person in a hundred has the disease. Someone tests positive, then takes the same test again and tests positive a second time. Before calculating, guess the chance they are sick. Then count it out for a million people, show the counts after each test, and say what you had to assume about the two tests. Here's what to check. After one positive: one in six. After two: about four in five, because the first answer became the new base rate. And it should say the two results were assumed independent. A real repeat test often isn't.

*On screen:* composer opens — 'Your turn.' → the prompt types in full → runningText 'paste this into Claude…' → three check lines land as each is spoken

## BOUT · OUTRO · ClaudeTitleOutro

*11 words · 5.5 s*

Bayes' Theorem: The Positive That's Usually Wrong. At Nik Bear Brown.

*On screen:* title restates; handle; slug-seeded mascot. Liam reads the title, then 'At Nik Bear Brown'.

**Total: 722 words · 223.4 s (3:43).**
