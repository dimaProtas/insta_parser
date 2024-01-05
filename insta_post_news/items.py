# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst, Compose


def cleaner_photo(value):
    if value[:5] == 'lenta':
        return f'/home/dima_protasevich/Documents/PycharmProjects/insta_news/insta_post_news/images/{value}'
    return value


class InstaPostNewsItem(scrapy.Item):
    title = scrapy.Field(output_processor=TakeFirst())
    photo = scrapy.Field(output_processor=TakeFirst())
    link = scrapy.Field(output_processor=TakeFirst())
    news_text = scrapy.Field(output_processor=TakeFirst())
    source = scrapy.Field(output_processor=TakeFirst())
    path = scrapy.Field()
    link_photo = scrapy.Field()
    _id = scrapy.Field()

