import vlc, requests, json
from time import sleep
# from arduino import *
from Worker import Worker
from colorama import Fore

class client():
    def __init__(self):
        pass

    def callfunc(self, emotion='happy'):
        emotion = emotion.lower()
        URL = f"http://localhost:5000/api/{emotion}"
        # objId = '5f081156182ca7df091d040d'
        # URL = f"http://localhost:5000/song/{objId}"
        response = requests.get(URL)
        data = json.loads(response.content)
        #print("Playlist is (content):\n", data)
        #print("Playlist is (headers):\n", response.headers)
        playlist = data['songs']
        # print("Playlist is:")
        # for song in playlist:
        #         print(f"{song['id']}:\t{song['name']}\t|\t{song['emotion']} ")
        ##TO PLAY THE SONG IN PLAYLIST, UNCOMMENT THE BELOW BLOCK. ALL THE SONGS WILL PLAY IN SEQUENCE
        # for song in playlist:
        #          player = vlc.MediaPlayer(f"http://localhost:5000/song/{song['id']}")
        #          print(f"Playing song {song['name']}")
        #          print(f"It is a {song['emotion']} song")
        #          status = player.play()
        #          sleep(3)
        #          while player.is_playing():
        #                 continue
        # print(status)
        # print("Done")
        return(playlist)

    def play_song(self, songid, playlist):
        song = requests.get(f"http://localhost:5000/song/{songid}")
        try:
            print("Debug: " , song.headers)
            data = song.headers
            player = vlc.MediaPlayer(song.headers.get("path"))
            # wplay = Worker(player.play)
            player.audio_set_volume(100)
            player.play()
            # print("PLaying in background")
            sleep(5)
            # print("PLaying in background after sleep")
            # player.stop()
        #     newPlaylist = enumerate(playlist)
        #     idx = {}
        #     for index, song in newPlaylist:
        #         idx[song["id"]] = index
        #     print(player.is_playing() == 1)
        #     while player.is_playing():
        #         # print(Fore.GREEN + "in loop" + Fore.RESET)
        #         event = getGesture()
        #         setGesture()
        #         print(event)
        #         # for event in g:
        #         if event == None:
        #             continue
        #         elif event == "UP":
        #             print(Fore.CYAN + "Volume up" + Fore.RESET)
        #             vol = player.audio_get_volume()
        #             player.audio_set_volume(20)
        #         elif event == "DOWN":
        #             vol = player.audio_get_volume()
        #             print(Fore.MAGENTA + "Volume down" + Fore.RESET)
        #             player.audio_set_volume(100)
        #         elif event == "LEFT":
        #             player.stop()
        #             print(Fore.YELLOW + "Changing Song" + Fore.RESET)
        #             prevsongID = playlist[max(idx[songid] - 1, 0)]["id"]
        #             self.play_song(prevsongID, playlist)
        #         elif event == "RIGHT":
        #             player.stop()
        #             print(Fore.YELLOW + "Changing Song" + Fore.RESET)
        #             nextsongID = playlist[min(idx[songid] + 1, len(playlist)-1)]["id"]
        #             self.play_song(nextsongID, playlist)

        # except Exception as e:
        #     print(e)
    
