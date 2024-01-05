# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from pymongo import MongoClient
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from transliterate import translit


class InstaPostNewsPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.news

    def process_item(self, item, spider):
        collection = self.mongo_base[spider.name]
        item['path'] = '/home/dima_protasevich/Documents/PycharmProjects/insta_news/insta_post_news/images/' + item['photo'][0]['path']
        item['link_photo'] = item['photo'][0]['url']
        collection.insert_one(item)
        return item


class NewsPhotosPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['photo']:
            try:
                cyrillic_text = item['title'].split(' ')[:2]
                res = ('_'.join(cyrillic_text))
                latin_text = translit(res, 'ru', reversed=True)
                yield scrapy.Request(item['photo'], meta={'name': info.spider.name, 'file':   f'{latin_text}'})
            except Exception as e:
                print(e)

    def item_completed(self, results, item, info):
        item['photo'] = [itm for ok, itm in results if ok]
        return item

    def file_path(self, request, response=None, info=None, *, item=None):
        return f"{request.meta['name']}/{request.meta['file']}.jpg"
        # return f"{item['name'][:10]}/" + os.path.basename(urlparse(request.url).path) # Вариант сохранения №2