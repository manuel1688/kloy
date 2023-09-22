from cfg import CLIENT_ID, CLIENT_SECRET, SPOTIPY_REDIRECT_URI, DB_CONNSTR
import spotipy
from spotipy.oauth2 import SpotifyOAuth


scope = "user-read-recently-played"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope))


print(CLIENT_SECRET, CLIENT_ID, SPOTIPY_REDIRECT_URI, DB_CONNSTR)