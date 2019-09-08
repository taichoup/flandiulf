import scrapy, time

from astrocrawl.items import AstrocrawlItem

class HFRSpider(scrapy.Spider):
    name = "hfr"
    allowed_domains = ["horoscope.fr"]
    start_urls = [
        "https://www.horoscope.fr/horoscopes/horoscope_belier.html",
        "https://www.horoscope.fr/horoscopes/horoscope_taureau.html",
        "https://www.horoscope.fr/horoscopes/horoscope_gemeaux.html",
        "https://www.horoscope.fr/horoscopes/horoscope_cancer.html",
        "https://www.horoscope.fr/horoscopes/horoscope_lion.html",
        "https://www.horoscope.fr/horoscopes/horoscope_vierge.html",
        "https://www.horoscope.fr/horoscopes/horoscope_balance.html",
        "https://www.horoscope.fr/horoscopes/horoscope_scorpion.html",
        "https://www.horoscope.fr/horoscopes/horoscope_sagittaire.html",
        "https://www.horoscope.fr/horoscopes/horoscope_capricorne.html",
        "https://www.horoscope.fr/horoscopes/horoscope_verseau.html",
        "https://www.horoscope.fr/horoscopes/horoscope_poissons.html"
    ]

    def parse(self, response):
        item = AstrocrawlItem()
        item["source"] = "Horoscope.fr"
        item["timestamp"] = time.ctime()
        item["sign"] = response.url[46:-5].lower()
        # item["love"] = response.xpath("//*[@id='horo-jour-amour']/div[1]/p[2]/text()").extract()[0]
        # item["money"] = response.xpath("//*[@id='horo-jour-travail']/div[2]/div[2]/p/text()").extract()[0]
        # item["health"] = response.xpath("//*[@id='horo-jour-bienetre']/div[1]/div[2]/p/text()").extract()[0]
        # item["work"] = response.xpath("//*[@id='horo-jour-travail']/div[1]/div[2]/p/text()").extract()[0]
        item["love"] = response.xpath("//*[@id='horo-jour-ambiance']/div/div[4]/p[1]/text()").extract()[0]
        item["money"] = response.xpath("//*[@id='horo-jour-ambiance']/div/div[7]/p/text()").extract()[0]
        item["health"] = response.xpath("//*[@id='horo-jour-ambiance']/div/div[8]/p/text()").extract()[0]
        item["work"] = response.xpath("//*[@id='horo-jour-ambiance']/div/div[6]/p/text()").extract()[0]
        yield item