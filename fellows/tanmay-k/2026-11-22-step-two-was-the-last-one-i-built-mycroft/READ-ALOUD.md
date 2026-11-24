# READ-ALOUD — Step Two Was the Last One I Built (work video, long film, 16:9), signed 2026-11-23

Narration only, in spoken order, numbers in words; each beat's tone follows its title and is not voiced. **Signed at Gate P, 2026-11-23.** Every figure comes from our own runs of our own recipe's scripts (`FACTCHECK.md`); the wrong file is a deliberate test on a scratch copy, and B04 says that out loud.

TTS notes: Mycroft is voiced "My-croft", the name "Cool-car-knee", NVDA as letters, JSON as "jay-son". Phonemes checked with Kokoro: jay-son, N-V-D-A, hash, manifest, stand-in and the long numbers read cleanly; plain "Mycroft" is voiced wrong, so the audio script must use "My-croft".

**B00 · THE LAST ONE** (~17 s) — curious

Step two was the last step I built. The recipe has six steps. I built step one, then three, then five, and only weeks later four and six. Step two, the one that runs second, was written last of all. So what were the other steps doing while it was missing?

**B01 · THE TWO SENTENCES** (~34 s) — plain

Tanmay Kulkarni, for Humanitarians AI. In Mycroft, a public repository, a recipe is a list of steps with a script behind each one. Mine fetches prices for five stocks and adds them up. In the recipe I wrote that step three reads the price files directly, since step two is still open. And that step five reads step three's output, since step four is still open. Those are my sentences, and when I wrote them they were true. Each is a stand-in: a shortcut for a step that did not exist yet. So I will put one check to each. What did it stand in for? What did it skip? And what happens when it and the real step get the same wrong input?

**B02 · THE REAL STEP** (~30 s) — plain

This week the real step two was merged. It reads the run settings and the workflow, then each price file, and checks every file against the hash recorded in a manifest when the sample files were made. It keeps each file exactly as it came. A file goes to a reject list if the manifest does not list it, if its hash has changed, if it is missing, or if it is not valid jay-son. It does not judge whether a price makes sense. That stays with steps three and four.

**B03 · WHAT THE STAND-IN GOT RIGHT** (~20 s) — warm

First, the good news. I ran the stand-in and the real step on the same six sets of sample files, and they saw the same files every time. In the clean set, five files and five records. In the set of deliberately defective files, step two took in four and turned one away, while step three looked at the same five and rejected all of them, for its own reasons. Six sets out of six: the shortcut was right about which files were there.

**B04 · ONE WRONG FILE** (~22 s) — curious

Then I gave both a wrong file, deliberately, on a scratch copy that never went near the repository. In the N-V-D-A price file I switched two digits around. Five hundred four point five six two five became five hundred forty point five six two five. It is still a number. It is still valid jay-son. It is the kind of slip a person makes at a keyboard.

**B05 · THE OLD ROUTE** (~36 s) — surprised

Here is what the old route did. Step one checks the files against the manifest, and it stopped. Its message says: fixture changed since the manifest froze it. But step three, run on the same folder, said pass: five promoted, none rejected. And step five priced the portfolio at sixty-six thousand eight hundred ninety-eight dollars and thirteen cents. The committed run says sixty-five thousand ninety-eight dollars and thirteen cents. That is eighteen hundred dollars more, from two switched digits, and a return of twenty-four point three five percent instead of twenty-one.

**B06 · WHERE THE STOP LIVED** (~27 s) — careful

I want to be careful here. Step one did stop. What step three, on its own, has no way to know is that it did. Each step is a separate command, and the stop was only a message in a file until someone read it. The stand-in never had to ask the question, because I had put the question somewhere else. Nobody was wrong. It was my sentence, since step two is still open, doing exactly what it said.

**B07 · THE NEW DOOR** (~20 s) — measured

Now the same folder, through the real step two. Four files taken in. One turned away, N-V-D-A, with its reason written beside it: it differs from the hash recorded in the manifest. The same wrong file, through a different door, and this time it is stopped by the step whose job is to ask. Wiring step three to read what step two kept is the next change. I have not made it.

**B08 · TWO QUESTIONS** (~22 s) — plain

So what did the stand-in skip? Two questions. Is this file one that was ever recorded? And is it the same file that was recorded? Step three asked whether a file parsed, named one of my five tickers, and had a price. It never asked whether it was the very file I had recorded. A hash can only say a file is unchanged. It cannot say the file is right. But unchanged was exactly what was missing.

**B09 · THE ONE STILL STANDING** (~21 s) — honest

There is a second stand-in, and I have not paid it back. Step five still reads step three's output, and the recipe still says, since step four is still open, even though step four now exists. I have not compared the two yet, so I will not say anything about it here, except that I have it written down.

**B10 · WHAT YOURS SKIPPED** (~25 s) — clear

If you build out of order, you have stand-ins too. Search your own notes for the words since and until. For each one, write down what it replaced and what it skipped. Then, when the real step arrives, hand the stand-in and the real step one deliberately wrong input, and read where they disagree. That one wrong file told me more than six clean sets.

**B11 · WHAT I DID NOT CHECK** (~24 s) — careful

Here is what I did not check. This was sample mode, with invented prices: one swapped pair, in one file, in one recipe. Step one does catch it when it is run and read; my claim is only about step three on its own. No live call was made. The wrong file was a scratch copy, so none of it is in the repository, and the recipe's own text is unedited, so it still says step two is open.

**B12 · THE LOAN** (~12 s) — warm

Step two was the last one I built. It was the one the others were standing in for. A stand-in is a loan, and this was the week I started paying it back.
