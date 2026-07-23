# PEDAGOGY AUDIT — vox-channel-reset

## Act structure check

| Required act | Present | Beat(s) |
|---|---|---|
| COLD OPEN (concrete case, no thesis) | YES | B01–B02 |
| THE QUESTION (on screen AND narration) | YES | B03 |
| THE PROBLEM | YES | B04–B05 |
| THE MECHANISM | YES | B06–B08 |
| THE IMPLICATION | YES | B09–B11 |
| THE EXAMPLE (16:9 full cut, right before RECAP) | YES | B12 |
| RECAP endcard (question→answer + topic) | YES | B13 |

## Question on screen check
B03 card copy: "The agent caught the impersonator in channel 1. Why did it believe them in channel 2?"
B03 narration: "If the agent correctly caught an impersonator in one channel — what makes the same impersonator trusted in the next?"
Both on screen (card) and in narration. ✓

## Topic check
B01 scene: "COMPUTATIONAL SKEPTICISM" eyebrow (TEAL text, DISPLAY font) ✓
B13 endcard card.topic: "COMPUTATIONAL SKEPTICISM" — no book title, no chapter number on screen ✓
B13 narration: no book title or chapter number ✓

## Concrete case before thesis
B02 introduces the specific Discord display-name attack scenario (caught in public channel, succeeded in private) before explaining session-boundary mechanics. ✓

## Exclusions honored
- No cryptographic-credential redesign ✓
- No post-compromise file-wiping aftermath (Case #8 aftermath) ✓
- No generalization to prompt injection ✓
- No failure taxonomy ✓

## THE EXAMPLE act check
B12 presents a support ticket scenario: ticket #47 correctly flagged (email mismatch), attacker submits ticket #48 with fresh session, no history carried over — export runs. All details are illustrative and labeled in FACTCHECK.md. The example walks the channel-boundary reset mechanism end-to-end. ✓

## Length check
Estimated total: ~210s ≈ 3:30. Within 5:00 cap. ✓

## Vocabulary law
"Session context" and "trust context" each introduced after the viewer has seen the mechanism fail (new channel, same attacker, trusted). ✓

## Utility-framing lint
No "is critical for" / "important to understand" / "we'll cover" / "in this video" in opening acts. ✓

VERDICT: PASS
