import scrapy, time

from astrocrawl.items import AstrocrawlItem

class IDVoyanceSpider(scrapy.Spider):
    name = "idealvoyance"
    allowed_domains = ["idealvoyance.fr"]
    start_urls = [
        "https://www.idealvoyance.fr/horoscope-jour-belier",
        "https://www.idealvoyance.fr/horoscope-jour-balance",
        "https://www.idealvoyance.fr/horoscope-jour-cancer",
        "https://www.idealvoyance.fr/horoscope-jour-capricorne",
        "https://www.idealvoyance.fr/horoscope-jour-verseau",
        "https://www.idealvoyance.fr/horoscope-jour-poissons",
        "https://www.idealvoyance.fr/horoscope-jour-gemeaux",
        "https://www.idealvoyance.fr/horoscope-jour-taureau",
        "https://www.idealvoyance.fr/horoscope-jour-vierge",
        "https://www.idealvoyance.fr/horoscope-jour-scorpion",
        "https://www.idealvoyance.fr/horoscope-jour-sagittaire",
        "https://www.idealvoyance.fr/horoscope-jour-lion"
    ]

    def parse(self, response):
        item = AstrocrawlItem()
        item["source"] = "Ideal Voyance"
        item["timestamp"] = time.ctime()
        item["sign"] = response.url[43:].lower()
        item["love"] = response.css(".content")[2].extract().split(">")[1].split("<")[0].strip()
        item["money"] = response.css(".content")[3].extract().split(">")[1].split("<")[0].strip()
        item["health"] = response.css(".content")[4].extract().split(">")[1].split("<")[0].strip()
        item["work"] = response.css(".content")[5].extract().split(">")[1].split("<")[0].strip()
        yield item