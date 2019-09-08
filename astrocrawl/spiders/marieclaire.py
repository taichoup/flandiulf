import scrapy, time

from astrocrawl.items import AstrocrawlItem

class MarieClaireSpider(scrapy.Spider):
    name = "marieclaire"
    allowed_domains = ["marieclaire.fr"]
    start_urls = [
        "https://www.marieclaire.fr/astro/horoscope/horoscope-du-jour/belier",
        "https://www.marieclaire.fr/astro/horoscope/horoscope-du-jour/gemeaux",
        "https://www.marieclaire.fr/astro/horoscope/horoscope-du-jour/poissons",
        "https://www.marieclaire.fr/astro/horoscope/horoscope-du-jour/verseau",
        "https://www.marieclaire.fr/astro/horoscope/horoscope-du-jour/cancer",
        "https://www.marieclaire.fr/astro/horoscope/horoscope-du-jour/taureau",
        "https://www.marieclaire.fr/astro/horoscope/horoscope-du-jour/balance",
        "https://www.marieclaire.fr/astro/horoscope/horoscope-du-jour/scorpion",
        "https://www.marieclaire.fr/astro/horoscope/horoscope-du-jour/capricorne",
        "https://www.marieclaire.fr/astro/horoscope/horoscope-du-jour/vierge",
        "https://www.marieclaire.fr/astro/horoscope/horoscope-du-jour/lion",
        "https://www.marieclaire.fr/astro/horoscope/horoscope-du-jour/sagittaire"
    ]

    def parse(self, response):
        item = AstrocrawlItem()
        item["source"] = "Marie Claire"
        item["timestamp"] = time.ctime()
        item["sign"] = response.url[61:-1].lower()
        item["love"] = response.css(".Article-textContainer p")[0].extract().split(">")[1].split("<")[0].strip()
        item["money"] = ""
        item["health"] = ""
        item["work"] = response.css(".Article-textContainer p")[1].extract().split(">")[1].split("<")[0].strip()
        yield item