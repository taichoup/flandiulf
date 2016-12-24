import os

spiders = [
    "asia",
    "jdf",
    "hfr",
    "mhdj",
    "paris"
    ]

for s in spiders:
    print "Running the %s spider..." % s
    os.system("scrapy crawl %s -o %s.json -t json" % (s, s))
    print "Finished with the %s spider." % s