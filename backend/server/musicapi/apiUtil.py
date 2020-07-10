import os
from musicapi.models import Song
from bson.objectid import  ObjectId

#-------------------------------------------------------------------------
# Function to send music data in multiple packets to avoid buffering
def generate(path:str):
    '''
    Function to send music data in multiple packets to avoid buffering
    '''
    with open(path, "rb") as fwav:
        data = fwav.read(1024)
        while data:
            yield data
            data = fwav.read(1024)
 
#--------------------------------------------------------------------------
# Function to return Playlist
def getSongsList(emotion):
    '''
    Function to return Playlist based on given emotion
    '''
    pass

def getSongsListold(emotion):
    cwd = os.getcwd()
    loc = os.path.join(cwd, 'musicapi', 'static', 'songs', emotion)
    content = os.listdir(loc)
    songName = content[0]
    songPath = os.path.join(loc, songName)
    return [songPath]

#----------------------------------------------------------------------------
# Funtion to return absolute path to required song
def getSong(songid):
    '''
    Funtion to return absolute path to required song
    '''
    print(songid)
    foundSong = Song.objects.get(id=songid)
    if foundSong:
        return foundSong
    else:
        print("SONG NOT FOUND")
        return None