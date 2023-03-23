#!/usr/bin/env python3
# coding: utf-8

from telethon import TelegramClient, sync
from datetime import datetime
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.sessions import StringSession
from config import api_id, api_hash, phone, session
import os


# with TelegramClient(StringSession(session), api_id, api_hash) as client:
#     print(client.session.save()) # generate and save string session -- need for the first run


def main():
    now = datetime.now().strftime('%H:%M')
    pwd = os.path.dirname(os.path.realpath(__file__))
    with TelegramClient(StringSession(session), api_id=api_id, api_hash=api_hash).start() as client:
        client(DeletePhotosRequest(client.get_profile_photos('me')))
        file = client.upload_file(f'{pwd}/time_images/{now}.jpg')
        client(UploadProfilePhotoRequest(file))
        client(UpdateProfileRequest(
            first_name = f"{now}"
        ))


if __name__ == '__main__':
	main()
