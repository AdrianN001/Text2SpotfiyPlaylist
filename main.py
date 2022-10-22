import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


import os
from dotenv import load_dotenv
load_dotenv()

SAMPLE_TEXT = "My Name is walter".split(" ")


birdy_uri = 'spotify:artist:2q3GG88dVwuQPF4FmySr9I'
spotify = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials())

#response = spotify.search(q="walter", type='track')['tracks']['items']
current_pointer = 0

while current_pointer < len(SAMPLE_TEXT):
    current_inc = 0

    while True:
        response = spotify.search(q=SAMPLE_TEXT[current_pointer], type='track')[
            'tracks']['items']
        break

    print(SAMPLE_TEXT[current_pointer])

    current_pointer += 1
