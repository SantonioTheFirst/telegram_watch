#!/usr/bin/env python3
# coding: utf-8

from telethon import TelegramClient, sync
from datetime import datetime
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.sessions import StringSession
from config import api_id, api_hash, phone, session
import os

print('import ok')

# with TelegramClient(StringSession(session), api_id, api_hash) as client:
#     print(client.session.save()) # generate and save string session -- need for the first run


def main():
    now = datetime.now().strftime('%H:%M')
    pwd = os.path.dirname(os.path.realpath(__file__))
    print(pwd)
    print('now ok')

    with TelegramClient(StringSession(session), api_id=api_id, api_hash=api_hash).start() as client:
        print('session ok')
        client(DeletePhotosRequest(client.get_profile_photos('me')))
        print('delete ok')
        file = client.upload_file(f'{pwd}/time_images/{now}.jpg')
        print(type(file))
        client(UploadProfilePhotoRequest(file))
        print('update ok')
        client(UpdateProfileRequest(
            first_name = f"{now}",
            about = f"{now} "
        ))


main()
print('end')