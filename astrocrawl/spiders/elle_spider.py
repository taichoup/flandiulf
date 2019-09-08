import scrapy, time

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
        item["source"] = "Elle"
        item["timestamp"] = time.ctime()
        item["sign"] = response.url[46:].lower()
        item["love"] = response.css('div.zone-resultat>p::text').extract()[0]
        item["money"] = response.css('div.zone-resultat>p::text').extract()[1]
        item["health"] = response.css('div.zone-resultat>p::text').extract()[2]
        item["work"] = response.css('div.zone-resultat>p::text').extract()[3]
        yield item