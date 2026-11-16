# ReAct: the loop behind AI agents

Version 2. Estimated 2:25 before the approved narration is measured.

## Title card

Kicker “HUMANITARIANS AI · AI AGENTS”. Title “ReAct: the loop behind AI agents”. Presenter “Poojith K. · Humanitarians AI”.
Composer question “How does an AI agent decide what to do next?”. Chip “ReAct · Concept”.
This video uses AI-generated narration.

Hi, I am Poojith and this video is about ReAct, the loop many AI agents use to decide what to do next. This video uses AI-generated narration.

## Beat 1 · Two ways to fall short

- Reasoning only · Plans, never checks
- Acting only · Checks, never plans
- ReAct · Plans, then checks

A model can reason step by step without looking anything up. But if it starts from a wrong fact, every later step carries the mistake. Or it can use tools with no written plan, and lose track of what comes next. ReAct, from a 2022 paper by researchers at Princeton and Google, gives the model both.

## Beat 2 · Thought, action, observation

- Thought · What should I check?
- Action · Call a tool
- Observation · What came back
- Repeat · The result guides the next thought

The loop has three steps. A thought says what to check. An action calls a tool. The observation is what comes back, and it shapes the next thought. Then the loop repeats. Agent frameworks today, like OpenAI's Agents SDK, run this same loop of tool calls and results.

## Beat 3 · Find a quiet study room

- Thought · Check Room A
- Observation · Room A is booked
- Thought · Try Room B
- Observation · Room B is free

Say an agent needs a quiet study room. It thinks: check Room A. It reads the schedule, and Room A is booked. So it changes course, checks Room B, and finds it free. Now it can recommend Room B, and you can see exactly which result changed its mind.

## Beat 4 · What the paper found

- Household tasks · 71% vs 45% success, best of six prompts
- Online shopping · 40% vs 30.1% success
- Question answering · Reasoning alone scored higher

In simulated household tasks, the best ReAct prompt succeeded seventy-one percent of the time, against forty-five for the best acting-only prompt. In a simulated online store, it reached forty percent, against thirty point one. It didn't win everywhere: on a question-answering test, reasoning alone scored higher.

## Beat 5 · Where the loop stalls

- Context grows · Every round adds more to read
- Repeats · Same thought, same action
- Errors compound · Old mistakes invite new ones

The loop has limits. Every round adds more for the model to sift through. The paper shows agents stuck repeating the same thought and action. And later experiments found that errors left in the history make new errors more likely.

## Takeaway and close

Read the trace. Find the observation that justified the next step.

In my RL environment project, an agent runs this loop again and again while the world changes around it. So the next time an agent uses a tool, ask what it learned from the result, and whether that changed its next move. Thanks for watching.

## Credit

Poojith K. · Humanitarians AI · @HumanitariansAI
