from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from insta_post_news import settings
from insta_post_news.spiders.lenta import LentaSpider

if __name__ == '__main__':

    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    # process.crawl(AvitoruSpider, query='Volkswagen', region='moskva')
    process.crawl(LentaSpider)

    process.start()
