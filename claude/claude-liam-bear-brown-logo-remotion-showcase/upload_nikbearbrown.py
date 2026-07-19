#!/usr/bin/env python3
"""Upload Bear Brown Logo Remotion Showcase (9:16) to @NikBearBrown / Shorts."""
import argparse, sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

VIDEO = Path("/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/claude-liam-bear-brown-logo-remotion-showcase/claude-liam-bear-brown-logo-remotion-showcase.mp4")
CREDS_DIR = Path("/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/credentials/nikbearbrown")
CLIENT_SECRET = CREDS_DIR / "client_secret.json"
TOKEN_FILE    = CREDS_DIR / "youtube_token.json"

TITLE = "Every Remotion Move, One Logo — Bear Brown Mark Technique Showcase"
TAGS  = ["Remotion", "React Animation", "Motion Design", "Logo Animation",
         "Remotion Tutorial", "SVG Animation", "NikBearBrown", "Bear Brown",
         "Motion Techniques", "Remotion Showcase"]
DESCRIPTION = """\
One logo. Every move Remotion knows. Which ones deserve to live?

A technique-showcase reel animating the Bear Brown mark 20 different ways — a review pass to judge which motion patterns are worth keeping.

0:00 Cold Open
0:09 Spring Entrance
0:16 Overshoot Spring
0:24 Draw-On Stroke
0:31 Mask Reveal
0:38 Scale Zoom
0:45 Rotation
0:52 Skew And Shear
0:58 Opacity Through Blur
1:06 Color Interpolation
1:13 Kinetic Grid
1:20 Glitch Slices
1:29 Trail Echo
1:36 Noise Wobble
1:44 Elastic Physics
1:51 Card Flip
1:58 Shadow Play
2:06 Composer Summon
2:13 Stroke Pulse
2:20 Scale Breathe
2:27 Exit Family
2:33 Your Turn
2:41 Outro

Built with Remotion 4.x · @remotion/paths · Kokoro am_onyx voice · Claude fidelity skin.

youtube.com/@NikBearBrown

#Remotion #MotionDesign #LogoAnimation #NikBearBrown
"""
PLAYLIST_NAME = "Shorts"
CATEGORY      = "28"

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
        if not page: break
    if title in cache:
        print(f"  playlist '{title}' → {cache[title]}"); return cache[title]
    resp = yt.playlists().insert(part="id,snippet,status",
        body={"snippet": {"title": title}, "status": {"privacyStatus": "public"}}).execute()
    pid = resp["id"]; print(f"  created playlist '{title}' → {pid}"); return pid

def upload_video(yt, path, publish_at):
    from googleapiclient.http import MediaFileUpload
    body = {"snippet": {"title": TITLE, "description": DESCRIPTION, "tags": TAGS, "categoryId": CATEGORY},
            "status": {"privacyStatus": "private", "publishAt": publish_at.strftime("%Y-%m-%dT%H:%M:%S.000Z"), "selfDeclaredMadeForKids": False}}
    media = MediaFileUpload(str(path), chunksize=-1, resumable=True, mimetype="video/mp4")
    req = yt.videos().insert(part="snippet,status", body=body, media_body=media)
    vid_id = None
    while vid_id is None:
        status, resp = req.next_chunk()
        if resp: vid_id = resp["id"]
        elif status: print(f"  upload {int(status.progress()*100)}%", end="\r")
    print(f"  uploaded → https://www.youtube.com/watch?v={vid_id}"); return vid_id

def add_to_playlist(yt, playlist_id, video_id):
    yt.playlistItems().insert(part="snippet",
        body={"snippet": {"playlistId": playlist_id, "resourceId": {"kind": "youtube#video", "videoId": video_id}}}).execute()
    print(f"  added to playlist {playlist_id}")

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--dry-run", action="store_true"); args = ap.parse_args()
    if not VIDEO.exists(): sys.exit(f"Video not found: {VIDEO}")
    print(f"Video: {VIDEO.name} ({VIDEO.stat().st_size//1024//1024} MB)\nTitle: {TITLE}\nChannel: @NikBearBrown\nPlaylist: {PLAYLIST_NAME}")
    if args.dry_run: print("[dry-run] would upload now"); return
    publish_at = datetime.now(timezone.utc) + timedelta(minutes=15)
    print(f"Publish at: {publish_at.isoformat()}")
    yt = get_service()
    vid_id = upload_video(yt, VIDEO, publish_at)
    playlist_id = ensure_playlist(yt, PLAYLIST_NAME)
    add_to_playlist(yt, playlist_id, vid_id)
    print(f"\nDone. Video ID: {vid_id}\nStudio: https://studio.youtube.com/video/{vid_id}/edit")

if __name__ == "__main__":
    main()
