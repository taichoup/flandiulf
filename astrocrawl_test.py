 # coding: utf8
from __future__ import unicode_literals

import urllib
import lxml.html as HTML
import codecs
import os
import json
# from lxml.cssselect import CSSSelector
# import cssselect
import requests


sources = [{
    # "name":"20minutes.fr",
    # "charset":"utf-8",
    # "url":"http://horoscope.20minutes.fr/horoscope-jour-%s",
    # "amour":"div[@id='ctn_horoscope_jour']/p[3]",
    # "argent":"/html/body/table[3]/tbody/tr/td[2]/table/tbody/tr/td/text()[2]",
    # "sante":"/html/body/table[3]/tbody/tr/td[2]/table/tbody/tr/td/text()[3]",
    # "travail":"/html/body/table[3]/tbody/tr/td[2]/table/tbody/tr/td/text()[4]"
    "name": "Mon horoscope du jour",
    "url": "http://www.mon-horoscope-du-jour.com/horoscopes/quotidien/%s.htm",
    "amour": "/tbody/"
    # "amour": "/tbody/tr[2]/td[3]/p"
    }
]

usersigns = ["belier", "gemeaux", "balance"]

categories = ["amour"]
# categories = ["amour", "sante", "travail", "argent"]



for website in sources:
    for sign in usersigns:
        for category in categories:
            try:
                # print "Looking for %s %s on %s" % (sign, category, website["name"])
                page = requests.get(website["url"] % sign)
                tree = HTML.fromstring(page.text)
                amour = tree.xpath("//p")[2].text.strip()
                print amour.encode("utf-8")

            except SyntaxError as e:
                continue