# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import re

from scrapy.exceptions import DropItem


class DuplicatesTextPipeline(object):

    def __init__(self):
        self.texts_seen = set()

    def process_item(self, item, _spider):
        if item['text'] in self.texts_seen:
            raise DropItem("Duplicate item found: %s" % item['text'])
        else:
            self.texts_seen.add(item['text'])
            return item


class CorrectLanguagePipeline(object):

    @staticmethod
    def is_correct_language(text, language):
        if language == "th":
            return re.search("[ก-๙]+", text)
        elif language == "en":
            return re.search("[a-zA-Z]+", text)
        else:
            return False

    def process_item(self, item, _spider):
        if not self.is_correct_language(item['text'], item['lang']):
            raise DropItem(f"Incorrect language found: {item['text_id']}")
        else:
            return item


class RemoveScriptTextPipeline(object):

    @staticmethod
    def is_script(text):
        return re.search("(__NEXT_DATA__|function|{|var|;)", text)

    def process_item(self, item, _spider):
        if self.is_script(item['text']):
            raise DropItem(f"Script found: {item['text_id']}")
        else:
            return item
