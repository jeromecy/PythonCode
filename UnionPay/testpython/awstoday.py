import urllib, re,datetime
import os, sys, string
import socket
import urllib2
#from httplib import IncompleteRead
import httplib
from DB import DB
import country


# timeout in seconds
socket.setdefaulttimeout(30)

today =datetime.date.today()
ISOFORMAT='%Y-%m-%d'


baseCurrency=country.base
transactionCurrency=country.trans


url = 'http://www.unionpayintl.com/MainServlet'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
 'Accept':'text/html;q=0.9,*/*;q=0.8',
 'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
 'Accept-Encoding':'gzip',
 'Connection':'close',
 'Referer':None 
}



db=DB()

deltadays=datetime.timedelta(days=0)
date=today-deltadays
k=0
while k<len(baseCurrency):
    base=baseCurrency[k]
    i=0
    while i<len(transactionCurrency):
        tran=transactionCurrency[i]
        data= {'baseCurrency': base, 'transactionCurrency':transactionCurrency[i], 'curDate':date,'go':'BIZTOOL_MERCHANT_PG_exchangeRateEn'}
        if base==tran:
            price=1.000
            print "the rate on",date,"is 1 ",base," = 1",tran
        else:             
            request = urllib2.Request(url=url,data=urllib.urlencode(data),headers=headers)                
            try:
                response = urllib2.urlopen(request,timeout=30).read()
                regex = '                \t\t'+'(.+?)&nbsp;'+base
                pattern = re.compile(regex)
                price_temp = re.findall(pattern,response)[0]
                price=float(price_temp)
                #print "the rate on",date,"is 1 ",base," = ",price,tran
            except urllib2.URLError as e:
                price=0.000
                print type(e)
            except socket.timeout as e:
                price=0.000
                print type(e)
            except httplib.IncompleteRead as e:
                price=0.000
                print type(e)

#sql = "insert into unionpay(date,base,transact,currency) values ('%s','%s','%s',%s)" % (date,base,tran,price)
        sql = "insert into `unionpay`(`date`,`base`,`transact`,`currency`) values ('%s','%s','%s',%f)" % (date,base,tran,price)

        try:  
            db.query(sql)
            db.commit()
        except Exception, e:  
            print e  
        
                    
        i+=1     
    k+=1
