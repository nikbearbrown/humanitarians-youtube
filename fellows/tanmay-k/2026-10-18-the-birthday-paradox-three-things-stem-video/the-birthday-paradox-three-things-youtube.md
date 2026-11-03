The Birthday Paradox: Three Things You Could Change

Put 23 people in a room and the odds that two of them share a birthday are about even. That's the famous
bit. What I wanted to know is which part of that claim does the work. Three things could change the odds:
how many people there are, how uneven the birthdays are, and how many days they have to land on. I changed
each one and watched the number. One barely matters, one matters the way you'd expect, and one decides
almost everything. From that comes a rule you can use on your own numbers, and a question at the end to try
it on. Pause when I ask you to.

Chapters:
0:00 Twenty three people, one bet
0:10 Three things you could change
0:29 Count pairs, not people
0:42 First change: the people
1:17 Second change: how even the days are
2:07 Third change: how many days there are
2:51 What actually moved the odds
3:08 The rule: 1.2 times the square root
3:45 A new case: birth months
4:03 Your turn: 50 slots
4:24 The answer
4:37 Ask how many slots

Data and credit:
Births data: US National Center for Health Statistics and Social Security Administration, via
FiveThirtyEight (CC BY 4.0). All simulations and calculations are my own; the code and the numbers behind
every figure are in the Humanitarians AI repository.

What this video claims, and what it does not:

- With 23 people and every day equally likely, the chance that at least two share a birthday is 50.7%
  (exact calculation; 400,000 simulated groups agree). It reaches 99% at 57 people.
- Someone sharing YOUR birthday is a different question: you need 253 other people for even odds, and
  with 22 others the chance is under 6%.
- On the real US calendar, births pooled by calendar day for 2000 to 2014, the odds for 23 people are 50.8%,
  at most about a tenth of a point above the even-days figure. 96% of days sit within 10% of an average day.
  February 29 runs at about a quarter of a normal day because it exists one year in four.
- Squeezing the group into fewer days is what changes the odds: 23 people born in the same 90 days have a
  95.4% chance of a shared birthday; in the same 30 days, above 99.99%. The window is a calculation, not a
  claim about any real group.
- The rule, people for even odds is about round(1.2 times the square root of the days plus a half), matches the
  exact answer for every window shown and is never more than one person off for any number of equally likely
  days from 2 to 2,000 (exact for 1,161 of those 1,999, one off for the other 838). It assumes every slot is
  equally likely. The textbook version is about 1.18 times the square root; I use 1.2 plus a half, rounded, because it is easy to say, and I checked it against the exact answer rather than assuming it.
- A school-year cohort covers every day of the calendar once, so it behaves like the full year. That is a
  property of the calendar model, not a finding about real schools.
- The dots on screen: the two dot patterns (one random group of 23, one random group inside 90
  days) are labelled illustrations from fixed seeds, not data.

Narration is a synthetic voice (Kokoro, run locally). Visuals are original code-drawn slates and
animations: no third-party images, recordings or music, and open-licence fonts only (EB Garamond, Inter).

Humanitarians AI — @HumanitariansAI
Tanmay Kulkarni, in for Humanitarians AI

Tags: birthday paradox, birthday problem, probability, coincidences, statistics explained, square root rule,
collision probability, counterintuitive probability, probability simulation, Humanitarians AI
