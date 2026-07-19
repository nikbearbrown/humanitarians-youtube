#!/usr/bin/env python3
"""Upload Claude, Seeded. to @NikBearBrown / Claude research playlist."""
import argparse, sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

VIDEO = Path("/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/claude-liam-algorithmic-art/claude-liam-algorithmic-art.mp4")
SRT   = Path("/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/claude-liam-algorithmic-art/claude-liam-algorithmic-art.srt")
CREDS_DIR     = Path("/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/credentials/nikbearbrown")
CLIENT_SECRET = CREDS_DIR / "client_secret.json"
TOKEN_FILE    = CREDS_DIR / "youtube_token.json"

TITLE = "Claude, Seeded. — Inside Anthropic's Algorithmic-Art Skill"
TAGS  = ["Claude", "Anthropic", "Algorithmic Art", "Generative Art", "Claude Skills",
         "AI Art", "p5.js", "Art Blocks", "Remotion", "NikBearBrown",
         "Claude Code", "Teardown", "Liam in for Bear"]
DESCRIPTION = """\
Ask Claude for art, and the first thing it writes is a manifesto. Not the code. Not the artwork. A manifesto for a named generative art movement. Only then does it write the algorithm. That is not a metaphor — it is literally the instruction file.

Teardown of Anthropic's algorithmic-art skill: the two-phase pipeline (philosophy → code), the Art Blocks reproducibility contract, the fixed viewer chrome vs. the variable algorithm inside, and why the skill repeats certain phrases over and over.

0:00 Cold open — the manifesto comes first
0:17 Act 1 — what a skill actually is
0:45 Act 2 — Organic Turbulence (live flow field, seed 42)
1:12 Act 2 — movement gallery (Quantum Harmonics · Recursive Whispers · Field Dynamics · Stochastic Crystallization)
1:47 Act 3 — the conceptual seed (φ = 1.618 hidden in the parameters)
2:17 Act 4 — the Art Blocks seed pattern (same seed → identical output, forever)
2:38 Act 4 — same plate, different prints (3×3 seed grid)
3:01 Act 4 — fixed chrome, variable algorithm (the artifact viewer)
3:26 Act 5 — the quality dial (repetition steers the register)
4:00 Verdict
4:36 Your turn
5:02 Outro

All generative visuals in this video are live Remotion renders — not screenshots, not stock art. Each is seeded and deterministic: seed 42 → identical output every render.

Built with Remotion 4.x · Kokoro am_onyx voice · Claude fidelity skin.
Liam, in for Bear.

Source: Anthropic, algorithmic-art SKILL.md

youtube.com/@NikBearBrown

#Claude #AnthropicAI #GenerativeArt #AlgorithmicArt #AIArt #Remotion #NikBearBrown
"""
PLAYLIST_NAME = "Claude research"
CATEGORY      = "28"   # Science & Technology

SCOPES = ["https://www.googleapis.com/auth/youtube.upload",
          "https://www.googleapis.com/auth/youtube",
          "https://www.googleapis.com/auth/youtube.force-ssl"]


def get_service():
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    creds = None
    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(str(CLIENT_SECRET), SCOPES)
            creds = flow.run_local_server(port=0)
        TOKEN_FILE.write_text(creds.to_json())
    return build("youtube", "v3", credentials=creds)


def ensure_playlist(yt, title):
    cache, page = {}, None
    while True:
        resp = yt.playlists().list(part="id,snippet", mine=True, maxResults=50, pageToken=page).execute()
        for item in resp.get("items", []):
            cache[item["snippet"]["title"]] = item["id"]
        page = resp.get("nextPageToken")
        if not page:
            break
    if title in cache:
        print(f"  playlist '{title}' → {cache[title]}")
        return cache[title]
    resp = yt.playlists().insert(
        part="id,snippet,status",
        body={"snippet": {"title": title}, "status": {"privacyStatus": "public"}},
    ).execute()
    pid = resp["id"]
    print(f"  created playlist '{title}' → {pid}")
    return pid


def upload_video(yt, path, publish_at):
    from googleapiclient.http import MediaFileUpload
    body = {
        "snippet": {
            "title": TITLE,
            "description": DESCRIPTION,
            "tags": TAGS,
            "categoryId": CATEGORY,
        },
        "status": {
            "privacyStatus": "private",
            "publishAt": publish_at.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
            "selfDeclaredMadeForKids": False,
        },
    }
    media = MediaFileUpload(str(path), chunksize=-1, resumable=True, mimetype="video/mp4")
    req = yt.videos().insert(part="snippet,status", body=body, media_body=media)
    vid_id = None
    while vid_id is None:
        status, resp = req.next_chunk()
        if resp:
            vid_id = resp["id"]
        elif status:
            print(f"  upload {int(status.progress() * 100)}%", end="\r")
    print(f"  uploaded → https://www.youtube.com/watch?v={vid_id}")
    return vid_id


def upload_captions(yt, video_id, srt_path):
    from googleapiclient.http import MediaFileUpload
    media = MediaFileUpload(str(srt_path), mimetype="application/octet-stream")
    resp = yt.captions().insert(
        part="snippet",
        body={"snippet": {"videoId": video_id, "language": "en", "name": "English", "isDraft": False}},
        media_body=media,
    ).execute()
    print(f"  captions uploaded → {resp.get('id')}")


def add_to_playlist(yt, playlist_id, video_id):
    yt.playlistItems().insert(
        part="snippet",
        body={"snippet": {"playlistId": playlist_id,
                          "resourceId": {"kind": "youtube#video", "videoId": video_id}}},
    ).execute()
    print(f"  added to playlist {playlist_id}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not VIDEO.exists():
        sys.exit(f"Video not found: {VIDEO}")

    size_mb = VIDEO.stat().st_size // 1024 // 1024
    print(f"Video : {VIDEO.name} ({size_mb} MB)")
    print(f"Title : {TITLE}")
    print(f"Channel : @NikBearBrown")
    print(f"Playlist: {PLAYLIST_NAME}")
    print(f"Captions: {SRT.name if SRT.exists() else 'MISSING'}")

    if args.dry_run:
        print("[dry-run] would upload now")
        return

    publish_at = datetime.now(timezone.utc) + timedelta(minutes=15)
    print(f"Publish at: {publish_at.isoformat()}")

    yt = get_service()
    vid_id = upload_video(yt, VIDEO, publish_at)
    if SRT.exists():
        upload_captions(yt, vid_id, SRT)
    playlist_id = ensure_playlist(yt, PLAYLIST_NAME)
    add_to_playlist(yt, playlist_id, vid_id)

    ledger = CREDS_DIR / "youtube_publish_ledger.json"
    import json
    log = json.loads(ledger.read_text()) if ledger.exists() else []
    log.append({"video_id": vid_id, "title": TITLE, "playlist": PLAYLIST_NAME,
                "uploaded_at": datetime.now(timezone.utc).isoformat()})
    ledger.write_text(json.dumps(log, indent=2))

    print(f"\nDone.")
    print(f"  Video ID : {vid_id}")
    print(f"  Watch    : https://www.youtube.com/watch?v={vid_id}")
    print(f"  Studio   : https://studio.youtube.com/video/{vid_id}/edit")
    print(f"  Flip public in Studio when ready.")


if __name__ == "__main__":
    main()
