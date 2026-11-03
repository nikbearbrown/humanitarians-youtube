# CARRY-OUT.md (GATE C)

**Carry-out sentence (BCRY):**
> Pulling a patient's record out of the system, and making sense of what it means, are
> two different jobs — fhir only does the first one.

**Wrong guess it defeats:** a newcomer hearing "connect Claude to a hospital's FHIR
server" assumes the connection itself means Claude reads and interprets the patient —
diagnoses, summarizes the case, forms a clinical judgment. It doesn't. `fhir`'s whole
job stops at structured retrieval: connect to a FHIR R4 endpoint (Epic, Oracle Health/
Cerner, MEDITECH, athenahealth, or any SMART-on-FHIR system), pull the patient's
clinical data and notes, and extract structured findings. Interpretation is a separate
step, done by a person or another skill *after* the pull, not by this skill.

**Test:** "pulling a record and making sense of it are two different jobs" survives
being repeated by someone who wasn't paying full attention, and stays true — it
compresses the actual distinction (structured retrieval vs. clinical judgment), not the
topic ("this video is about connecting Claude to a hospital system").
