#!/usr/bin/env python3
"""
upload_nikbearbrown.py — Upload Bear Brown Initials Remotion Showcase (9:16) to
@HumanitariansAI in the "Shorts" playlist.

Usage: python3 upload_nikbearbrown.py [--dry-run]
"""
import argparse, sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

VIDEO = Path("/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/claude-liam-bear-brown-initials-remotion-showcase/mp4/claude-liam-bear-brown-initials-remotion-showcase.mp4")
CREDS_DIR = Path("/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/credentials/nikbearbrown")
CLIENT_SECRET = CREDS_DIR / "client_secret.json"
TOKEN_FILE    = CREDS_DIR / "youtube_token.json"

TITLE = "Every Remotion Move, One Mark — Bear Brown Initials Technique Showcase"
TAGS  = [
    "Remotion", "React Animation", "Motion Design", "Logo Animation",
    "Remotion Tutorial", "SVG Animation", "Brand Animation",
    "NikBearBrown", "Bear Brown", "Motion Techniques", "Remotion Showcase",
]
DESCRIPTION = """\
One initials mark. Every move Remotion knows. Which ones deserve to live?

A technique-showcase reel animating the Bear Brown initials mark 20 different ways — a review pass to judge which motion patterns are worth keeping.

0:00 Cold Open
0:12 Spring Entrance
0:19 Overshoot Spring
0:30 Draw-On Stroke
0:40 Mask Reveal
0:50 Scale Zoom
0:59 Rotation
1:09 Skew And Shear
1:18 Opacity Through Blur
1:27 Color Interpolation
1:38 Kinetic Grid
1:50 Glitch Slices
1:59 Trail Echo
2:09 Noise Wobble
2:19 Elastic Physics
2:30 Card Flip
2:41 Shadow Play
2:50 Composer Summon
2:59 Stroke Pulse
3:08 Scale Breathe
3:17 Exit Family
3:27 Your Turn
3:36 Outro

Built with Remotion 4.x · @remotion/paths · Kokoro af_kore voice · Claude fidelity skin.

youtube.com/@HumanitariansAI

#Remotion #MotionDesign #LogoAnimation #NikBearBrown
"""
PLAYLIST_NAME = "Shorts"
CATEGORY      = "28"  # Science & Technology

SCOPES = [
    "https://www.googleapis.com/auth/youtube.upload",
    "https://www.googleapis.com/auth/youtube",
    "https://www.googleapis.com/auth/youtube.force-ssl",
]


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


def ensure_playlist(yt, title: str) -> str:
    cache = {}
    page = None
    while True:
        resp = yt.playlists().list(
            part="id,snippet", mine=True, maxResults=50, pageToken=page
        ).execute()
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


def upload_video(yt, path: Path, publish_at: datetime) -> str:
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


def add_to_playlist(yt, playlist_id: str, video_id: str):
    yt.playlistItems().insert(
        part="snippet",
        body={"snippet": {"playlistId": playlist_id, "resourceId": {
            "kind": "youtube#video", "videoId": video_id
        }}},
    ).execute()
    print(f"  added to playlist {playlist_id}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not VIDEO.exists():
        sys.exit(f"Video not found: {VIDEO}")
    print(f"Video: {VIDEO.name} ({VIDEO.stat().st_size // 1024 // 1024} MB)")
    print(f"Title: {TITLE}")
    print(f"Channel: @HumanitariansAI")
    print(f"Playlist: {PLAYLIST_NAME}")

    if args.dry_run:
        print("[dry-run] would upload now")
        return

    publish_at = datetime.now(timezone.utc) + timedelta(minutes=15)
    print(f"Publish at: {publish_at.isoformat()}")

    yt = get_service()
    vid_id = upload_video(yt, VIDEO, publish_at)
    playlist_id = ensure_playlist(yt, PLAYLIST_NAME)
    add_to_playlist(yt, playlist_id, vid_id)
    print(f"\nDone. Video ID: {vid_id}")
    print(f"Studio: https://studio.youtube.com/video/{vid_id}/edit")


if __name__ == "__main__":
    main()
