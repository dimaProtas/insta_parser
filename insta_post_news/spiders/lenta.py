import scrapy
from scrapy.http import HtmlResponse
from insta_post_news.items import InstaPostNewsItem
from scrapy.loader import ItemLoader


class LentaSpider(scrapy.Spider):
    name = "lenta"
    allowed_domains = ["lenta.ru"]
    start_urls = ["https://lenta.ru"]

    def parse(self, response: HtmlResponse):
        links_news = response.xpath("//a[contains(@class, 'card-mini')]/@href | //a[contains(@class, 'card-big')]/@href").extract()
        for news in links_news:
            yield response.follow(news, callback=self.news_parse)

    def news_parse(self, response: HtmlResponse):
        title = response.xpath("//span[@class='topic-body__title']//text()").extract_first()
        # loader.add_xpath('photo', "//img[@class='picture__image']/@src")
        source = self.name
        res = response.xpath("//div[@class='topic-body__content']//text()").extract()
        news_text = ' '.join(res)
        link = response.url
        photo_link = response.xpath("//a[@class='topic-body__title-image-zoom']/@href").extract_first()
        yield response.follow(photo_link, callback=self.photo_save, cb_kwargs={'title': title, 'source': source,
                                                                               'news_text': news_text, 'link': link},)

    def photo_save(self, response: HtmlResponse, title, news_text, source, link):
        loader = ItemLoader(item=InstaPostNewsItem(), response=response)
        loader.add_xpath('photo', "//img[@class='comments-page__title-image']/@src")
        loader.add_value('title', title)
        loader.add_value('news_text', news_text)
        loader.add_value('source', source)
        loader.add_value('link', link)
        yield loader.load_item()
