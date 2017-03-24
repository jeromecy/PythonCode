import datetime
import os, sys, string
import socket
#from DB import DB  ## database MySQL
#import country  ### all countries.
import urllib.request
import urllib.parse
import re
import ssl
import json
from scrapy.http import FormRequest


# timeout in seconds
socket.setdefaulttimeout(30)

today = datetime.date.today()
ISOFORMAT='%Y-%m-%d'

#url = 'http://www.unionpayintl.com/MainServlet'
#url = 'http://www.unionpayintl.com/upiweb-card/serviceCenter/rate?language=cn'
url = 'http://www.unionpayintl.com/upiweb-card/serviceCenter/rate/search'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
 'Accept':'text/html;q=0.9,*/*;q=0.8',
 'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
 'Accept-Encoding':'gzip',
 'Connection':'close',
 'Referer':None,
 'X-Requested-With': 'XMLHttpRequest'
}

base = 'CNY'
tran = 'NZD'


deltadays = datetime.timedelta(days=0)
date      = today-deltadays

for j in range(1):  #date from today to X days before
    deltadays = datetime.timedelta(days=j)
    date      = today - deltadays
    i=0
    while i<len(transactionCurrency):
        data = {'baseCurrency': base, 'transactionCurrency':tran, 'curDate':date}
        req  = urllib.request.Request(url = url,data = urllib.parse.urlencode(data),headers=headers)                
        
        req = FormRequest(url = url,callback = self.json_parser,formdata = data)
        
        try:
            response = urllib.request.urlopen(req,timeout=30).read().decode('utf-8')
            regex = '                \t\t'+'(.+?)&nbsp;'+base
            pattern = re.compile(regex)
            price_temp = re.findall(pattern,response)[0]
            price=float(price_temp)
        except urllib.URLError as e:
            price=0.000
            print type(e)
        except socket.timeout as e:
            price=0.000
            print type(e)
        except httplib.IncompleteRead as e:
            price=0.000
            print type(e)
           
        file1=open('unionpay.txt','a')
        file1.write(op+'\n') 
        file1.close()
                    
        i+=1     
    k+=1




json_url = 'http://www.unionpayintl.com/upiweb-card/serviceCenter/rate?curDate=2017-03-24&baseCurrency=CNY&transactionCurrency=NZD'

r = requests.get(json_url).text

from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
import requests
import re, json

import scrapy


class unionpyItem(scrapy.Item):
    baseCurrency        = scrapy.Field()
    transactionCurrency = scrapy.Field()
    exchangeRate        = scrapy.Field()


class unionpayPipeline(object):
    def process_item(self, item, spider):
        return item
    
    
    
    
    
    
    
    
    
    
    
data = {'baseCurrency':"AUD",'createDate':1490284800000,
        'createUser':55,'curDate':1490284800000,'exchangeRate':1.314720147,
        'exchangeRateId':185401,'transactionCurrency':"USD",
        'transactionCurrencyOption':'null',
        'updateDate':1490284800000,'updateUser':55}
    
    
jason_url = 'http://www.unionpayintl.com/upiweb-card/serviceCenter/rate/search'   

url = 'http://www.unionpayintl.com/upiweb-card/serviceCenter/rate/search HTTP/1.1'  

url2 = 'http://www.unionpayintl.com/upiweb-card/serviceCenter/rate/search'
   
req = requests.post(url,data)

req = requests.get(jason_url)

req = requests.post(url2, data=data, headers=headers)    
    
    
req  = urllib.request.Request(url = url,data = urllib.parse.urlencode(data),headers=headers)                
           
    
    
    
    
    
    
    