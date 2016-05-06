# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class topPostProgramming(scrapy.Item):
	postName = scrapy.Field()     ### we are only scraping two fields here
	postLink = scrapy.Field()     ### just the post name, and url. Could consider scraping username + upvotes.
