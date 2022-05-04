import requests
import json
import wget
import os
import time
import telegram
from dotenv import load_dotenv
load_dotenv()

TELEGRAM_BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
TELEGRAM_CHAT_ID = os.environ['TELEGRAM_CHAT_ID']
bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

def post_image():
    dogapi_url = "https://dog.ceo/api/breed/"
    dog_breed = "pug"
    get_image_url = dogapi_url + dog_breed + "/" + "images/random"
    get_image_url_request = requests.get(get_image_url).json()['message']
    download_image = wget.download(get_image_url_request, "doge.jpg")
    bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=open("doge.jpg", 'rb'))
    os.remove("doge.jpg")

while True:
    post_image()
    time.sleep(43200)
