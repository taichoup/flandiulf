import scrapy, time

from astrocrawl.items import AstrocrawlItem

class IDVoyanceSpider(scrapy.Spider):
    name = "idealvoyance"
    allowed_domains = ["idealvoyance.fr"]
    start_urls = [
        "http://www.idealvoyance.fr/horoscope-jour-belier",
        "http://www.idealvoyance.fr/horoscope-jour-balance",
        "http://www.idealvoyance.fr/horoscope-jour-cancer",
        "http://www.idealvoyance.fr/horoscope-jour-capricorne",
        "http://www.idealvoyance.fr/horoscope-jour-verseau",
        "http://www.idealvoyance.fr/horoscope-jour-poissons",
        "http://www.idealvoyance.fr/horoscope-jour-gemeaux",
        "http://www.idealvoyance.fr/horoscope-jour-taureau",
        "http://www.idealvoyance.fr/horoscope-jour-vierge",
        "http://www.idealvoyance.fr/horoscope-jour-scorpion",
        "http://www.idealvoyance.fr/horoscope-jour-sagittaire",
        "http://www.idealvoyance.fr/horoscope-jour-lion"
    ]

    def parse(self, response):
        item = AstrocrawlItem()
        item["source"] = "Ideal Voyance"
        item["timestamp"] = time.ctime()
        item["sign"] = response.url[42:].lower()
        item["love"] = response.css(".content")[2].extract().split(">")[1].split("<")[0].strip()
        item["money"] = response.css(".content")[3].extract().split(">")[1].split("<")[0].strip()
        item["health"] = response.css(".content")[4].extract().split(">")[1].split("<")[0].strip()
        item["work"] = response.css(".content")[5].extract().split(">")[1].split("<")[0].strip()
        yield item