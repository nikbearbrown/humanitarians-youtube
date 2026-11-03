# FACTCHECK — Automating the YouTube Review Pipeline

Every on-screen or spoken claim, with its verdict and source. Rule: if a claim
cannot be traced to a document, it is either cut or explicitly hedged on camera.

| # | Beat | Claim | Verdict | Source |
|---|---|---|---|---|
| 1 | B03 | YouTube offers a 4K option based on source resolution; 4K is 3840x2160 | VERIFIED | support.google.com/youtube/answer/16597617 |
| 2 | B04 | Brutalist upscales an undersized clip to fill the frame with no warning on the video path | VERIFIED (code) | `runtime/scripts/compile.py:184` `vf_fit()`; the under-size warning exists only on the STILL branch at `:256` |
| 3 | ~~B05~~ | The render default changed from 1080 to 2160 | **DISPROVEN - BEAT CUT** | GitHub commit `279e925` (22 Jul 2026), the first commit of `brutalist.art`, already reads `HEIGHT=2160`. The `(was 1080)` comment refers to the parent toolkit, before this repo existed. No version of this repo ever shipped 1080. |
| 4 | ~~B05~~ | Fellows on older copies are why failures cluster | **DISPROVEN - BEAT CUT** | Followed from #3, which is false. Beat removed from the reel entirely. |
| 5 | B06 | Brutalist's own docs specify this check but no code implements it | VERIFIED (code) | `docs/PUBLISHING.md` specifies `all_beats_4k`; `RENDER-4K-AND-UPLOAD.md:46` documents GATE T blocking `./art final`. No `type_check.py` exists in the repo; no `GATE` string in `compile.py`. |
| 6 | B07 | Shipping the wrong channel handle has happened before | VERIFIED (code) | `OUTRO-LOCK.md:14` - "This is the bug that shipped @Musinique." |
| 7 | B07 | A fellows/HAI reel must not use the @NikBearBrown outro | VERIFIED (code) | `skills/make/fellows/SKILL.md:132` |
| 8 | B09 | A video uploaded via an unapproved API project is locked private, permanently | VERIFIED | developers.google.com/youtube/v3/guides/quota_and_compliance_audits - applies to projects created after 28 July 2020; earlier projects exempt |
| 9 | B09 | Invited channel managers cannot manage via YouTube APIs | VERIFIED | support.google.com/youtube/answer/9481328 |
| 10 | B09 | Service accounts are not supported; returns NoLinkedYouTubeAccount | VERIFIED | developers.google.com/youtube/v3/guides/authentication |

## The beat that was cut

**B05 (version drift) was removed after checking the commit history.** The claim survived
two rounds of hedging before a commit check killed it outright. The lesson worth keeping:
a hedge is not a substitute for a source. Checking `git log` took one minute and would
have prevented the beat being written at all.

An accurate replacement existed - Nik committed `RENDER-4K-AND-UPLOAD.md` on 27 Jul 2026,
five days after the toolkit landed, so a fellow on a copy from that window has a working
toolkit and no guide. It was rejected deliberately: it still puts an individual's process
on screen, which is not what this reel is for.

## Claims CUT after fact-checking

| Claim | Why cut |
|---|---|
| "Roughly six uploads a day" is a constraint | **FALSE.** Came from Brutalist's own `docs/PUBLISHING.md` (10,000 units / ~1,600 per upload), which is out of date. `videos.insert` now costs 1 unit against a dedicated allowance of **100 calls per day**. At this volume it is not a constraint at all. Sources: developers.google.com/youtube/v3/determine_quota_cost and .../guides/quota_and_compliance_audits |
| "The script has to be authorised as a manager" | **FALSE.** Delegation is impossible - see claims 9 and 10. Reframed: the channel owner authorises personally, once, and the credential never comes near me. |
| "Liam in for Bear is a branding mistake volunteers forget to fix" | **FALSE.** It is required behaviour under the IN-FOR-BEAR LAW (`HOW-TO.md:74`). Flagging it would flag correct work. Replaced with the wrong-channel-outro check (claims 6 and 7). |

## Sources

- https://developers.google.com/youtube/v3/guides/quota_and_compliance_audits
- https://developers.google.com/youtube/v3/determine_quota_cost
- https://developers.google.com/youtube/v3/guides/authentication
- https://support.google.com/youtube/answer/9481328
- https://support.google.com/youtube/answer/16597617

## Standing rule for this reel

The audience includes professors who may know the YouTube API better than the
author. One wrong number ends the pitch. Nothing goes on camera that is not in
the table above, and claim 4 is the only unproven one - deliberately worded so
that being wrong costs nothing.
