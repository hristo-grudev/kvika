import scrapy

from scrapy.loader import ItemLoader
from ..items import KvikaItem
from itemloaders.processors import TakeFirst


class KvikaSpider(scrapy.Spider):
	name = 'kvika'
	start_urls = ['https://www.kvika.is/frettir']
	page = 1

	def parse(self, response):
		post_links = response.xpath('//h3/a/@href')
		yield from response.follow_all(post_links, self.parse_post)

	def parse_post(self, response):
		title = response.xpath('//h1/text()').get()
		description = response.xpath('//div[@class="main-text"]/p/text()').getall()
		description = ' '.join(description)
		date = response.xpath('//div[@class="date"]/text()').get()

		item = ItemLoader(item=KvikaItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
