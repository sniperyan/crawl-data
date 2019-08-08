# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import ItcastItem

# scrapy crawl itcast -o tt.json
class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ("http://www.itcast.cn/channel/teacher.shtml",)

    # def parse(self, response):
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     self.log('Saved file %s' % filename)

    # def parse(self, response):
    #     # 获取网站标题
    #     context = response.xpath('/html/head/title/text()')   
       
    #     # 提取网站标题
    #     title = context.extract_first()  
    #     print(title) 
    #     pass
    
    #  scrapy crawl itcast -o teachers.json
    def parse(self, response):
        #open("teacher.html","wb").write(response.body).close()
    
        # 存放老师信息的集合
        # items = []
        for each in response.xpath("//div[@class='li_txt']"):
            # 将我们得到的数据封装到一个 `ItcastItem` 对象
            item = ItcastItem()
            #extract()方法返回的都是unicode字符串
            name = each.xpath("h3/text()").extract()
            title = each.xpath("h4/text()").extract()
            info = each.xpath("p/text()").extract()
    
            #xpath返回的是包含一个元素的列表
            item['name'] = name[0].encode("utf-8").decode("utf-8")
            item['title'] = title[0].encode("utf-8").decode("utf-8")
            item['info'] = info[0].encode("utf-8").decode("utf-8")
    
            # items.append(item)
            yield item
    
        # 直接返回最后数据
        # return items