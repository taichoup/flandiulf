import scrapy, time

from astrocrawl.items import AstrocrawlItem

class AsiaSpider(scrapy.Spider):
    name = "asia"
    allowed_domains = ["asiaflash.com"]
    start_urls = [
        "http://www.asiaflash.com/horoscope/horoscope-taureau.html",
        "http://www.asiaflash.com/horoscope/horoscope-belier.html",
        "http://www.asiaflash.com/horoscope/horoscope-gemeau.html",
        "http://www.asiaflash.com/horoscope/horoscope-cancer.html",
        "http://www.asiaflash.com/horoscope/horoscope-lion.html",
        "http://www.asiaflash.com/horoscope/horoscope-vierge.html",
        "http://www.asiaflash.com/horoscope/horoscope-balance.html",
        "http://www.asiaflash.com/horoscope/horoscope-scorpion.html",
        "http://www.asiaflash.com/horoscope/horoscope-sagittaire.html",
        "http://www.asiaflash.com/horoscope/horoscope-capricorne.html",
        "http://www.asiaflash.com/horoscope/horoscope-verseau.html",
        "http://www.asiaflash.com/horoscope/horoscope-poisson.html"
    ]

    def parse(self, response):
        item = AstrocrawlItem()
        item["source"] = "Asiaflash"
        item["timestamp"] = time.ctime()
        item["sign"] = response.url[45:-5].lower()
        item["love"] = response.css("body > div.af_section_container > article > div.af_rubrique > p:nth-child(1)::text").extract()[0]
        item["money"] = response.css("body > div.af_section_container > article > div.af_rubrique > p:nth-child(2)::text").extract()[0]
        item["health"] = response.css("body > div.af_section_container > article > div.af_rubrique > p:nth-child(3)::text").extract()[0]
        item["work"] = response.css("body > div.af_section_container > article > div.af_rubrique > p:nth-child(4)::text").extract()[0]
        yield item

