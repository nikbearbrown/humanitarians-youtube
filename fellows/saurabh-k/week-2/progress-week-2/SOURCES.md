# SOURCES — hai-brutalist-week-2

A progress report about the toolkit it was built with, so every source is a command that
can be re-run against the same commit. Claim-level verdicts are in [FACTCHECK.md](FACTCHECK.md).

## The environment variables

`grep -rhoE "os\.environ(\.get)?\(?\[?['\"][A-Z_]{3,}['\"]" runtime/` over brutalist.art,
unique-sorted, on 2026-10-26. Fourteen results:

```
ART_CHROME  ART_CHROME_MODE  ART_HOME  ART_NO_DRAWTEXT  ART_OUT  ART_PALETTE
ART_REMOTION_TIMEOUT_MS  FFMPEG  KOKORO_MODEL  KOKORO_VOICES  LATO_TTF
REPOLOOP_MODEL  SEIS_BOOKS  VOX_PALETTE
```

An earlier draft of B01 said eleven, counted from a narrower grep. The full sweep returned
fourteen and the beat was rewritten and re-voiced before any frame was rendered.

## The two you never set

- **`ART_HOME`** — `art` lines 29-30: `ART_HOME="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"`
  then `export ART_HOME`. The script works out its own location.
- **`REEL_DIR`** — `runtime/scripts/run.sh` line 27 resolves the argument's dirname and
  re-joins the basename, making it absolute. It is a shell variable inside `run.sh`, not
  one of the fourteen `os.environ` reads above.

## The defaults shown in B04

Read from `runtime/scripts/`:

| Variable | Default | Source |
|---|---|---|
| `ART_REMOTION_TIMEOUT_MS` | `180000` | `os.environ.get("ART_REMOTION_TIMEOUT_MS", "180000")` |
| `FFMPEG` | `ffmpeg` | `os.environ.get("FFMPEG", "ffmpeg")` |
| `KOKORO_MODEL` | `kokoro-v1.0.onnx` | `Path(os.environ.get("KOKORO_MODEL") or base / ...)` |
| `KOKORO_VOICES` | `voices-v1.0.bin` | same shape |
| `ART_NO_DRAWTEXT` | off | presence flag: `if os.environ.get("ART_NO_DRAWTEXT")` |

## The correction to week one

Week one reported a missing library as a toolkit defect. Checked again on 2026-10-26:

- `/usr/bin/python3 -V` → 3.9.6, and `import scipy` **succeeds** — scipy 1.13.1 is installed.
- Running `type_check.py` under it raises
  `TypeError: unsupported operand type(s) for |: 'type' and 'NoneType'` at line 999, which
  annotates `float | None` — syntax that needs Python 3.10+.
- `.venv/bin/python -V` → 3.13.12 with scipy 1.18.1, and the gate runs there.

So the install worked; the interpreter was the blocker. That is the week's finding and it
corrects the previous report.

## Narration

Kokoro `am_onyx`, generated locally at $0.00, disclosed aloud in B00.
