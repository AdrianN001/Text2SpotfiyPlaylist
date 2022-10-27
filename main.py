import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import string

import os
from dotenv import load_dotenv
load_dotenv()

#SAMPLE_TEXT = "My Name is walter".split(" ")
SAMPLE_TEXT = ["My", "Name", "is", "Walter", "Hartwell", "White", "I", "Live",
               "At", "308", "Negra", "Arroyo", "Lane", "Albuquerque", "New Mexico", "87104"]


def filter_name(name): return "".join(
    [x for x in name if x in string.ascii_letters or x == " "])


def create_and_fill_playlist(songs: list, name: str) -> None:
    filtered_song = [url.split("/")[0] for title, url in songs]


def doesSongExist(song_name: str, sp: spotipy.Spotify) -> tuple | None:

    # Check for both ...
    if song_name == "" or song_name == " ":
        return
    # Hungarian market
    for item in sp.search(q=song_name, type='track', limit=40, market="HU")['tracks']['items']:
        print(item['name'])
        if filter_name(item['name']) == filter_name(song_name):
            return item['name'], item["external_urls"]["spotify"]

    # and american market
    for item in sp.search(q=song_name, type='track', limit=40, market="US")['tracks']['items']:
        print(item['name'])
        if filter_name(item['name']) == filter_name(song_name):
            return item['name'], item["external_urls"]["spotify"]
    # and UK market
    for item in sp.search(q=song_name, type='track', limit=40, market="GB")['tracks']['items']:
        print(item['name'])
        if filter_name(item['name']) == filter_name(song_name):
            return item['name'], item["external_urls"]["spotify"]


def main():

    client = spotipy.Spotify(
        client_credentials_manager=SpotifyClientCredentials())

    pointer = 0
    offset = 0
    founds = []

    while pointer < SAMPLE_TEXT.__len__():

        if is_exist := (doesSongExist("".join(SAMPLE_TEXT[pointer:offset]), client)):
            local_founds = [is_exist]
            local_max = -1
            for x in range(1, 4):
                try:
                    print(
                        f"ASDASDDSSDD : { ' '.join(SAMPLE_TEXT[pointer:offset + x])}")
                    found = doesSongExist(
                        ' '.join(SAMPLE_TEXT[pointer:offset + x]), client)
                    print(found)
                    if found:
                        print("Találat")
                        local_founds.append(found)
                        local_max = x
                except IndexError:
                    break

            founds.append(local_founds[-1])
            pointer = offset + (local_max if local_max != -1 else 0)
        else:
            offset += 1

        if offset > 20:
            pointer += 1
            offset = 0
        print(f"{pointer = }")
        print(f"{offset = }")
        print("_______")

    # Create a txt file for the URLs
    with open("Links.txt", "w") as file:

        for title, url in founds:
            file.write(url + "\n")

    #print(doesSongExist("White", client))


if __name__ == "__main__":
    main()
