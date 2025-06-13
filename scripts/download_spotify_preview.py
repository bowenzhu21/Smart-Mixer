import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests

# Set your credentials (replace these!)
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id="",
    client_secret=""
))

# Example track (you can swap in any Spotify link)
track_url = "https://open.spotify.com/track/4cOdK2wGLETKBW3PvgPWqT"  # Rick Astley – Never Gonna Give You Up
track = sp.track(track_url)
preview_url = track['preview_url']

# Download the preview if available
if preview_url:
    r = requests.get(preview_url)
    with open("audio/lose_yourself_preview.mp3", "wb") as f:
        f.write(r.content)
    print("✅ Preview downloaded")
else:
    print("❌ No preview available for this track")
