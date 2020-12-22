import vlc, requests, json
from time import sleep

def callfunc(emotion='happy'):
    # emotion = 'happy'
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

def play_song(songid):
    song = requests.get(f"http://localhost:5000/song/{songid}")
    try:
        print("Debug: " , song.headers)
        data = song.headers
        player = vlc.MediaPlayer(song.headers.get("path"))
        player.play()
        sleep(10)
        player.stop()
    except Exception as e:
        print(e)
    
