import logging
import os
import time
from pathlib import Path

from instagrapi import Client
from instagrapi.story import StoryBuilder
from instagrapi.types import Usertag, Location
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag
from pymongo import MongoClient
from pprint import pprint

# proxy_url_with_auth = '45.146.88.162:8000'
# os.environ["HTTPS_PROXY"] = proxy_url_with_auth
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

client = MongoClient('localhost', 27017)
db = client['news']
lenta = db.lenta


def serch_all_vacancy():
    list_search = []
    for i in lenta.find({}, {'_id': False}).sort('_id', -1).limit(10):
        list_search.append(i)
        pprint(i)
    print(f'Всего вакансий: {len(list_search)}')


def upload_post():
    bot = Client()
    bot.logger.setLevel(logging.INFO)
    bot.set_proxy('45.146.88.162:8000')
    bot.login(username='voyage_and_more', password='klassadidas0147')

    # for i in lenta.find({}, {'_id': False}).sort('_id', -1).limit(10):
    #     image = i["path"]
    #     print(image, '\n', type(image))
    #     # clean_up(image)
    #     caption = f'{i["title"]}\n\n{i["news_text"][:1200]}\n\nИсточник: {i["source"]}\nСсылка: {i["link"]}'
    #     caption_story = f'{i["title"][:30]}\nИсточник: {i["source"]}'
    #     bot.photo_upload(
    #         path=image,
    #         caption=caption,
    #         )
    # example = bot.user_info_by_username('dima_protasevich92')

    bot.photo_upload_to_story(path=Path('/home/dima_protasevich/Documents/PycharmProjects/insta_news/insta_post_news/images/lenta/Gubernator_Belgorodskoj.jpg')
          # , upload_id="upload_first_one"
        # caption='caption_story',
        # mentions=[StoryMention(user=example, x=0.49892962, y=0.703125, width=0.8333333333333334, height=0.125)]
        # links=[i['source']],
    )


        # time.sleep(10)
    bot.logout()


def load_post():
    bot = Client()
    bot.logger.setLevel(logging.INFO)
    bot.set_proxy('45.146.88.162:8000')
    bot.login(username='voyage_and_more', password='klassadidas0147')

    media = bot.media_pk_from_url('https://www.instagram.com/p/CsgoxJnIB8S/')
    print(media)

    bot.photo_download(media_pk=int(media), folder=Path('/home/dima_protasevich/Documents/PycharmProjects/insta_news/insta_post_news/pic'))

    bot.logout()

if __name__ == '__main__':
    upload_post()
    # load_post()


    # media_pk = bot.media_pk_from_url('https://www.instagram.com/p/Cuz7pyGI-VY/')
    # media_path = bot.video_download(media_pk)
    # example = bot.user_info_by_username('dima_protasevich92')
    # hashtag = bot.hashtag_info('news')
    # web_uri = 'https://github.com/subzeroid/instagrapi'
    # bot.video_upload_to_story(
    #     media_path,
    #     "Credits @example",
    #     mentions=[StoryMention(user=example, x=0.49892962, y=0.703125, width=0.8333333333333334, height=0.125)],
    #     links=[StoryLink(webUri=web_uri)],
    #     hashtags=[StoryHashtag(hashtag=hashtag, x=0.23, y=0.32, width=0.5, height=0.22)],
    #     medias=[StoryMedia(media_pk=str(media_pk), x=0.5, y=0.5, width=0.6, height=0.8)],
    # )

    # buildout = StoryBuilder(image).photo()
    # bot.video_upload_to_story(buildout.path)