# SOURCES — The Role That Lied

## Narration provenance

All narration is the operator's own script text (`script.md`), written before the
build. Kokoro synthesised it verbatim.

## On-camera claims

Six rows in `FACTCHECK.md`, all traced to source files:

| Source | Used for |
|---|---|
| `lib/lti-v1-oauth.ts` | `parseLTIRole`, the split-and-lookup fix, the student default |
| `lib/lti-auth-bridge.ts` | `determineUserRole`, the admin and instructor allow-list sets |
| `tests/lti-roles.test.ts` | The three escalation strings and their asserted results |
| LTI 1.3 specification (IMS Global) | What a role URN is and where its identifier sits |

## Invented values

**None.** `LearnerInstructorFake`, `urn:lti:role:ims/lis/Learner#PseudoInstructor`
and `NotAnInstructorReally` are literal test inputs. The URN shown in B01 and B04
is the standard IMS membership vocabulary URN.

## Deliberately excluded

No hostname, no key material, no individual named, no institution's review
process, and no claim about the production environment. No live unfixed weakness
is described.
