# PEDAGOGY — "How Apps Find a Song's Tempo"

How the reel is built to teach someone who has seen a BPM number but never been told how it is found.

## The register

The standing corrections still apply: *no assumed knowledge* and *the viewer has to learn something*.
So the reel starts from a foot tapping (a beat every half second), shows each step on one real groove
before any statistics, uses one idea of maths (a shift and a division), and ends on what to do when a
number looks wrong.

## The shape

| Beat | Job | What the viewer can do after it |
|---|---|---|
| B00 ASK | the question: how does an app hear the beat? | name the answer's shape: hits, a repeat, a choice |
| B01 BACKGROUND | what BPM means, on a real groove they hear | turn a BPM into seconds between beats |
| B02 MECHANISM | the onset curve: where new sounds start | say what the app actually listens for |
| B03 MATH | autocorrelation: slide, match, divide | turn a repeat into a tempo, and see two candidates |
| B04 MEASURED | my detector on 40 grooves; the preference near 120 | explain why a preference is needed at all |
| B05 THE CATCH | the preference cuts both ways: double and half | recognise an octave error when they see one |
| B06 DRIFT | a live drummer; a grid vs a tracker | know why one number isn't enough for live music |
| B07 WHAT TO DO | tap, halve or double, check the grid | fix a wrong BPM in their own tools |
| B08 OUTRO | sign-off | — |

## Choices worth defending

- **Synthetic Western grooves.** Every number is reproducible, no recordings enter a public repo, and the
  true tempo of every groove is known exactly, which a scraped dataset would not give.
- **Showing the failures.** Seventeen of forty exactly right is not a flattering number. It is the honest
  one, and it is the lesson: the method finds real repeats; choosing among them is where it fails.
- **A cross-check, not just my code.** librosa on the same grooves agrees on 34 of 40, so the
  behaviour is the method's, not a bug of mine.
