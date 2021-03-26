BOT_NAME = 'timberlandbancorpq4ir'

SPIDER_MODULES = ['timberlandbancorpq4ir.spiders']
NEWSPIDER_MODULE = 'timberlandbancorpq4ir.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'timberlandbancorpq4ir.pipelines.Timberlandbancorpq4irPipeline': 100,

}

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
