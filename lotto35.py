# -*- coding: utf-8 -*-
## this is python 3.5
import urllib.request
import urllib.parse
import re
import ssl
import pandas as pd
import requests
import matplotlib.pyplot as plt

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

user_agent    = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
headers       = {'User-Agent': user_agent}

datahead      = ['DrawNumber','Number1','Number2','Number3','Number4','Number5',\
                'Number6','Bonus','Power']

address       = 'C:/Users/zcao/Documents/unionpay/lotto.txt'
lotto         = pd.read_table(address, sep=",",header=None)
lotto.columns = datahead
sofar         = lotto['DrawNumber'][0]
rows          = len(lotto)

session = requests.Session()

new_headers = { 'Host': 'apigw.mylotto.co.nz',
           'Connection': 'keep-alive',
           'Accept': 'application/json, text/plain, */*',
           'Origin': 'https://mylotto.co.nz',
           'X-Requested-With': 'XMLHttpRequest',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'https://mylotto.co.nz/results',
            'Accept-Encoding': 'gzip, deflate, sdch, br',
            'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh-TW;q=0.4'
        }

thisnumber = 1643
counts = 0
while(thisnumber > sofar):
    numbers  = []
    url      = 'https://apigw.mylotto.co.nz/api/results/v1/results/lotto/'+str(thisnumber)
    req      = urllib.request.Request(url=url)
    response = urllib.request.urlopen(req)
    page     = response.read().decode('utf-8')
    regex1   = '\n        "(.*?)",'
    regex2   ='\n        "(.*?)"\n      ],\n      "bonusBalls": "(.*?)"\n'
    regex3   = '"powerballWinningNumber": "(.*?)",\n'
    pattern  = re.compile(regex1)
    numbers  = re.findall(pattern,page)[0:5]
    pattern  = re.compile(regex2)
    numbers.extend(list(re.findall(pattern,page)[0]))
    pattern  = re.compile(regex3)
    numbers.extend(re.findall(pattern,page))    
    #print(numbers)   
    #print(thisnumber)
    numbers.insert(0,thisnumber)
    lotto.loc[rows + counts] = numbers
    counts += 1
    thisnumber = thisnumber - 1
      
print("work done")

lotto              = lotto.drop_duplicates('DrawNumber')
reverselotto       = lotto.sort_values(by = 'DrawNumber',ascending = 0)
reverselotto.index = range(len(reverselotto))

## lotto = lotto.iloc[:,0:9]

open(address, 'w').close()
for ctr in range(len(reverselotto)):
    output  = ''
    for m in range(len(reverselotto.loc[ctr])):
        output = output + str(reverselotto[datahead[m]].loc[ctr])+','
    output  = output[:-1]    
    file1   = open(address,'a')
    file1.write(output +'\n') 
    file1.close()

print('complete')

plt.subplot(3, 3, 1)
plt.hist(list(map(int,lotto['Number1'])))
plt.title("Number 1")
plt.subplot(3, 3, 2)
plt.hist(list(map(int,lotto['Number2'])))
plt.title("Number 2")
plt.subplot(3, 3, 3)
plt.hist(list(map(int,lotto['Number3'])))
plt.title("Number 3")
plt.subplot(3, 3, 4)
plt.hist(list(map(int,lotto['Number4'])))
plt.title("Number 4")
plt.subplot(3, 3, 5)
plt.hist(list(map(int,lotto['Number5'])))
plt.title("Number 5")
plt.subplot(3, 3, 6)
plt.hist(list(map(int,lotto['Number6'])))
plt.title("Number 6")
plt.subplot(3, 3, 7)
plt.hist(list(map(int,lotto['Bonus'])))
plt.title("Bonus")
plt.subplot(3, 3, 8)
plt.hist(list(map(int,lotto['Power'])))
plt.title("PowerBall")
plt.savefig("hist.pdf")
plt.show()