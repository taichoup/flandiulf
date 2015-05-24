 # coding: utf8
from __future__ import unicode_literals

import urllib
import lxml.html as HTML
import codecs
import os
import json
# from lxml.cssselect import CSSSelector
import cssselect


sources = [{
    "name":"20minutes.fr",
    "charset":"utf-8",
    "url":"http://horoscope.20minutes.fr/horoscope-jour-%s",
    "amour":"div[@id='ctn_horoscope_jour']/p[3]",
    # "amour":"//*[@id='ctn_horoscope_jour']/p[3]",
    "argent":"/html/body/table[3]/tbody/tr/td[2]/table/tbody/tr/td/text()[2]",
    "sante":"/html/body/table[3]/tbody/tr/td[2]/table/tbody/tr/td/text()[3]",
    "travail":"/html/body/table[3]/tbody/tr/td[2]/table/tbody/tr/td/text()[4]"
    }
]

usersigns = ["belier", "gemeaux", "balance", "scorpion", "sagittaire", "taureau", "vierge", "capricorne", "verseau", "lion", "cancer", "poissons"]

categories = ["amour"]
# categories = ["amour", "sante", "travail", "argent"]



for website in sources:
    for sign in usersigns:
        for category in categories:
            try:
                print "Looking for %s %s on %s" % (sign, category, website["name"])
                p = HTML.fromstring(urllib.urlopen(website["url"] % sign).read())
                print website[category]
                desc = p.find(website[category]).text.strip()
                if desc is not None:
                    print "found : %s" % desc
                else:
                    print "couldn't find a matching elt."

            except SyntaxError as e:
                continue