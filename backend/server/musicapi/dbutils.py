import os
from musicapi.models import Song
from colorama import Fore
import random

CWD = os.getcwd()
SONG_DIR = os.path.join(CWD, 'musicapi', 'static', 'songs')


def scanAndUpdateDB():
    add = update = 0
    songFolderContent = os.listdir(SONG_DIR)
    for song in songFolderContent:
        # print(song)
        # song_doc = Song(
        #         name= song,
        #         path= os.path.join(SONG_DIR, emotion, song),
        #         emotion= emotion
        #     )
        foundSong = Song.objects(name=song)
        # print(foundSong)
        if foundSong:
            # print(Fore.CYAN + f"{song} already in database.\nChecking for change in path..." + Fore.RESET)
            newPath = os.path.join(SONG_DIR, song)
            for FoundSong in foundSong:
                if newPath != FoundSong.path:
                    FoundSong.path = newPath
                    FoundSong.save()
                    # print(Fore.LIGHTCYAN_EX + f'Paths of song updated' + Fore.RESET)
                    update += 1
                # else:
                #     print(Fore.GREEN + "No change in file path detected..." + Fore.RESET)
        else:
            emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}
            emotion = emotion_dict[random.randint(0,6)] # this is supposed to come from music classifier
            song_doc = Song(
                name=song,
                path=os.path.join(SONG_DIR, song),
                emotion=emotion.lower() 
            )
            print(f'{song} found with emotion: {emotion}' )
            song_doc.save()
            # print(Fore.LIGHTCYAN_EX + f"{song} added to database successfully!" + Fore.RESET)
            add += 1
    print(Fore.GREEN + f"Total {len(songFolderContent)} songs found" + Fore.RESET)
    print(Fore.MAGENTA + f"Total {update} songs updated" + Fore.RESET)
    print(Fore.MAGENTA + f"Total {add} new songs added" + Fore.RESET)
