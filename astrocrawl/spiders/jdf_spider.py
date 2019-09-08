import scrapy, time

from astrocrawl.items import AstrocrawlItem

class JDFSpider(scrapy.Spider):
    name = "jdf"
    allowed_domains = ["journaldesfemmes.com"]
    start_urls = [
        "http://sante.journaldesfemmes.com/psychologie/horoscope/zodiaque/belier-jour/",
        "http://sante.journaldesfemmes.com/psychologie/horoscope/zodiaque/taureau-jour/",
        "http://sante.journaldesfemmes.com/psychologie/horoscope/zodiaque/gemeaux-jour/",
        "http://sante.journaldesfemmes.com/psychologie/horoscope/zodiaque/cancer-jour/",
        "http://sante.journaldesfemmes.com/psychologie/horoscope/zodiaque/lion-jour/",
        "http://sante.journaldesfemmes.com/psychologie/horoscope/zodiaque/vierge-jour/",
        "http://sante.journaldesfemmes.com/psychologie/horoscope/zodiaque/balance-jour/",
        "http://sante.journaldesfemmes.com/psychologie/horoscope/zodiaque/scorpion-jour/",
        "http://sante.journaldesfemmes.com/psychologie/horoscope/zodiaque/sagittaire-jour/",
        "http://sante.journaldesfemmes.com/psychologie/horoscope/zodiaque/capricorne-jour/",
        "http://sante.journaldesfemmes.com/psychologie/horoscope/zodiaque/verseau-jour/",
        "http://sante.journaldesfemmes.com/psychologie/horoscope/zodiaque/poissons-jour/"
    ]

    def parse(self, response):
        item = AstrocrawlItem()
        item["source"] = "Le Journal Des Femmes"
        item["timestamp"] = time.ctime()
        # item["sign"] = response.url[65:-6].lower()
        # item["sign"] = response.url[59:-6].lower()
        item["sign"] = response.url[51:-6].lower()
        item["love"] = response.xpath("//*[@id='adsLayout']/div[2]/div[1]/div/main/p[1]/text()").extract()[0].strip()
        item["money"] = response.xpath("//*[@id='adsLayout']/div[2]/div[1]/div/main/p[2]/text()").extract()[0].strip()
        item["health"] = response.xpath("//*[@id='adsLayout']/div[2]/div[1]/div/main/p[3]/text()").extract()[0].strip()
        item["work"] = response.xpath("//*[@id='adsLayout']/div[2]/div[1]/div/main/p[4]/text()").extract()[0].strip()
        yield item


