import urllib, re,datetime
import os, sys, string
import socket
import urllib2
import httplib
import re

# timeout in seconds
socket.setdefaulttimeout(30)

def chunks(arr, n):
    return [arr[i:i+n] for i in range(0, len(arr), n)]

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
 'Accept':'text/html;q=0.9,*/*;q=0.8',
 'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
 'Accept-Encoding':'utf-8',
 'Connection':'close',
 'Referer':None 
}

#for NO in range(1513,1618):
for NO in range(1618,1618):
      url = 'https://mylotto.co.nz/lotto/results/?draw='+str(NO)
      request = urllib2.Request(url=url,headers=headers)                 
      try:
            response = urllib2.urlopen(request,timeout=30)
            page = response.read()
            regex= '<span class="lottoResultsBall lottoBallNumber-(.+?)">'
            #print regex
            pattern = re.compile(regex)
            #print pattern.pattern
            numbers = re.findall(pattern,page)
            #print int(numbers[0])
            #print int(numbers[1])
            #print numbers
      except urllib2.URLError as e:
          print type(e)
      except socket.timeout as e:
          print type(e)
      except httplib.IncompleteRead as e:
          print type(e)

      op=str(NO)
      for i in range(0,len(numbers)):
          op=op+','+str(numbers[i])
      #print op

      file1=open('lotto.txt','a')
      file1.write(op+'\n') 
      file1.close()

print "work done"
###1513-->['05', '10', '11', '14', '15', '18', '37', '07', '10', '15', '14', '05']













