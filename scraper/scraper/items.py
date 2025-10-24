from scrapy.item import Item, Field


class Item(Item):
    title = Field()
    date = Field()
    category = Field()
    text = Field()
    author = Field()
