# Overfitting, One Memorized Point at a Time — script (final, as shot)

Channel claude-liam · Persona Liam (in for Bear) · Register Teardown · Voice Kokoro `am_onyx` (AI narration)
16:9 long cut: 2:48 (167.9s) · 9:16 cut: same length

Timestamps come from the measured audio and are approximate. This is what is spoken in the final render; on-screen props live in `beat_sheet.json`.

Opening line required by the weekly guide (not yet spoken in this video): "Hi, I am Rohan, and this video is about machine learning."

## 16:9 — long cut

### B00 · ask (0:00–0:16)
> Hi, this is Liam, in for Bear. The ask: why can a model score perfectly on its training data and still fail on new data? Show me with real numbers. A flexible model can memorize the noise in its examples. So judge it on points it has never seen. A perfect training score can hide a worse model.

### B01 · overview (0:16–0:25)
> A perfect fit means it memorized. Not that the model learned the pattern, but that it learned the noise along with it. That is why a perfect training score proves very little.

### B02 · a straight line (0:25–0:40)
> Eight points, scattered around a rising line. Fit a straight line and it misses every point a little. The training error is point oh nine nine. Now bring fresh points the model has never seen. The test error is point oh seven four. About the same. That is what learning looks like.

### B03 · full freedom (0:40–0:48)
> Now give the model more freedom. A degree seven curve. It bends through every single point. Training error: zero. A perfect score.

### B04 · fresh points (0:48–0:59)
> But look at the fresh points. The curve swings between its memorized dots and misses them. Test error, point two two one. Three times the straight line's. The perfect model is the worse model.

### B05 · every degree (0:59–1:14)
> Try every degree from one to seven. Training error only falls, from point oh nine nine to zero. Test error doesn't. It sits near point oh eight through degree three, then jumps to point one three nine, and climbs to point two two one. The gap between the two lines is the memorizing.

### B06 · more data (1:14–1:28)
> The fix is not always a simpler model. Give the degree seven curve forty points instead of eight. Training error becomes point oh three five. Test error drops from point two two one to point oh six six. More data starves the memorizing.

### B07 · where it bites (1:28–1:42)
> Where it bites. Even a perfect model can't beat the noise in the data. Here, about point oh six two five. Degree one's test error is point oh seven four. Degree seven's is point two two one. A training error of zero sits below that floor. That should worry you, not please you.

### BVDT · verdict (1:42–2:02)
> Let's recap with Claude. Training error always falls as the model gets more flexible. Test error falls, then rises: a line scores point oh seven four, degree seven scores point two two one. A perfect training score can mean memorized noise, and the gap between the two errors is the memorizing. More data shrinks the gap. And noise sets a floor, so a training error below it is a warning.

### BHTF · your turn (2:02–2:42)
> Your turn. Paste this into Claude: Write a short Python script, numpy only, that draws 8 noisy points from y = 2x with noise standard deviation 0.25, fits polynomials of degree 1 to 7, and prints the training error and the test error on 200 fresh points for each degree. Before running it, predict which degree has the lowest test error and why. Then repeat with 40 training points. Here's what to check. Training error should fall to nearly zero by degree seven, while test error ends up several times larger. The lowest test error should sit at a low degree, since the true pattern is a straight line. With forty points, the degree seven test error should come down close to the noise floor. And see whether Claude explains why, rather than just printing the table.

### BOUT · outro (2:42–2:48)
> Overfitting, One Memorized Point at a Time. At Nik Bear Brown.
