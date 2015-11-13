import scrapy

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
        item["love"] = response.xpath("//*[@id='papierlarge']/div[3]/table[1]/tbody/tr[6]/td/text()").extract()
        item["money"] = response.xpath("//*[@id='papierlarge']/div[3]/table[1]/tbody/tr[9]/td/text()").extract()
        item["health"] = response.xpath("//*[@id='papierlarge']/div[3]/table[1]/tbody/tr[12]/td/text()").extract()
        item["work"] = response.xpath("//*[@id='papierlarge']/div[3]/table[1]/tbody/tr[15]/td/text()").extract()
        yield item