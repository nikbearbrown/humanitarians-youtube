# Frictional log — Will AI Replace My Test Scripts?

Counts toward Week 2.

## Topic and research

- **Tried:** a topic from my own work. I write Selenium and JUnit test scripts, so I wanted to know whether AI testing agents will replace them.
- **Resisted:** I was new to AI in testing. Self-healing locators and vision-based testing agents were new ideas to me, and I wasn't sure how an agent "checks" a page the way I do.
- **Did next:** read the Selenium and JUnit docs, Healenium's docs and an AI testing resource list, and worked it out with my own example: to close a popup, I look for the X, Selenium looks for an ID, and an agent looks at a screenshot.
- **Learned:** self-healing tools pick the best matching element and report it, so a person can fix the script; vision-based agents loop through look, decide, act and check. I'm still new to this and exploring it.

## Script and fact check

- **Tried:** a 14-beat story starting from a real pain point: a test that kept failing because a button's ID changed overnight.
- **Resisted:** beats 1 and 2 both said I write test scripts for a living. The fact check also showed beat 7's Healenium description didn't match Healenium's own docs, and beat 11 had a claim with no source.
- **Did next:** removed the repeated line, rewrote beat 7 from Healenium's docs, found a source for beat 11, and marked beat 10 as my own experience.
- **Learned:** my own experience is valid evidence, but it has to be labelled as mine, not presented as a general fact.

## Audio and build

- **Resisted:** beats 2, 8, 9 and 10 looked clumsy in the vertical cut because they were squeezed landscape layouts. Remotion renders froze again. Claude Code offered to skip Gate T or edit a generated report to fit my no-dates rule. After one fix, a "Gate T pass" was read from old frames while the scene file was actually broken.
- **Did next:** the four beats were redesigned for portrait, one idea at a time with bigger text, and I approved each preview with audio. Every Remotion render ran through a wrapper with a timeout. I kept every gate on and left the pipeline's own reports as they are. The broken scene was fixed and the gates re-run.
- **Learned:** a vertical cut needs its own layout, not a shrunk landscape one. A finished command or a printed "pass" isn't proof; the real status is in build-state.json.
