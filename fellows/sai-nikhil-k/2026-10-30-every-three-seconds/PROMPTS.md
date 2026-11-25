# PROMPTS — Every Three Seconds

**No open generation slots.** Eight Remotion compositions and two plates of real
Gavia screenshots. No image model, no paid API.

## B00 — the on-screen typed ask

> Gavia 0.4.0 listens for loon calls in a recording. Show me how it decides, three seconds at a time, and test it under our drone's propeller noise.

## B08 — the handoff the viewer can paste

> I have a one-minute phone recording from a lake. Explain what a 3 s window, a BirdNET embedding and a 0.5 logistic threshold each do to it, and what could make a loon call slip through. Cite your sources.

## Evidence commands

```bash
REEL=weekly_updates/2026-10-30-every-three-seconds
CLIPS=<scratch>/drone_mix          # 325 WAVs, not committed
# 1. loonet's drone test, rebuilt + scored the Python way (loonet's audio venv)
~/.venvs/loonet-audio/bin/python $REEL/evidence/drone_mix.py $CLIPS > $REEL/evidence/drone_mix.out
# 2. the demo recording for B06
~/.venvs/loonet-audio/bin/python $REEL/evidence/demo_mix.py <scratch>/cap
# 3. Gavia's own code: clone github.com/nikhil-kunapareddy/gavia at v0.5.0, copy
#    evidence/noise_check.rs and evidence/listen.rs into desktop/src-tauri/examples/, then:
cd desktop/src-tauri
cargo test --release --test call_parity -- --nocapture      # -> call_parity.out
cargo run --release --example noise_check -- $CLIPS         # -> noise_check.out
cargo run --release --example listen -- <scratch>/cap/loon_maine_clean.wav \
    <scratch>/cap/loon_maine_drone5db.wav tests/fixtures/audio/bullfrog.mp3   # -> listen.out
```
