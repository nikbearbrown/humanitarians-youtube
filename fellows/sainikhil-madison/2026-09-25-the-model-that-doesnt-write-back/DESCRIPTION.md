Everyone is talking about Jev. Here's the gentle version: a model that answers your software's questions with a number instead of writing it a paragraph.

Jev is the first "System One" model from TypeSafe AI, in early access since September 15, 2026. It gets its name from the fast, intuitive System 1 in Daniel Kahneman's Thinking, Fast and Slow. Think of a switchboard operator. A call comes in and they decide, in a moment, which line it belongs on. They never write anyone a letter. Jev is built for that kind of quick decision, made for software.

A chatbot answers by writing a reply one word at a time, and your program then has to read that text to find the answer. Jev never writes. You give it the situation and your questions, and every answer comes back at once as a typed value your code can use directly. It understands three kinds of question. A Choice asks which of your options fits. A Score asks where something sits on your scale. A Noul asks whether a statement is true, yes or no. TypeSafe's own example asks three at once about a refund: was one requested, is it a duplicate charge, and does policy allow it.

Each answer comes with a probability. Those probabilities are meant to be calibrated. Of all the answers Jev gives at 0.8, about eight in ten should turn out true: Pr(s true | p̂ = 0.8) ≈ 0.8. As TypeSafe's docs put it, calibration is measured across groups of predictions and does not guarantee that any single answer is correct. The 82-out-of-100 figure in the video is a seeded simulation of that definition, not a measurement of Jev.

TypeSafe says replies take 70 to 500 milliseconds and input costs $0.042 per million tokens, with output free. At that price, a million support tickets of about 500 tokens each would cost roughly $21. TypeSafe also publishes a list of what Jev is bad at. It isn't a calculator, it reads dates as text, instructions hidden in the input can steer it, it doesn't write text, and for now it only reads text.

The fair question is about the biggest claims, up to 200× faster than frontier chatbots. They come from tests TypeSafe's own team built, and at launch they had not been independently verified. Also, "it can't hallucinate" means every answer has the right shape. It doesn't mean every answer is right. The good news is that Jev is cheap enough to test on your own data for pocket change.

Try it yourself: take one decision your code makes today, whether an if-statement or a chatbot call, and ask an assistant to split it into yes/no, choice and score questions. Ask which parts should stay as plain code, and how you would check that its eight in ten really means eight in ten on your data.

Chapters:
0:00 What is Jev?
0:13 Fast thinking: a decision, not a reply
0:31 How it differs from a chatbot
0:47 Three kinds of question: Choice, Score, Noul
1:05 What does 0.8 mean? Calibration
1:23 Fast and cheap, by TypeSafe's numbers
1:41 What Jev isn't for
1:57 The fair question about the headline numbers
2:15 One page
2:28 Your turn
2:45 Outro

Sources:
TypeSafe AI, "Introducing System One Models & Jev" (Sep 15, 2026) — https://typesafe.ai/blog/introducing-system-one-models-and-jev
TypeSafe docs — https://docs.typesafe.ai/introduction · https://docs.typesafe.ai/concepts/system-one · https://docs.typesafe.ai/model-jaggedness/jev-1.13
Simon Willison, "Jev introduces a new shape of LLM" — https://simonwillison.net/2026/Sep/21/jev/
SiliconANGLE (Sep 16, 2026) — https://siliconangle.com/2026/09/16/typesafe-ai-exits-stealth-with-40m-to-build-ai-for-use-by-software/

Photographs (Wikimedia Commons):
Telephone operators, Fort Richardson, Alaska, 1950 — U.S. Army, public domain
U.S. Army Signal Corps operators, Toul, France — public domain
Daniel Kahneman — nrkbeta.no, CC BY-SA (https://creativecommons.org/licenses/by-sa/2.0/)
Automatic letter sorting, Härkingen — Hadi, CC0
Locomotive pressure dials, Da Lat, Vietnam — Dragfyre, CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
Hand-operated railway switch, Mielec, Poland — PIVISO, CC0
Thomas de Colmar arithmometer, 1860 — MKFI, public domain
Greek–French Julian/Gregorian calendar, Sept. 1914 — public domain
G. D. Tiepolo, The Procession of the Trojan Horse into Troy, c. 1760 — public domain
Theodore Roosevelt's typewriter, Sagamore Hill — U.S. Fish and Wildlife Service, public domain

Hosted by Sai. Voice: Kokoro am_onyx, free and local, no account. AI-generated narration. Motion graphics built with Remotion. The equation is typeset locally as outlined SVG. No call to Jev was made for this video, so every Jev figure is TypeSafe's own published claim and is labelled that way. The cost total and the calibration example are arithmetic and a seeded simulation, run locally. All images are real photographs or paintings under public-domain, CC0 or CC BY-SA terms, credited on screen. None were generated. No human-performed audio or video in this production.

Humanitarians AI — https://humanitarians.ai
Musinique — https://musinique.com
Medhavy AI — https://medhavy.com

#AI #Jev #TypeSafe #MachineLearning #LLM #AIExplained #OpenSource #HumanitariansAI #WeeklyUpdate

TAGS

Jev, TypeSafe AI, System One model, decision model, structured outputs, typed outputs, AI for software, calibration, calibrated probability, probability, Daniel Kahneman, Thinking Fast and Slow, System 1 System 2, LLM, large language model, chatbot, AI explained, AI for beginners, gentle introduction, hallucination, AI pricing, tokens, prompt injection, computational skepticism, Humanitarians AI, weekly progress

HASHTAGS

#AI #Jev #TypeSafe #MachineLearning #LLM #AIExplained #OpenSource #HumanitariansAI #WeeklyUpdate
