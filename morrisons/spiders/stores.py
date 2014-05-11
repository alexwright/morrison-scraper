from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
import urlparse

from morrisons.items import Store, Region

class StoreSpider(Spider):
    name = "stores"
    start_urls = [
        "http://your.morrisons.com/Store-finder/Store-Index/",
    ]

    def start_requests(self):
        return [Request(url, callback=self.parse_index) for url in self.start_urls]

    def parse_index(self, response):
        sel = Selector(response)
        regions = sel.css(".region")
        items = []
        for r in regions:
            more = r.css("span > a::attr(href)")
            if len(more) == 0:
                break;

            qs = r.css("span > a::attr(href)").extract()[0]
            url = response.url + qs
            yield Request(url, callback=self.parse_region)

    def parse_region(self, response):
        sel = Selector(response)
        region = sel.css(".region")
        name = region.css("h3::text").extract()[0]
        stores = region.css("ul > li > strong")
        for store in stores:
            name = store.css("a::text").extract()[0]
            href = store.css("a::attr(href)").extract()[0]
            url = urlparse.urljoin(response.url, href)
            yield Request(url,
                          callback=self.parse_store,
                          meta={"store_name": name})

    def parse_store(self, response):
        sel = Selector(response)
        address = sel.css(".storeAddress p:not(.telephone)::text").extract()
        phone_number = sel.css(".storeAddress p.telephone::text").extract()[0]

        store = Store()
        store["name"] = response.meta["store_name"]
        store["address"] = address
        store["phone_number"] = phone_number
        yield store
