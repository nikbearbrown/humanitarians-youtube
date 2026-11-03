# READ-ALOUD — Gate P sheet (the work video)

*Read the Receipt Backwards* · generated from `beat_sheet.json` (built from `SCRIPT.md`) by `make_read_sheet.py`.

**How to run Gate P:** read each beat out loud at speaking pace. Listen for rhythm and emphasis,
whether each line of the receipt feels earned in turn, and whether the boundaries (B07, B09, B11)
sound confident rather than apologetic, since they're the build stopping where the public record
stops. Mark anything that trips you in the box. A reply of "Gate P PASS" (with any notes) is
recorded verbatim in `PEDAGOGY.md`. No audio is generated before that.

## Say-it-right checklist (every item already checked against Kokoro's phonemes)

| Word | Should sound like | Where |
|---|---|---|
| Tanmay Kulkarni | as you say it; Kokoro: tˈænmeɪ kˈʌlkɑːɹni | B02, B13 |
| Mastercard | MASTER-card, one word; checked ✓ | B02–B11 |
| Devon / Morgan | DEV-un / MOR-gun; checked ✓ | B01, B05, B06, B09 |
| Verifiable Intent | VAIR-uh-fy-uh-bul in-TENT; checked ✓ | B02 |
| cryptographic / cryptography | krip-tuh-GRAF-ik / krip-TOG-ruh-fee; checked ✓ | B10 |
| "a capital H" | the letter aitch; checked ✓ (the lint flags it as a lone letter; it's intended) | B06 |
| money and years | written in words: "forty-two dollars and fifty cents", "a hundred and fifty dollars", "twenty twenty-six", "eighty-two", "minus five hundred dollars"; all checked ✓ | B01, B02, B06, B08, B12 |

## Quotes: read exactly as written (verified verbatim on Mastercard's own pages, 2026-09-28)

| Beat | Quote | Source |
|---|---|---|
| B02 | "a tamper-resistant record of what a user authorized" | Mastercard, Verifiable Intent page, Mar 5 2026 |
| B03 | "How do we know an agent is doing exactly what we asked, and nothing more?" | same page (the page uses a dash; spoken as a comma) |
| B04 | "begins by registering and verifying AI agents before they are permitted to transact" | Mastercard, Agent Pay Acceptance Framework, Oct 14 2025 |
| B05 | "confirms the cardholder authorizing the AI agent" | Verifiable Intent page |

## Two deliberate echoes the lint flagged (your call by ear)

| Beat | Lines | Note |
|---|---|---|
| B01 | "Every line is filled in. Every field is well-formed." | deliberate parallel; keep, or merge if it sounds listy |
| B03 | "A line with an answer is proven. A line without one is just being carried along." | deliberate parallel: it's the method's two halves |

## The script

### [0:00] B01 · COLD OPEN, the receipt that shouldn't exist

_Tone: quiet and a little unsettled; let "Morgan never saw it" land on its own_

Here's a receipt an early version of my own build wrote. An AI shopping agent bought forty-two dollars and fifty cents of groceries. Every line is filled in. Every field is well-formed. And it says the purchase was authorized for Morgan. Morgan never saw it. The agent belonged to somebody else, a cardholder called Devon. So how does a receipt like that get written? And what would you check to make sure yours never does?

_On screen: the receipt, full height. `consumer_id: morgan-02` highlighted. Small label: "RECONSTRUCTION: early version, before review round 2"._

> ☐ reads cleanly   ☐ note: ______________________

### [0:23] B02 · WHAT THIS IS, and what it gives you

_Tone: friendly, plain; the build is a gift, not a boast_

Hi, this is Tanmay Kulkarni, in for Humanitarians AI. This one's about Mastercard Agent Pay, the system that lets an AI agent pay on a cardholder's behalf. I built a working version of its checks using only public information, and it's yours to run: eighty-two tests, all passing. For purchases like these, Mastercard has described a record called Verifiable Intent, "a tamper-resistant record of what a user authorized." Every completed purchase in my build writes one.

_On screen: the pipeline as a thin strip above the receipt (validation → agent → owner → permissions → gate → receipt); "82 tests · 82 passing"; the M1 quote with its source._

> ☐ reads cleanly   ☐ note: ______________________

### [0:47] B03 · THE MOVE

_Tone: slow down; this is the method, said once_

So here's how I read it now. Backwards. Start at the bottom of the receipt, and for every line, ask one question. Which step checked this, before it was written down? A line with an answer is earned. A line without one is just being carried along. Mastercard asks the same thing, in its own words. "How do we know an agent is doing exactly what we asked, and nothing more?"

_On screen: an empty stamp column appears beside the receipt's lines; the M3 question._

> ☐ reads cleanly   ☐ note: ______________________

### [1:10] B04 · THE AGENT LINE

_Tone: steady, matter-of-fact; ends on a small yes: "This line is earned."_

The agent line first. Mastercard's framework "begins by registering and verifying AI agents before they are permitted to transact." In my build, that's two separate checks. An agent the network has never seen and an agent whose credentials just failed are two different problems, with two different answers. This line is earned.

_On screen: `agent_id` stamped **registration + verification**; the two reasons `unregistered_agent`, `unverified_agent`._

> ☐ reads cleanly   ☐ note: ______________________

### [1:26] B05 · THE PERSON LINE, the centre

_Tone: the centre of the film: tell it like a story, then relief at "The second review round caught that."_

Now the person line, the one on that first receipt. An agent can be registered and verified, and still not be yours. In the early version, nothing compared who the agent actually belongs to with who it said it was buying for. So Devon's agent could buy "for Morgan." And because Morgan had never set any rules for that agent, it looked like an ordinary new kind of purchase. So it went to the gate that decides new cases, the demo's gate said yes, and the receipt said Morgan approved it. The second review round caught that. Now one step asks first: does this agent belong to this person? If it doesn't, the purchase stops, before anything else runs. Mastercard says its record "confirms the cardholder authorizing the AI agent." In my build, this is the step that earns that line.

_On screen: `consumer_id` line; the reconstruction receipt vs. today's result `REJECTED · agent_consumer_mismatch`; stamp **ownership check (round 2)**; the M2 quote._

> ☐ reads cleanly   ☐ note: ______________________

### [2:11] B06 · THE CATEGORY LINE, found while making this video

_Tone: genuine discovery, a bit of surprise at "with a capital H"_

The category line, and I found this one while making this video. Devon set a rule: groceries, up to a hundred and fifty dollars, until the end of twenty twenty-six. A grocery order dated after that should come back to Devon for a decision, and it did. But write the category with a capital H, and the lookup missed Devon's rule completely. It treated it as a category Devon had never set, sent it to that same gate, and the gate said yes. The receipt looked perfect. So now every category is compared in one spelling. Capitals and spaces don't matter anymore, and that order comes back to Devon, like it should.

_On screen: two rows of the original build: `household_staples` → **ESCALATED · outside_timeframe**; `Household_Staples` → **COMPLETED** (receipt `authorized_via: authorization_gate`). Then v2: **ESCALATED**. Stamp **permission check, one spelling (round 3)**._

> ☐ reads cleanly   ☐ note: ______________________

### [2:46] B07 · WHERE THAT FIX STOPS, on purpose

_Tone: calm confidence: stopping here is the point, not an apology_

What I didn't do is teach it that "groceries" means the same thing as "household staples." That would mean inventing a category list Mastercard hasn't published. So a different word still counts as a new category, and the build says so, in a test, instead of guessing.

_On screen: `groceries` → "treated as a new category (by design)", with the pinned test's name._

> ☐ reads cleanly   ☐ note: ______________________

### [3:01] B08 · AMOUNT AND DATE, one line

_Tone: brisk, one breath of context_

Amount and date. The first review round made sure those are a real number and a real date before anything compares them. A value that isn't a number, or minus five hundred dollars, used to slip through as an ordinary price. Now they're stopped at the door.

_On screen: `amount`, `transaction_date` stamped **validation + limit and window (round 1)**._

> ☐ reads cleanly   ☐ note: ______________________

### [3:15] B09 · THE PATH LINE, and the gate with no built-in rule

_Tone: measured; "on purpose" is a choice, said without defensiveness_

The path line says how the purchase was approved: within the limits Devon set, or by the authorization gate, for the one case Devon never covered. And that gate ships with no built-in rule at all, on purpose. Mastercard hasn't said what should happen when a consumer never set a rule, so the build asks whoever runs it to decide, instead of deciding for them.

_On screen: `authorized_via` stamped **the path taken**: `within_configured_limits` | `authorization_gate`; a note, "Gate: no default rule, by design"._

> ☐ reads cleanly   ☐ note: ______________________

### [3:36] B10 · THE TURN, what a seal can and can't do

_Tone: the turn: slower, reflective_

Here's what reading backwards taught me. A seal protects a record after it's written. It can show that nobody changed it, and who wrote it. It can't make the lines true. Mastercard describes its record as tamper-resistant, with cryptographic proof. Mine has no cryptography at all, on purpose, because the signing scheme isn't public. But whatever the real one uses, a seal can only seal what the pipeline hands it. The truth of every line comes from the checks before it.

_On screen: a seal lands on the finished receipt; the stamp column stays visible beneath it._

> ☐ reads cleanly   ☐ note: ______________________

### [4:02] B11 · THE MERCHANT LINE, the open box

_Tone: honest and warm: the open box is a feature; lift on "exactly which line you're taking on trust"_

Which leaves one line. Merchant. Mastercard says a token can be restricted by merchant. It hasn't published how that restriction gets checked. So my build carries the merchant onto the receipt, and checks it against nothing. Buy running shoes at a grocery store, and the receipt says the grocery store. That's the build telling you exactly where the public record stops, and exactly which line you're taking on trust.

_On screen: `merchant` line with an open box, labelled **carried, not checked (mechanism not published)**; the live shoes-at-grocery receipt; the M8 quote._

> ☐ reads cleanly   ☐ note: ______________________

### [4:23] B12 · YOUR TURN

_Tone: direct and encouraging, to the viewer_

So try it on something you've built. Take one record your system writes: a receipt, an approval, a line in a log. Go through it from the bottom to the top, and next to every line, write down the step that checked it. For any line with nothing next to it, either add the check, or say on the record that it isn't verified. That's the whole move. The build's repository is linked below: eighty-two tests, plain Python, and a receipt you can audit yourself.

_On screen: a blank receipt template with an empty stamp column; "82 tests · Python 3.10+ · standard library only"._

> ☐ reads cleanly   ☐ note: ______________________

### [4:50] B13 · OUTRO

_Tone: warm sign-off_

Read the receipt backwards. Tanmay Kulkarni, in for Humanitarians AI, signing off.

_On screen: title card, @HumanitariansAI._

> ☐ reads cleanly   ☐ note: ______________________

_Estimated runtime 4:54 (933 words at 3.17 words/s, the voice's measured pace). Kokoro audio becomes the master clock once generated, and cues are then timed on the Whisper clock._

Every sentence traces to `FACTCHECK.md` (refs under each beat in `SCRIPT.md`). The mechanical pass
(`gate_p_lint.py`): the one BREATH flag (B04, 31 words) is already split; the remaining flags are
the NAME checklist above, the letter H (intended), and the two echoes above.
