# GATE P — Encrypted Twice

**The one idea.** Storage encryption defends a disk. It cannot defend a secret
from a query the database is required to answer, which is why the value is
encrypted again above it, with a key the database does not hold.

| Beat | The viewer should be able to say afterwards |
|---|---|
| B00 | this is about a secret encrypted twice |
| B01 | the hub stores a signing key and a shared secret in a column |
| B02 | the database already encrypts storage, so the second layer needs justifying |
| B03 | storage encryption answers the stolen-disk threat and nothing above it |
| B04 | what lands in the column is version, IV, auth tag and ciphertext |
| B05 | GCM signs as well as hides, so tampering fails instead of returning garbage |
| B06 | old rows without the marker still read in clear, and that is temporary |
| B07 | two layers because there are two different threats |

**Register check.** Second person, plain English. IV, auth tag and authenticated
encryption are each named and then explained in the same breath. The format is
shown rather than described.

**Honesty check.** Eight claims, eight fact-check rows. Two carry explicit
qualifications. Row 2 is marked **VENDOR CLAIM** because the storage-layer
encryption is Supabase's statement and we did not measure it, and the narration
says "Supabase applies" rather than "we verified". Row 7 is a transitional
weakness that B06 states on camera rather than leaving out: a row written before
the encryption shipped still reads in clear.

**Weakest beat.** B04. Four fields named in one breath is the densest moment, and
a viewer who does not already know what an initialisation vector is will take the
label on trust. The accumulating labels hold it, but it is the beat most likely to
need a rewatch.

**Gate status.** Narration is the operator's own script text. Kokoro synthesis is
free, so audio was generated with `--no-gate`. This file is not self-signed.

VERDICT: PENDING — human signature required
