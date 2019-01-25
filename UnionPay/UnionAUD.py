import datetime
import socket
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

socket.setdefaulttimeout(30)

today = datetime.date.today()
ISOFORMAT='%Y-%m-%d'

headers = { 'Host': 'www.unionpayintl.com',
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

url     = 'http://www.unionpayintl.com/cardholderServ/serviceCenter/rate/search'
base    = "CNY"
tran    = "AUD"
address = 'C:/Users/279302D/OneDrive - Curtin/Documents/Personal/Python/UnionPay/aud.txt'
rateData = pd.read_table(address, sep=",",names = ["date", "base", "tran", "rate"])
sofar    = rateData['date'][0]
rows     = len(rateData)

session = requests.Session()

j     = 0
sofar = datetime.datetime.strptime(sofar, "%Y-%m-%d").date()
date  = sofar + datetime.timedelta(days=1)
while(date < today):
    if(date.weekday()<5):
        pop = session.post(url, headers = headers , data = {
                'curDate': str(date),
                'baseCurrency': base,
                'transactionCurrency': tran
                })
    #exRate = str(date) +','+ base +','+ tran +','+  str(pop.json()['exchangeRate'])     
    try:
        pop.json()
        rateData.loc[rows+j] = [str(date),base,tran,str(pop.json()['exchangeRate'])]
    except ValueError:
        print('Decoding JSON has failed')
        rateData.loc[rows+j] = [str(date),base,tran,rateData.loc[rows+j-1]['rate']]
  
    j+= 1
    date  = date + datetime.timedelta(days=1)    
print('done')



rateData           = rateData.drop_duplicates('date')
#rateData['date'] = pd.to_datetime(rateData.date)
reversedData       = rateData.sort_values(by = 'date',ascending = 0)
reversedData.index = range(len(reversedData))

exRate     = '' 
open(address, 'w').close()
for ctr in range(len(reversedData)):
    exRate = str(reversedData['date'].loc[ctr]) +','+ 'CNY'+','+ 'AUD'+','+ \
                str(reversedData['rate'].loc[ctr])
    file1  = open(address,'a')
    file1.write(exRate +'\n') 
    file1.close() 
print('complete')



rateData         = pd.read_table(address, sep=",")
rateData.columns = ["date", "CNY", "AUD", "rate"]
#plt.plot(rateData['rate'])
rateData[rateData.duplicated('date')==True]
rateData = rateData.drop_duplicates('date')
reversedData = rateData.iloc[::-1]  # reverse Data 
reversedData = rateData.sort_index(axis=0,ascending=False)
reversedData.index = range(len(rateData))

k = np.arange(0, reversedData.shape[0], 270)

plt.plot(reversedData['rate'])
plt.xticks(k,reversedData['date'][k])
plt.savefig('figAUD.pdf')

