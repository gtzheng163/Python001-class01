# -*- coding: utf-8 -*-
import scrapy
from maoyanmovie.items import MaoyanmovieItem
from scrapy.selector import Selector


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）。
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)
        
    def parse(self, response):
        urls = response.xpath('//div[@class="channel-detail movie-item-title"]/a/@href')[:10].getall()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse1)

    # 解析函数
    
    def parse1(self, response):
        details = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        for i in range(10):
            detail = details[i]
            item = MaoyanmovieItem()
            title = detail.xpath('./div[1]/span[1]/text()').extract()[0]
            movie_type = detail.xpath('./div[2]/text()[2]').extract()[0].strip()
            release_date = detail.xpath('./div[4]/text()[2]').extract()[0].strip()
            item['title'] = title
            item['movie_type'] = movie_type
            item['release_date'] = release_date
            yield item
