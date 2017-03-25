# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request, Spider


class ZhihuspiderSpider(Spider):
    name = "zhihuSpider"
    allowed_domains = ["www.zhihu.com"]
    start_urls = ['http://www.zhihu.com/']

    def start_requests(self):
        url = ''

    def parse(self, response):
        pass
