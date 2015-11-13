import scrapy

from astrocrawl.items import AstrocrawlItem

class ElleSpider(scrapy.Spider):
    name = "elle"
    allowed_domains = ["elle.fr"]
    start_urls = [
        "http://www.elle.fr/Astro/Horoscope/Quotidien/belier/",
        "http://www.elle.fr/Astro/Horoscope/Quotidien/taureau/",
        "http://www.elle.fr/Astro/Horoscope/Quotidien/gemeaux/",
        "http://www.elle.fr/Astro/Horoscope/Quotidien/cancer/",
        "http://www.elle.fr/Astro/Horoscope/Quotidien/lion/",
        "http://www.elle.fr/Astro/Horoscope/Quotidien/vierge/",
        "http://www.elle.fr/Astro/Horoscope/Quotidien/balance/",
        "http://www.elle.fr/Astro/Horoscope/Quotidien/scorpion/",
        "http://www.elle.fr/Astro/Horoscope/Quotidien/sagittaire/",
        "http://www.elle.fr/Astro/Horoscope/Quotidien/capricorne/",
        "http://www.elle.fr/Astro/Horoscope/Quotidien/verseau/",
        "http://www.elle.fr/Astro/Horoscope/Quotidien/poissons/"
    ]

    def parse(self, response):
        item = AstrocrawlItem()
        item["love"] = response.xpath("//*[@id='main']/div/div/div[3]/div[1]/div/div[3]/div/p[1]/text()").extract()
        item["money"] = response.xpath("//*[@id='main']/div/div/div[3]/div[1]/div/div[3]/div/p[2]/text()").extract()
        item["health"] = response.xpath("//*[@id='main']/div/div/div[3]/div[1]/div/div[3]/div/p[3]/text()").extract()
        item["work"] = response.xpath("//*[@id='main']/div/div/div[3]/div[1]/div/div[3]/div/p[4]/text()").extract()
        yield item