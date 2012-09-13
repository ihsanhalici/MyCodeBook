from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from orumcek.items import OrumcekItem


class OrumcekSpider(CrawlSpider):
    name = 'orumcek'
    start_urls = ['http://www.halitalptekin.com/blog/'] # urls from which the spider will start crawling
    rules = [Rule(SgmlLinkExtractor(allow=[r'\?page=\d+']), follow=True),
             # r'page/\d+' : regular expression for http://isbullsh.it/page/X URLs
             Rule(SgmlLinkExtractor(allow=[r'\w+.html']), callback='parse_blogpost')]
    # r'\d{4}/\d{2}/\w+' : regular expression for http://isbullsh.it/YYYY/MM/title URLs

    def parse_blogpost(self, response):
        hxs = HtmlXPathSelector(response)
        item = OrumcekItem()

        item['title']       = hxs.select("//div[@class='span9']/h1/a/text()").extract()
        item['description'] = hxs.select("//div[@class='span9']/p[@class='lead']/text()").extract()
        item['date']        = hxs.select("//div[@class='span9']/h1/small/text()").extract()
        #item['post']        = hxs.select("//div[@class='span9']/p/text()").extract()
        return item
