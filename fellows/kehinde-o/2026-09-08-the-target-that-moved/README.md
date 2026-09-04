# The Target That Moved

**Volunteer:** Kehinde Obidele

Why my trained deep Q-learning agent scored worse than random, and the one-line
cause behind it.

## Video Files

On the shared Google Drive under `Medhavy_Kehinde/STEM Topic/the-target-that-moved/`:

**[Google Drive folder](https://drive.google.com/drive/folders/1V-BZnGQ8a2soQqO7zD2N_atkRd7OYYPp)**

| File | Aspect | Spec |
|---|---|---|
| `the-target-that-moved.mp4` | 16:9 | 3840x2160, 30fps, 2m 30s |
| `the-target-that-moved-short.mp4` | 9:16 | 2160x3840, 30fps, native render |

## The idea

A DQN learns by comparing its estimate to a target built from its own opinion of
the next state. If that target is computed with the same weights being updated,
every improvement also moves the target. Freeze a copy of the network and the
target holds still long enough to learn against.

## Measured, not rounded

| | Mean reward (100 greedy episodes) | Episodes landing |
|---|---|---|
| Trained checkpoint that shipped | -391 | 0/100 |
| Picking a thruster at random | -213 | n/a |
| After the target-network fix | **-13.9** | **52/100** |

The trained model was worse than random. After the fix it lands about half the
time, which is real improvement but still short of the conventional "solved" bar
of 200 mean reward. Reported as measured.

## Source project

https://github.com/Kenny0bi/Deep-Q-learning-lunarlander

## Files in this repo

- `beat_sheet.json` — the script, one beat per moment
- `PEDAGOGY.md` — narration gate, VERDICT: PASS

Media files are not committed.
