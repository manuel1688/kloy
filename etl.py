from config import CLIENT_ID, CLIENT_SECRET, SPOTIPY_REDIRECT_URI
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime, timedelta


scope = "user-read-recently-played"

spotify_api = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope))

def extraer(date, limit=50):
    """Obtiene un listado de canciones escuchadas en una fecha determinada

    Args:
        timestamp (unix - milliseconds): fecha a partir de la cual se obtendrán los datos
        limit (int): el limite de registros a obtener es de 50
    """
    ds = int(date.timestamp()) * 1000
    return spotify_api.current_user_recently_played(limit=limit, after=ds)

if __name__ == "__main__":
    # Fecha a partir de la cual se obtendrán los datos
    fecha_apartir = datetime.today() - timedelta(days=10)

    data= extraer(fecha_apartir)
    print(f"Datos extraidos {len(data['items'])} registros")
