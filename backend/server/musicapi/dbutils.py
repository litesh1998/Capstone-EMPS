import os
from musicapi.models import Song
from colorama import Fore

CWD = os.getcwd()
SONG_DIR = os.path.join(CWD, 'musicapi', 'static', 'songs')

def scanAndUpdateDB():
    dirs = os.listdir(SONG_DIR)
    for Dir in dirs:
        emotion = Dir.lower()
        emotionFolderContent = os.listdir(os.path.join(SONG_DIR, Dir))
        for song in emotionFolderContent:
            # print(song)
            song_doc = Song(
                    name= song,
                    path= os.path.join(SONG_DIR, emotion, song),
                    emotion= emotion
                )
            foundSong = Song.objects(name= song)[0]
            # print(foundSong)
            if foundSong:
                print(Fore.GREEN+f"{song} already in database.\nChecking for change in path..."+Fore.RESET)
                newPath = os.path.join(SONG_DIR, emotion, song)
                if newPath != foundSong.path:
                    foundSong.path = newPath
                    foundSong.save()
                    print(Fore.GREEN+f'Paths of song updated'+Fore.RESET)
                else:
                    print(Fore.GREEN+"No change in file path detected..."+Fore.RESET)
            else:
                song_doc = Song(
                    name= song,
                    path= os.path.join(SONG_DIR, emotion, song),
                    emotion= emotion
                )
                song_doc.save()
                print(Fore.GREEN+f"{song} added to database successfully!"+Fore.RESET)
