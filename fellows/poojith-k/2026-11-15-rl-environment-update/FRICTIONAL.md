# Friction log

## 2026-11-15

This entry records the presenter’s account of problems during the project week.

### Overnight model service

- What was hard: A model service stopped responding overnight.
- What I tried: I restarted it so it could run independently of the active connection.
- Result / still open: The service could run without an open session. Check whether it keeps responding through later overnight runs.

### First answer during the live demo

- What was hard: The first demo timed out waiting for the model’s first answer after a reload.
- What I tried: I removed the per-call deadlines, added a warm-up, and timed every call.
- Result / still open: The demo can wait for the first answer while recording its delay. Measure how much warm-up changes the first-answer time.

### Temporary test files

- What was hard: The test suite failed when it used the default temporary folder.
- What I tried: I used a temporary folder in the allowed runs area.
- Result / still open: I could rerun the suite with the same tests. Keep the temporary directory selection explicit for future runs.

### Interrupted overnight runs

- What was hard: Runs stopped when the laptop slept or the connection reset.
- What I tried: I added a wake request and connection keepalives, and queued the affected episodes to rerun.
- Result / still open: The affected episodes were scheduled again. Verify they complete and check for new interruptions.

### Demo recording format

- What was hard: Recording the full ultrawide screen made the viewer too narrow.
- What I tried: I recorded the browser window at 16:9.
- Result / still open: The viewer occupies more of the recording frame. Check the framing again before the next demo.

### Run-to-run variation

- What was hard: A repeat at identical settings did not reproduce the earlier score.
- What I tried: I compared the two runs under the same condition and kept the difference visible in the report.
- Result / still open: A single run per condition cannot establish how stable the result is. Repeat each condition and measure the variation.

- What was hard: The first Whisper check heard the model name as the letter sequence QN.
- What I tried: I added the toolkit's voice-only pronunciation for Qwen and regenerated the two affected spoken beats.
- Result / still open: The voice uses the intended Kwen sound. The source script and cards keep Qwen.

- What was hard: The landscape closing subtitles fell one pixel below the typography minimum.
- What I tried: I enlarged only those subtitles in the isolated ai-explainer layout.
- Result / still open: The four closing cards fit and the stock typography check passed.

- What was hard: The measured narration was shorter than the target cut, and the stock master checker lacked its duration helper.
- What I tried: I kept Kokoro synthesis at speed 1, used a 0.94× pitch-preserving pace edit, aligned the reading pauses to spoken phrases, and checked the exact frame count independently.
- Result / still open: Both final layouts have the same 2:22 clock.

- What was hard: Whisper spelled the corrected model name as “Quen,” heard “warned” as “worn,” and inserted words during the end card.
- What I tried: I compared both exported tracks against the approved script, checked the earlier isolated “warned” reading, and decoded the audio across the full credit.
- Result / still open: The credit is digital silence, so its transcript insertion was excluded. The four remaining differences are in the listening review for each cut.
