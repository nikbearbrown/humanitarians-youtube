# FRICTIONAL.md — Week 5: Banking Domain Interview, Part 1

**Date:** 2026-08-31
*(Written retrospectively on 2026-10-17.)*

**What I worked on:** Rebuilt "Interview End-to-End" (banking) after PM review flagged low bitrate, a broken 9:16 fill, and the wrong production format.

**What I tried, and what I expected:** Expected a patch, not a full rebuild.

**Where it resisted:** PM wanted a different format entirely (cli-explainer, Claude-branded). The 9:16 had a real bug: the portrait resolution flag didn't actually reconfigure Manim's coordinate system, so content rendered landscape-sized inside a small corner -- and passed the automated check anyway.

**What Claude contributed:** Diagnosed the portrait bug with a direct test rather than trusting the automated check. I approved the full rebuild and made the call on the outro branding fix.

**What I understand now, and what I still don't:** An automated check can pass while the real render is still wrong -- looking at actual frames matters. Still learning how the toolkit's various video skills differ.
