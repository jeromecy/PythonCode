# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
## this is python 3.5
import urllib.request
import urllib.parse
import re
import ssl

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# timeout in seconds

def chunks(arr, n):
    return [arr[i:i+n] for i in range(0, len(arr), n)]

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
headers = {'User-Agent': user_agent}

#for NO in range(1513,1618):
for NO in range(1610,1618):
    url = 'https://mylotto.co.nz/lotto/results/?draw='+str(NO)
    req = urllib.request.Request(url=url)                 
    
    response = urllib.request.urlopen(req)
    page = response.read().decode('utf-8')
    regex= '<span class="lottoResultsBall lottoBallNumber-(.*)">'
    #print regex
    pattern = re.compile(regex)
    #print pattern.pattern
    numbers = re.findall(pattern,page)
    #print int(numbers[0])
    #print int(numbers[1])
    #print(numbers)


    op=str(NO)
    for i in range(0,len(numbers)):
        op=op+','+str(numbers[i])
    #print(op)

    file1=open('lotto.txt','a')
    file1.write(op+'\n') 
    file1.close()
      
print("work done")



