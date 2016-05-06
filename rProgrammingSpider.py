# -*- coding: utf-8 -*-
from scrapy.spider import Spider
from scrapy.selector import Selector
from topprogramming.items import *


class FirstSpider(scrapy.Spider):
    name = "rProgrammingSpider"
    allowed_domains = ["www.reddit.com"]
    start_urls = ['https://www.reddit.com/r/programming/top/?sort=top&t=day']   ### sorts reddit's top results by most recent 24-hrs
                                                                                ### Suppose I could change this to a weekly/monthly 
                                                                                ### format for potentially better collection of posts
    def parse(self, response):
		items = topPostProgramming()
		for sel in response.xpath('//*[@id="thing_t3_4i052a"]/div[2]/p[1]/a'):      ### GETTING THIS XPATH IS HARDER THAN IT LOOKS
			items['postName'] = sel.xpath('text()').extract()                         ### assigning the extracted text to a "name" 
			items['postLink'] = sel.xpath('@href').extract()                          ### and the url to a "link" as we defined them

		yield items  ### this is more just to make sure the spider is actually working and not hitting errors while traversing
		             ### provides immediate visual output of what was scraped
