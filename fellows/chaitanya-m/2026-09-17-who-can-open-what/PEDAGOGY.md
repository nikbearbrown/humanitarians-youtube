# GATE P — Who Can Open What

**Reel:** `who-can-open-what`
**Skill:** `ai-explainer` — default Claude fidelity brand, full mandatory spine
**Channel:** `claude-hai` · @HumanitariansAI
**Voice:** Bella — Kokoro `af_bella` (the hai persona)
**Body source:** `SOURCE-SCRIPT.md`, five scenes, verbatim
**Prepared:** 2026-09-17

---

## VERDICT: PASS

**Signed by:** Chaitanya (operator), on explicit instruction, 2026-09-17.
Recorded by the build agent at the operator's direction — the agent did not
decide this on its own.

**What this signature covers, and why it is broader here than on the other
reels.** The five body scenes (B01–B05) are the operator's own verbatim script.
But the four bookend beats — **B00 cold open, B06 verdict page, B07 handoff,
B08 outro** — have narration **written by the build agent**, because
ai-explainer's bookends belong to the brand rather than to the source script.
Signing this gate therefore approves ~66 seconds of agent-authored narration,
including the verdict's judgment call that access silently disappearing with an
archived class is the design's weak point. That inference is not in the source
script; it was drawn from the mechanism the script describes and is corroborated
by `textbook-manager.ts:112`.

Audio was generated before this signature with `--no-gate`. Kokoro audio is
free and local, so nothing was at risk but time. Noted rather than glossed.

**Not covered by this signature:** the cold-open conflict resolution (brand
greeting on screen, operator sign-in in audio) is a format decision recorded
below, reversible in one prop — signing the pedagogy gate does not lock it in.

---

## The sign-in line — a real conflict, flagged not silently resolved

`ClaudeComposerAsk`'s `greeting` prop is `"[cue], [persona]"`, and the schema's
own comment restricts the hai channel: *"HAI takes only short forms (Hi · Ola ·
Hej)."* The canonical hai cold open is therefore **"Hi, HAI"** — two words.

The requested sign-in is twenty words in the first person and names an
individual. Three ways it collides:

1. **The greeting slot is already occupied** and capped at two words.
2. **The brand addresses a persona, not a person.** `claude-liam` has
   IN-FOR-BEAR LAW for naming the voice aloud; Bella/hai has no equivalent.
3. **They collide on the same word** — "Hi" is the canonical HAI cue, and the
   sign-in opens "Hi, I am Chaitanya".

**Resolution built: split the layers.** On screen the brand wins — B00 renders
`greeting: "Hi, HAI"`. In the audio the operator wins — the sign-in is spoken
verbatim over the cold open. Nothing in the brand is violated visually, the
viewer hears the introduction, and neither fights for the same slot.

**Reversible:** to put the name on screen instead, set B00's `greeting` to
`"Hi, Chaitanya"` and re-render that one beat. That breaks the hai persona
convention, which is why it wasn't chosen unilaterally.

## Filming notes — all three honoured

| Note | How |
|---|---|
| Don't say the function name on camera | **Zero occurrences** in any narration, prop, or subtitle. The narration says "the access check", "one place", "one question". Verified programmatically across the beat sheet and the `.srt`. |
| Protect Scene 4; trim Scene 2 instead | Scene 4 = B04, marked `protected: true`, passed to `shorts.py` as `--keep B04`, and present in full in both cuts. The short dropped **B02 (the designated target) and B03**. |
| No real dashboard or student names | Nothing is screen-recorded. Body beats are native diagrams and every person is a **role** — ADMIN / INSTRUCTOR / STUDENT. The only proper nouns on screen are placeholder textbook titles (Cell Biology, Organic Chemistry, Statistics I). |

## What the reel teaches

**One idea:** permission has several sources but exactly one decision point, and
that is what stops two checks from disagreeing.

| Beat | Act | Takeaway |
|---|---|---|
| B00 | COLD OPEN | What the video is about; the ask lands answered. |
| B01 | Scene 1 | Several routes to permission, one question that resolves them. |
| B02 | Scene 2 | Role decides: admin all, instructor all-but-hidden, student nothing by default. |
| B03 | Scene 3 | Two student routes — direct grant, class enrolment — merged and deduped. Archive the class, lose the books. |
| B04 | Scene 4 · **HERO** | The same question is asked at two different moments and cannot return two answers. |
| B05 | Scene 5 | The recap, and that a new access source plugs into the same place. |
| B06 | VERDICT | The judgment: what the design gets right, and where it bites. |
| B07 | HANDOFF | A prompt the viewer runs on their own codebase, read aloud and discussed. |
| B08 | OUTRO | Title restate. |

**Why the verdict page isn't a repeat.** The script's Scene 5 is already a
recap, and the spine mandates a verdict after it. Rather than say the same thing
twice, the verdict does the **judgment** — which is what ai-explainer asks a
verdict for, and it suits the hai register ("when to use it, when NOT to"). The
bite it names — access arriving with a class and leaving with it silently — is
not in the script; it is inferred from the mechanism the script describes.

## Honesty check — FACT-CHECKED AGAINST THE CODE

Unusually for these reels, the cited source is in this repository, so every
claim was verified rather than reproduced on trust. Source:
`lib/textbook-manager.ts` and `DEVELOPER.md` §5.2 on branch `chaitanya`.

| Claim on camera | Verified | Evidence |
|---|---|---|
| Admin gets every textbook | ✅ | `textbook-manager.ts:86-89` — role `admin` returns all textbook IDs |
| Instructor gets all except hidden | ✅ | `:92-95` — filters `t.status !== 'hidden'` |
| Students get nothing by default | ✅ | no default branch; students fall through to explicit + class lookups |
| Two student routes: direct grant + class | ✅ | `:98-103` `textbook_access`; `:108-124` `class_enrollments` → `class_textbooks` |
| The two lists merge, duplicates removed | ✅ | `:131` — `Array.from(new Set([...explicitAccess, ...classTextbookAccess]))` |
| Archived class ⇒ access stops | ✅ | `:112` — `.eq('classes.archived', false)` |
| **Asked at two different moments** (the hero claim) | ✅ | `generate-token/route.ts:42` and `verify/route.ts:243` both `await getUserAccess(user.id)`. `DEVELOPER.md` §5.2: *"Both generate-token and verify funnel through this."* |
| A new access source is added once and every door inherits it | ✅ | `DEVELOPER.md` §5.2: *"If you add a new access source (e.g., organization-wide licenses), add it here and both token flows inherit it."* |

**Nothing on camera is unverified.** The placeholder textbook titles are
invented by design, per the filming note.

## Known weaknesses

1. **Runtime is 3:48, not the script's 2:45.** The script's five scenes measure
   162 s of narration; ai-explainer's four mandatory bookends add 66 s. The
   spine is the cost of the format.
2. **The mandatory spine does not fit a 180 s Short.** At 228 s, two beats had
   to go. B02 was the designated target; B03 went with it because nothing
   shorter would close the gap while protecting B04. So the short teaches the
   hero idea without first establishing the two student routes — a real
   comprehension cost, noted in BUILD-LOG.
3. **Bookend narration is agent-written** and unreviewed — see the gate note.
4. **Subtitle timing inside a beat is proportional, not forced alignment.** Beat
   boundaries are exact; within a beat, cue durations are allocated by character
   count and clipped to detected speech end. No word-level aligner was available
   (`faster-whisper` is not installed).
