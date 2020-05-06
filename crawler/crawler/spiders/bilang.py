# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy_splash import SplashRequest

from crawler.items import BilangItem


class BilangSpider(scrapy.Spider):
    name = 'bilang'
    allowed_domains = ['*']

    def __init__(self, file=None, *args, **kwargs):
        super(BilangSpider, self).__init__(*args, **kwargs)

        self.logger.debug(file)
        with open(file, "r") as f:
            self.urls = json.loads(f.read())

    def start_requests(self):
        for i, url in enumerate(self.urls):
            self.logger.debug(f"{i}/{len(self.urls)}")
            yield SplashRequest(url.get("th_url"), meta={
                "lang": "th",
                "url_id": i
                })
            yield SplashRequest(url.get("en_url"), meta={
                "lang": "en",
                "url_id": i
                })

    def parse(self, response):
        language = response.meta.get("lang")
        url_id = response.meta.get("url_id")
        url = response.url

        texts = response.css("*::text").extract()

        for i, text in enumerate(texts):
            stripped_text = text.strip()
            if stripped_text:
                yield BilangItem(
                    text_id=f"{language}-{url_id}-{i}",
                    text=stripped_text,
                    lang=language,
                    url=url,
                    url_id=url_id
                )
