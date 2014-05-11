# Scrapy settings for morrisons project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'morrisons'

SPIDER_MODULES = ['morrisons.spiders']
NEWSPIDER_MODULE = 'morrisons.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'shopcrawl (+http://www.yourdomain.com)'

HTTPCACHE_ENABLED = True
