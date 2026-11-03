#!/usr/bin/env python3
"""Book-wide + parallel-agents PM-gate videos: brutalist 4K, intro line, 16:9 + 9:16.

Regenerate:
  cd ~/physics-vol-1 && npm start          # :3002
  cd ~/agreement_renewal_docs/video
  source .venv/bin/activate
  python build_videos_bookwide.py

Cards: brutalist-title-cards-bookwide.html
Scripts: VIDEO_SCRIPTS_BOOKWIDE.md · STORYBOARD_BOOKWIDE.md
"""

from __future__ import annotations

import asyncio
import json
import os
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Awaitable, Callable

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "output"
BASE_URL = os.environ.get("VIDEO_BASE_URL", "http://localhost:3002")

VOLUNTEER = os.environ.get("VIDEO_VOLUNTEER_NAME", "Charitha_Sree_Veluru")
PM_NAME = os.environ.get("VIDEO_PM_NAME", "Sanjana")
PROJECT = os.environ.get("VIDEO_PROJECT_NAME", "physics_vol_1_bookwide")

ELEVENLABS_VOICE_ID = os.environ.get(
    "ELEVENLABS_VOICE_ID", "FGY2WhTYpPnrIDTdsKH5"
)
ELEVENLABS_VOICE_NAME = os.environ.get("ELEVENLABS_VOICE_NAME", "Laura")
ELEVENLABS_MODEL = os.environ.get("ELEVENLABS_MODEL", "eleven_multilingual_v2")

FPS = 30
VIDEO_CRF = 18
CARDS_HTML = ROOT / "brutalist-title-cards-bookwide.html"

PageFn = Callable[..., Awaitable[None]]


@dataclass(frozen=True)
class Aspect:
    name: str
    width: int
    height: int

    @property
    def suffix(self) -> str:
        return f"_{self.name}"


ASPECT_16 = Aspect("16x9", 3840, 2160)
ASPECT_9 = Aspect("9x16", 2160, 3840)
ASPECTS = (ASPECT_16, ASPECT_9)


def load_env_file() -> None:
    env_path = ROOT / ".env"
    if not env_path.is_file():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip().strip("'\""))


def elevenlabs_api_key() -> str:
    load_env_file()
    key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not key:
        raise RuntimeError(
            f"Missing ELEVENLABS_API_KEY — set in env or {ROOT / '.env'}"
        )
    return key


def run(cmd: list[str], **kw) -> None:
    print("+", " ".join(cmd), flush=True)
    subprocess.run(cmd, check=True, **kw)


def duration(path: Path) -> float:
    out = subprocess.check_output(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(path),
        ],
        text=True,
    )
    return float(out.strip())


def scale_vf(aspect: Aspect, pad_color: str = "white") -> str:
    w, h = aspect.width, aspect.height
    return (
        f"scale={w}:{h}:force_original_aspect_ratio=decrease,"
        f"pad={w}:{h}:(ow-iw)/2:(oh-ih)/2:color={pad_color}"
    )


def x264_args() -> list[str]:
    return [
        "-c:v",
        "libx264",
        "-pix_fmt",
        "yuv420p",
        "-crf",
        str(VIDEO_CRF),
        "-preset",
        "medium",
        "-r",
        str(FPS),
    ]


async def tts_elevenlabs(text: str, out: Path) -> None:
    import urllib.error
    import urllib.request

    api_key = elevenlabs_api_key()
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVENLABS_VOICE_ID}"
    payload = json.dumps(
        {
            "text": text,
            "model_id": ELEVENLABS_MODEL,
            "voice_settings": {
                "stability": 0.45,
                "similarity_boost": 0.8,
                "style": 0.0,
                "use_speaker_boost": True,
            },
        }
    ).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=payload,
        method="POST",
        headers={
            "xi-api-key": api_key,
            "Content-Type": "application/json",
            "Accept": "audio/mpeg",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            out.write_bytes(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"ElevenLabs TTS failed ({e.code}): {body}") from e


async def tts_edge(text: str, out: Path) -> None:
    """Fallback when ElevenLabs key is missing/invalid (same pipeline, edge neural voice)."""
    import edge_tts

    voice = os.environ.get("EDGE_TTS_VOICE", "en-US-JennyNeural")
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(str(out))


async def tts(text: str, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    prefer = os.environ.get("VIDEO_TTS", "auto").strip().lower()
    if prefer == "edge":
        await tts_edge(text, out)
        return
    if prefer == "elevenlabs":
        await tts_elevenlabs(text, out)
        return
    # auto: skip ElevenLabs after first auth failure in this process
    if getattr(tts, "_skip_eleven", False):
        await tts_edge(text, out)
        return
    try:
        await tts_elevenlabs(text, out)
    except Exception as e:
        print(f"  TTS ElevenLabs unavailable ({e}); falling back to edge-tts", flush=True)
        if "401" in str(e) or "invalid_api_key" in str(e) or "Unauthorized" in str(e):
            tts._skip_eleven = True  # type: ignore[attr-defined]
        await tts_edge(text, out)


def image_clip(img: Path, seconds: float, out: Path, aspect: Aspect) -> None:
    run(
        [
            "ffmpeg",
            "-y",
            "-loop",
            "1",
            "-i",
            str(img),
            "-f",
            "lavfi",
            "-i",
            "anullsrc=channel_layout=stereo:sample_rate=44100",
            "-t",
            str(seconds),
            "-vf",
            scale_vf(aspect),
            *x264_args(),
            "-c:a",
            "aac",
            "-shortest",
            str(out),
        ]
    )


def mux_av(video: Path, audio: Path | None, out: Path, aspect: Aspect) -> None:
    if audio and audio.exists():
        d = duration(audio)
        run(
            [
                "ffmpeg",
                "-y",
                "-i",
                str(video),
                "-i",
                str(audio),
                "-vf",
                scale_vf(aspect),
                *x264_args(),
                "-c:a",
                "aac",
                "-b:a",
                "192k",
                "-t",
                str(d),
                "-shortest",
                str(out),
            ]
        )
    else:
        normalize_clip(video, out, aspect)


def normalize_clip(src: Path, dst: Path, aspect: Aspect) -> None:
    run(
        [
            "ffmpeg",
            "-y",
            "-i",
            str(src),
            "-vf",
            scale_vf(aspect),
            *x264_args(),
            "-ar",
            "44100",
            "-ac",
            "2",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            str(dst),
        ]
    )


def concat_clips(clips: list[Path], out: Path) -> None:
    norm_dir = out.parent / f".norm-{out.stem}"
    norm_dir.mkdir(parents=True, exist_ok=True)
    aspect = ASPECT_16 if "16x9" in out.name else ASPECT_9
    normalized: list[Path] = []
    for i, clip in enumerate(clips):
        n = norm_dir / f"{i:02d}.mp4"
        normalize_clip(clip, n, aspect)
        normalized.append(n)
    lst = out.with_suffix(".txt")
    lst.write_text("\n".join(f"file '{c.resolve()}'" for c in normalized))
    run(
        [
            "ffmpeg",
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(lst),
            "-c",
            "copy",
            "-movflags",
            "+faststart",
            str(out),
        ]
    )


async def capture_title_cards(work: Path) -> dict[str, Path]:
    from playwright.async_api import async_playwright

    cards = work / "cards"
    cards.mkdir(parents=True, exist_ok=True)
    paths: dict[str, Path] = {}

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(CARDS_HTML.as_uri())
        await page.wait_for_timeout(1200)

        labels = await page.locator(".frame-label").all_inner_texts()
        frames = page.locator(".frame-16, .frame-9")
        count = await frames.count()
        if count != len(labels):
            raise RuntimeError(
                f"Card count mismatch: {count} frames vs {len(labels)} labels"
            )

        for i, label in enumerate(labels):
            key = label.replace(".png", "").strip()
            frame = frames.nth(i)
            is_portrait = key.endswith("9x16")
            aspect = ASPECT_9 if is_portrait else ASPECT_16
            await page.set_viewport_size(
                {"width": aspect.width, "height": aspect.height}
            )
            path = cards / f"{key}.png"
            await frame.screenshot(path=path)
            paths[key] = path
            print(f"  card [{aspect.name}]: {path.name}")

        await browser.close()
    return paths


async def record_screen(
    work: Path,
    name: str,
    action: PageFn,
    seconds: float,
    aspect: Aspect,
) -> Path:
    from playwright.async_api import async_playwright

    vid_dir = work / "raw" / name / aspect.name
    vid_dir.mkdir(parents=True, exist_ok=True)
    webm_out = work / "raw" / f"{name}-{aspect.name}.webm"

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(
            viewport={"width": aspect.width, "height": aspect.height},
            record_video_dir=str(vid_dir),
            record_video_size={"width": aspect.width, "height": aspect.height},
        )
        page = await context.new_page()
        await action(page, aspect)
        await page.wait_for_timeout(int(max(seconds, 2) * 1000))
        await context.close()
        await browser.close()

    webms = list(vid_dir.glob("*.webm"))
    if not webms:
        raise FileNotFoundError(f"No webm recorded for {name} ({aspect.name})")
    shutil.move(str(webms[0]), webm_out)

    mp4 = work / "raw" / f"{name}-{aspect.name}.mp4"
    run(
        [
            "ffmpeg",
            "-y",
            "-i",
            str(webm_out),
            "-vf",
            scale_vf(aspect),
            *x264_args(),
            str(mp4),
        ]
    )
    return mp4


async def _drag_canvas(
    page, frac_x0: float, frac_y0: float, frac_x1: float, frac_y1: float
) -> None:
    canvas = page.locator("#c")
    if await canvas.count() == 0:
        canvas = page.locator("canvas").first
    box = await canvas.bounding_box()
    if not box:
        return
    x, y, w, h = box["x"], box["y"], box["width"], box["height"]
    await page.mouse.move(x + w * frac_x0, y + h * frac_y0)
    await page.mouse.down()
    await page.mouse.move(x + w * frac_x1, y + h * frac_y1, steps=14)
    await page.mouse.up()


async def _safe_play(page) -> None:
    play = page.locator("#play")
    if await play.count():
        try:
            await play.click(timeout=2000)
        except Exception:
            pass


# ——— Video 1: parallel specialist agents ———


async def v1_claim(page, aspect: Aspect | None = None) -> None:
    await page.goto(f"{BASE_URL}/embeds/ch04/projectile.html")
    await page.wait_for_selector("#c", timeout=15000)
    await page.wait_for_timeout(500)
    await _safe_play(page)
    await page.wait_for_timeout(900)
    await _drag_canvas(page, 0.28, 0.78, 0.42, 0.58)


async def v1_contrast(page, aspect: Aspect | None = None) -> None:
    await page.goto((ROOT / "agent-parallel-demo.html").as_uri())
    await page.wait_for_timeout(5500)
    await page.goto(f"{BASE_URL}/embeds/ch05/incline.html")
    await page.wait_for_selector("#c", timeout=15000)
    await page.wait_for_timeout(400)
    await _drag_canvas(page, 0.45, 0.55, 0.55, 0.45)
    await _safe_play(page)
    await page.wait_for_timeout(1200)


async def v1_why(page, aspect: Aspect | None = None) -> None:
    fs = 40 if aspect and aspect.name == "9x16" else 34
    await page.set_content(
        f"""<!DOCTYPE html><html><head>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@600;800&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet"/>
        <style>
          body {{ margin:0; font-family:Inter,sans-serif; background:#fff; color:#121212;
                 padding:56px; border-left:12px solid #C8860E; }}
          .tag {{ font-family:JetBrains Mono,monospace; color:#C8102E; letter-spacing:.12em;
                 text-transform:uppercase; font-size:18px; margin-bottom:24px; }}
          h1 {{ font-size:{fs + 18}px; font-weight:800; max-width:95%; line-height:1.15; }}
          pre {{ margin-top:40px; font-family:JetBrains Mono,monospace; font-size:{fs - 6}px;
                line-height:1.55; color:#545454; border:2px solid #D4D4D4; padding:28px; }}
          .hi {{ color:#C8860E; }}
        </style></head><body>
        <div class="tag">Shared contract</div>
        <h1>Agents share utils — not one overloaded prompt</h1>
        <pre>public/embeds/
  ch04/  <span class="hi">← gold standard</span>
  ch05/ … ch17/  <span class="hi">← one specialist each</span>
  utils.js · bindCanvasInteraction
  style.css · HUD · Play · handles</pre>
        </body></html>"""
    )
    await page.wait_for_timeout(800)


async def v1_showcase(page, aspect: Aspect | None = None) -> None:
    await page.goto(f"{BASE_URL}/embeds/ch01/diagrams.html")
    await page.wait_for_timeout(600)
    # Click-to-highlight orders of magnitude if present
    for sel in ("td", ".cell", "[data-row]", "canvas"):
        loc = page.locator(sel).first
        if await loc.count():
            try:
                await loc.click(timeout=1500)
                break
            except Exception:
                continue
    await page.wait_for_timeout(900)

    await page.goto(f"{BASE_URL}/embeds/ch05/incline.html")
    await page.wait_for_selector("#c", timeout=15000)
    await _drag_canvas(page, 0.4, 0.6, 0.52, 0.48)
    await _safe_play(page)
    await page.wait_for_timeout(1000)

    await page.goto(f"{BASE_URL}/embeds/ch09/elasticCollision1D.html")
    await page.wait_for_selector("#c", timeout=15000)
    await _drag_canvas(page, 0.25, 0.5, 0.35, 0.45)
    await _safe_play(page)
    await page.wait_for_timeout(1200)


async def v1_your_turn(page, aspect: Aspect | None = None) -> None:
    await page.goto(f"{BASE_URL}/embeds/ch06/atwood.html")
    await page.wait_for_selector("#c", timeout=15000)
    await _drag_canvas(page, 0.35, 0.4, 0.4, 0.55)
    await _safe_play(page)
    await page.wait_for_timeout(1000)
    await page.goto(f"{BASE_URL}/embeds/ch16/traveling-wave.html")
    await page.wait_for_selector("#c", timeout=15000)
    await _safe_play(page)
    await page.wait_for_timeout(1500)


# ——— Video 2: project update book-wide ———


async def v2_hook(page, aspect: Aspect | None = None) -> None:
    name = (
        "figure-with-sim-demo-portrait.html"
        if aspect and aspect.name == "9x16"
        else "figure-with-sim-demo.html"
    )
    await page.goto((ROOT / name).as_uri())
    await page.wait_for_timeout(1500)


async def v2_claim(page, aspect: Aspect | None = None) -> None:
    fs = 36 if aspect and aspect.name == "9x16" else 32
    await page.set_content(
        f"""<!DOCTYPE html><html><head>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@700;800&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet"/>
        <style>
          body {{ margin:0; font-family:Inter,sans-serif; background:#fff; color:#121212;
                 padding:56px; border-left:12px solid #C8860E; }}
          .tag {{ font-family:JetBrains Mono,monospace; color:#C8102E; letter-spacing:.12em;
                 text-transform:uppercase; font-size:18px; margin-bottom:20px; }}
          h1 {{ font-size:{fs + 20}px; font-weight:800; line-height:1.12; max-width:95%; }}
          ul {{ margin-top:36px; list-style:none; display:grid;
               grid-template-columns:1fr 1fr; gap:14px 40px; font-size:{fs}px; }}
          li {{ border-bottom:1px solid #D4D4D4; padding:10px 0; }}
          li span {{ color:#C8860E; font-family:JetBrains Mono,monospace; font-size:0.75em; }}
        </style></head><body>
        <div class="tag">Project update</div>
        <h1>What does book-wide Ch. 4 parity look like?</h1>
        <ul>
          <li><span>01–03</span> Interaction upgrades</li>
          <li><span>04</span> Gold standard contract</li>
          <li><span>05–17</span> Specialist agents</li>
          <li><span>*</span> FigureWithSim inline</li>
        </ul>
        </body></html>"""
    )
    await page.wait_for_timeout(800)


async def v2_contrast(page, aspect: Aspect | None = None) -> None:
    await page.goto(f"{BASE_URL}/embeds/ch01/parametric-graph.html")
    await page.wait_for_timeout(700)
    for sel in ("#tmax", "#T", "#time", "input[type=range]", "#dt"):
        sl = page.locator(sel)
        if await sl.count():
            try:
                for v in ("2", "5", "8", "12"):
                    await sl.first.fill(v)
                    await page.wait_for_timeout(350)
                break
            except Exception:
                try:
                    await sl.first.evaluate(
                        "(el, v) => { el.value = v; el.dispatchEvent(new Event('input', {bubbles:true})); }",
                        "8",
                    )
                    await page.wait_for_timeout(500)
                    break
                except Exception:
                    continue
    await _safe_play(page)
    await page.wait_for_timeout(1200)


async def v2_why(page, aspect: Aspect | None = None) -> None:
    await v2_hook(page, aspect)
    await page.wait_for_timeout(1200)


async def v2_showcase(page, aspect: Aspect | None = None) -> None:
    stops = [
        f"{BASE_URL}/embeds/ch01/diagrams.html",
        f"{BASE_URL}/embeds/ch08/energy-skate.html",
        f"{BASE_URL}/embeds/ch13/orbit.html",
        f"{BASE_URL}/embeds/ch16/traveling-wave.html",
    ]
    for url in stops:
        await page.goto(url)
        await page.wait_for_timeout(500)
        if await page.locator("#c").count():
            await _drag_canvas(page, 0.4, 0.5, 0.55, 0.4)
        await _safe_play(page)
        await page.wait_for_timeout(1100)


async def v2_your_turn(page, aspect: Aspect | None = None) -> None:
    await page.goto(f"{BASE_URL}/embeds/ch13/gravity-orbit.html")
    await page.wait_for_timeout(600)
    if await page.locator("#c").count() == 0:
        await page.goto(f"{BASE_URL}/embeds/ch13/orbit.html")
    await page.wait_for_selector("#c", timeout=15000)
    await _drag_canvas(page, 0.55, 0.35, 0.65, 0.45)
    await _safe_play(page)
    await page.wait_for_timeout(1800)


VIDEO1 = {
    "slug": "video1",
    "title": "Why one agent can't polish seventeen physics chapters",
    "intro_line_key": "v1-intro-line",
    "intro_line_text": (
        "This is Charitha Sree Veluru in for Sanjana about "
        "why one agent can't polish seventeen physics chapters."
    ),
    "intro_key": "video-1-intro",
    "outro_key": "video-1-outro",
    "segments": [
        (
            "claim",
            v1_claim,
            "Someone gives one agent the whole textbook and calls it a rollout. That isn't how Chapter 4 got good. "
            "So why can't one agent polish seventeen physics chapters the way a single chapter actually teaches?",
        ),
        (
            "contrast",
            v1_contrast,
            "Take accuracy versus precision. One mega-pass put the high precision cluster on the bullseye — that's accuracy, not precision. "
            "Slider-only graphs auto-scaled the Y axis so changing time looked like nothing happened. "
            "Now run it differently. One specialist agent per chapter. Same Chapter 4 contract: layout, drag handles, Play that pauses when you grab a tip, stable axes. "
            "Thirteen agents in parallel — chapters five through seventeen — each owning one folder under public slash embeds.",
        ),
        (
            "why",
            v1_why,
            "Here's why it works. The contract is shared. The context is not. "
            "An agent that only sees Chapter 9 collisions can drag velocity tips correctly. "
            "An agent that sees the whole book invents half-finished chrome and ships uneven quality. "
            "Parallel specialists share utils and style from Chapter 4 — they don't share one overloaded prompt.",
        ),
        (
            "showcase",
            v1_showcase,
            "Look at it directly. Chapter 1 orders of magnitude: a click highlights the row. "
            "Chapter 5 incline: drag the block and the angle tip. Chapter 9 elastic collision: drag v-one and v-two. "
            "Same Play. Same pause-on-drag. Same brutalist chrome. "
            "One agent on seventeen chapters is a volume metric. Specialist agents are a teaching metric.",
        ),
        (
            "your_turn",
            v1_your_turn,
            "Your turn. Open two embeds from different chapters — say chapter six Atwood and chapter sixteen traveling wave. "
            "Drag a handle on each. If the interaction language matches, the parallel pass worked.",
        ),
    ],
}

VIDEO2 = {
    "slug": "video2",
    "title": "What shipped when Chapter 4's sim contract went book-wide",
    "intro_line_key": "v2-intro-line",
    "intro_line_text": (
        "This is Charitha Sree Veluru in for Sanjana about "
        "what shipped when Chapter 4's sim contract went book-wide."
    ),
    "intro_key": "video-2-intro",
    "outro_key": "video-2-outro",
    "segments": [
        (
            "hook",
            v2_hook,
            "We had one chapter done well. The rest of the book still trained students not to click. "
            "So what shipped when Chapter 4's sim contract went book-wide?",
        ),
        (
            "claim",
            v2_claim,
            "Before: decorative canvases, images missing next to sims, relative-uncertainty graphs where time and delta did nothing you could see. "
            "After: FigureWithSim keeps the OpenStax figure on the left and the live embed on the right. "
            "Every linked sim uses the Chapter 4 stack — HUD, canvas, readout, controls — with drag handles and Play.",
        ),
        (
            "contrast",
            v2_contrast,
            "Here's why that matters. The sentence in the textbook creates a pointer. The UI has to resolve it with a tool that moves. "
            "Sharing Chapter 4's utils across chapters one through seventeen means bindCanvasInteraction and animationDt stay consistent. "
            "We unlinked decorative photo sims where a photograph teaches better than a fake diagram — and kept the embed code.",
        ),
        (
            "showcase",
            v2_showcase,
            "Look at the book directly. Chapter 1: click orders of magnitude. Chapter 8 energy skate: drag the skater. "
            "Chapter 13: drag the satellite. Chapter 16 traveling wave: scrub the waveform. "
            "Heights locked at 620. Light and dark theme still sync without wiping scrub state. "
            "Scope discipline from the Chapter 4 revert still holds: one contract done well, then multiplied — not seventeen brittle inventions.",
        ),
        (
            "your_turn",
            v2_your_turn,
            "Your turn. Open any section from chapters five through seventeen. Find a FigureWithSim. "
            "Without scrolling away from the citation, drag once. If the handle moves and Play pauses, the book-wide pass landed.",
        ),
    ],
}


def output_name(spec: dict, aspect: Aspect) -> str:
    return f"{PROJECT}_{VOLUNTEER}_{spec['slug']}{aspect.suffix}.mp4"


def card_key(base: str, aspect: Aspect) -> str:
    return f"{base}-{aspect.name}"


async def build_one(
    spec: dict, cards: dict[str, Path], work: Path, aspect: Aspect
) -> Path:
    out_name = output_name(spec, aspect)
    print(f"\n=== {spec['title']} [{aspect.name} @ 4K] ===\n")
    segments_dir = work / spec["slug"] / aspect.name / "segments"
    segments_dir.mkdir(parents=True, exist_ok=True)
    clips: list[Path] = []

    intro_line_img = cards[card_key(spec["intro_line_key"], aspect)]
    intro_line_clip = segments_dir / "00-intro-line.mp4"
    image_clip(intro_line_img, 4.0, intro_line_clip, aspect)
    intro_line_audio = segments_dir / "00-intro-line.mp3"
    print("  TTS: intro-line (required)")
    await tts(spec["intro_line_text"], intro_line_audio)
    intro_line_final = segments_dir / "00-intro-line-final.mp4"
    mux_av(intro_line_clip, intro_line_audio, intro_line_final, aspect)
    clips.append(intro_line_final)

    intro_img = cards[card_key(spec["intro_key"], aspect)]
    intro_clip = segments_dir / "01-title.mp4"
    image_clip(intro_img, 3.0, intro_clip, aspect)
    clips.append(intro_clip)

    for i, (name, action, text) in enumerate(spec["segments"], start=2):
        audio = segments_dir / f"{i:02d}-{name}.mp3"
        print(f"  TTS: {name}")
        await tts(text, audio)
        aud_d = duration(audio)
        print(f"  Record: {name} ({aud_d:.1f}s) [{aspect.name}]")
        raw = await record_screen(
            work / spec["slug"], name, action, aud_d + 0.5, aspect
        )
        seg = segments_dir / f"{i:02d}-{name}-final.mp4"
        mux_av(raw, audio, seg, aspect)
        clips.append(seg)

    outro_img = cards[card_key(spec["outro_key"], aspect)]
    outro_clip = segments_dir / "99-outro.mp4"
    image_clip(outro_img, 5.0, outro_clip, aspect)
    clips.append(outro_clip)

    final = OUTPUT / out_name
    concat_clips(clips, final)
    meta = {
        "title": spec["title"],
        "aspect": aspect.name,
        "resolution": f"{aspect.width}x{aspect.height}",
        "file": str(final),
        "naming": out_name,
        "intro_line": spec["intro_line_text"],
        "volunteer": VOLUNTEER,
        "pm": PM_NAME,
        "project": PROJECT,
        "template": "brutalist-4k",
        "voice": ELEVENLABS_VOICE_NAME,
        "voice_id": ELEVENLABS_VOICE_ID,
        "segments": len(clips),
        "builder": "build_videos_bookwide.py",
    }
    (OUTPUT / f"{out_name}.json").write_text(json.dumps(meta, indent=2))
    return final


async def main() -> None:
    venv_python = ROOT / ".venv" / "bin" / "python"
    if not venv_python.exists():
        print(
            "Run: cd agreement_renewal_docs/video && python3 -m venv .venv "
            "&& .venv/bin/pip install playwright && .venv/bin/playwright install chromium",
            file=sys.stderr,
        )
        sys.exit(1)

    if not CARDS_HTML.is_file():
        print(f"Missing cards HTML: {CARDS_HTML}", file=sys.stderr)
        sys.exit(1)

    # ElevenLabs preferred; edge-tts is installed as fallback when key is invalid.
    try:
        elevenlabs_api_key()
        print(f"TTS: ElevenLabs — {ELEVENLABS_VOICE_NAME} (auto-fallback to edge-tts)")
    except RuntimeError:
        print("TTS: edge-tts (no ELEVENLABS_API_KEY)")

    import urllib.request

    try:
        urllib.request.urlopen(f"{BASE_URL}/embeds/ch05/incline.html", timeout=5)
    except Exception as e:
        print(f"Start physics-vol-1 on {BASE_URL} first ({e})", file=sys.stderr)
        sys.exit(1)

    print(f"TTS: ElevenLabs — {ELEVENLABS_VOICE_NAME}")
    print(
        f"Export: 4K brutalist · 16:9 + 9:16 · naming: {PROJECT}_{VOLUNTEER}_videoN_*.mp4"
    )

    OUTPUT.mkdir(parents=True, exist_ok=True)
    work = Path(tempfile.mkdtemp(prefix="hai-bookwide-", dir=OUTPUT))

    print("Capturing brutalist title cards at 4K…")
    cards = await capture_title_cards(work)

    built: list[Path] = []
    for spec in (VIDEO1, VIDEO2):
        for aspect in ASPECTS:
            built.append(await build_one(spec, cards, work, aspect))

    print("\nDone — PM gate exports:")
    for p in built:
        print(f"  {p.name}")
    print("\nUpload all four files + GitHub repo URL to shared drive.")


if __name__ == "__main__":
    asyncio.run(main())
