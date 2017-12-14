# -*- coding: utf-8 -*-
from scrapy.spiders import Spider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from POCO_GIRL.items import PocoGirlItem
import scrapy
import threading


class girlSpiders(Spider):
    name = "PocoGirlSpiders"
    start_urls = ["http://my.poco.cn/lastphoto_v2-htx-id-6031616-user_id-55629005-p-0.xhtml"]  # 学姐

    def parse(self, response):
        selector = Selector(response)
        item = PocoGirlItem()
        item['name'] = selector.xpath('//h1[@class = "mt10"]/text()').extract_first(default="N/A")
        item['url'] = response.url
        item['imgUrls'] = selector.xpath('//div[@class="photo"]/a/img/@src').extract()

        rightUrl = selector.xpath('//div[@class="poco_page_right"]/a/@herf').extract_first(default="N/A")
