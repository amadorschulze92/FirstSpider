from scrapy import Selector
from scrapy.selector import HtmlXPathSelector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from scraper.items import SpiderPPL

class PPL_Spider(CrawlSpider):
    name = "PPL_Spider"
    allowed_domains = ["http://www.avanade.com/"]
    start_urls = ["http://www.avanade.com//en-us/about-avanade/leadership/executive-leadership",
    "http://www.avanade.com/en-us/about-avanade/leadership/regional-leadership",
    "http://www.avanade.com/en-us/about-avanade/leadership/board-of-directors"
    ]
    
    url_set = set([])
    
    def parse(self, response):
        selector = Selector(response)
        
        try:
            name = response.xpath('//div[@class="exp-detail-item"]//span/text()').extract()
        except:
            name = ''
        
        try:
            title = response.xpath('//h3[@class="exp-title exp-title-clicked"]/text()').extract()
        except:
            title = ''
            
        title = [x.replace("  ", "") for x in title]
        title = [x.replace('\r', '') for x in title]

        data_dict = {'url':response._url, 'title':title, 'name':name}
        for dd in [data_dict]:
            yield SpiderPPL(**dd)
           
        for url in selector.xpath('//a/@href').extract():
            if "/leadership/" not in url:
                continue
            if url in self.url_set:
                continue
            try:
                full_url = "http://www.avanade.com//en-us/about-avanade/leadership/%s" % url
                self.url_set.add(url)
                yield Request(full_url, callback=self.parse)
            except:
                print "Exception triggered by: %s" % full_url
                continue
