from scrapy.spider import Spider
from scrapy.selector import Selector
import urlparse

from morrisons.items import Store, Region

class RegionSpider(Spider):
    name = "regions"
    start_urls = [
        "http://your.morrisons.com/Store-finder/Store-Index/",
    ]

    def parse(self, response):
        sel = Selector(response)
        regions = sel.css(".region")
        items = []
        for r in regions:
            more = r.css("span > a::attr(href)")
            if len(more) == 0:
                break;

            item = Region()
            item["name"] = r.css("h3::text").extract()[0]

            qs = r.css("span > a::attr(href)").extract()[0]
            item["url"] = response.url + qs
            items.append(item)

        return items
