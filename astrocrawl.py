 # coding: utf8
from __future__ import unicode_literals

import urllib
import lxml.html as HTML
import codecs
import os
import json
# from collections import defaultdict

# class WebSource:
#     "Common base class for all sites with scrapable horoscope."
#     def __init__(self, name, charset, url, amour_sel, argent_sel, sante_sel, travail_sel):
#         self.name = name
#         self.charset = charset
#         self.url = url
#         self.argent_sel = argent_sel
#         self.sante_sel = sante_sel
#         self.travail_sel = travail_sel
#         self.amour_sel = amour_sel

# source1 = WebSource("journaldesfemmes", "iso-8859-1", "http://sante.journaldesfemmes.com/psychologie/horoscope/zodiaque/%s-jour/", ".//div[@class='layout_main']/table/tbody/tr[6]/", ".//div[@class='layout_main']/table/tbody/tr[9]/", ".//div[@class='layout_main']/table/tbody/tr[12]/", ".//div[@class='layout_main']/table/tbody/tr[15]/")

# print source1.url

sources = [{
    "name":"journaldesfemmes",   # same as 20 minutes.fr ?
    "charset": "iso-8859-1",
    "url":"http://sante.journaldesfemmes.com/psychologie/horoscope/zodiaque/%s-jour/",
    "amour":".//div[@class='layout_main']/table/tbody/tr[6]/",
    "argent":".//div[@class='layout_main']/table/tbody/tr[9]/",
    "sante":".//div[@class='layout_main']/table/tbody/tr[12]/",
    "travail":".//div[@class='layout_main']/table/tbody/tr[15]/"
    }, {
    "name":"horoscope_fr",
    "charset":"utf-8",
    "url":"http://www.horoscope.fr/horoscopes/horoscope_%s.html",
    "amour":".//div[@id='horo-jour-amour']/div/p[2]",
    "argent":".//div[@id='horo-jour-travail']/div[2]/div[2]/p",
    "sante":".//div[@id='horo-jour-bienetre']/div[1]/div[2]/p",
    "travail":".//div[@id='horo-jour-travail']/div[1]/div[2]/p"
    }, {
    "name":"le_parisien",
    "charset":"utf-8",
    "url":"http://astrologie.leparisien.fr/astrologie/zodiaque/%s.html",
    "amour":".//article[@class='np-article-predictionvipsign']/section/div/article/p[1]",
    "argent":"",
    "sante":".//article[@class='np-article-predictionvipsign']/section/div/article/p[3]",
    "travail":".//article[@class='np-article-predictionvipsign']/section/div/article/p[2]"
    }, {
    "name":"elle_fr",
    "charset":"utf-8",
    "url":"http://www.elle.fr/Astro/Horoscope/Quotidien/%s",
    "amour":".//article[@id='text']/p[1]",
    "argent":".//article[@id='text']/p[2]",
    "sante":".//article[@id='text']/p[3]",
    "travail":".//article[@id='text']/p[4]"
    }, {
    "name": "astrowi_com",
    "charset":"utf-8",
    "url":"http://www.astrowi.com/horoscope-astrologie-jour-%s",
    "amour":".//div[@id='zParaArticle']/p[1]",
    "argent":".//div[@id='zParaArticle']/p[2]",
    "sante":".//div[@id='zParaArticle']/p[3]",
    "travail":".//div[@id='zParaArticle']/p[4]"
    }
]

usersigns = ["belier", "gemeaux", "balance", "scorpion", "sagittaire", "taureau", "vierge", "capricorne", "verseau", "lion", "cancer", "poissons"]

categories = ["amour", "sante", "travail", "argent"]

with open("astrodump.json", "w") as outfile:
    response = {site["name"]:{sign:{cat:{} for cat in categories} for sign in usersigns} for site in sources}
    print response
    for website in sources[:1]:
        for sign in usersigns:
            for category in categories:
                try:
                    print u"Recherche d'horoscope sur %s pour %s/%s" % (website["name"], sign, category)
                    p = HTML.fromstring(urllib.urlopen(website["url"] % sign).read())
                    desc = p.find(website[category]).text.strip()
                    sitename = website["name"]
                    response[sitename][sign][category] = desc
                except SyntaxError as e:
                    continue
    json.dump(response, outfile, encoding="utf-8", sort_keys=True, indent=4, separators=(',', ': '))