# GATE P — Ten Prefixes, Eleven Tables

**The one idea.** The schema does three jobs and nothing else, and a table whose
job is to expire is doing security work rather than bookkeeping.

| Beat | The viewer should be able to say afterwards |
|---|---|
| B00 | this is about the database behind the integration |
| B01 | three jobs: who may launch, mapping identity, forgetting on a timer |
| B02 | two tables are the guest list, and a launch from outside them is not a launch |
| B03 | we store a correspondence between two identifiers, not a copy of a person |
| B04 | two tables exist in order to forget, and that is a security control |
| B05 | three more carry the older protocol, same shapes, older handshake |
| B06 | ten is a count of names, eleven is a count of protections, and both were right |
| B07 | RLS is on all eleven, service role only, and a smaller schema leaks less |

**Register check.** Second person, plain English. Table names appear in mono,
spelled exactly as they are in the migration files, because a schema reel that
paraphrases identifiers is useless. Row level security is named and then
explained in the same breath.

**Honesty check.** Eight claims, eight fact-check rows. One of them, the
launch-audit retention figure in B04, is marked **SEE NOTE**: a later audit of the
codebase found the privacy policy states 12 months against the schema's 1 hour,
and the purge job is not actually scheduled. The note is recorded rather than the
claim quietly dropped, because the claim is on camera.

**Weakest beat.** B06. It asks the viewer to hold two counts, the reason they
differ, and the arithmetic, inside twenty seconds. The frame carries it because
both numerals and both captions stay up while the narration finishes, but it is
the beat most likely to need a rewatch.

**Gate status.** Narration is the operator's own script text, written and reviewed
before the build. Kokoro synthesis is free, so audio was generated with
`--no-gate`. This file is not self-signed.

VERDICT: PENDING — human signature required
