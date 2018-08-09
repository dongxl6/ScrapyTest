import scrapy
import json
from ScrapyTest.items import HouseItem
import logging

class LianjiaSprider(scrapy.Spider):
    name='LianjiaSpider'

    def start_requests(self):
        url='https://bj.lianjia.com/ershoufang'
        yield  scrapy.Request(url = url,callback=self.parseDistrict)

    def parseDistrict(self,response):
        districtLinks = response.css('.section_sub_nav a::attr(href)') .extract()
        for link in districtLinks:
            yield scrapy.Request(url = response.urljoin(link), callback=self.parseArea)

    def parseArea(self,response):
        areaLinks = response.css('.section_sub_sub_nav a::attr(href)') .extract()
        for link in areaLinks:
            yield scrapy.Request(url = response.urljoin(link), callback=self.parsePage)

    def parsePage(self,response):
        pageInfoStr = response.css('.house-lst-page-box::attr(page-data)') .extract_first()
        if pageInfoStr != '' and pageInfoStr!=None:
            pageJson = json.loads(pageInfoStr)
            for number in range(1,pageJson['totalPage']+1):
                link = response.url + 'pg' + str(number)+'/'
                yield scrapy.Request(url = link, callback=self.parse)

    def parse(self, response):
        houses = response.css('li.LOGCLICKDATA')
        for house in houses:
            id = house.css('.img::attr(data-housecode)').extract_first()

            title = house.css('.title a::text').extract_first()
            housingEstate = house.css('.houseInfo a::text').extract_first()

            features = house.css('.houseInfo')[0].css('div::text').extract()
            incr = 0;
            if len(features) >= 6:
                incr = 1

            structure = features[0+incr]
            size = features[1+incr]
            direction = features[2+incr]
            decoration = ""
            if len(features)-incr >= 4:
                decoration = features[3+incr]
            elevator = ""
            if len(features)-incr >= 5:
                elevator = features[4+incr]

            positions = house.css('.positionInfo')[0].css('div::text').extract()
            floor = positions[0]
            age = ""
            if len(positions) >= 2:
                age = positions[1]

            area = house.css('.positionInfo a::text').extract_first()

            price = house.css('.totalPrice span::text').extract_first()

            unitprice = house.css('.unitPrice span::text').extract_first()

            item = HouseItem()
            item['id'] = id
            item['title'] = title
            item['housingEstate'] = housingEstate
            item['structure'] = structure
            item['size'] = size
            item['direction'] = direction
            item['decoration'] = decoration
            item['elevator'] = elevator
            item['floor'] = floor
            item['age'] = age
            item['area'] = area
            item['price'] = price
            item['unitprice'] = unitprice

            yield item