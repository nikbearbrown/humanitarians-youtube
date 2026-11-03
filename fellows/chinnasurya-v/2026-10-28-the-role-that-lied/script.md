# THE ROLE THAT LIED
### Why a substring match is the wrong way to read an LTI role

Single-topic explainer. Source: `medhavi-hub/lib/lti-v1-oauth.ts` (`parseLTIRole`),
`lib/lti-auth-bridge.ts` (`determineUserRole`), `tests/lti-roles.test.ts`, and
`medhavy-lti-security-review.md`.

---

## ART DIRECTION

**Script-native brutalism.** Same system as the other reels in this series.

| Role | Value |
|---|---|
| ground | `#0A0A0A` |
| paper | `#F2F0EB` |
| signal | `#E8452C` |
| mute | `#6B6B6B` |

Four colours. Never a fifth.

**Type** — two families only. Display: one grotesk, weight 700+, tracking -2%.
Data/labels: one mono, 400/700.

**Layout** — single column, stacked. Every beat must read at 16:9 and at 9:16
without a second layout, so nothing is placed side by side and nothing is placed
by a fraction of the frame width.

**Hard rules**

- Hard cuts only. No easing, no fades between states.
- `border-radius: 0`. Boxes drawn as four filled rectangles.
- No screenshots, no logos, no photography. Drawn frames only.
- Role URNs appear in mono, spelled exactly as the code spells them.
- Nothing key-shaped, credential-shaped or hostname-shaped ever appears.

---

## SCENES

### B00 — INTRO · title card

> Hi, I am Surya, and this video is about one line of code that decided who was
> a teacher, and why the way it decided was wrong.

**Shot** — TITLE. "THE ROLE THAT LIED" flush left; signal rule above; mono
subtitle `READING AN LTI ROLE`.

---

### B01 — WHERE THE ROLE COMES FROM

> When Canvas launches our tool, the signed token carries a roles claim. It is a
> list, and the entries are not words. They are identifiers, written as full
> URNs. Our job is to turn that list into one decision: is this person a
> student, or do they run the course.

**Shot** — One mono line, full width, in paper:
`http://purl.imsglobal.org/vocab/lis/v2/membership#Instructor`. Beneath it, in
mute: `A LIST OF URNs - NOT WORDS`. Then a single downward arrow to a signal
block: `STUDENT OR INSTRUCTOR`.

---

### B02 — THE SHORTCUT

> The quick way to do that is to ask whether the text contains the word
> Instructor. It is one line, it reads naturally, and it passes every test you
> would think to write.

**Shot** — A single mono line in signal, centred in its own bordered box:
`roles.includes("Instructor")`. Beneath, in mute: `ONE LINE - READS NATURALLY -
PASSES THE OBVIOUS TESTS`.

---

### B03 — WHAT IT ACTUALLY MATCHES

> The problem is what else contains that word. A role identifier ending in
> PseudoInstructor contains it. So does one that is simply named badly. The
> check is not asking what the role is. It is asking whether those ten letters
> appear anywhere at all, and that is a different question.

**Shot** — Three mono rows stacked, each appearing 4 frames apart, each with the
substring `Instructor` picked out in signal while the rest stays paper:
`LearnerInstructorFake` · `urn:lti:role:ims/lis/Learner#PseudoInstructor` ·
`NotAnInstructorReally`. Beneath, in signal: `ALL THREE MATCH`.

---

### B04 — WHERE THE MEANING LIVES

> The meaning of a role URN is not spread through the string. It sits in the
> last segment, after the final slash or hash. Everything before it is
> namespace. So the right question is not does this contain Instructor. It is
> does the final segment equal one of the identifiers we accept.

**Shot** — One long mono URN across the full width, with everything before the
final `#` dimmed to mute and only the final segment in signal, boxed. Caption
beneath: `THE LAST SEGMENT - EVERYTHING ELSE IS NAMESPACE`.

---

### B05 — THE FIX

> So we split on the separator, take the final segment, lowercase it, and look
> it up in a set of the identifiers we actually recognise. Instructor,
> TeachingAssistant, ContentDeveloper, Administrator. Anything not in that set
> is a student. It fails closed, which is the direction you want a mistake to
> fall.

**Shot** — A vertical pipeline, each stage a full-width bordered row appearing 3
frames apart: `SPLIT ON / # :` · `TAKE THE LAST SEGMENT` · `LOWERCASE` · `LOOK UP
IN THE ALLOW LIST`. Terminal row, filled signal: `NOT IN THE SET = STUDENT`.

---

### B06 — THE TESTS ARE THE RECORD

> And then the escalation strings become test cases. Those three go in as inputs
> that must come back as student, so the next person who finds the one-line
> version attractive has to make them pass first.

**Shot** — Three mono rows, each with a signal marker and the expected result in
mono: `LearnerInstructorFake -> student` · `Learner#PseudoInstructor -> student`
· `instructor-wannabe -> student`. Caption: `FAILS CLOSED - AND STAYS THAT WAY`.

---

### B07 — OUTRO

> One line became four, and the four say what they mean. Substring matching is
> not a cheap version of an allow list. It is a different check that happens to
> agree with it most of the time.

**Shot** — Two full-width rows: `SUBSTRING - IS IT IN THERE SOMEWHERE` in mute,
and `ALLOW LIST - IS IT EXACTLY THIS` in signal. Hard cut to the title restated.

---

## APPENDIX — CLAIMS AND SOURCES

| # | Beat | Claim | Source |
|---|---|---|---|
| 1 | B01 | The launch token carries a roles claim, as a list of URN identifiers | LTI 1.3 specification (IMS Global); `lib/lti-auth-bridge.ts` reads `roles` from the validated claims |
| 2 | B03 | A substring check matches strings whose final segment is not an accepted role | `tests/lti-roles.test.ts` — the three strings shown are literal test inputs asserted to return `student` |
| 3 | B04 | The role identifier is the final segment after `/`, `#` or `:` | LTI 1.3 role vocabulary; `parseLTIRole` splits on `[/#:]` and takes the last element |
| 4 | B05 | The fix splits, lowercases and looks up an allow-list set | `lib/lti-v1-oauth.ts` `INSTRUCTOR_ROLES`; `lib/lti-auth-bridge.ts` `ADMIN_ROLES` / `INSTRUCTOR_ROLES` |
| 5 | B05 | Unrecognised roles resolve to student | `parseLTIRole` returns `"student"` as its default |
| 6 | B06 | The escalation strings are committed as test cases | `tests/lti-roles.test.ts`, the "fails closed on substring-escalation attempts" block |

**Threat model, stated precisely.** The roles claim arrives inside a
platform-signed token, so this is not a reel about forging a token: signature
verification already covers that, and is the subject of a separate reel. What
this fixes is **misreading legitimate platform input**. Role vocabularies are
extensible, platforms can define custom and sub-roles, and a substring test
cannot tell an accepted identifier from a longer string that merely contains it.
The reel does not claim an exploit was observed in production.

**Invented values: none.** The three strings in B03 and B06 are copied from the
test file.
