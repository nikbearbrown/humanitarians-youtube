#!/usr/bin/env python3
"""PM-gate video build: brutalist 4K cards, required intro line, 16:9 + 9:16 exports."""

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
PROJECT = os.environ.get("VIDEO_PROJECT_NAME", "physics_vol_1_ch4")

ELEVENLABS_VOICE_ID = os.environ.get(
    "ELEVENLABS_VOICE_ID", "FGY2WhTYpPnrIDTdsKH5"
)
ELEVENLABS_VOICE_NAME = os.environ.get("ELEVENLABS_VOICE_NAME", "Laura")
ELEVENLABS_MODEL = os.environ.get("ELEVENLABS_MODEL", "eleven_multilingual_v2")

FPS = 30
VIDEO_CRF = 18

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
    html = ROOT / "brutalist-title-cards.html"
    paths: dict[str, Path] = {}

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(html.as_uri())
        await page.wait_for_timeout(1200)

        labels = await page.locator(".frame-label").all_inner_texts()
        frames = page.locator(
            ".frame-16, .frame-9"
        )
        count = await frames.count()
        if count != len(labels):
            raise RuntimeError(f"Card count mismatch: {count} frames vs {len(labels)} labels")

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


# ——— Screen actions (accept optional aspect) ———


async def v1_claim(page, aspect: Aspect | None = None) -> None:
    fs = 48 if aspect and aspect.name == "9x16" else 36
    img = f"{BASE_URL}/media/CNX_UPhysics_04_01_Dispvec.jpg"
    await page.set_content(
        f"""<body style="margin:0;font-family:Inter,sans-serif;padding:60px;background:#fff;color:#121212">
        <p style="font-size:{fs}px;line-height:1.55;max-width:95%;border-left:8px solid #C8860E;padding-left:24px">
        As shown in <strong style="color:#C8102E">Figure 4.7</strong>, the displacement vector connects initial and final positions.
        </p>
        <img src="{img}" style="max-width:90%;border:2px solid #D4D4D4;margin-top:40px" />
        </body>"""
    )
    await page.wait_for_timeout(500)


async def v1_projectile(page, aspect: Aspect | None = None) -> None:
    await page.goto(f"{BASE_URL}/embeds/ch04/projectile.html")
    await page.wait_for_selector("#c")
    await page.wait_for_timeout(600)
    await page.click("#play")
    await page.wait_for_timeout(1200)
    canvas = page.locator("#c")
    box = await canvas.bounding_box()
    if box:
        x, y, w, h = box["x"], box["y"], box["width"], box["height"]
        await page.mouse.move(x + w * 0.25, y + h * 0.75)
        await page.mouse.down()
        await page.mouse.move(x + w * 0.45, y + h * 0.55, steps=12)
        await page.mouse.up()
    await page.wait_for_timeout(800)
    slider = page.locator("#t")
    for v in [100, 250, 400, 600]:
        await slider.fill(str(v))
        await page.wait_for_timeout(200)


async def v1_architecture(page, aspect: Aspect | None = None) -> None:
    await page.goto(f"{BASE_URL}/embeds/ch04/vector-2d.html")
    await page.wait_for_timeout(400)
    await page.goto(f"{BASE_URL}/embeds/ch04/newtons-cannon.html")
    await page.wait_for_selector("#play")
    await page.wait_for_timeout(400)
    await page.click("#play")
    await page.wait_for_timeout(2000)


async def v1_showcase(page, aspect: Aspect | None = None) -> None:
    await page.goto(f"{BASE_URL}/embeds/ch04/vector-2d.html")
    await page.wait_for_selector("#c")
    await page.wait_for_timeout(500)
    canvas = page.locator("#c")
    box = await canvas.bounding_box()
    if box:
        x, y, w, h = box["x"], box["y"], box["width"], box["height"]
        await page.mouse.move(x + w * 0.6, y + h * 0.4)
        await page.mouse.down()
        await page.mouse.move(x + w * 0.7, y + h * 0.35, steps=10)
        await page.mouse.up()
    chip = page.locator(".chip").first
    if await chip.count():
        await chip.click()
    await page.wait_for_timeout(800)
    await page.goto(f"{BASE_URL}/embeds/ch04/newtons-cannon.html")
    await page.wait_for_timeout(400)
    await page.click("#play")
    await page.wait_for_timeout(1500)


async def v1_your_turn(page, aspect: Aspect | None = None) -> None:
    await page.goto(f"{BASE_URL}/embeds/ch04/projectile.html")
    await page.wait_for_timeout(500)
    await page.click("#play")
    await page.wait_for_timeout(1500)


async def v2_gallery(page, aspect: Aspect | None = None) -> None:
    await page.goto((ROOT / "bottom-gallery-demo.html").as_uri())
    await page.wait_for_timeout(800)
    await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    await page.wait_for_timeout(1200)


async def v2_side_by_side(page, aspect: Aspect | None = None) -> None:
    name = (
        "figure-with-sim-demo-portrait.html"
        if aspect and aspect.name == "9x16"
        else "figure-with-sim-demo.html"
    )
    await page.goto((ROOT / name).as_uri())
    await page.wait_for_timeout(1500)


async def v2_layout(page, aspect: Aspect | None = None) -> None:
    aspect = aspect or ASPECT_16
    await page.goto(f"{BASE_URL}/embeds/ch04/orbit.html")
    if aspect.name == "9x16":
        await page.wait_for_timeout(400)
        await page.click("#play")
        await page.wait_for_timeout(2000)
        return
    await page.set_viewport_size({"width": 400, "height": 720})
    await page.wait_for_timeout(1200)
    await page.set_viewport_size({"width": aspect.width, "height": aspect.height})
    await page.wait_for_timeout(400)
    await page.click("#play")
    await page.wait_for_timeout(2000)


async def v2_scroll(page, aspect: Aspect | None = None) -> None:
    await v2_side_by_side(page, aspect)
    await page.wait_for_timeout(1000)


VIDEO1 = {
    "slug": "video1",
    "title": "Why a green build still ships a broken physics demo",
    "intro_line_key": "v1-intro-line",
    "intro_line_text": (
        "This is Charitha Sree Veluru in for Sanjana about "
        "why a green build still ships a broken physics demo."
    ),
    "intro_key": "video-1-intro",
    "outro_key": "video-1-outro",
    "segments": [
        (
            "claim",
            v1_claim,
            "Someone ships when the build passes. That isn't when the sim is done. "
            "So why does a textbook figure need its own canvas page in an iframe — instead of another React chart inside the app? "
            "The physics is the same. The reader experience isn't.",
        ),
        (
            "contrast",
            v1_projectile,
            "Take projectile motion. Wire it as a generic integrated chart: sliders move numbers, click resets the animation, Play is too fast to see the path. "
            "Now open the same scenario as a standalone canvas embed: drag the launch pad, press Play, scrub the trajectory. "
            "Same chapter. Same physics. Different result — because one lets you explore; the other trains you not to click.",
        ),
        (
            "why",
            v1_architecture,
            "Here's why. Thirteen sims in public embeds chapter four, each loaded through a thin React wrapper. "
            "Shared utils dot j s — bind Play, drag handles, scene fitting. The iframe is a boundary: tune teaching UX without redeploying the whole textbook. "
            "Build green inside Next.js didn't mean the mechanism was explorable.",
        ),
        (
            "showcase",
            v1_showcase,
            "Look at the difference directly. Vector 2D: drag a tip — Play pauses while you interact. "
            "Newton's cannon: change speed — orbit stays in frame. Every embed has the same Play control. That consistency is deliberate. "
            "A passing build isn't a teaching pass. If exploring resets the sim, you're not adding interactivity — you're punishing curiosity. "
            "Same physics. Iframe boundary. Reader-first UX.",
        ),
        (
            "your_turn",
            v1_your_turn,
            "Your turn. Open localhost port 3002 slash embeds slash ch04 slash projectile dot html. "
            "Drag the launch point. Press Play. Scrub the path. Then ask: would a slider-only chart have shown you the same thing?",
        ),
    ],
}

VIDEO2 = {
    "slug": "video2",
    "title": "Why putting the simulation at the bottom breaks the lesson",
    "intro_line_key": "v2-intro-line",
    "intro_line_text": (
        "This is Charitha Sree Veluru in for Sanjana about "
        "why putting the simulation at the bottom breaks the lesson."
    ),
    "intro_key": "video-2-intro",
    "outro_key": "video-2-outro",
    "segments": [
        (
            "hook",
            v2_gallery,
            "The sim worked. The student still couldn't use it. "
            "So why does putting the simulation at the bottom of the section break the lesson? "
            "The code runs. The pointer in the prose says see Figure 4.7 — three scroll lengths above the only place you can touch it.",
        ),
        (
            "contrast",
            v2_side_by_side,
            "Same chapter, two layouts. Bottom gallery: one iframe, many preset chips, far from the sentence that references the figure. "
            "Side by side: OpenStax figure on the left, live sim on the right — citation and tool in one viewport. "
            "We tried rolling embeds across the whole book first. We reverted to Chapter 4 only. One chapter done well beats a whole book halfway.",
        ),
        (
            "why",
            v2_side_by_side,
            "Here's why. The sentence creates a pointer. The UI has to resolve it there — not later, not at the bottom. "
            "We restored inline OpenStax figures, mapped twenty-eight plus figure-to-sim pairs, and synced theme with postMessage "
            "so dark mode doesn't remount the iframe and wipe scrub state.",
        ),
        (
            "layout",
            v2_layout,
            "Look at the layout directly. HUD and legend above the canvas — not on top of it. "
            "Narrow the window: chrome scrolls horizontally; the drawable band stays. "
            "Orbit sim: vectors inside the frame, not clipped past the edge. "
            "Layout isn't decoration. It's part of the physics lesson. Reverting a large rollout isn't failure if the reader stops getting lost. "
            "Citation here. Sim here. Not three scrolls later.",
        ),
        (
            "your_turn",
            v2_scroll,
            "Your turn. Open any Chapter 4 section. Find a figure citation in the prose. "
            "Without scrolling, can you see the matching sim? If not, the layout is still teaching the wrong lesson.",
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

    # Required PM intro line (spoken + on-screen card)
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
    }
    (OUTPUT / f"{out_name}.json").write_text(json.dumps(meta, indent=2))
    return final


async def main() -> None:
    venv_python = ROOT / ".venv" / "bin" / "python"
    if not venv_python.exists():
        print(
            "Run: cd fellows/charitha-v/video-pipeline && python3 -m venv .venv "
            "&& .venv/bin/pip install -r requirements.txt && .venv/bin/playwright install chromium",
            file=sys.stderr,
        )
        sys.exit(1)

    try:
        elevenlabs_api_key()
        print(f"TTS: ElevenLabs — {ELEVENLABS_VOICE_NAME} (auto-fallback to edge-tts)")
    except RuntimeError:
        print("TTS: edge-tts (no ELEVENLABS_API_KEY)")

    import urllib.request

    try:
        urllib.request.urlopen(f"{BASE_URL}/embeds/ch04/projectile.html", timeout=5)
    except Exception as e:
        print(f"Start physics-vol-1 on {BASE_URL} first ({e})", file=sys.stderr)
        sys.exit(1)

    print(f"Export: 4K brutalist · 16:9 + 9:16 · naming: {PROJECT}_{VOLUNTEER}_videoN_*.mp4")

    OUTPUT.mkdir(parents=True, exist_ok=True)
    work = Path(tempfile.mkdtemp(prefix="hai-video-", dir=OUTPUT))

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
