import scrapy, time

from astrocrawl.items import AstrocrawlItem

class PARISpider(scrapy.Spider):
    name = "paris"
    allowed_domains = ["leparisien.fr"]
    start_urls = [
        "http://astrologie.leparisien.fr/astrologie/zodiaque/belier.html",
        "http://astrologie.leparisien.fr/astrologie/zodiaque/taureau.html",
        "http://astrologie.leparisien.fr/astrologie/zodiaque/gemeaux.html",
        "http://astrologie.leparisien.fr/astrologie/zodiaque/cancer.html",
        "http://astrologie.leparisien.fr/astrologie/zodiaque/lion.html",
        "http://astrologie.leparisien.fr/astrologie/zodiaque/vierge.html",
        "http://astrologie.leparisien.fr/astrologie/zodiaque/balance.html",
        "http://astrologie.leparisien.fr/astrologie/zodiaque/scorpion.html",
        "http://astrologie.leparisien.fr/astrologie/zodiaque/sagittaire.html",
        "http://astrologie.leparisien.fr/astrologie/zodiaque/capricorne.html",
        "http://astrologie.leparisien.fr/astrologie/zodiaque/verseau.html",
        "http://astrologie.leparisien.fr/astrologie/zodiaque/poissons.html"
    ]

    def parse(self, response):
        item = AstrocrawlItem()
        item["source"] = "Le Parisien"
        item["timestamp"] = time.ctime()
        item["sign"] = response.url[52:-5].lower()
        item["love"] = response.css("article p::text")[1].extract().strip()
        item["money"] = ""
        item["health"] = response.css("article p::text")[5].extract().strip()
        item["work"] = response.css("article p::text")[3].extract().strip()
        yield item