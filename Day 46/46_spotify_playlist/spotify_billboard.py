from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Week of the Top 100's ? (YYYY-MM-DD)\n")

my_request = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}")
data = my_request.text
soup = BeautifulSoup(data, "html.parser")
artists = soup.find_all(name="span", class_="chart-element__information__artist text--truncate color--secondary")
songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
artist_list = [artist.getText() for artist in artists]
song_list = [song.getText() for song in songs]
artist_song = [f"{artist_list[i]} - {song_list[i]}" for i in range(len(artist_list))]

CLIENT_ID = YOUR CLIENT ID
SECRET_KEY = YOUR CLIENT KEY
sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="http://example.com",
            client_id=CLIENT_ID,
            client_secret=SECRET_KEY,
            show_dialog=True,
            cache_path="token.txt"
    )
)
url_list = []
for item in artist_song:
    try:
        result = sp.search(q=item, limit=1)
        url = result["tracks"]["items"][0]["external_urls"]["spotify"]
    except:
        pass
    else:
        url_list.append(result["tracks"]["items"][0]["external_urls"]["spotify"])

user_id = sp.current_user()["id"]
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100's using python", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=url_list)