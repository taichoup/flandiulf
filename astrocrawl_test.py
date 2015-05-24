 # coding: utf8
from __future__ import unicode_literals

import urllib
import lxml.html as HTML
import codecs
import os
import json
from lxml.cssselect import CSSSelector


sources = [{
    "name":"mon-astrocenter.fr",
    "charset":"utf-8",
    "url":"http://mon.astrocenter.fr/horoscope/quotidien/%s",
    "amour":"div.article-horoscope p",
    "argent":"",
    "sante":"",
    "travail":""
    }
]

usersigns = ["belier", "gemeaux", "balance", "scorpion", "sagittaire", "taureau", "vierge", "capricorne", "verseau", "lion", "cancer", "poissons"]

categories = ["amour"]
# categories = ["amour", "sante", "travail", "argent"]



for website in sources:
    for sign in usersigns:
        for category in categories:
            try:
                p = HTML.fromstring(urllib.urlopen(website["url"] % sign).read())
                # desc = p.find(website[category]).text.strip()
                desc = p.cssselect(website[category].text.strip())
                print "found : %s" % desc
            except SyntaxError as e:
                continue