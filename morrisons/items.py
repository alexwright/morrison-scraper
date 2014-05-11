# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class Store(Item):
    name = Field()
    address = Field()
    phone_number = Field()
    open_times = Field()

class Region(Item):
    url = Field()
    name = Field()

