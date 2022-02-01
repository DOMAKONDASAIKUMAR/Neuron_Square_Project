# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NeuronItem(scrapy.Item):
    # define the fields for your item here like:
    price = scrapy.Field()
    title = scrapy.Field()
    stock = scrapy.Field()
    maftr = scrapy.Field()
    pass
