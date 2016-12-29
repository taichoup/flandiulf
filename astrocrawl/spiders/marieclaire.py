import scrapy, time

from astrocrawl.items import AstrocrawlItem

class MarieClaireSpider(scrapy.Spider):
    name = "marieclaire"
    allowed_domains = ["marieclaire.fr"]
    start_urls = [
        "http://www.marieclaire.fr/astro/horoscope/horoscope-du-jour/belier",
        "http://www.marieclaire.fr/astro/horoscope/horoscope-du-jour/gemeaux",
        "http://www.marieclaire.fr/astro/horoscope/horoscope-du-jour/poissons",
        "http://www.marieclaire.fr/astro/horoscope/horoscope-du-jour/verseau",
        "http://www.marieclaire.fr/astro/horoscope/horoscope-du-jour/cancer",
        "http://www.marieclaire.fr/astro/horoscope/horoscope-du-jour/taureau",
        "http://www.marieclaire.fr/astro/horoscope/horoscope-du-jour/balance",
        "http://www.marieclaire.fr/astro/horoscope/horoscope-du-jour/scorpion",
        "http://www.marieclaire.fr/astro/horoscope/horoscope-du-jour/capricorne",
        "http://www.marieclaire.fr/astro/horoscope/horoscope-du-jour/vierge",
        "http://www.marieclaire.fr/astro/horoscope/horoscope-du-jour/lion",
        "http://www.marieclaire.fr/astro/horoscope/horoscope-du-jour/sagittaire"
    ]

    def parse(self, response):
        item = AstrocrawlItem()
        item["source"] = "Marie Claire"
        item["timestamp"] = time.ctime()
        item["sign"] = response.url[60:].lower()
        item["love"] = response.css(".Article-textContainer p")[0].extract().split(">")[1].split("<")[0].strip()
        item["money"] = ""
        item["health"] = ""
        item["work"] = response.css(".Article-textContainer p")[1].extract().split(">")[1].split("<")[0].strip()
        yield item