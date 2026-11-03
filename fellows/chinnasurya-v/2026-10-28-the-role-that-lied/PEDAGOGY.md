# GATE P — The Role That Lied

**The one idea.** The meaning of a role URN lives in its final segment, so
"does this string contain Instructor" and "is this role Instructor" are two
different questions that happen to agree most of the time.

| Beat | The viewer should be able to say afterwards |
|---|---|
| B00 | this is about how a tool decides who is a teacher |
| B01 | the roles claim is a list of URN identifiers, and it has to become one decision |
| B02 | the tempting fix is a one-line substring check |
| B03 | strings that are not instructor roles still contain the word |
| B04 | the identifier is the last segment; everything before it is namespace |
| B05 | split, take the last segment, lowercase, look it up, default to student |
| B06 | the escalation strings are now test cases, so the shortcut cannot come back |
| B07 | substring and allow-list are different checks, not cheap and expensive versions of one |

**Register check.** Second person, plain English. URN, namespace and allow list
are each named and explained in the same sentence. The code line in B02 is shown
rather than described.

**Honesty check.** Six claims, six fact-check rows. The threat model is stated
precisely in the fact-check rather than implied on camera: the token is
platform-signed, so this is about misreading legitimate input, not about forging
a token. The reel does not claim an exploit was observed. The change and its tests
are both shipped, so nothing on camera describes a live unfixed weakness.

**Weakest beat.** B04. Asking a viewer to parse a long URN and locate its final
segment is the one moment the reel depends on reading rather than listening. The
boxed segment in signal carries it, but a viewer not watching closely will miss
why the namespace is dimmed.

**Gate status.** Narration is the operator's own script text. Kokoro synthesis is
free, so audio was generated with `--no-gate`. This file is not self-signed.

VERDICT: PENDING — human signature required
