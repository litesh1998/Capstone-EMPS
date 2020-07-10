import vlc, requests
from time import sleep

# emotion = 'happy'
# URL = f"http://localhost:5000/api/{emotion}"

objId = '5f081156182ca7df091d040d'
URL = f"http://localhost:5000/song/{objId}"


response = requests.get(URL)

player = vlc.MediaPlayer(URL)
print("Playing song", response.headers)

status = player.play()
sleep(3)

while player.is_playing():
        continue

print(status)
print("Done")
