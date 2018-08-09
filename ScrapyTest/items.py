# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    title = scrapy.Field()
    housingEstate = scrapy.Field()
    structure = scrapy.Field()
    size = scrapy.Field()
    direction = scrapy.Field()
    decoration = scrapy.Field()
    elevator = scrapy.Field()
    floor = scrapy.Field()
    age = scrapy.Field()
    area = scrapy.Field()
    price = scrapy.Field()
    unitprice = scrapy.Field()
