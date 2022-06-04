import requests
import json
import wget
import os
import time
import telegram
import random
from simpledemotivators import Demotivator
from dotenv import load_dotenv
load_dotenv()

TELEGRAM_BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
TELEGRAM_CHAT_ID = os.environ['TELEGRAM_CHAT_ID']
bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)


def get_image():
    dogapi_url = "https://dog.ceo/api/breed/"
    dog_breed = "pug"
    get_image_url = dogapi_url + dog_breed + "/" + "images/random"
    get_image_url_request = requests.get(get_image_url).json()['message']
    download_image = wget.download(get_image_url_request, "doge.jpg")

def post_image():
    bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=open("demo_doge.jpg", 'rb'))

def auf_phrase():
    data = requests.get('https://raw.githubusercontent.com/Infqq/auf_gen/main/phrases.txt').text.splitlines()
    phrase = random.choice(data)
    return(phrase)

def create_demotivator():
    phrase = auf_phrase()
    print(phrase)
    dem = Demotivator(phrase) 
    dem.create('doge.jpg', result_filename='demo_doge.jpg')
    os.remove("doge.jpg")

def main():
    while True:
        get_image()
        create_demotivator()
        post_image()
        os.remove("demo_doge.jpg")
        time.sleep(43200)

if __name__ == "__main__":
    main()
