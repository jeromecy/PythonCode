import urllib2
import re

symbolist=["aapl","spy","goog","nflx"]

i=0

while i<len(symbolist):
    url= "https://nz.finance.yahoo.com/q?s="+symbolist[i]
    htmlfile = urllib2.urlopen(url)
    htmltext = htmlfile.read()
    regex = '<span id="yfs_l84_'+symbolist[i]+'">(.+?)</span>'
    pattern = re.compile(regex)
    price = re.findall(pattern,htmltext)
    print "the price of",symbolist[i], "is ",price
    i+=1
