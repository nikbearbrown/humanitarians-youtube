# Video 4: Reading the Claims — Narration Draft

## B00A — Presenter intro
Hi, I'm Aishwarya
from the Mycroft team.
This video covers the harder half of the Claims Agent — not splitting claims apart, but reading what one actually protects.

## B00 — Cold open
Nine independent claims. Word counts from forty-seven to three hundred and three. Not one clean line separating broad from narrow.

## B01 — The real evidence against a shortcut
Method: the cheap approach was tried first — word count, limitation markers, method-versus-system. Real data across nine claims showed neither one predicts scope on its own. A short claim can be narrow by being specific. A long claim can still be broad. This was the real reason to reach for judgment instead of a rule.

## B02 — The first real classification
Running one real independent claim through Claude: broad, offensive, with a reasoning that pointed to the actual claim language — not the word count — and a caveat naming something specific and checkable: whether the dependent claims narrow the broad term used in the independent one.

## B03 — The real refusal
A second real claim, a real refusal. Plant cell cultures, a pharmaceutical compound family — the model correctly flagged the subject matter and declined to classify it. Not a bug. A real, structural limit of using this kind of model call on real, varied patent content.

## B04 — Handling it honestly
The fix wasn't to route around the refusal. It was to catch it, and say so — mark the reading as unclear, name the real reason, and point back to the raw text instead of pretending a scope reading exists when it doesn't.

## B05 — Building the real agent class
The pieces needed one real home: a `ClaimReading` for each claim's structural facts plus, for independent claims, a scope reading; a `PatentClaimsReading` holding the whole set with real counts, not invented ones. The `ClaimsAgent` class itself does one job — split the claims, flag genuine multi-dependencies, and call the classifier only on the independent ones, with an option to skip classification entirely when only the free, structural reading is needed.

## B06 — The real end-to-end test
Run against a real, cached patent — no new BigQuery cost, one real classification call. Structural pass first, zero API cost: seventeen claims, one independent, sixteen dependent, matching the verified count exactly. Full pass with classification: the same real numbers, plus one honest scope reading with its own confidence caveat. No crash, nothing invented.

## B07 — Handoff
Your turn. Take any independent claim, run it through the same classifier, and read the confidence caveat before trusting the label — it's there to tell you exactly where the reading's judgment could be wrong.

## B08 — Outro
Reading the Claims. Built with Claude, for Humanitarians AI.
