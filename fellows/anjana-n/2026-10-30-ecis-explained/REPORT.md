# Video Report: ECIS Episode 13 

**Type:** Weekly Implementation Video
**Project:** [Mycroft — ECIS + Decision Scorecard](https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis)
**Week:** Week 18 (Phase 18), October 25 – 31, 2026

---

## Summary

This episode covers the Week 18 progress on ECIS. The theme is the system learning when to be careful with its own predictions. It now:
- checks that its confidence scores are accurate
- notices when one earnings call sends mixed signals
- explains every prediction in plain English
- recognizes when a call looks unfamiliar



## What the Episode Covers

1. **Opening:** a confidence score is only useful if it is accurate.
2. **Recap:** a short overview of what the system already does.
3. **Accurate confidence:** when the system says it is 80% sure, it should be right about 80% of the time. Two standard methods are used to adjust the scores, and both are tested on data the system has not seen.
4. **Mixed signals:** the system looks for three patterns where one call's signals disagree, and rates how strong each disagreement is.
5. **Plain-English explanations:** each prediction shows which factors pushed it up or down, written as a sentence.
6. **Unfamiliar calls:** when a call looks very different from what the system learned from, its confidence is lowered. The more unusual the call, the bigger the reduction.
7. **Closing summary,** key takeaways, and a prompt for viewers to try.

## Main Ideas

- **A confidence score should mean what it says.**
- **Mixed signals are useful information, not just noise.** They can point to real uncertainty or a mixed outlook.
- **Every prediction now comes with a reason.**
- **The system knows its limits.** It is more careful with calls that are unlike anything it has seen.



## Links

- **Video:**
  - GitHub: https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-10-30-ecis-explained
  - Drive: https://drive.google.com/drive/folders/1klBky8EUmX9enNkT9Oogro15lO03a5n_
- **Week 18 work folder:** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-10-30-weekly-work-progress
## Status

Complete