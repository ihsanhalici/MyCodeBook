# Scrapy settings for orumcek project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'orumcek'
BOT_VERSION = '1.0'
ITEM_PIPELINES = ['orumcek.pipelines.JsonWriterPipeline',]
SPIDER_MODULES = ['orumcek.spiders']
NEWSPIDER_MODULE = 'orumcek.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)


