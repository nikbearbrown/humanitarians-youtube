# SCRIPT — *Read the Receipt Backwards* (Week 24 work video, Mastercard Agent Pay)

**Draft 2, 2026-09-28** (PROOF pre-production fixes 1–5 applied; Gate P delta on B01, B02, B03, B05, B06, B12 signed 2026-09-28). Structure: ONE RECEIPT (see ANGLE.md). A single Verifiable Intent record
is on screen for the whole film, read bottom to top. Each line gets a stamp naming the step that
checked it, or an honest open box. ~1,000 words, about 5:20 at the voice's measured pace.

**Framing (Tanmay, 2026-09-28):** the build uses public information only. Wherever Mastercard hasn't
published how something works, the build doesn't pretend to, and the film says that plainly and
positively ("the build stops where the public record stops"). No "gap", "flaw", "missing" or
"defect". The review findings are shown as the method working.

**TTS spelling:** numbers and years are written in words in the narration (Week 24 lesson: Kokoro
reads digit years as "nineteen hundred…"). On-screen text keeps digits and code names.

---

### B01 · COLD OPEN, the receipt that shouldn't exist
> Here's a receipt an early version of my own build wrote. An AI shopping agent bought forty-two dollars and fifty cents of groceries. Every line is filled in. Every field is well-formed. And it says the purchase was authorized for Morgan. Morgan never saw it. The agent belonged to somebody else, a cardholder called Devon. So how does a receipt like that get written? And what would you check to make sure yours never does?

*On screen:* the receipt, full height. `consumer_id: morgan-02` highlighted. Small label: "RECONSTRUCTION: early version, before review round 2". *Refs:* B7, B4.

### B02 · WHAT THIS IS, and what it gives you
> Hi, this is Tanmay Kulkarni, in for Humanitarians AI. This one's about Mastercard Agent Pay, the system that lets an AI agent pay on a cardholder's behalf. I built a working version of its checks using only public information, and it's yours to run: eighty-two tests, all passing. For purchases like these, Mastercard has described a record called Verifiable Intent, "a tamper resistant record of what a user authorized." Every completed purchase in my build writes one.

*On screen:* the pipeline as a thin strip above the receipt (validation → agent → owner → permissions → gate → receipt); "82 tests · 82 passing"; the M1 quote with its source. *Refs:* B1, B2, B3, M1.

### B03 · THE MOVE
> So here's how I read it now. Backwards. Start at the bottom of the receipt, and for every line, ask one question. Which step checked this, before it was written down? A line with an answer is earned. A line without one is just being carried along. Mastercard asks the same thing, in its own words. "How do we know an agent is doing exactly what we asked, and nothing more?"

*On screen:* an empty stamp column appears beside the receipt's lines; the M3 question. *Refs:* M3, G2.

### B04 · THE AGENT LINE
> The agent line first. Mastercard's framework "begins by registering and verifying AI agents before they are permitted to transact." In my build, that's two separate checks. An agent the network has never seen and an agent whose credentials just failed are two different problems, with two different answers. This line is earned.

*On screen:* `agent_id` stamped **registration + verification**; the two reasons `unregistered_agent`, `unverified_agent`. *Refs:* M5, B6.

### B05 · THE PERSON LINE, the centre
> Now the person line, the one on that first receipt. An agent can be registered and verified, and still not be yours. In the early version, nothing compared who the agent actually belongs to with who it said it was buying for. So Devon's agent could buy "for Morgan." And because Morgan had never set any rules for that agent, it looked like an ordinary new kind of purchase. So it went to the gate that decides new cases, the demo's gate said yes, and the receipt said Morgan approved it. The second review round caught that. Now one step asks first: does this agent belong to this person? If it doesn't, the purchase stops, before anything else runs. Mastercard says its record "confirms the cardholder authorizing the AI agent." In my build, this is the step that earns that line.

*On screen:* `consumer_id` line; the reconstruction receipt vs. today's result `REJECTED · agent_consumer_mismatch`; stamp **ownership check (round 2)**; the M2 quote. *Refs:* B7, B8, M2.

### B06 · THE CATEGORY LINE, found while making this video
> The category line, and I found this one while making this video. Devon set a rule: groceries, up to a hundred and fifty dollars, until the end of twenty twenty-six. A grocery order dated after that should come back to Devon for a decision, and it did. But write the category with a capital H, and the lookup missed Devon's rule completely. It treated it as a category Devon had never set, sent it to that same gate, and the gate said yes. The receipt looked perfect. So now every category is compared in one spelling. Capitals and spaces don't matter anymore, and that order comes back to Devon, like it should.

*On screen:* two rows of the original build: `household_staples` → **ESCALATED · outside_timeframe**; `Household_Staples` → **COMPLETED** (receipt `authorized_via: authorization_gate`). Then v2: **ESCALATED**. Stamp **permission check, one spelling (round 3)**. *Refs:* B9, B10.

### B07 · WHERE THAT FIX STOPS, on purpose
> What I didn't do is teach it that "groceries" means the same thing as "household staples." That would mean inventing a category list Mastercard hasn't published. So a different word still counts as a new category, and the build says so, in a test, instead of guessing.

*On screen:* `groceries` → "treated as a new category (by design)", with the pinned test's name. *Refs:* B11.

### B08 · AMOUNT AND DATE, one line
> Amount, and date. The first review round made sure those are a real number and a real date before anything compares them. A value that isn't a number, or minus five hundred dollars, used to slip through as an ordinary price. Now they're stopped at the door.

*On screen:* `amount`, `transaction_date` stamped **validation + limit and window (round 1)**. *Refs:* B12.

### B09 · THE PATH LINE, and the gate with no built-in rule
> The path line says how the purchase was approved: within the limits Devon set, or by the authorization gate, for the one case Devon never covered. And that gate ships with no built-in rule at all, on purpose. Mastercard hasn't said what should happen when a consumer never set a rule, so the build asks whoever runs it to decide, instead of deciding for them.

*On screen:* `authorized_via` stamped **the path taken**: `within_configured_limits` | `authorization_gate`; a note, "Gate: no default rule, by design". *Refs:* B13, B14.

### B10 · THE TURN, what a seal can and can't do
> Here's what reading backwards taught me. A seal protects a record after it's written. It can show that nobody changed it, and who wrote it. It can't make the lines true. Mastercard describes its record as tamper resistant, with cryptographic proof. Mine has no cryptography at all, on purpose, because the signing scheme isn't public. But whatever the real one uses, a seal can only seal what the pipeline hands it. The truth of every line comes from the checks before it.

*On screen:* a seal lands on the finished receipt; the stamp column stays visible beneath it. *Refs:* G1, M1, B16.

### B11 · THE MERCHANT LINE, the open box
> Which leaves one line. Merchant. Mastercard says a token can be restricted by merchant. It hasn't published how that restriction gets checked. So my build carries the merchant onto the receipt, and checks it against nothing. Buy running shoes at a grocery store, and the receipt says the grocery store. That's the build telling you exactly where the public record stops, and exactly which line you're taking on trust.

*On screen:* `merchant` line with an open box, labelled **carried, not checked (mechanism not published)**; the live shoes-at-grocery receipt; the M8 quote. *Refs:* B15, M8.

### B12 · YOUR TURN
> So try it on something you've built. Take one record your system writes: a receipt, an approval, a line in a log. Go through it from the bottom to the top, and next to every line, write down the step that checked it. For any line with nothing next to it, either add the check, or say on the record that it isn't verified. That's the whole move. The build's repository is linked below: eighty-two tests, plain Python, and a receipt you can audit yourself.

*On screen:* a blank receipt template with an empty stamp column; "82 tests · Python 3.10+ · standard library only". *Refs:* G2, B3.

### B13 · OUTRO
> Read the receipt backwards. Tanmay Kulkarni, in for Humanitarians AI, signing off.

*On screen:* title card, @HumanitariansAI.

---

## Fact trace

Every sentence maps to a FACTCHECK row (refs under each beat). Quotes used verbatim: M1 (B02),
M3 (B03), M5 (B04), M2 (B05), M8 paraphrased as "a token can be restricted by merchant" (B11).
Mastercard facts are primary reads (2026-09-28); code facts are live runs on v2 or the original
build. The one reconstruction (B01/B05) is labelled on screen.

## Checks before Gate P (the Week 24 time lesson, front-loaded)

- [ ] `gate_p_lint.py` on the narration (BREATH, ECHO, NAME)
- [ ] Phonemize every name and number: Tanmay Kulkarni, Mastercard, Devon, Morgan, forty-two
  dollars and fifty cents, twenty twenty-six, eighty-two, "authorization"
- [ ] Uniqueness re-check of the final narration against W15–W23 (no "confident, wrong answer"; no
  "tell them apart"; no "two things became one")
