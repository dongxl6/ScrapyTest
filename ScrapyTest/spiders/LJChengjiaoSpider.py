import json

import scrapy

from ScrapyTest.items import ChengjiaoItem


class LJChengjiaoSpider(scrapy.Spider):
    name='LJChengjiaoSpider'

    def start_requests(self):
        url = 'https://bj.lianjia.com/chengjiao'
        yield  scrapy.Request(url=url, callback=self.parseDistrict)

    def parseDistrict(self,response):
        districtLinks = response.xpath('//div[@data-role="ershoufang"]/div[1]/a/@href') .extract()
        for link in districtLinks:
            yield scrapy.Request(url = response.urljoin(link), callback=self.parseArea)

    def parseArea(self,response):
        areaLinks = response.xpath('//div[@data-role="ershoufang"]/div[2]/a/@href').extract()
        for link in areaLinks:
            yield scrapy.Request(url = response.urljoin(link), callback=self.parseFilter)

    def parseFilter(self,response):
        for i in range(8):
            for j in range(8):
                filterLink = response.url+'p'+str(i+1)+'a'+str(j+1)+'/'
                yield scrapy.Request(url=filterLink, callback=self.parsePage)

    def parsePage(self,response):
        pageInfoStr = response.css('.house-lst-page-box::attr(page-data)') .extract_first()
        if pageInfoStr != '' and pageInfoStr!=None:
            pageJson = json.loads(pageInfoStr)
            for number in range(1,pageJson['totalPage']+1):
                link = response.url + 'pg' + str(number)+'/'
                yield scrapy.Request(url = link, callback=self.parseList)

    def parseList(self,response):
        detailLinks = response.xpath('//ul[@class="listContent"]/li/a[@class="img"]/@href').extract()
        for link in detailLinks:
            yield scrapy.Request(url=response.urljoin(link), callback=self.parse)

    def parse(self, response):
        title = response.xpath('//div[@class="house-title LOGVIEWDATA LOGVIEW"]/div/text()').extract_first()
        dealTime = response.xpath('//div[@class="house-title LOGVIEWDATA LOGVIEW"]/div/span/text()').extract_first()
        dealPrice = response.xpath('//span[@class="dealTotalPrice"]/i/text()').extract_first()
        onlinePrice = response.xpath('//div[@class="msg"]/span[1]/label/text()').extract_first()
        onlinePeriod =  response.xpath('//div[@class="msg"]/span[2]/label/text()').extract_first()
        changePriceTime =  response.xpath('//div[@class="msg"]/span[3]/label/text()').extract_first()
        viewTime =  response.xpath('//div[@class="msg"]/span[4]/label/text()').extract_first()
        focusTime =  response.xpath('//div[@class="msg"]/span[5]/label/text()').extract_first()
        onlineViewTime =  response.xpath('//div[@class="msg"]/span[6]/label/text()').extract_first()

        structure = response.xpath('//div[@class="base"]//div[@class="content"]//li[1]/text()').extract_first()
        floor= response.xpath('//div[@class="base"]//div[@class="content"]//li[2]/text()').extract_first()
        size = response.xpath('//div[@class="base"]//div[@class="content"]//li[3]/text()').extract_first()
        style= response.xpath('//div[@class="base"]//div[@class="content"]//li[4]/text()').extract_first()
        innerSize= response.xpath('//div[@class="base"]//div[@class="content"]//li[5]/text()').extract_first()
        buildingStyle= response.xpath('//div[@class="base"]//div[@class="content"]//li[6]/text()').extract_first()
        direction= response.xpath('//div[@class="base"]//div[@class="content"]//li[7]/text()').extract_first()
        buildingAge= response.xpath('//div[@class="base"]//div[@class="content"]//li[8]/text()').extract_first()
        decoration= response.xpath('//div[@class="base"]//div[@class="content"]//li[9]/text()').extract_first()
        buildingStructure= response.xpath('//div[@class="base"]//div[@class="content"]//li[10]/text()').extract_first()
        warmType = response.xpath('//div[@class="base"]//div[@class="content"]//li[10]/text()').extract_first()
        stairHouse = response.xpath('//div[@class="base"]//div[@class="content"]//li[10]/text()').extract_first()
        rightYear = response.xpath('//div[@class="base"]//div[@class="content"]//li[10]/text()').extract_first()
        elevator = response.xpath('//div[@class="base"]//div[@class="content"]//li[10]/text()').extract_first()

        lianjiaId = response.xpath('//div[@class="transaction"]//div[@class="content"]//li[1]/text()').extract_first()
        dealRightType = response.xpath('//div[@class="transaction"]//div[@class="content"]//li[2]/text()').extract_first()
        showTime = response.xpath('//div[@class="transaction"]//div[@class="content"]//li[3]/text()').extract_first()
        useType = response.xpath('//div[@class="transaction"]//div[@class="content"]//li[4]/text()').extract_first()
        houseOwnYear = response.xpath('//div[@class="transaction"]//div[@class="content"]//li[5]/text()').extract_first()
        houseRight = response.xpath('//div[@class="transaction"]//div[@class="content"]//li[6]/text()').extract_first()


        item = ChengjiaoItem()
        item['title'] = title
        item['dealPrice'] = dealPrice
        item['dealTime'] = dealTime
        item['onlinePrice'] = onlinePrice
        item['onlinePeriod'] = onlinePeriod
        item['changePriceTime'] = changePriceTime
        item['viewTime'] = viewTime
        item['focusTime'] = focusTime
        item['onlineViewTime'] = onlineViewTime
        item['structure'] = structure
        item['floor'] = floor
        item['size'] = size
        item['style'] = style
        item['innerSize'] = innerSize
        item['buildingStyle'] = buildingStyle
        item['direction'] = direction
        item['buildingAge'] = buildingAge
        item['decoration'] = decoration
        item['buildingStructure'] = buildingStructure
        item['warmType'] = warmType
        item['stairHouse'] = stairHouse
        item['rightYear'] = rightYear
        item['elevator'] = elevator
        item['lianjiaId'] = lianjiaId
        item['dealRightType'] = dealRightType
        item['showTime'] = showTime
        item['useType'] = useType
        item['houseOwnYear'] = houseOwnYear
        item['houseRight'] = houseRight

        yield item

