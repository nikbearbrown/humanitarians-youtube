# FACTCHECK — hai-brutalist-week-2

Status: **GATE F — drafted 2026-10-26. 6 rows VERIFIED-LOCAL, 1 row SPEC-ASSERTED,
2 rows ARGUMENT.**

Verdict vocabulary: **VERIFIED-LOCAL** = checked against first-party evidence on this
machine during the build, reproducible by re-reading the named file or re-running the named
command. **SPEC-ASSERTED** = a statement about how the toolkit is documented to work,
consistent with observed behaviour but not independently re-derived. **ARGUMENT** =
reasoning or advice, not a measurement.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B01 | The toolkit reads fourteen environment variables | **VERIFIED-LOCAL** | `grep -rhoE "os\.environ(\.get)?\(?\[?['\"][A-Z_]{3,}['\"]" runtime/` on 2026-10-26, unique-sorted: ART_CHROME, ART_CHROME_MODE, ART_HOME, ART_NO_DRAWTEXT, ART_OUT, ART_PALETTE, ART_REMOTION_TIMEOUT_MS, FFMPEG, KOKORO_MODEL, KOKORO_VOICES, LATO_TTF, REPOLOOP_MODEL, SEIS_BOOKS, VOX_PALETTE | Recount if the toolkit commit changes. An earlier draft said eleven and was corrected before the audio was generated |
| 2 | B02 | Narration is generated first and its duration is the clock every beat is cut to | **VERIFIED-LOCAL** | `generate_audio_kokoro.py` header: *"Durations are GROUND TRUTH for all downstream timing. Downstream never knows"*. Observed this build: nine mp3s written, `actual_duration_s` written back into the beat sheet before any render | — |
| 3 | B03 | `ART_HOME` is the toolkit root, worked out by `art` from its own location and exported | **VERIFIED-LOCAL** | `art` lines 29-30: `ART_HOME="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"` then `export ART_HOME` | — |
| 4 | B03 | `REEL_DIR` is the reel folder turned into an absolute path by `run.sh` | **VERIFIED-LOCAL** | `runtime/scripts/run.sh` line 27 resolves the argument's dirname and re-joins the basename | Note it is a shell variable inside run.sh, not one of the fourteen `os.environ` reads in row 1 |
| 5 | B04 | The settable ones and their defaults: `KOKORO_MODEL` → `kokoro-v1.0.onnx`, `KOKORO_VOICES` → `voices-v1.0.bin`, `ART_REMOTION_TIMEOUT_MS` → `180000`, `ART_NO_DRAWTEXT` off, `FFMPEG` → `ffmpeg` | **VERIFIED-LOCAL** | Read from the defaults in `runtime/scripts/`: `os.environ.get("ART_REMOTION_TIMEOUT_MS", "180000")`, `os.environ.get("FFMPEG", "ffmpeg")`, `Path(os.environ.get("KOKORO_MODEL") or base / "kokoro-v1.0.onnx")`, same shape for voices, and `if os.environ.get("ART_NO_DRAWTEXT")` as a presence flag | — |
| 6 | B05 | scipy was already installed on system python; the gate still would not run there, because `type_check.py` line 999 annotates `float | None` and the system interpreter is 3.9.6. The toolkit venv is 3.13.12 and runs it | **VERIFIED-LOCAL** | `/usr/bin/python3 -V` -> 3.9.6 and `/usr/bin/python3 -c "import scipy"` -> scipy 1.13.1 present. Running `type_check.py` under it raises `TypeError: unsupported operand type(s) for |: 'type' and 'NoneType'` at line 999. `.venv/bin/python -V` -> 3.13.12 with scipy 1.18.1, and the gate runs there. All checked 2026-10-26 | Re-check if the venv is rebuilt or the toolkit drops the 3.10+ syntax |
| 7 | B05/B06 | The blocker was never the library, it was the interpreter | **ARGUMENT** | Conclusion drawn from row 6. Week one installed the library and treated that as the fix; the gate still could not run, so the library was never the whole cause. Reasoning, not a measurement | Keep framed as a conclusion drawn |
| 8 | B06 | A default is a decision someone already made for you | **ARGUMENT** | Advice. Narrated as a judgement and not as a finding | — |
| 9 | B02 | The pipeline order is beat sheet, narration, beats, gates, master | SPEC-ASSERTED | The toolkit's own described flow in `HOW-TO.md` and `docs/what-is-brutalist.md`, consistent with the observed order of this build | Confirm against the docs if the pipeline changes |

## Honesty notes

- **Narration is AI-generated** (Kokoro `am_onyx`), disclosed aloud in B00. The work, the
  environment and the evidence are the fellow's own.
- **Row 1 is the one that nearly shipped wrong.** The first draft of B01 said eleven
  variables, counted from a narrower grep. The full sweep returned fourteen and the beat was
  rewritten and re-voiced before any frame was rendered. The count on screen is the swept one.
- **Row 6 is the correction to week one, and it corrects this reel too.** The first draft of B05
  said the system python had no scipy. That was checked on 2026-10-26 and is false — scipy 1.13.1
  is installed there. Week one's install worked. What still fails on 3.9.6 is the 3.10+ union
  annotation at line 999, so the gate only runs inside the venv. The beat was rewritten and
  re-voiced before the final cut. The earlier, false version was never rendered to a master.
- **The reel reports on the toolkit it was built with**, so every claim here is checkable by
  re-running the command in the Source column against this commit.
