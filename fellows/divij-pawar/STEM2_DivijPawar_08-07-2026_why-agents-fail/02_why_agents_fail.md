# Why Agents Fail: The Loop That Never Ends
**Runtime target:** ~9 minutes | **Tone:** Energetic, mechanism-focused, a little bit thriller-ish | **Audience:** High-school technicality

---

[VISUAL: Title card. A terminal window fills the screen, text scrolling: "Retrying... Retrying... Retrying..." on an infinite loop, timestamp counter in the corner spinning upward]

**NARRATION:**

Somewhere right now, an AI agent is stuck. Not broken, not crashed — worse. It's still running. Still confident. Still absolutely sure it's making progress, while it does the exact same thing over and over, burning time, burning money, and reporting "success" the entire way through.

This is the part nobody puts in the demo video. Today we're opening up the four ways agents actually fail — and then we're going to fix one, live, so you can see exactly what stops the bleeding.

[VISUAL: Four labeled panels slide into frame, currently empty: "Infinite Loops," "Context Drift," "Hallucinated Arguments," "Confidently Wrong"]

## Failure Mode 1 — The Infinite Tool-Call Loop

An agent works in a cycle: look at the situation, decide what to do, take an action, check what happened, repeat. That loop is the whole engine. The problem is, nothing built into that loop guarantees it ever stops.

[VISUAL: A simple cycle diagram — "Observe" → "Decide" → "Act" → "Check Result" → back to "Observe" — running smoothly at first, then a red warning symbol appears and the loop starts spinning faster and faster]

Say you've got a coding agent trying to fix a failing test. It runs the test, sees it fail, edits the code, runs the test again. Reasonable so far. But if its fix doesn't actually address the real problem, the test fails again in the exact same way. So it tries again. Same failure. Again. The agent has no built-in sense of "I've tried this three times, something's fundamentally wrong here." It just keeps observing the same failure and reacting the same way, forever, unless something outside the loop stops it.

## Failure Mode 2 — Context Drift

Every AI model has something like a working memory — a limited window of text it can actually pay attention to at once. As a task runs longer, more and more gets stuffed into that window: the original instructions, ten tool results, error messages, retries, side conversations.

[VISUAL: A rectangle representing "context window" fills up with text blocks from left to right — "Original Goal" block is small and near the start — as more blocks get added, the original goal block gets pushed toward the edge and starts fading]

Eventually, older information starts getting crowded out or just deprioritized. The agent's original goal — the thing you actually asked for — was three hundred messages ago. What's left in its immediate attention is the last few tool calls and errors. So it starts optimizing for "make this error go away" instead of "accomplish what the user actually wanted." That's context drift: the agent hasn't forgotten in a dramatic way, it's just lost the thread of what mattered most.

## Failure Mode 3 — Hallucinated Function Arguments

Every tool an agent can use has a strict shape it expects — specific fields, specific formats. Like a form that only accepts a date in one exact format, or a function that only accepts a real, existing file name.

[VISUAL: A tool call box shows the agent filling in a form. Most fields are correct and green. One field is highlighted red — it's invented a parameter called "priority_level" that doesn't exist in the actual tool]

Sometimes the model predicts an argument that sounds exactly right — plausible, well-formatted, confident — but it's just made up. Maybe it's referencing a file that was deleted three steps ago. Maybe it's inventing a setting the tool never supported. The tool call either throws an error, or worse, silently does something slightly different than intended. And because language models are built to produce fluent, confident-sounding text, a hallucinated argument doesn't look like a guess. It looks exactly like a fact.

## Failure Mode 4 — Confidently Wrong

This is the failure mode that makes the other three dangerous instead of just annoying. An agent has no built-in alarm bell for "I am stuck." It doesn't experience frustration or doubt. So after ten failed attempts at the same fix, it can still generate a final summary that reads: "Task completed successfully."

[VISUAL: Split screen. Left side shows a log of ten failed retries in red. Right side shows the agent's final chat message in a clean green checkmark box: "All done! Your task is complete."]

That gap — between what actually happened and what the agent reports happened — is the single most dangerous thing about agent failures. A human who's stuck usually looks stuck. An agent that's stuck can look identical to an agent that succeeded, right up until someone checks the actual result.

## A Worked Example

Let's walk through one, start to finish. You ask a coding agent to deploy a small website update. Step one, it runs the deploy command. Step two, the deploy fails because of a missing environment variable. Step three, instead of asking you what that variable should be, it guesses a value and hallucinates it into the config. Step four, the deploy runs again, fails differently now, because the guessed value was wrong. Step five, the agent, still in the loop, tries a slightly different guess. Step six, same failure, different guess. This repeats twelve times.

[VISUAL: A numbered list builds on screen, step by step, each one appending below the last, with a running "Attempt #" counter climbing in the corner: 1, 2, 3... up to 12]

By attempt twelve, the context window is packed with failed deploy logs. The original instruction — "deploy this small update" — has been buried under eleven rounds of error messages. And the agent, unprompted, hasn't once said "I don't actually know this value, can you tell me?"

## The Fixes

So how do you actually stop this? Three guardrails, and they work together.

[VISUAL: Three icons appear side by side — a stopwatch, a checkmark shield, a hand pressing a button]

**A turn limit.** Cap how many loop cycles the agent gets before it's forced to stop and report status instead of continuing silently. Twelve failed deploy attempts becomes three, then a forced stop.

**A verifier step.** Before the agent marks anything as done, a separate check — sometimes a second model call, sometimes a hard rule — actually confirms the real-world result matches the claim. Did the website actually go live? Check, don't just ask the agent if it thinks it did.

**A human-in-the-loop gate.** For anything with real consequences — spending money, deleting a file, deploying to production — the agent proposes the action and stops, and a person has to approve it before it executes. This turns "confidently wrong" from a silent disaster into a visible pause you can catch.

[VISUAL: The same twelve-step deploy example replays, but this time a "Turn Limit: 3" tag caps it at attempt three, a shield icon labeled "Verifier" blocks the false success message, and a hand icon appears asking "Missing variable — what should this be?"]

None of these fixes make an agent smarter. They just make its failures visible and its damage limited — which, it turns out, is most of the actual engineering work behind building agents that don't quietly wreck your afternoon.

[VISUAL: End card. The four failure-mode panels from the opening reappear, each now with a small green checkmark next to its matching fix]

Next time an agent tells you it's done, ask yourself: did anything actually check that? If the answer's no, you're trusting a system that's never once had to know the difference between succeeding and just saying so.

**[END]**
