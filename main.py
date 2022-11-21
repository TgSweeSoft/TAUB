# GitHub: TgSweeSoft
import random
from time import sleep
import pyrogram
# Слито в @SweeSoft
from pyrogram import Client, filters, sync, idle
from pyrogram.raw import functions


import os
import time
from time import strftime
# Слито в @SweeSoft
import datetime
import colorama
import asyncio

os.system("clear")
# Слито в @SweeSoft
app = Client('TAUB', api_id=1016382, api_hash='c27834e5683d50a9bacf835a95ec4763')

app.start()
app.stop()# Слито в @SweeSoft

os.system("clear")

print("script started\nGo to the Telegram and write .help")
# Слито в @SweeSoft
@app.on_message(filters.command("start", prefixes=".") & filters.me)
async def start(app, message):
	g1 = strftime("%H_%M")# Слито в @SweeSoft
	await app.send_message(message.chat.id, "Скрипт успешно запущен✅")
	await app.set_profile_photo(photo="src/" + g1 + ".png")
	while True:
		h1 = strftime("%S")
		g1 = strftime("%H_%M")# Слито в @SweeSoft
		if h1 == '00':
			photos = [p async for p in app.get_chat_photos("me")]
			await app.delete_profile_photos(photos[0].file_id)
			sleep(1)# Слито в @SweeSoft
			await app.set_profile_photo(photo="src/" + g1 + ".png")
			
			
 # Слито в @SweeSoft
        
app.run()
