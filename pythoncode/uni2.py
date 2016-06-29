import urllib, urllib2,re,datetime,csv

today =datetime.date.today()
ISOFORMAT='%Y-%m-%d'
#date= today -deltadays

baseCurrency=['CNY','EUR','GBP','HKD','JPY','MOP','NZD','SGD','THB','USD']
#transactionCurrency=['CAD','CNY','HKD','EUR','JPY','NZD','USD']
transactionCurrency=['HKD','EUR','JPY','NZD','USD']

url = 'http://www.unionpayintl.com/MainServlet'

headers = {  
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  
}

i=0

while i<len(transactionCurrency):
      for j in range(15,16):
            deltadays =datetime.timedelta(days=j)
            date= today -deltadays
            data= {'baseCurrency': 'CNY', 'transactionCurrency':transactionCurrency[i], 'curDate':date,'go':'BIZTOOL_MERCHANT_PG_exchangeRateEn'}
         
            #response = urllib2.urlopen(url,urllib.urlencode(data),timeout=10).read()

            request = urllib2.Request(url=url,data=urllib.urlencode(data),headers=headers)  
            #request.add_header('User-Agent', 'fake-client')  
            response = urllib2.urlopen(request,timeout=10).read()

            regex = '                \t\t'+'(.+?)&nbsp;CNY'
            pattern = re.compile(regex)
            price = re.findall(pattern,response)
            print "the rate on",date,"is 1 CNY=",price,transactionCurrency[i]

            #with open('unicur.csv','a') as csvfile:
            #      spamwriter = csv.writer(csvfile)
            #      spamwriter.writerow([date]+['CNY']+[transactionCurrency[i]]+price)
            #      csvfile.close()
      i+=1
      
#print response
