Same Logic, Two Languages: How I Checked My Python Rewrite Against the Original

Here's one number: 0.625. Ask JavaScript to round it to two places and you get 0.63. Ask Python the
everyday way and you get 0.62. I'd just rewritten the core of a finance detector from one of those
languages into the other, for a recipe in Mycroft, so the question I couldn't put down was this: if my
version had quietly done that somewhere, would I have noticed?

This video is how I checked, in three matches. My own reading of the original against the original
(the answers written down before any code). My Python against the original JavaScript, run side by side
on sixteen invented companies (16 out of 16 agreed, and that told me almost nothing). And two of my own
files describing the same run. The useful part was finding where two versions could quietly disagree,
including two places my own test data never reached, and putting a test exactly there.

Chapters:
0:00 One number, two answers
0:22 What this is
0:50 The detector, in one breath
1:12 Match one: the answers before the code
1:34 Match two: the first comparison
1:58 Where the two languages differ
2:20 Where my test data never stood
2:43 Standing on the line
3:05 Match three: two files that were both mine
3:35 Where I stopped
3:54 Leaving it as I found it
4:10 One question
4:24 Sign-off

Your turn: if you've rewritten something you depend on (a new language, a new tool, or just a cleaner
version), where would your two versions most likely disagree? Find that one spot, and make sure a single
test is standing exactly on it.

The recipe (Mycroft):
https://github.com/nikbearbrown/mycroft/blob/main/recipes/contradiction-detection-agent.md

Sources, in order of appearance:

- Mycroft README ("both a book and a working agentic repository")
  https://github.com/nikbearbrown/mycroft
- Mycroft SNICKERDOODLE.md, principle P6 ("no artifact silently wins")
  https://github.com/nikbearbrown/mycroft/blob/main/SNICKERDOODLE.md
- JavaScript vs Python on 0.625, 1.0 and `[] || "x"`: live runs in Node and Python (2026-10-04)

What this video claims, and what it does not:

- The Python port, the sample corpus, the comparison against the original JavaScript and the checks shown
  are my contribution to this recipe. The original workflow is credited as "the original workflow"; this
  video doesn't review or judge it.
- Every company on screen is invented ("… Fixture Co"). No real company is judged.
- 16/16 means my port and the original JavaScript produced the same flags, word for word, on those sixteen
  sample companies. It is not a claim that the patterns are good investment signals.
- The "changed on purpose" runs (0.6 → 0.61, Python's rounding) were scratch runs on a copy, labelled on
  screen, not the shipped code.
- Everything ran on invented data: no database, no news feed and no AI model was ever called. Live mode
  was declined on the record; that decision belongs to the people with live access.

Narration is a synthetic voice (Kokoro, run locally). Visuals are original code-drawn animations of real
code and real results; no third-party images, and open-licence fonts only.

Humanitarians AI — @HumanitariansAI
Tanmay Kulkarni, in for Humanitarians AI

Tags: software testing, code migration, JavaScript, Python, porting code, parity testing, test data,
edge cases, floating point rounding, Mycroft, Humanitarians AI
