# -*- coding: utf-8 -*-
import scrapy
import pandas as pd

class ShopcluesSpider(scrapy.Spider):
    print("Shreyas Prakash 19BCE2111")
    name = 'samsung'
    #list of allowed domains
    allowed_domains = ['www.samsung.com']
    #starting url
    start_urls = ['https://www.samsung.com/in/offer/online/samsung-fest/']
    def parse(self, response):
        titles = response.xpath('//div[@class="product-detail-text"]/h2/text()').getall()
        prices = response.xpath('//div[@class="product-detail-text"]/h4/text()').getall()
        images = response.xpath('//div[@class="product-detail-text"]/preceding-sibling::img[1]/@src').getall()
        discounts = response.css('.discount_tag::text').extract()
        img = []
        name = []
        price = []
        dis = []
        for item in zip(discounts, titles, prices, images):
            img.append(item[3])
            name.append(item[1])
            price.append(item[2][:-4])
            dis.append(item[0])
        df = pd.DataFrame({"product_image":img,"product_name":name,"product_price":price,"product_discount":dis})    
        print(df)    
        df.to_csv('products_scrapy.csv',index=False,encoding='utf-8')