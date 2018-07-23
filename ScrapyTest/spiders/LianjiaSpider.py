import scrapy
import json

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
        houses=response.css('li.LOGCLICKDATA')
        for house in houses:
            title = house.css('.title a::text').extract_first()
            housingEstate = house.css('.houseInfo a::text').extract_first()

            features = house.css('.houseInfo::text').extract()
            structure = features[0]
            size = features[1]
            direction = features[2]
            if len(features)>= 4:
                decoration = features[3]
            if len(features)>= 5:
                elevator = features[4]

            positions = house.css('.positionInfo::text').extract()
            floor = positions[0]
            if len(positions)>= 2:
                age = positions[1]

            area = house.css('.positionInfo a::text').extract_first()

            price = house.css('.totalPrice span::text').extract_first()

            unitprice = house.css('.unitPrice span::text').extract_first()


            fileName = 'LianjiaHouse.txt'
            f = open(fileName,'a+',encoding="utf-8")
            f.write(title)
            f.write('\t')
            f.write(housingEstate)
            f.write('\t')
            f.write(structure)
            f.write('\t')
            f.write(size)
            f.write('\t')
            f.write(direction)
            f.write('\t')
            f.write(decoration)
            f.write('\t')
            f.write(elevator)
            f.write('\t')
            f.write(floor)
            f.write('\t')
            f.write(age)
            f.write('\t')
            f.write(area)
            f.write('\t')
            f.write(price)
            f.write('\t')
            f.write(unitprice)
            f.write('\n')
            f.close()