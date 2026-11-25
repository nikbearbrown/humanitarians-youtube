# SCRIPT — Both Sides Passed

Narration as delivered. Kokoro `am_onyx`; measured durations are the master clock.

**Total 2:19.9** across 8 beats. Master 16:9 3840x2160.

---

### B00 — ASK  ·  18.20s

*ClaudeComposerAsk*

> Selam. This is Jainil. Two services. The one that produces the data validates what it sends. The one that consumes it validates what it receives. Both sets of tests are green, both have been green all week, and the numbers downstream are still wrong. This is not a rare situation and it is not anybody being careless. It is a gap in where the checks are placed.

### B01 — BLUF  ·  14.04s

*BrutalistHesitantWriter*

> Here is the whole idea in one breath. A record can be perfectly valid on the way out and perfectly valid on the way in, and still mean something different at each end. Validation inside a stage cannot see that. Only a check between the stages can.

### B02 — SETUP  ·  18.77s

*StageRail*

> Here is the shape of it. The producer emits five thousand payment events and checks its own output: every field present, every type right, every timestamp positive. The consumer receives them and runs the same kind of check on its input. Both pass. And in between those two boxes there is a place where nobody has put anything at all, because it belongs to neither team.

### B03 — EVIDENCE  ·  27.49s

*ClaudeBarChart*

> So I took a clean batch and broke it seven ways — all ordinary integration failures. Timestamps in seconds instead of milliseconds. Amounts in cents instead of dollars. A new status value nobody announced. Nulls written as minus one. A timezone shift. Amounts arriving as strings. Late rows duplicating an id. Each stage's own checks caught exactly one of the seven: the string, because that is the only one that changes a type. A contract at the boundary caught six.

### B04 — LAND  ·  22.74s

*CardSet*

> The seventh is the interesting one. A timezone shift of five and a half hours. Against an epoch timestamp in milliseconds that is a change of about one thousandth of one percent — far inside any range check you would write. So the boundary contract waved it through. But the events have a daily rhythm, quiet overnight and busy in the afternoon, and shifting everything by five hours moves that shape a long way. Profile the distribution instead of the median, and it is obvious.

### B05 — SOURCE  ·  18.28s

*FormACard*

> This is not a niche concern. Google built a production system for exactly this problem and described it in twenty nineteen: validation that sits in the pipeline and checks each batch of data, rather than tests that sit inside one service. It runs inside their machine learning platform across a very large amount of production data.

### B06 — HANDOFF  ·  17.00s

*ClaudeComposerAsk*

> Your turn. Point this at a handoff you actually own: here are two services that exchange data — help me write down the contract between them as a set of checks on a batch, not on a row, including the ranges, the allowed values, the key uniqueness and the shape of the distribution. The last of those is the one most people leave out.

### B07 — OUTRO  ·  3.41s

*HaiTitleOutro*

> Both sides passed. This is Jainil. Subscribe.
