import datetime
#import os, sys, string
import socket
#from DB import DB  ## database MySQL
#import country  ### all countries.
#import urllib.request
#import urllib.parse
#import re
#import ssl
#import json
#from scrapy.http import FormRequest
#from bs4 import BeautifulSoup
#from lxml.etree import fromstring
import requests
# timeout in seconds

import pandas as pd
import matplotlib.pyplot as plt



socket.setdefaulttimeout(30)

today = datetime.date.today()
ISOFORMAT='%Y-%m-%d'

url = 'http://www.unionpayintl.com/upiweb-card/serviceCenter/rate/search'

'''
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
 'Accept':'text/html;q=0.9,*/*;q=0.8',
 'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
 'Accept-Encoding':'gzip',
 'Connection':'close',
 'Referer':None,
 'X-Requested-With': 'XMLHttpRequest'
}
'''

new_headers = { 'Host': 'www.unionpayintl.com',
           'Proxy-Connection': 'keep-alive',
           'Content-Length': '59',
           'Accept': '*/*',
           'Origin': 'http://www.unionpayintl.com',
           'X-Requested-With': 'XMLHttpRequest',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'http://www.unionpayintl.com/upiweb-card/serviceCenter/rate?language=cn',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh-TW;q=0.4'
        }

url = 'http://www.unionpayintl.com/upiweb-card/serviceCenter/rate/search'
base = 'CNY'
tran = 'NZD'

deltadays = datetime.timedelta(days=0)
date      = today-deltadays

session = requests.Session()


for j in range(500,1001):  #date from today to X days before  0:1000
    exRate    = ''
    deltadays = datetime.timedelta(days=j)
    date      = today - deltadays
    pop       = session.post(url , headers = new_headers , data = {
                'curDate': date,
                'baseCurrency': base,
                'transactionCurrency': tran
                })
    
    exRate = str(date) +','+ base +','+ tran +','+  str(pop.json()['exchangeRate'])           
    file1  = open('unionpay.txt','a')
    file1.write(exRate +'\n') 
    file1.close()   
    
    

print('done')

rateData         = pd.read_table('unionpay.txt', sep=",")
plt.plot(rateData['rate'])
#rateData.columns = ["date", "CNY", "NZD", "rate"]
#rateData[rateData.duplicated('date')==True]
#rateData = rateData.drop_duplicates('date')
reversedData = rateData.iloc[::-1]  # reverse Data 
#reversedData = rateData.sort_index(axis=0,ascending=False)
reversedData.index = range(1001)
plt.plot(reversedData['rate'])
plt.xticks([0,250,500,750,1000],[reversedData['date'][0],reversedData['date'][250],
           reversedData['date'][500],reversedData['date'][750],reversedData['date'][1000]])
plt.show()

### this is an old method before system updating.
'''
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
'''