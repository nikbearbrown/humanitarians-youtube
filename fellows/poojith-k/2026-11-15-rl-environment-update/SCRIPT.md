# Relief Dispatch: week two

## Title card

- Kicker “RELIEF DISPATCH”
- Title “Relief Dispatch”
- Presenter “Poojith K. · Humanitarians AI”
- Composer question “Can an agent keep a relief shift on track?”
- Chip “Relief Dispatch · Week two”
- Disclosure “This video uses AI-generated narration.”

Hi, I am Poojith and this video is about week two of Relief Dispatch, my RL environment project. This video uses AI-generated narration.

## A quick recap

- One shift · 150 requests with deadlines
- The world changes · Roads close, trucks break, stock spoils
- Exact verifier · Checks what's still possible

A quick recap. Relief Dispatch runs one relief shift with a hundred and fifty supply requests, each with a deadline. Roads close, trucks break down and stock spoils while the agent works. After every change, an exact solver checks which requests can still be met, so every score is exact, with no AI judge.

## First full model runs

- 12 full shifts · Qwen, an open model
- 103 of 103 · Warned dead ends noticed
- 115 early closes · Requests it could still deliver

The first full model runs finished: Qwen, an open model, played twelve full shifts. It noticed every dead end, a request that can no longer be met, that gave it a turn of warning: a hundred and three of a hundred and three. Its main loss was giving up early. It closed a hundred and fifteen requests that could still have been delivered.

## Built this week

- Replay viewer · Pauses on key decisions
- Live mode · Watch the model decide
- Harder level · Passed its screening checks

This week I built a replay viewer that pauses on key decisions and shows the solver's verdict, and a live mode that shows the model's decisions as it makes them. I demoed both to the team on Thursday. A harder level is ready too, and it passed its screening checks.

## Four experiments

- Pushed updates · Changes arrive automatically
- Faster world · More changes per turn
- Dead-end warnings · Extra cues
- Repeat run · Same world, same settings

Then I started four controlled experiments, with the plan locked before any run: sending changes to the agent automatically instead of making it check, a faster-changing world, extra warnings about dead ends, and a repeat of an earlier run.

## Early results

- Pushed updates · Within 4 of the best possible
- Dead-end warnings · Didn't help
- Repeat run · 118 → 95

These early results come from single runs on four of six planned world sets. With changes pushed automatically, Qwen finished within four requests of the best possible score on all four worlds. Dead-end warnings didn't help, since Qwen already noticed every warned dead end. And repeating an earlier run with identical settings moved its score from a hundred and eighteen to ninety-five, so single runs vary.

## Takeaway slide

How an agent hears about changes matters. Single runs vary, so test each setup more than once.

So far, the biggest lever is how the agent hears about changes.

## Next

- Repeat runs · Measure the variation
- Harder level · Model tests
- Training setup · Reward from the verifier
- Final report · November 30

Next come repeated runs to measure that variation, model tests on the harder level, and a training setup that takes its reward from the verifier. The final report is due November thirtieth. Thanks for watching.

## Credit

Poojith K. · Humanitarians AI · @HumanitariansAI
