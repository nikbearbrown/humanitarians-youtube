# CARRY-OUT.md (GATE C)

**Carry-out sentence (BCRY):**
> Coding a diagnosis and making the diagnosis are two different jobs —
> icd10-cm-skill only does the first one.

**Wrong guess it defeats:** a newcomer reading "extract billable ICD-10-CM diagnosis
codes from a clinical note" assumes the skill is deciding what's wrong with the patient
— diagnosing, not just coding. It isn't. `icd10-cm-skill`'s whole job stops at
translating a diagnosis the clinician already wrote down into the matching billing
code, the way a professional coder builds a claim. Deciding the diagnosis itself is
clinical judgment, and that's the clinician's job, not this skill's.

**Test:** "coding a diagnosis and making the diagnosis are two different jobs" survives
being repeated by someone who wasn't paying full attention, and stays true — it
compresses the actual distinction (translating documented facts into codes vs.
clinical judgment), not the topic ("this video is about a medical coding skill").
