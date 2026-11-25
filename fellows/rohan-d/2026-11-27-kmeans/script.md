# K-Means, One Reassignment at a Time — script (final, as shot)

Channel claude-liam · Persona Liam (in for Bear) · Register Teardown · Voice Kokoro `am_onyx` (AI narration)
16:9 long cut: 2:59 (179.1s) · 9:16 cut: same length

Timestamps come from the measured audio and are approximate. This is what is spoken in the final render; on-screen props live in `beat_sheet.json`.

Opening line required by the weekly guide (not yet spoken in this video): "Hi, I am Rohan, and this video is about machine learning."

## 16:9 — long cut

### B00 · ask (0:00–0:14)
> Hi, this is Liam, in for Bear. The ask: how does k-means find groups in data that has no labels? Show me with real numbers. Guess two centers. Give every point to its nearest center. Move each center to the mean of its points. Repeat until nothing moves.

### B01 · overview (0:14–0:25)
> K-means settles on a stable guess. It doesn't discover the true groups. It finds a grouping that stops changing, and where it stops depends on where it started. Same data, different start, different answer.

### B02 · the start (0:25–0:35)
> Seven points on a plane. We want two groups. Pick two starting centers: one, one, and five, six. Nothing about the data told us where to start. Any two spots would do.

### B03 · assign (0:35–0:46)
> Assign. Take the point three, four. Distance to the first center: three point six. To the second: two point eight. It joins the second. Do that for every point: two go to the first center, five to the second.

### B04 · update (0:46–0:59)
> Update. Move each center to the mean of its points. The first group, one, one and one point five, two, has its mean at one point two five, one point five. The second group's five points have their mean at three point nine, five point one.

### B05 · repeat (0:59–1:06)
> Repeat. Assign again from the new centers. Every point stays where it was. Nothing moves, so we're done. Two rounds.

### B06 · inertia (1:06–1:19)
> Is it getting better? Add up the squared distances from each point to its center. That's the inertia. At the starting centers, nineteen point two five. After one update, eight point five three. And it can't go up. Each step lowers it or leaves it alone.

### B07 · where it bites (1:19–1:36)
> Where it bites. Four points at the corners of a rectangle, four wide and two tall. Start the centers on the middles of the short sides: they split left from right, inertia four. Start them on the middles of the long sides: top from bottom, inertia sixteen. Both are stable. So run it from several starts, and keep the lowest inertia.

### BVDT · verdict (1:36–2:05)
> Let's recap with Claude. K-means guesses centers, assigns each point to the nearest one, moves each center to the mean, and repeats. The point three, four is three point six from one center and two point eight from the other. Starting from one, one and five, six, it settles in two rounds at one point two five, one point five and three point nine, five point one. Inertia falls from nineteen point two five to eight point five three, and never rises. A different start can settle on a worse split, so run it several times.

### BHTF · your turn (2:05–2:54)
> Your turn. Paste this into Claude: Write a short Python script, no ML libraries, that runs k-means with k = 2 on the points (1,1), (1.5,2), (3,4), (5,7), (3.5,5), (4.5,5) and (3.5,4.5), starting the centers at (1,1) and (5,6). Print the labels, the centers and the inertia after each round, and stop when nothing changes. Then run it on the rectangle corners (0,0), (0,2), (4,0) and (4,2) from the starts (0,1),(4,1) and (2,0),(2,2), and print each final inertia. Here's what to check. The first run should end at one point two five, one point five and three point nine, five point one, with inertia eight point five three. The rectangle should give inertia four from one start and sixteen from the other. And see whether Claude explains why both answers are stable.

### BOUT · outro (2:54–2:59)
> K-Means, One Reassignment at a Time. At Nik Bear Brown.
