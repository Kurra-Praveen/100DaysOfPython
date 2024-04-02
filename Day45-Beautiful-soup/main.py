import spotipy
from bs4 import BeautifulSoup
import requests
from spotipy import SpotifyOAuth

CLIENT_ID = "ae93704a043d4705bf1d713bee3bc241"
CLIENT_SECRET = "901593eef75c4c5db0e4d33a682d97a5"
RedirectUti = "http://127.0.0.1:8080"
x = spotipy.Spotify(
    auth_manager=SpotifyOAuth(scope="playlist-modify-private", redirect_uri=RedirectUti, client_id=CLIENT_ID,
                              client_secret=CLIENT_SECRET, show_dialog=True, cache_path="token.txt"))
user_id = x.current_user()["id"]
print(user_id)
date = input("enter the date you want to go..\n MAKE SURE YOU ENTER IN YYYY-MM-DD")
url = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(url)
data = response.text

soap = BeautifulSoup(data, "html.parser")
top_songs = soap.find_all(name="h3",
                          class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")

songs_list = [song.get_text().strip() for song in top_songs]
year = date.split("-")[0]
song_uris = []
for each_song in songs_list:
    result = x.search(q=f"track:{each_song} year:{year}", type='track')
    try:
        uri = result['tracks']["items"][0]['uri']
    except IndexError:
        print(f" '{each_song}' song  not found")
    else:
        song_uris.append(uri)
# creating playlist
playlist = x.user_playlist_create(user=user_id, name=f" top 100 song on {date}")

# Adding songs to that playlist

x.playlist_add_items(playlist_id=playlist['id'], items=song_uris)


