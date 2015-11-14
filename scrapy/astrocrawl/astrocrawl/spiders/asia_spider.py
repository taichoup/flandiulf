import scrapy

from astrocrawl.items import AstrocrawlItem

class AsiaSpider(scrapy.Spider):
    name = "asia"
    allowed_domains = ["asiaflash.com"]
    start_urls = [
        "http://www.asiaflash.com/horoscope/horoscope-taureau.shtml",
        "http://www.asiaflash.com/horoscope/horoscope-belier.shtml",
        "http://www.asiaflash.com/horoscope/horoscope-gemeau.shtml",
        "http://www.asiaflash.com/horoscope/horoscope-cancer.shtml",
        "http://www.asiaflash.com/horoscope/horoscope-lion.shtml",
        "http://www.asiaflash.com/horoscope/horoscope-vierge.shtml",
        "http://www.asiaflash.com/horoscope/horoscope-balance.shtml",
        "http://www.asiaflash.com/horoscope/horoscope-scorpion.shtml",
        "http://www.asiaflash.com/horoscope/horoscope-sagittaire.shtml",
        "http://www.asiaflash.com/horoscope/horoscope-capricorne.shtml",
        "http://www.asiaflash.com/horoscope/horoscope-verseau.shtml",
        "http://www.asiaflash.com/horoscope/horoscope-poisson.shtml"
    ]

    def parse(self, response):
        item = AstrocrawlItem()
        item["love"] = response.css("td.textenormal::text")[17].extract().strip()
        item["money"] = response.css("td.textenormal::text")[20].extract().strip()
        item["health"] = response.css("td.textenormal::text")[23].extract().strip()
        item["work"] = response.css("td.textenormal::text")[26].extract().strip()
        yield item