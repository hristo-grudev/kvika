BOT_NAME = 'kvika'

SPIDER_MODULES = ['kvika.spiders']
NEWSPIDER_MODULE = 'kvika.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'kvika.pipelines.KvikaPipeline': 100,

}