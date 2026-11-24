Step Two Was the Last One I Built: What a Stand-In Skips When the Real Step Arrives

The recipe I contribute to in Mycroft has six steps, and I built them out of order: one, three and five first, four and six later, and step two last of all. While step two was missing, my own recipe said two things: step three reads the price files directly, "since step two is still open", and step five reads step three's output, "since step four is still open". Both were true when I wrote them. Each is a stand-in, a shortcut for a step that did not exist yet. This week the real step two was merged: it reads the run settings and the workflow, checks each price file against a hash recorded when the sample files were made, keeps each file exactly as it came, and turns away a file that is unlisted, changed, missing or not valid JSON. I ran the stand-in and the real step on the same six sets of sample files and they saw the same files every time. Then I gave both one wrong file, deliberately, on a scratch copy: two digits switched in a stock's price, still a number, still valid JSON. Step one stopped. Step three, on its own, passed it. Step five priced the portfolio at 66,898.13 instead of 65,098.13, a return of 24.35% instead of 21%. The real step two turned the file away on a hash mismatch. The stand-in had skipped two questions: was this file ever recorded, and is it the same file that was recorded? The video ends on a check you can run on your own stand-ins.

Chapters:
0:00 The last step I built
0:14 Two sentences in the recipe
0:47 The real step two
1:11 What the stand-in got right
1:33 One wrong file
1:53 The old route
2:22 Where the stop lived
2:42 The new door
3:02 Two questions the stand-in skipped
3:22 The second stand-in, still standing
3:39 What yours skipped
3:56 What I did not check, and the close

The contribution:
nikbearbrown/mycroft pull request #94 (merged 2026-11-23, merge commit fef5caa): step two of the Portfolio Price Fetcher recipe, "ingest declared inputs", in sample mode. It reads the run envelope, the declared workflow and the fixtures; checks each fixture against the SHA-256 frozen in two manifests; keeps each response body unchanged; rejects a file that is unlisted, changed, missing or not JSON; and does not judge whether a price makes sense (that stays with steps three and four). 19 files added, none edited or removed, and a self-test of 28 checks with break tests guards it.
https://github.com/nikbearbrown/mycroft/pull/94
It builds on the steps already merged in earlier pull requests.

What this video claims, and what it does not:

- Everything here is sample mode with invented prices. Nothing is investment advice, and no live call was made.
- The wrong file is a deliberate test on a scratch copy; it was never committed. Step one does stop it, when it is run and read. The claim is only about step three on its own: it passed the file, and step five priced from it.
- Step two and step three saw the same files in all six sample sets. In the set of deliberately defective files, step two took in four and turned one away, while step three looked at the same five and rejected all of them, for its own reasons.
- Step three also checks that a file parses, names one of the five tickers and has a usable price. It does not check that the file is the one that was recorded; a hash can say a file is unchanged, not that it is right.
- Step three still reads the sample folder directly, and the recipe's own text still says step two is open; wiring step three to what step two kept is the next change and is not made. The second stand-in (step five reading step three's output, "since step four is still open") is not paid back, and I have not compared the two, so I say nothing about it.
- This is one swapped pair, in one file, in one recipe. It is not a claim about any other pipeline.

Source: the merged repository (nikbearbrown/mycroft, main at merge commit fef5caa) and our own reruns of its scripts on the sample files. Every figure on screen comes from those reruns.

Narration is a synthetic voice (Kokoro, run locally). Visuals are original code-drawn animations: no third-party images, recordings or music.

Humanitarians AI - @HumanitariansAI
Tanmay Kulkarni, in for Humanitarians AI

Tags: stand-in, shortcut, testing, hashes, SHA-256, data validation, pipelines, open source finance, Mycroft, Python, explainer, Humanitarians AI
