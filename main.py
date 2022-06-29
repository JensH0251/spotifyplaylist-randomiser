import random


def spotifyrandomiser():
    with open("../spotify_playlist_randomiser/spotify_songs.txt") as SpotifySongsL:
        songlist = SpotifySongsL.readlines()
    newsonglist = ""
    bettersonglist = ""
    for songs in songlist:
        newsonglist = newsonglist + songs

    newplaylist = list(newsonglist.split("\n"))

    random.shuffle(newplaylist)

    for song in newplaylist:
        bettersonglist = bettersonglist + song + "\n"

    with open("../spotify_playlist_randomiser/randomised_spotify_playlist.txt", "w") as newspotifyplaylist:
        newspotifyplaylist.truncate(0)
        newspotifyplaylist.writelines(bettersonglist)


spotifyrandomiser()
