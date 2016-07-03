import urllib, re,datetime,csv
import os, sys, string  
import MySQLdb
import socket
import urllib2
#from httplib import IncompleteRead
import httplib
import country



# timeout in seconds
socket.setdefaulttimeout(30)

today =datetime.date.today().isoformat()

#baseCurrency=['CNY','EUR','GBP','HKD','JPY','MOP','NZD','SGD','THB','USD']
#transactionCurrency=['CNY','EUR','GBP','HKD','JPY','MOP','NZD','SGD','THB','USD','AED','AFN','AOA','ARS','AUD','AZN','BDT','BGN','BHD','BND','BRL','BSD','BWP','BYR','CDF','CHF','CLP','COP','CRC','CUC','CZK','DKK','DZD','EGP','ETB','FJD','GBP','GEL','GHS','GMD','GNF','HUF','IDR','ILS','INR','ISK','JOD','KES','KGS','KMF','KRW','KWD','KZT','LAK','LBP','LKR','MAD','MGA','MMK','MNT','MOP','MRO','MUR','MVR','MWK','MXN','MYR','NGN','NOK','NPR','OMR','PEN','PGK','PHP','PKR','PLN','QAR','RON','RUB','RWF','SAR','SCR','SDG','SEK','SLL','SRD','SSP','SYP','THB','TJS','TOP','TRY','TWD','TZS','UAH','UGX','UYU','UZS','VEF','VND','VUV','XAF','XOF','XPF','YER','ZAR','ZMK','ZMW']

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


conn = MySQLdb.Connection(host='ec2union-cluster.cluster-c8tmmdxu2zy8.us-east-1.rds.amazonaws.com',user='victorcraft',passwd='ilove86415175',db='iosunion')
cursor = conn.cursor()

sql="SELECT * FROM `unionpay` WHERE date=%s" % (today)

try:
    cursor.execute(sql)
    results=cursor.fetchall()
    print "done fetch"

    for row in results:
        ID = row[0]
        date = row[1]
        base = row[2]
        transaction = row[3]
        currency = round(row[4],4)
        # Now print fetched result
        print "ID = %d, date=%s, base=%s, transaction=%s, price=%f" % (ID, date, base, transaction, currency)
        data= {'baseCurrency': base, 'transactionCurrency':transaction, 'curDate':date,'go':'BIZTOOL_MERCHANT_PG_exchangeRateEn'}
        request = urllib2.Request(url=url,data=urllib.urlencode(data),headers=headers)
        try:
            response = urllib2.urlopen(request,timeout=30).read()
            regex = '                \t\t'+'(.+?)&nbsp;'+base
            pattern = re.compile(regex)
            price_temp = re.findall(pattern,response)[0]
            price=float(price_temp)
        except urllib2.URLError as e:
            price=0.000
            print type(e)
        except socket.timeout as e:
            price=0.000
            print type(e)
        except httplib.IncompleteRead as e:
            price=0.000
            print type(e)
        
        sql2="UPDATE `unionpay`  SET `currency` =%f WHERE ID=%d" %(price,ID)
        try:
            cursor.execute(sql2)
            conn.commit()
            print sql2
        except Exception, e:
            print e

except:
    print "Error: unable to fecth data"

cursor.close()
conn.close()