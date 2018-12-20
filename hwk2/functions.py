import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0,parent_dir)
from hwk1 import song

def genre():
    """
    return genre of the song
    """
    return song.genre

def artist():
    """
    return the name of the artist
    """
    return song.artist

def year():
    """
    return the year of the release
    """
    return song.release_year

def is_available(platform):
    """
    is the song available on 'x' platform?
    """
    return platform in song.availability

print("Genre: {}".format(genre()))
print("Artist: {}".format(artist()))
print("Year: {}".format(year()))
platform = "Spotify"
is_song_in = "{}".format("Yes" if is_available(platform) else "No")
print("Is '{}' available in {}? '{}'".format(song.title,
                                             platform,
                                             is_song_in))
