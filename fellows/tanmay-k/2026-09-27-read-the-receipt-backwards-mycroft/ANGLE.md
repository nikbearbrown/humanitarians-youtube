# Week 24 work-video — angle

**Source material:** `14-mastercard-agentic-ai-payments.md` (case study; corrected 2026-09-27,
original kept as `.original.md`) and `mastercard-agent-pay-pipeline-v2.zip` (original zip kept). The zip is the reference implementation of an AI shopping
agent's purchase through Mastercard Agent Pay: Input Validation → Registration/Verification →
Agent-Consumer Ownership → Permission/Limit → Authorization Gate (unconfigured categories only) →
Verifiable Intent record, run fail-fast by one orchestrator. It has 8 source files, 8 test files and
11 logged design decisions.

**Independently re-run before writing anything below:**
- `python3.12 -m unittest discover -s tests`: **72 tests, 72 passed.** It needs Python 3.10+; the
  system's 3.9 can't import it (`X | None`).
- `demo.py`: all seven scenarios behave as documented.

`docs/DESIGN_DECISIONS.md` and the module docstrings were read first, per the standing rule that a
marked absence is a decision, not a defect.

---

## Survey — prior work-video angles, so nothing repeats

| Week | Company | Film | Teachable claim | Structure |
|---|---|---|---|---|
| 18 | HSBC | *Their Numbers, My Arrows* | one figure, two meanings depending on the citing document | ledger, two columns |
| 19 | DBS | *Where the Record Stops* | label every element CONFIRMED / CONSTRUCTED / BLANK | three-category label |
| 20 | Morgan Stanley | *…Drafts One Thing and Files Another* | a misread source sentence produced a real code error | A/A′, one card run twice |
| 21 | Zurich | *The Stages That Stayed Dark* | output-only tests can pass while the system did the wrong thing; assert on what was never reached | pipeline lamps, dark stages |
| 22 | Capital One | *What Had to Be Invented* | per stage: what would a builder have had to invent? | five-stage interrogation |
| 23 | Lloyds | *The Emptiest Row* | risk concentrates on the system with the least paperwork | four-system matrix |

---

## Ruled out

- **"The Gate ships with zero default criteria"** (DD004, the build's own headline). It's real and
  deliberate, and it has already been the thesis at Zurich (W21) and Capital One (W22) and ruled out at
  Lloyds (W23). A fourth time would be the least original option. It gets one honest line as a
  deliberate boundary, never framed as a gap.
- **"Reach disclosed, performance not"** (case study §5.2, §6.8). The case study itself says this is
  the Lloyds finding again. One line of context, not the spine.
- **DI Pro and Agent Pay read as one story** (§6.3, the case study's central finding). It's genuine,
  but there's no build to run for it (the repo deliberately models Agent Pay only), and every film in
  this series pairs its claim with runnable code. It's kept as a scope line: "two systems; this build
  is about one."
- **Visa vs Mastercard "competing standards"** (§6.5). A framing note with no mechanism to test.

---

## Uniqueness audit (2026-09-28) — the first angle failed it

Every work video we've made was read, not just the survey above: **W15–W23** (Weeks 12–14 were
written reports with no video). The full narration of each was searched for the first angle's ideas.

**First angle, "What Step Two Couldn't Tell Apart" (two different inputs, one state): REJECTED as not unique.**

| Prior film | What it already said |
|---|---|
| **W20** *…Drafts One Thing and Files Another* | Its whole thesis: "two ideas in your source that quietly became one idea in your build"; the card asks "are they still two different things in the code?" |
| **W23** *The Emptiest Row*, B10–B13 | "A clean pass only proves what you actually tested for"; then an attack pass, where a malformed date came back as "no transaction found": "a wrong answer wearing a right answer's clothes" |
| **W21** *The Stages That Stayed Dark*, B13 | "No assertion in the suite can tell them apart" (two builds, same output) |

The lookalike mechanism, the adversarial-pass story and the "confident wrong answer" framing are all
already on the channel. Recolouring them with Mastercard data would be a repeat.

**What no earlier film has: an output that makes a claim about authority.** Mastercard's
Verifiable Intent is, in its own words, a tamper-resistant record of *what a consumer authorized*.
This build writes one for every completed purchase. And the build's most serious finding was a
**receipt that was false**: it named Morgan as authorizing a purchase Morgan never saw. Searched
across W15–W23, no film is built around an output record or asks what earns each line on it. The
nearest is one sentence in W21 B11: "A trail tells you what happened. It cannot tell you that what
happened shouldn't have." That's about an accurate log of a wrong action; this is about a record whose
claims were false, traced field by field. It's cited as the boundary, and the film does not re-make
W21's point.

## The angle — READ THE RECEIPT BACKWARDS

**The film is one receipt.** A single Verifiable Intent record is on screen throughout, and each beat
takes one line of it and asks: **which step checked this before it was written down?**

| Line on the receipt | What vouches for it | What happened when nothing did |
|---|---|---|
| `agent_id` | registration + verification (Step 1) | — |
| `consumer_id` | the ownership check (Step 1b), **added in review round 2** | before it: the receipt named **Morgan**, who never saw the purchase (confirmed pre-fix, README #5) |
| `category` | the permission lookup (Step 2), **exact-spelling only until round 3** | reproduced on the original build: `Household_Staples`, dated after Devon's window, **COMPLETED**, with the receipt reading `authorized_via: authorization_gate` for a purchase Devon had restricted |
| `amount`, `transaction_date` | validation (Step 0) + limit and window (Step 2) | round 1: NaN and −$500 would have passed as ordinary amounts (**one line only; W23 territory**) |
| `authorized_via` | set by the path taken: within limits, or the Gate | the Gate's criteria are **deliberately absent** (DD004): a boundary, said once, not the thesis |
| `merchant` | **nothing**: accepted, carried onto the receipt, never checked (DD011, a named scope limit) | live, today: shoes bought at the grocery merchant **complete**, and the receipt reads `merchant: greenleaf-grocery` |

**The turn:** a seal protects a record *after* it's written. It can't make the lines true. Whatever
cryptography the real Verifiable Intent adds, and this build deliberately adds none (DD005), it can only
seal what the pipeline hands it. That's a general property of signed records, stated as such, not a
claim about Mastercard's implementation.

**The honest ending:** the last line, `merchant`, is still carried rather than proved in v2, on
purpose. Mastercard hasn't disclosed a merchant-restriction mechanism, so the build doesn't invent one.
The film ends on a receipt with one line nothing vouches for, and says so. That's the method working,
not a flaw.

**Teachable move (reusable anywhere):** read any record your system writes (a receipt, an audit log,
an approval, an invoice) **backwards**. For every line, name the check that earned it. A line no
check earned is something the record *carries*, not something it *proves*. Then either add the check,
or say on the record that the line is unverified.

**Framing (standing rules):**
- Lead with what the artifact gives a viewer: a runnable blueprint whose receipt you can audit line by
  line, with 82 tests.
- The false-receipt finding is evidence the review rounds worked.
- DD003, DD004, DD005 and DD011 are stated as deliberate.

## Structure — ONE RECEIPT

The whole film lives on one Verifiable Intent record, read **bottom-up, line by line**. Each line gets
a stamp: the step that vouches for it, or an empty box. This is not a stage walk (W19/W21/W22), a
matrix (W23), a ledger (W18) or one card run twice (W20). It's an output artifact audited backwards.

1. Cold open: a receipt that says Morgan authorized a purchase. Every field is well-formed. It was false.
2. The build, what it gives a viewer, and Mastercard's confirmed functions (Verifiable Intent in
   Mastercard's own words).
3. The move, stated before the first line: read it backwards; who vouches for each line?
4. `agent_id`: vouched for (registration + verification).
5. `consumer_id`: the Morgan receipt, and the ownership check that now earns this line.
6. `category`: live on the original build, a restricted purchase with an authorizing receipt; then v2.
7. `amount` / `date`: one line on round 1.
8. `authorized_via`: which path wrote it; the Gate's deliberate absence of criteria.
9. The turn: a seal protects the record after it's written, not the lines inside it.
10. `merchant`: the empty box, live, and why the build leaves it empty on purpose.
11. The viewer's task: take one record your system writes and stamp every line.
12. Outro.

## Production plan (Week 24's time lesson applied)

1. FACTCHECK (Mastercard facts from the case study's sources; every code claim from a live run),
   then script, then **Gate P with a pronunciation check on every name, number and code token**
   (NaN, `datetime`, `isinstance`, "−$500").
2. Audio, then **Whisper-align immediately**, so every cue is on the Whisper clock before the first
   render.
3. New twin scene: **one beat as stills in both aspects** (UI zones, label sizes, GATE V) before
   rendering the rest.
4. Render once, compile once, then **full PROOF on the first compile**. Batch the fixes, then
   recompile once.
5. The Short gets its own script from the start.
