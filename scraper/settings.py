BOT_NAME = 'PPL_Spider'

SPIDER_MODULES = ['scraper.spiders']

ITEM_PIPELINES = {'scraper.pipelines.SpiderPipeline': 200,}

DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'MichaelSchulze',
    'password': '',
    'database': 'scrape'
}
