import urllib, re,datetime,csv
import os, sys, string  
import MySQLdb
import socket
import urllib2
#from httplib import IncompleteRead
import httplib


class DB:
  conn = None

  def connect(self):
    self.conn = MySQLdb.connect(host='ec2union-cluster.cluster-c8tmmdxu2zy8.us-east-1.rds.amazonaws.com',user='victorcraft',passwd='ilove86415175',db='iosunion')

  def query(self, sql):
    try:
      cursor = self.conn.cursor()
      cursor.execute(sql)
    except (AttributeError, MySQLdb.OperationalError):
      self.connect()
      cursor = self.conn.cursor()
      cursor.execute(sql)
    return cursor
  def commit(self):
      self.conn.commit()


# timeout in seconds
socket.setdefaulttimeout(30)

today =datetime.date.today()
ISOFORMAT='%Y-%m-%d'

#baseCurrency=['CNY','EUR','GBP','HKD','JPY','MOP','NZD','SGD','THB','USD']
#transactionCurrency=['AED','AFN','AOA','ARS','AUD','AZN','BDT','BGN','BHD','BND','BRL','BSD','BWP','BYR','CDF','CHF','CLP','COP','CRC','CUC','CZK','DKK','DZD','EGP','ETB','FJD','GBP','GEL','GHS','GMD','GNF','HUF','IDR','ILS','INR','ISK','JOD','KES','KGS','KMF','KRW','KWD','KZT','LAK','LBP','LKR','MAD','MGA','MMK','MNT','MOP','MRO','MUR','MVR','MWK','MXN','MYR','NGN','NOK','NPR','OMR','PEN','PGK','PHP','PKR','PLN','QAR','RON','RUB','RWF','SAR','SCR','SDG','SEK','SLL','SRD','SSP','SYP','THB','TJS','TOP','TRY','TWD','TZS','UAH','UGX','UYU','UZS','VEF','VND','VUV','XAF','XOF','XPF','YER','ZAR','ZMK','ZMW']

baseCurrency=['CNY']
transactionCurrency=['NZD','USD']


url = 'http://www.unionpayintl.com/MainServlet'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
 'Accept':'text/html;q=0.9,*/*;q=0.8',
 'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
 'Accept-Encoding':'gzip',
 'Connection':'close',
 'Referer':None 
}



db=DB()
print "db loaded"

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
                print "the rate on",date,"is 1 ",base," = ",price,tran
            except urllib2.URLError as e:
                price=0.000
                print type(e)
            except socket.timeout as e:
                price=0.000
                print type(e)
            except httplib.IncompleteRead as e:
                price=0.000
                print type(e)

        sql = "insert into `unionpay`(`date`,`base`,`transact`,`currency`) values ('%s','%s','%s',%f)" % (date,base,tran,price)
        print sql
        try:  
            db.query(sql)
            db.commit()
            print   "insert done"
        except Exception, e:  
            print e  
        
                    
        i+=1     
    k+=1
