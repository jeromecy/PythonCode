import urllib, urllib2,re,datetime,csv,string

today =datetime.date.today()
ISOFORMAT='%Y-%m-%d'
#date= today -deltadays

#baseCurrency=['CNY','EUR','GBP','HKD','JPY','MOP','NZD','SGD','THB','USD']
baseCurrency=['CNY','EUR']
transactionCurrency=['CAD','CNY']
#transactionCurrency=['AED','AFN','AOA','ARS','AUD','AZN','BDT' 'BGN' 'BHD' 'BND' 'BRL' 'BSD','BWP','BYR' 'CAD','CDF','CHF','CLP','CNY','COP','CRC','CUC','CZK','DKK','DZD','EGP','ETB','EUR','FJD','GBP','GEL','GHS','GMD','GNF','HKD','HUF','IDR','ILS','INR','ISK','JOD','JPY','KES','KGS','KMF','KRW','KWD','KZT','LAK','LBP','LKR','MAD','MGA','MMK','MNT','MOP','MRO','MUR','MVR','MWK','MXN','MYR','NGN','NOK','NPR','NZD','OMR','PEN','PGK','PHP','PKR','PLN','QAR','RON','RUB','RWF','SAR','SCR','SDG','SEK','SLL','SRD','SSP','SYP','THB','TJS','TOP','TRY','TWD','TZS','UAH','UGX','USD','UYU','UZS','VEF','VND','VUV','XAF','XOF','XPF','YER','ZAR','ZMK','ZMW']

url = 'http://www.unionpayintl.com/MainServlet'

#headers = {  
#    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  
#}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
 'Accept':'text/html;q=0.9,*/*;q=0.8',
 'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
 'Accept-Encoding':'gzip',
 'Connection':'close',
 'Referer':None #注意如果依然不能抓取的话，这里可以设置抓取网站的host
}

for j in range(0,2):
      deltadays =datetime.timedelta(days=j)
      date= today-deltadays
      k=0
      while k<len(baseCurrency):
            base=baseCurrency[k]
            i=0
            while i<len(transactionCurrency):
                  tran=transactionCurrency[i]                                          
                  data= {'baseCurrency': base, 'transactionCurrency':transactionCurrency[i], 'curDate':date,'go':'BIZTOOL_MERCHANT_PG_exchangeRateEn'}
                                
                  if base==tran:
                        price=['1']
                        print "the rate on",date,"is 1 ",base," = 1",tran
                  else:
                        #response = urllib2.urlopen(url,urllib.urlencode(data),timeout=10).read()
                        request = urllib2.Request(url=url,data=urllib.urlencode(data),headers=headers)  
                        #request.add_header('User-Agent', 'fake-client')  
                        response = urllib2.urlopen(request,timeout=30).read()

                        regex = '                \t\t'+'(.+?)&nbsp;'+base
                        pattern = re.compile(regex)
                        price_temp = re.findall(pattern,response)
                        #price=float(price_temp)
                        price=price_temp
                        print "the rate on",date,"is 1 ",base," = ",price,tran

                  with open('unicur.csv','ab+') as csvfile:
                        spamwriter = csv.writer(csvfile,dialect='excel')
                        spamwriter.writerow([date]+[base]+[tran]+price)
                        csvfile.close()
                  i+=1     
            k+=1
#print response
