#!/usr/bin/python

import os, codecs, json, shutil

spiders = [
    "asia",
    "elle",
    "jdf",
    "hfr",
    "mhdj",
    "paris"
    ]

# delete json exports first because scrapy can't do it on its own
shutil.rmtree("out/")

# populate the files with scraped data
for s in spiders:
    print "======= Running the %s spider =======" % s
    # os.system("scrapy crawl %s -o astrocrawl3.json -t json" % s) #--> mauvaise idee, ne gere pas bien l'appending json
    os.system("scrapy crawl %s -o out/%s.json -t json" % (s, s))
    print "======= Finished with the %s spider =======" % s



# aggregate the data in one big file to use in front end
data = []
for s in spiders:
    with codecs.open("out/%s.json" % s, "r") as _file:
        jsonstring = _file.read()
        jsondata = json.loads(jsonstring)
        for item in jsondata:
            data.append({"category": "amour", "content": item["love"], "sign": item["sign"], "source": item["source"], "timestamp": item["timestamp"]})
            data.append({"category": "argent", "content": item["money"], "sign": item["sign"], "source": item["source"], "timestamp": item["timestamp"]})
            data.append({"category": "travail", "content": item["work"], "sign": item["sign"], "source": item["source"], "timestamp": item["timestamp"]})
            data.append({"category": "sante", "content": item["health"], "sign": item["sign"], "source": item["source"], "timestamp": item["timestamp"]})


with codecs.open("astrodump2.json", "w") as outfile:

    json.dump(data, outfile, encoding="utf-8", sort_keys=True, indent=4, separators=(',', ': '))