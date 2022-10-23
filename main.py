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


def doesSongExist(song_name: str, sp: spotipy.Spotify) -> bool:

    # Check for both ...
    if song_name == "" or song_name == " ":
        return False
    # Hungarian market
    for item in sp.search(q=song_name, type='track', limit=40, market="HU")['tracks']['items']:
        print(item['name'])
        if filter_name(item['name']) == filter_name(song_name):
            return True
    # and american market
    for item in sp.search(q=song_name, type='track', limit=40, market="US")['tracks']['items']:
        print(item['name'])
        if filter_name(item['name']) == filter_name(song_name):
            return True
    return False


def main():

    client = spotipy.Spotify(
        client_credentials_manager=SpotifyClientCredentials())

    pointer = 0
    offset = 0
    founds = []

    while pointer < SAMPLE_TEXT.__len__():

        if doesSongExist("".join(SAMPLE_TEXT[pointer:offset]), client):
            local_founds = [" ".join(SAMPLE_TEXT[pointer:offset])]
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
                        local_founds.append(
                            " ".join(SAMPLE_TEXT[pointer:offset + x]))
                        local_max = x
                except IndexError:
                    break
            # founds.append("".join(SAMPLE_TEXT[pointer:offset]))
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
    print(founds)

    #print(doesSongExist("White", client))


if __name__ == "__main__":
    main()
