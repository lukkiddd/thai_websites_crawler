# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BilangItem(scrapy.Item):
    text_id = scrapy.Field()
    text = scrapy.Field()
    lang = scrapy.Field()
    url = scrapy.Field()
    url_id = scrapy.Field()
