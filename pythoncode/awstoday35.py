import datetime
import os, sys, string
import socket
#from DB import DB
#import country
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
 'Referer':None 
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










class Handler(BaseHandler):
    def on_start(self):
        self.crawl('http://www.unionpayintl.com/upiweb-card/serviceCenter/rate/search?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0',
                   callback=self.json_parser)
    def json_parser(self, response):
        return [{
            "baseCurrency": x['baseCurrency'],
            "transactionCurrency": x['transactionCurrency'],
            "url": x['url']
        } for x in response.json['subjects']]