import vlc, requests
from time import sleep

emotion = 'happy'

URL = f"http://localhost:5000/api/{emotion}"

response = requests.get(URL)

player = vlc.MediaPlayer(URL)
print("Playing song", response.headers['name'])

status = player.play()
sleep(3)

desc = player.get_full_title_descriptions()
for x in desc:
    print(x)

while player.is_playing():
        continue

print(status)
print("Done")
