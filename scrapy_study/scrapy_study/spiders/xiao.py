import scrapy


class XiaoSpider(scrapy.Spider):
    name = "xiao"
    allowed_domains = ["www.4399.com"]
    start_urls = ["http://www.4399.com/flash"]

    def parse(self, response):
        texts=response.xpath("/html/body/div[8]/ul/li")
        for text in texts:
            name=text.xpath("a/img/@alt").extract()[0]

            dic={
                'name':name,
                'class':'game'

            }

            yield dic

