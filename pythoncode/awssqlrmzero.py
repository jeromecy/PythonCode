import urllib, re,datetime
import os, sys, string
import MySQLdb
import socket
import urllib2
import httplib
#import MySQLdb.cursors
import country


# timeout in seconds
socket.setdefaulttimeout(30)

today =datetime.date.today()
ISOFORMAT='%Y-%m-%d'
#date= today -deltadays

#baseCurrency=['CNY','EUR']
#baseCurrency=['CNY','EUR','GBP','HKD','JPY','MOP','NZD','SGD','THB','USD']
#transactionCurrency=['CAD','CNY','HKD','EUR','JPY','NZD','USD']
#transactionCurrency=['HKD','EUR','CNY']

baseCurrency=country.base
transactionCurrency=country.trans

url='http://www.unionpayintl.com/MainServlet'

#headers = {
#    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
#}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept':'text/html;q=0.9,*/*;q=0.8',
        'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding':'gzip',
                'Connection':'close',
                    'Referer':None
}



#db=DB()
conn = MySQLdb.connect(host='unionintokyo-cluster.cluster-cg6x01smgrfp.ap-northeast-1.rds.amazonaws.com',user='victorcraft',passwd='ilove86415175',db='unionpayTokyo')
cursor = conn.cursor()

sql="SELECT * FROM `unionpay` WHERE `currency`=0"
#sql="SELECT  *  FROM unionpay WHERE length(`currency`) <4 and `currency` != 1"

try:
    cursor.execute(sql)
    #conn.commit()
    #db.query(sql)
    results=cursor.fetchall()
    print "done fetch"
    #if results>0
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
        
        #sql2 = "insert into unionpay(date,base,transact,currency) values ('%s','%s','%s',%s)" % (date,base,tran,price)
        #sql2="UPDATE `unionpay`  SET `currency` =%d WHERE ID=%d and date=%s and 'base'=%s and `transact` =%s and `currency` =0" %(price,ID,date,base,transaction)
        sql2="UPDATE `unionpay`  SET `currency` =%f WHERE ID=%d" %(price,ID)
        try:
            cursor.execute(sql2)
            conn.commit()
            print sql2
        except Exception, e:
            print e
#else:
#print   "none 0"
except:
    print "Error: unable to fecth data"

cursor.close()
conn.close()