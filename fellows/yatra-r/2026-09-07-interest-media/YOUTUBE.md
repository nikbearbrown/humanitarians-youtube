# YouTube metadata — "Interest Media."

Not published by the toolkit. Copy-paste when you decide to upload.

## Title

```
Interest Media. — Why Your Feed Stopped Caring Who You Follow
```

Alternates:
- `Interest Media. — Social Media Changed Its Sort Key`
- `You Don't Need Followers First Anymore — Gary Vee's "Interest Media," Explained`

## Description

```
Social media stopped running on who you know. It runs on what you're interested
in — and that changes what a post has to do to travel.

The framing is Gary Vaynerchuk's: social media as we knew it is basically dead.
Not gone, transformed. What we're in now is closer to interest media. Social
media asks who do you know. Interest media asks what do you care about.

Test it on your own feed. When did it last show you your cousin, or your old
college roommate? You're seeing strangers instead — because the algorithm
noticed what you watched, what you paused on, what you searched for. That didn't
happen by accident: there's simply too much posted every single day for your
network of friends and family to surface the best of it. The network stopped
being able to sort.

Here's why that matters if you make anything. In the old model you needed
thousands of followers before anyone saw your work — followers were the gate.
Now a single well-made post can reach people who've never heard of your brand,
because it matches what they already care about. So the real question changed
too. It isn't how do I get more followers. It's how do I make something that
earns attention on its own, one post at a time.

One thing this video is careful about: it doesn't claim followers are worthless,
it doesn't claim every feed works the same way, and it cites no statistics —
because none were verified for it. Gary Vaynerchuk is credited for the framing
and paraphrased throughout, never quoted. Test it on your own feed before you
believe it.

CHAPTERS
0:00  The ask
0:13  The whole idea in one breath
0:23  Where this comes from, and the rename
0:39  Your own feed
0:54  Why the old sort key gave out
1:04  Same machine, different key
1:11  Asking for both models
1:16  The gate, and what replaced it
1:30  The question a marketer is answering
1:39  What this isn't
1:52  The verdict
2:10  Your turn
2:24  Outro

THE PROMPT FROM THIS VIDEO
Look at the last twenty things my feed showed me. How many came from accounts I
actually follow, and what interest was each of the others matching? Then tell me
which interest of mine the feed is most confident about.

Grade the answer on three things: can it name the interest, not just the
account; does it separate follows from matches; and does it say what it can't
know from a feed alone?

CREDIT
The "interest media" framing is Gary Vaynerchuk's. This video paraphrases it
throughout and does not quote him.

Built with Claude. Narration is Kokoro (local, free). Every graphic is
rendered, not screenshotted — and there is not one statistic in this video,
on screen or spoken, because none was verified for it.

@Yatra
```

> **Chapter timings are computed from the measured beat durations in
> `beat_sheet.json`** (cumulative starts including B10's 0.5s lead silence,
> floored to the second). If any narration is re-recorded, recompute — do not
> hand-edit.

## Tags

```
interest media, Gary Vaynerchuk, Gary Vee, social media algorithm, algorithmic
feed, content strategy, social media marketing, organic reach, follower count,
creator economy, Humanitarians AI, AI explainer, Claude, marketing strategy
```

## Playlist

`Humanitarians AI`

## Thumbnail note

Two candidates from the QC frames:

- **B02** — `SOCIAL media` struck through beside `INTEREST media` in terracotta.
  This is the whole video in one image and reads at small sizes. Strongest option.
- **B07** — the two tracks, with the post stopped dead at the gate on one and
  passing through the match on the other. Better for the marketing audience,
  slightly busier as a thumbnail.

Pull either from `_qc/frames/` after the QC pass rather than re-rendering.

## Vertical cut

`short/yatra-interest-media-short.mp4` — **2160×3840**, the complete video
(2:33.6 including the endcard, inside the 3:00 cap, no beats dropped). For
Instagram and LinkedIn.

The portrait cut is genuinely re-banded, not cropped: the rename stacks, the
sorter machine runs top-to-bottom, each reach model becomes a vertical chain,
and the two-column ledger stacks into two groups.

**Two manual steps when generating it** — both were needed here, both are
written up in `QC-LOG.md`:

1. **Pass `--handle "@Yatra"` to `shorts.py`.** Its default is `@nikbearbrown`
   and it never reads the reel's own `channel_handle`, so the endcard will
   otherwise carry the wrong channel.
2. **Regenerate the endcard PNG at 2160×3840.** `shorts.py` hardcodes it at
   1080×1920, so compiling at `--height 3840` upscales it — compile.py warns
   about this itself. Every other beat is a native 4K render, so the endcard
   would be the only soft moment in the cut.

## Series note

This one sits apart from the rest of the channel: the other episodes are weekly
work recaps or statistics-led explainers, and this is a concept explainer with
no data in it whatsoever. It is also the first episode narrated by a stand-in
voice ("Bella, in for Yatra"), which is worth a line in the caption so the
change doesn't read as an error.
