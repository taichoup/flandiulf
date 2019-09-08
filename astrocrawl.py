#!/usr/bin/python

import os, codecs, json, shutil

JSON_PATH_STRING = "out/"
# JSON_PATH_STRING = "out_tests/"

spiders = [
    "asia",
    "elle",
    "jdf",
    "hfr",
    "mhdj",
    "paris", 
    "marieclaire",
    "idealvoyance"
    ]

# delete json exports first because scrapy can't do it on its own
if os.path.exists("out/"):
    shutil.rmtree("out/")


def scrape_and_populate_jsons():
    ''' populate the files with scraped data'''

    for s in spiders:

        print "======= Running the %s spider =======" % s

        # os.system("scrapy crawl %s -o %s%s.json -t json" % (JSON_PATH_STRING, s, s))
        os.system("env/bin/scrapy crawl %s -o %s%s.json -t json" % (s, JSON_PATH_STRING, s)) # running scrapy from the virtual environment
        
        print "======= Finished with the %s spider =======" % s




def aggregate_for_front_end(p):
    '''aggregate the data in one big file to use in front end'''

    data = []
    for s in spiders:

        with codecs.open("%s%s.json" % (p, s), "r") as _file:
            jsonstring = _file.read()
            jsondata = json.loads(jsonstring)

            for item in jsondata:

                if item["love"]:
                    data.append({"category": "amour", "content": item["love"], "sign": item["sign"], "source": item["source"], "timestamp": item["timestamp"]})

                if item["money"]:
                    data.append({"category": "argent", "content": item["money"], "sign": item["sign"], "source": item["source"], "timestamp": item["timestamp"]})

                if item["work"]:
                    data.append({"category": "travail", "content": item["work"], "sign": item["sign"], "source": item["source"], "timestamp": item["timestamp"]})

                if item["health"]:
                    data.append({"category": "sante", "content": item["health"], "sign": item["sign"], "source": item["source"], "timestamp": item["timestamp"]})


    with codecs.open("astrodump2.json", "w") as outfile:

        json.dump(data, outfile, encoding="utf-8", sort_keys=True, indent=4, separators=(',', ': '))




scrape_and_populate_jsons() # not needed in tests mode

aggregate_for_front_end(JSON_PATH_STRING)