import vk_api
from vk_api import audio
import requests
from time import time
import os

REQUEST_STATUS_CODE = 200
name_dir = 'music_vk'
path = r'./audio' + name_dir 
login = ''  # Номер телефона
password = ''  # Пароль
my_id = ''

if not os.path.exists(path):
    os.makedirs(path)

vk_session = vk_api.VkApi(login=login, password=password)
vk_session.auth()
vk = vk_session.get_api()  # Теперь можно обращаться к методам API как к обычным 
                                        # классам
vk_audio = audio.VkAudio(vk_session)  # Получаем доступ к audio

os.chdir(path)

time_start = time()
for i in vk_audio.get(owner_id=my_id):
    try:
        r = requests.get(i["url"])
        if r.status_code == REQUEST_STATUS_CODE:
            with open(i["artist"] + '_' + i["title"] + '.mp3', 'wb') as output_file:
                output_file.write(r.content)
    except OSError:
        print(i["artist"] + '_' + i["title"])
time_finish = time()
print("Time seconds:", time_finish - time_start)
