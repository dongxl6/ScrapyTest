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


class ChengjiaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    dealPrice = scrapy.Field()
    dealTime = scrapy.Field()
    onlinePrice = scrapy.Field()
    onlinePeriod = scrapy.Field()
    changePriceTime = scrapy.Field()
    viewTime = scrapy.Field()
    focusTime = scrapy.Field()
    onlineViewTime = scrapy.Field()
    structure = scrapy.Field()
    floor = scrapy.Field()
    size = scrapy.Field()
    style = scrapy.Field()
    innerSize = scrapy.Field()
    buildingStyle = scrapy.Field()
    direction = scrapy.Field()
    buildingAge = scrapy.Field()
    decoration = scrapy.Field()
    buildingStructure = scrapy.Field()
    warmType = scrapy.Field()
    stairHouse = scrapy.Field()
    rightYear = scrapy.Field()
    elevator = scrapy.Field()
    lianjiaId = scrapy.Field()
    dealRightType = scrapy.Field()
    showTime = scrapy.Field()
    useType = scrapy.Field()
    houseOwnYear = scrapy.Field()
    houseRight = scrapy.Field()





