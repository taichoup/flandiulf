 # coding: utf8
from __future__ import unicode_literals

import urllib
import lxml.html as HTML
import codecs
import os
import json

usersigns = ["belier", "gemeaux", "balance", "scorpion", "sagittaire", "taureau", "vierge", "capricorne", "verseau", "lion", "cancer", "poissons"]

categories = ["amour", "sante", "travail", "argent"]

class WebSource:
    "Common base class for all sites with scrapable horoscope."
    def __init__(self, lang, name, url, amour_sel, argent_sel, sante_sel, travail_sel):
        self.lang = lang
        self.name = name
        # self.charset = charset
        self.url = url
        self.amour_sel = amour_sel
        self.argent_sel = argent_sel
        self.sante_sel = sante_sel
        self.travail_sel = travail_sel

    def build_url(self, sign):
        return self.url % sign


source1 = WebSource("fr", "Le Journal des Femmes", "http://sante.journaldesfemmes.com/psychologie/horoscope/zodiaque/%s-jour/", ".//div[@class='layout_main']/table/tbody/tr[6]/", ".//div[@class='layout_main']/table/tbody/tr[9]/", ".//div[@class='layout_main']/table/tbody/tr[12]/", ".//div[@class='layout_main']/table/tbody/tr[15]/")
source2 = WebSource("fr", "horoscope.fr", "http://www.horoscope.fr/horoscopes/horoscope_%s.html", ".//div[@id='horo-jour-amour']/div/p[2]", ".//div[@id='horo-jour-travail']/div[2]/div[2]/p", ".//div[@id='horo-jour-bienetre']/div[1]/div[2]/p", ".//div[@id='horo-jour-travail']/div[1]/div[2]/p")
# source3 = WebSource("fr", "Le Parisien", "http://astrologie.leparisien.fr/astrologie/zodiaque/%s.html", ".//article[@class='np-article-predictionvipsign']/section/div/article/p[1]", "", ".//article[@class='np-article-predictionvipsign']/section/div/article/p[3]", ".//article[@class='np-article-predictionvipsign']/section/div/article/p[2]")
source4 = WebSource("fr", "Elle.fr", "http://www.elle.fr/Astro/Horoscope/Quotidien/%s", ".//article[@id='text']/p[1]", ".//article[@id='text']/p[2]", ".//article[@id='text']/p[3]", ".//div[@id='zParaArticle']/p[4]")
# source5 = WebSource("fr", "Astrowi.com", "http://www.astrowi.com/horoscope-astrologie-jour-%s", ".//div[@id='zParaArticle']/p[1]", ".//div[@id='zParaArticle']/p[2]", ".//div[@id='zParaArticle']/p[3]", ".//div[@id='zParaArticle']/p[4]")

sources = [source1, source2, source4]

sources2 = [i.__dict__ for i in sources]



with open("astrodump2.json", "w") as outfile:
    response = []
    for source in sources:
        for sign in usersigns:
            for cat in categories:
                try:
                    print u"Recherce d'horoscope sur %s pour %s/%s" % (source.name, sign, cat)
                    p = HTML.fromstring(urllib.urlopen(source.build_url(sign)).read())
                    selector = source.__dict__["%s_sel" % cat]
                    desc = p.find(selector).text.strip()
                    response.append({"sign":sign, "source":source.name, "category":cat, "content":desc})
                except Exception as e:
                    continue
    json.dump(response, outfile, encoding="utf-8", sort_keys=True, indent=4, separators=(',', ': '))
