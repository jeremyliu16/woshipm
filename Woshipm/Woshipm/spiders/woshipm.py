#coding:utf-8
import requests
import logging
from scrapy.spider import CrawlSpider
from scrapy.selector import Selector
from Woshipm.items import WoshipmItem
from Woshipm.woshipm_type import PM_TYPES
from scrapy.http import Request
import re
import json
import random


class Spider(CrawlSpider):
    name = 'WoshipmSpider'
    host = 'http://www.woshipm.com/'
    start_urls = list(set(PM_TYPES))
    logging.getLogger("requests").setLevel(logging.WARNING
                                          )  # 将requests的日志级别设成WARNING
    logging.basicConfig(
        level=logging.DEBUG,
        format=
        '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        datefmt='%a, %d %b %Y %H:%M:%S',
        filename='cataline.log',
        filemode='w')

    # test = True
    def start_requests(self):
        for pm_type in self.start_urls:
            yield Request(url='http://www.woshipm.com/%s' % pm_type,
                          callback=self.parse_pm_key)

    def parse_pm_key(self, response):
        selector = Selector(response)
        logging.debug('request url:------>' + response.url)
        divs = selector.xpath('//div[@class="postlist-item"]')
        logging.info(divs)

    
        for div in divs:
            articleItem = WoshipmItem()
            articleItem['item_title'] = div.xpath('div[@class="content"]/h2[@class="post-title"]/a/@title').extract()[0]
            articleItem['item_url'] = div.xpath('div[@class="content"]/h2[@class="post-title"]/a/@href').extract()[0]

           
            des = div.xpath('div[@class="content"]/p[@class="des"]/text()').extract()
            if des:
                articleItem['item_des'] = des[0]
            else:
                articleItem['item_des'] = ''

            articleItem['item_auth_name'] = div.xpath('div[@class="content"]/div[@class="stream-list-meta"]/span[@class="author"]/a/text()').extract()[0]
            articleItem['item_auth_link'] = div.xpath('div[@class="content"]/div[@class="stream-list-meta"]/span[@class="author"]/a/@href').extract()[0]
            articleItem['item_date'] = div.xpath('div[@class="content"]/div[@class="stream-list-meta"]/time/text()').extract()[0]
            articleItem['item_eye'] = div.xpath('div[@class="content"]//span[@class="fa fa-eye"]/../text()').extract()[0]
            articleItem['item_stars'] = div.xpath('div[@class="content"]//span[@class="fa fa-star"]/../text()').extract()[0]
            articleItem['item_thumbs_up'] = div.xpath('div[@class="content"]//span[@class="fa fa-thumbs-up"]/../text()').extract()[0]
    
            logging.info(articleItem['item_title']+'|'+articleItem['item_url'] +'|'+articleItem['item_des'] +'|'+articleItem['item_auth_name']+'|'+articleItem['item_auth_link']+'|'+articleItem['item_date']+'|'+articleItem['item_eye']+'|'+articleItem['item_stars'] +'|'+articleItem['item_thumbs_up'] )
            yield articleItem


        url_next = selector.xpath('//a[@class="next page-numbers"]/@href').extract()
        logging.debug(url_next)
        if url_next:
            # if self.test:
            logging.debug(' next page:---------->' + url_next[0])
            yield Request(url=url_next[0],callback=self.parse_ph_key)
            # self.test = False


    # def parse_ph_info(self, response):
    #     phItem = WoshipmItem()
    #     selector = Selector(response)
    #     _ph_info = re.findall('flashvars_.*?=(.*?);\n', selector.extract())
    #     logging.debug('PH信息的JSON:')
    #     logging.debug(_ph_info)
    #     _ph_info_json = json.loads(_ph_info[0])
    #     duration = _ph_info_json.get('video_duration')
    #     phItem['video_duration'] = duration
    #     title = _ph_info_json.get('video_title')
    #     phItem['video_title'] = title
    #     image_url = _ph_info_json.get('image_url')
    #     phItem['image_url'] = image_url
    #     link_url = _ph_info_json.get('link_url')
    #     phItem['link_url'] = link_url
    #     quality_480p = _ph_info_json.get('quality_480p')
    #     phItem['quality_480p'] = quality_480p
    #     logging.info('duration:' + duration + ' title:' + title + ' image_url:'
    #                  + image_url + ' link_url:' + link_url)
    #     yield phItem
