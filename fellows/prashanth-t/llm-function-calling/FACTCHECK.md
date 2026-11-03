# FACTCHECK — llm-function-calling

Every claim the narration makes, and what backs it. Written before rendering.
Full provenance discussion is in `SOURCES.md`; this is the claim-by-claim ledger.

Register is Plain, which permits **exactly one** flagged inference. It is at B05
and is marked in the narration itself ("One flag: that matching is learned
behaviour, not a lookup table"). Every other line is either definitional or
drawn from the published message schema.

| Beat | Claim | Status | Basis |
|---|---|---|---|
| B00 | A language model cannot know the current weather by itself | VERIFIED | Definitional — a text-generation model has no live input |
| B00 | You have likely seen a model answer such a question correctly | VERIFIED | Observable behaviour of deployed assistants; no rate claimed |
| B01 | Function calling is the model asking your program to run a tool, then using the result | VERIFIED | The published tool-use contract: the model emits a request, the caller executes |
| B02 | The common wrong guess is that the model fetched the data itself | VERIFIED | Stated explicitly as a guess to be tested, not as fact |
| B03 | If the model fetched it, your program would be optional — it is not | VERIFIED | Follows from the execution model: without the caller running the tool, no result exists |
| B03 | A model holds no clock, no connection, no keys | VERIFIED | Definitional |
| B04 | The loop is four steps: describe → request → execute → return | VERIFIED | The published tool-use request/response cycle |
| B05 | Tools are declared as written descriptions: name, description, arguments | VERIFIED | The published tool/function definition format |
| B05 | The description is sent as text in the conversation | VERIFIED | Tool definitions travel in the request payload alongside messages |
| B05 | How the model settles on a tool is learned behaviour, not a lookup table | **INFERENCE — FLAGGED ON SCREEN AND IN VOICE** | This is the one permitted flag; the selection is model behaviour, not a documented deterministic rule |
| B07 | `get_weather(city="Boston")` → `{"temp_f": 41}` → the finished sentence | CONSTRUCTED EXAMPLE, LABELLED | B07's on-screen caption reads "example values, shown to trace the mechanism — not a live reading" |
| B08 | The tool result is appended to the conversation as a message | VERIFIED | The published message schema: `tool_result` is message content, not a side channel |
| B08 | One question therefore costs two model turns | VERIFIED | Follows directly from the schema — the model is invoked again on the longer conversation |
| B08B | The loop can repeat; an agent is this loop run repeatedly | VERIFIED | Follows from the same schema; no new mechanism is introduced |
| B09 | A successful call does not prove the model understood the question | VERIFIED | Right tool with wrong arguments is a documented failure mode |
| B09 | An un-called tool does not prove the tool is wrong | VERIFIED | Under-triggering from a vague description is a documented failure mode |
| BVDT | The model never runs anything; you control the description | VERIFIED | Recapitulation of the above; verdict beats recapitulate, they do not assert new claims |

## Deliberately excluded (would date the video)

No model version numbers. No context-window sizes. No provider feature
comparison. No claim about which models support tool use. No success-rate or
reliability figure — B09 names the two failure *directions* and their shared
cause, with no frequency attached, because no such rate could be stated without
dating immediately.

## Numbers on screen

The only numbers in the reel are `41` (°F) and the step numbers 1–4. The 41 is
part of the constructed example and is captioned as such on the beat that shows
it. No number in this reel is presented as a measurement or a finding, so there
is no published figure to reconcile.

## Register check

Plain does not judge the design. Reviewed every line for drift into Teardown:
no beat rates function calling as a good or bad design choice, and no beat
names what it "optimizes for". B09 states failure modes as mechanism, not as
criticism.
