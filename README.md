# DailyTopProgrammingPost

Another Scrapy project!! 

I have only included the items.py file and my "spider".py file, as all others should be taken care of with "Scrapy startproject xyz" command.


Takes the top post from Reddit's /r/programming everyday, and exports the post's title and url to a JSON file, which can then be used for... anything

Unix-based systems can take advantage of cron to easily schedule the spider, and to export feed in to your file.

Will add a pipeline for non-cron users that will at least autoexport to a file upon running, or a more elegant solution if I can figure one out.


To output from shell command while executing spider: 

scrapy crawl rProgrammingSpider -o TopToday.json
