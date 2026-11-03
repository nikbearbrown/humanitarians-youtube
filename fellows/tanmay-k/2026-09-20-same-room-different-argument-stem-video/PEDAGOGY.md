# PEDAGOGY / GATE P — *Same Room, Different Argument* (working title)

**VERDICT (draft 4, current): PASS — signed 2026-09-20.**

## Verdict log

| Draft | Words | What changed | Verdict |
|---|---:|---|---|
| 1 | 863 | initial content pass | superseded before signing — mechanical pass caught a misquote and wrong voice, see below |
| 2 | 877 | voice/persona corrected to `am_onyx` | **Signed PASS by Tanmay Kulkarni** — given as a blanket verdict ("all beats pass"), not itemized per-beat or against the seven questions below. Recorded honestly as given, not backfilled with detail that wasn't provided. |
| 3 | 1034 | human-voice rewrite — first-person, curious framing, requested after the draft-2 PASS and before audio generation | **Signed PASS by Tanmay Kulkarni, 2026-09-20**, after reading `READ-ALOUD.md` in full ("read the read aloud file again and it is clear and good to go"). Given as a blanket verdict again, not itemized per-beat or against the nine questions below — recorded honestly as given, same as draft 2. |
| 4 (current) | 18 beats (was 17) | rubric-driven revision: B02 states the checklist explicitly, B11 (new) is a guess-along active task, B12 (new) is the reveal + correction after a padded silence, B17 (was B16) restates the checklist | **Signed PASS by Tanmay Kulkarni, 2026-09-20**, after reading all 18 beats of `READ-ALOUD.md` aloud ("read aloud and pass all beats"). Given as a blanket verdict, not itemized per-beat or against the specific pacing/B11-tone flags raised in the mechanical pass below — recorded honestly as given, same form as drafts 2 and 3. **This is the verdict that clears draft 4's wording — the audio and final master already built from this exact text.** |

### Mechanical pass, draft 4 (B02, B11, B12, B17 only — everything else unchanged from draft 3)

- **Quote fidelity:** B02's/B17's checklist is a synthesized framework, not a quote — no citation needed, and it fairly matches what B04/B08/B13-B14 actually show. B11's two questions are accurate restatements of FACTCHECK 1.4 (Searle) and FACTCHECK 3.2 (Bender & Koller) — neither is sharper than its source. B12's "close readers... are explicit" correctly attributes the distinction to commentary, matching FACTCHECK 3.5's own hedge, not claimed as B&K's own words.
- **Pacing flag:** B02 is ~140 words in one continuous breath — longest beat in the film. Read it and judge whether it needs a break or holds as one thought.
- **Not evaluated by this pass (needs the actual read):** whether B11's guess-game lands as an invitation or a gimmick; whether the 2.4s held pause after it feels earned or slow.

Per this repo's own rule (see Week 22's `PEDAGOGY.md`, and the house build/review loop in
`README.md`, step 4): Gate P is signed by a human after reading every line aloud against
the slates — **not by a script, and not by Claude.** Claude cannot judge whether narration
lands for an audience; that judgment is the entire point of this gate. What follows below
is the mechanical pass only — the part a script (or a careful read-through) can catch
before the live read happens, so the live read isn't spent on things that don't need a
human ear. It is not a substitute for the read, and audio must not be generated until
someone actually does it and fills in the verdict at the bottom.

---

## Mechanical pass — findings, already fixed in `beat_sheet.json`

1. **B12 was misquoting its own source.** Original draft dropped "haphazardly" from
   Bender et al.'s sentence without marking the omission, and silently substituted
   Margaret Mitchell's real name for the pseudonym she's actually credited under on the
   paper (Shmargaret Shmitchell) with no acknowledgment. Both are now fixed: the quote
   restores "haphazardly," and the narration names both the real person and her published
   byline. Word count rose 849 → 863; B12's duration estimate rose 16s → 19s.
2. **No other quote-fidelity issues found** on comparison against `FACTCHECK.md`'s
   verified rows (B03's Searle 1999 restatement, B04's Schank quote, B10's B&K abstract
   quote, B12's stochastic-parrot definition all match their FACTCHECK rows verbatim).
3. **Wrong presenter voice/persona inherited from the source stub.** Draft 1 used the
   house-default Kore persona (`af_kore`, "This is Kore, in for Humanitarians AI") copied
   from `chinese-room-explainer-vox`'s old metadata. Checking Weeks 20-22 shows this
   fellow has an established voice across the whole series — `am_onyx`, presenter
   "Tanmay Kulkarni, in for Humanitarians AI" — which `README.md` requires fellows to keep
   consistent absent an explicit re-voice decision. Fixed: all 18 beats now carry
   `am_onyx`; B00 is the generic brand card ("This is Humanitarians."), matching Weeks
   20-21's pattern; B02 now opens with "Hi — this is Tanmay Kulkarni, in for Humanitarians
   AI," matching Week 21's B02; B17 signs off by name, matching Week 21's and Week 22's
   outros. Word count rose 863 → 877; runtime 4:31 → 4:37.

## Mechanical pass — pronunciation risk (needs `metadata.pronunciation` before first Kokoro run)

Not yet added to `beat_sheet.json` — listed here so the first audio pass doesn't discover
these cold, same requirement Week 22 flagged.

| Term | Beat(s) | Risk |
|---|---|---|
| Searle | B01, B03–B05, B08, B11 | "SIRL" not "SEARL-ee" — common TTS miss |
| Schank | B04 | rhymes with "tank," not "shank" |
| SAM | B04 | spoken as the word "Sam" — a listener may momentarily parse it as a person's name, not an acronym; flagged for the read (question 2 below), not just pronunciation |
| Stevan Harnad | B06–B08 | "Stevan" (like Steven); "har-NAD," stress on second syllable |
| Alexander Koller | B09, B11 | German-origin surname, "KOH-ler" |
| Timnit Gebru | B12 | "TIM-nit guh-BROO" |
| Angelina McMillan-Major | B12 | hyphenated compound surname — pacing risk more than pronunciation |
| Shmargaret Shmitchell | B12 | deliberately absurd pseudonym; if mispronounced or rushed it can sound like a TTS glitch rather than a joke — needs a deliberate beat of space around it |
| "a priori" | B10 (verbatim quote) | Latin phrase inside a direct quote — cannot be paraphrased away; must be checked by ear |

## Mechanical pass — the film's own unit hazard

Week 22's Gate P flagged a "unit hazard" (the same physical rate spoken three different
ways). This film has the structural equivalent: the same underlying worry — *can a system
that only manipulates symbols/form ever mean or understand anything* — is named
differently by every act (Searle: "understanding"; Harnad: "intrinsic meaning"; Bender &
Koller: "meaning learned from form"; Bender et al.: "no reference to meaning"). The film's
entire thesis depends on a listener tracking that these are precise, non-interchangeable
claims, not four names for the same thing. This is not fixable mechanically — it's
question 1 below.

---

## Per-beat record (blank — for the human read on draft 3)

| beat | act | start | dur | PASS / FIX / CUT | what I heard |
|---|---|---:|---:|---|---|
| B00 | GREETING | 0:00 | 2s | | |
| B01 | HOOK | 0:02 | 18s | | |
| B02 | FRAMEWORK | 0:20 | 29s | | |
| B03 | ROOM | 0:49 | 25s | | |
| B04 | TARGET | 1:14 | 23s | | |
| B05 | PRE-REJECTION | 1:37 | 26s | | |
| B06 | GROUNDING | 2:03 | 16s | | |
| B07 | DICTIONARY | 2:19 | 20s | | |
| B08 | IRONY | 2:39 | 21s | | |
| B09 | OCTOPUS | 3:00 | 18s | | |
| B10 | SCENARIOS | 3:18 | 22s | | |
| B11 | CORRECTION | 3:40 | 24s | | |
| B12 | PARROT | 4:04 | 21s | | |
| B13 | DISAVOWAL | 4:25 | 20s | | |
| B14 | CONTESTED | 4:45 | 22s | | |
| B15 | VERDICT | 5:07 | 20s | | |
| B16 | TASK | 5:27 | 15s | | |
| B17 | OUTRO | 5:42 | 4s | | |

---

## Questions only the read can answer

1. **The four-names problem.** Does the ear actually track that "understanding,"
   "intrinsic meaning," "meaning learned from form," and "no reference to meaning" are
   four different, precise claims — or do they blur into "basically the same worry, said
   four ways"? If they blur, the film's central point (these people are *not* saying the
   same thing) fails on delivery even though the script is correct on paper.
2. **SAM.** In B04, does "Roger Schank's SAM" read clearly as a named program, or does it
   land as a person's name and cause a beat of confusion before the next sentence
   clarifies it?
3. **B08's pronoun load.** "Same room. Same rejected reply. A different person, a decade
   later, betting Searle was wrong about it." — three short sentences leaning on the
   listener remembering who proposed what from B05. Does it land as a payoff, or does it
   need Harnad's name repeated to stay clear?
4. **The callback gap.** B01 states the myth at 0:03. B11 answers it at 2:58 — nearly
   three minutes later, with three other people's material in between. Does the answer
   still land as answering that specific opening claim, or has the thread gone cold and
   need a one-line reminder of what B01 said?
5. **B11's metaphor.** "Two different questions wearing similar costumes." Does that read
   as a clarifying image, or as cute-but-confusing at the film's most important turn?
6. **Shmargaret Shmitchell.** Does the pseudonym land as the real, documented, slightly
   absurd fact that it is, or does it sound like a scripting error? This is the one place
   in the film where "true and cited" might still play as "wrong" to the ear.
7. **B14's placement.** Is the "this isn't settled" honesty beat, arriving right before
   the verdict, read as intellectual honesty or as the film undercutting its own argument
   at the worst possible moment?
8. **Genuine or performed curiosity.** Draft 3 added first-person asides — "here's what
   surprised me," "the part that made me sit up," "I want to be honest about something."
   Read aloud, do these land as real curiosity, or as a curiosity *voice* bolted onto
   sentences that are still fundamentally lecturing? This is the question the rewrite
   exists to answer.
9. **Pacing under the added words.** Draft 3 is 157 words and ~69 seconds longer than
   draft 2 (4:37 → 5:46) purely from the more conversational framing. Does the extra
   runtime buy real warmth, or does it start to drag by B14-B15 when the four-claim
   payoff should be tightening, not loosening?

---

## Verdict

Signed by: **Tanmay Kulkarni**  date: **2026-09-20**

`VERDICT:` **PASS** (draft 4 — 18 beats, 1154 words, ~5:46 measured)

Given as a blanket pass on the full `READ-ALOUD.md` read ("read aloud and pass all
beats"), not itemized against the per-beat table, the nine draft-3 questions, or the
draft-4 mechanical-pass flags (B02's pacing, B11's tone) above — same form as the
draft-2 and draft-3 verdicts. Recorded honestly rather than backfilled. This clears
draft 4's wording; the final master already built from this exact text (see
`PROOF-REVIEW.md` Review 9) stands as the signed deliverable.
