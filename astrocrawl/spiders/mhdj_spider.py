import scrapy, time

from astrocrawl.items import AstrocrawlItem

class MHDJSpider(scrapy.Spider):
    name = "mhdj"
    allowed_domains = ["https://www.mon-horoscope-du-jour.com"]
    start_urls = [
        "https://www.mon-horoscope-du-jour.com/horoscopes/quotidien/belier.htm",
        "https://www.mon-horoscope-du-jour.com/horoscopes/quotidien/taureau.htm",
        "https://www.mon-horoscope-du-jour.com/horoscopes/quotidien/gemeaux.htm",
        "https://www.mon-horoscope-du-jour.com/horoscopes/quotidien/cancer.htm",
        "https://www.mon-horoscope-du-jour.com/horoscopes/quotidien/lion.htm",
        "https://www.mon-horoscope-du-jour.com/horoscopes/quotidien/vierge.htm",
        "https://www.mon-horoscope-du-jour.com/horoscopes/quotidien/balance.htm",
        "https://www.mon-horoscope-du-jour.com/horoscopes/quotidien/scorpion.htm",
        "https://www.mon-horoscope-du-jour.com/horoscopes/quotidien/sagittaire.htm",
        "https://www.mon-horoscope-du-jour.com/horoscopes/quotidien/capricorne.htm",
        "https://www.mon-horoscope-du-jour.com/horoscopes/quotidien/verseau.htm",
        "https://www.mon-horoscope-du-jour.com/horoscopes/quotidien/poissons.htm"
    ]

    def parse(self, response):
        item = AstrocrawlItem()
        item["source"] = "Mon Horoscope du Jour"
        item["timestamp"] = time.ctime()
        item["sign"] = response.url[59:-4].lower()
        item["love"] = response.css("p::text")[2].extract()
        item["money"] = response.css("p::text")[3].extract()
        item["health"] = ""
        item["work"] = response.css("p::text")[4].extract()
        yield item