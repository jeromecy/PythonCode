import urllib2
import re

#symbolist=["aapl","spy","goog","nflx"]

#i=0

#while i<len(symbolist):

url= "http://www.unionpayintl.com/MainServlet"
htmlfile = urllib2.urlopen(url)
htmltext = htmlfile.read()
regex = "The exchange rate you inquired i"+"(.+?)&nbsp;CNY"
pattern = re.compile(regex)
price = re.findall(pattern,htmltext)
print "the rate is ",price
#i+=1
