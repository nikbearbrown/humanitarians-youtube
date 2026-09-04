# What Actually Makes an AI "Agentic"?
**Runtime target:** ~9 minutes | **Tone:** Energetic, myth-busting teardown | **Audience:** High-school technicality

---

[VISUAL: Title card. The word "AGENTIC" stamped in bold across a swirling tech-blue background, plastered like a marketing sticker. A red stamp slams down over it: "BUT WHAT DOES THAT MEAN?"]

**NARRATION:**

"Agentic AI." You've seen it on every startup's landing page, every keynote slide, every LinkedIn post promising the future just showed up. But here's the problem: half the products calling themselves "agentic" are doing something a form on a website could basically do. And the other half are running loops that can rack up real costs — or real consequences — while you're not even watching.

So today, we're doing a teardown. Not a dictionary definition — a spectrum. We're taking one task, "book me a flight," and running it through four tiers of AI capability. By the end, you'll be able to look at any "agentic" claim and know exactly where it actually lives.

[VISUAL: A horizontal bar graphic appears at the bottom of the screen, four sections labeled Tier 0 through Tier 3, all greyed out for now]

## TIER 0 — Just a Conversation

Let's start at the floor. Tier zero is a single question, a single answer. You type: "book me a flight to Chicago next Friday." The AI replies with words — maybe something like, "Try Google Flights, compare a few times, book whichever fits your schedule." Helpful advice. Zero action.

[VISUAL: A simple chat window. User message goes in on the left, plain text response comes back on the right. A small padlock icon sits over a greyed-out row of tool icons labeled "no tools available"]

Here's what's actually happening under the hood: the model is predicting the next likely word, over and over, until it's built a full sentence. That's the entire mechanism. There is no flight search, no browser, no bank card. If this were a person, it's like texting your well-traveled friend for advice. Great advice — but they didn't lift a finger to book anything.

## TIER 1 — Tool Use

Tier one is where things get real. Now the model has been given access to a tool — say, a flight search function. You ask the exact same question, and this time it doesn't just talk about flights. It sends a request to a real flight search system, gets back live prices and times, and shows you actual options.

[VISUAL: Diagram. User message flows into a box labeled "AI Model," an arrow labeled "tool call" shoots out to a box labeled "Flight Search API," data flows back in, and the AI displays a clean list of three real flights with prices]

This is what people mean by "function calling" or "tool use." The model recognized it needed outside information, formatted a request the tool could understand, waited for the result, and used it. But watch closely: it stops there. It hands you a list. You still pick a flight, enter your card, hit purchase. One tool call, one job done, then control comes straight back to you.

## TIER 2 — Multi-Step Planning

Tier two is where the AI stops acting like a search bar and starts acting more like an actual assistant. Instead of one tool call, it chains several together, building the plan itself as it goes.

[VISUAL: A flowchart builds one box at a time — "Check your calendar" → arrow → "Search flights" → arrow → "Cross-reference both" → arrow → "Flag a conflict" → arrow → "Ask you a question" → arrow → "Wait for your reply"]

Say it differently this time: "book me a flight to Chicago next Friday, but only if it doesn't clash with anything on my calendar." Now the model has to actually check your calendar, search flights, line the two up against each other, notice you've got a 9 AM meeting that same morning, and come back with something like: "There's a 7 AM flight that works, or an 11 AM one that would make you miss your meeting — which do you want?"

That's planning. A fuzzy goal got broken into ordered steps, multiple tools got used in sequence, and the plan adjusted based on what it actually found along the way. This is the tier most products marketed as "AI agents" genuinely live in. It looks autonomous. But it's bounded — a handful of steps, then it checks back in with you before spending your money.

## TIER 3 — The Autonomous Loop With Memory

And now, tier three — the one everybody actually means when they say "agentic," even though most products on the market can't really do it yet. This is an AI that doesn't just run a plan once and stop. It runs in an ongoing loop: watching, deciding, acting, remembering — and it keeps working toward a goal over hours, days, sometimes weeks, without you standing over its shoulder at every step.

[VISUAL: A looping arrow animation cycling through four labeled stages — "Monitor" → "Decide" → "Act" → "Remember" → back to "Monitor" — with a small calendar in the corner ticking forward day by day]

Picture this instead: you say it once — "get me the best fare to Chicago sometime this month, book it the moment the price looks good." Tier three means it checks prices every day on its own. It remembers that you like aisle seats and morning departures, because you mentioned that in a completely different conversation three weeks ago. It notices the airline cancelled your original flight, rebooks you automatically, and only messages you afterward to say "handled it."

Nothing restarted from zero. It's carrying context and decisions forward across time, and making its own calls about when to act. This is genuinely powerful — and genuinely risky, which happens to be an entire video on its own.

[VISUAL: Small on-screen card pops up briefly in the corner — a thumbnail reading "Why Agents Fail →" — then fades]

## The Actual Framework

So here's your teardown checklist. Next time you see "agentic AI" slapped on a landing page, ask three questions.

One — does it use tools, or does it just talk? If it's just talk, it's tier zero, no matter how it's branded.

Two — does it chain multiple steps into a plan, or does it fire off one tool call and stop? Chaining is tier two behavior.

Three — does it keep running without you, and does it remember what happened in past sessions? That's the only real tier three.

[VISUAL: The four-tier spectrum bar returns, now fully lit up left to right, with a small marker gliding along it as the narrator recaps each tier one more time]

Most of what's sold as "agentic" today comfortably sits in tier one or tier two. True tier three — autonomous, memory-carrying loops — is rare, harder to control, and honestly still being figured out by the best labs building this stuff.

"Agentic" was never a yes-or-no label. It's a spectrum of how much a system does on its own, and how far it carries what it knows between actions. Now you know exactly where to look.

[VISUAL: End card. The spectrum graphic locks in place, subscribe prompt appears, two thumbnail cards link out to "Why Agents Fail" and "Autonomy vs. Control"]

If you want to see what happens when tier two and tier three systems go wrong — and they do, constantly — that's exactly what's up next.

**[END]**
