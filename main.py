#!/usr/bin/env python3
# coding: utf-8


#import time
#start = time.time()
from telethon import TelegramClient, sync
from datetime import datetime
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.tl.functions.account import UpdateProfileRequest
from config import api_id, api_hash
#print(f'Import time {time.time() - start}')

#connection_time = time.time()


client = TelegramClient("ananasiko", api_id, api_hash)
client.start()
#print(f'Connection time {time.time() - connection_time}')

#upload_time = time.time()

now = datetime.now().strftime('%H:%M')
client(DeletePhotosRequest(client.get_profile_photos('me')))
file = client.upload_file(f"time_images/{now}.jpg")
client(UploadProfilePhotoRequest(file))
client(UpdateProfileRequest(
first_name = f"{now}",
about = f"{now} "
))
#print(f'Upload time {time.time() - upload_time}')
#print(f'Total {time.time() - start}')

