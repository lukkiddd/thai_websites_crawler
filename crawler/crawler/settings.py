# -*- coding: utf-8 -*-

BOT_NAME = 'crawler'
SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'
ROBOTSTXT_OBEY = True
CONCURRENT_REQUESTS = 64
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}
ITEM_PIPELINES = {
    'crawler.pipelines.RemoveScriptTextPipeline': 100,
    'crawler.pipelines.CorrectLanguagePipeline': 200,
    'crawler.pipelines.DuplicatesTextPipeline': 300,
}
LOG_ENABLED = True

# Splash Config
SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}
SPLASH_URL = 'http://127.0.0.1:8050'
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'