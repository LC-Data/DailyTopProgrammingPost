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
		for sel in response.xpath('//*[@data-rank="1"]/div[2]/p[1]/a')              ### USE data-rank="1", Reddit's dynamic xpathing changes daily, but you always want the top ranking post!!!
			items['postName'] = sel.xpath('text()').extract()                   ### assigning the extracted text to a "name" 
			items['postLink'] = sel.xpath('@href').extract()                    ### and the url to a "link" as we defined them
			###items['user'] = sel.xpath('xxx').extract()
			###items['upvotes'] = sel.xpath('xxx').extract()
			###items['commentSection'] = sel.xpath('xxx').extract()		    ### Will be adding a score, link to comment section
											    ### and the submitting user, credit where it is due.
			
			
			
			
		yield items  ### this is more just to make sure the spider is actually working and not hitting errors while traversing
		             ### provides immediate visual output of what was scraped
