from scrapy.item import Item, Field

class SpiderPPL(Item):
    """container (dictionary-like object) for scraped data"""
    url = Field()
    title = Field()
    name = Field()