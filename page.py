import urllib
import urllib2
import re
import time
import types 
import tool
from bs4 import BeautifulSoup
 
#抓取分析某一问题和答案
class Page:
    
    def __init__(self):
        self.tool = tool.Tool()
    
    #获取当前时间
    def getCurrentDate(self):
        return time.strftime('%Y-%m-%d',time.localtime(time.time()))
    
    #获取当前时间
    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))
 
    #通过页面的URL来获取页面的代码
    def getPageByURL(self, url):
        try:
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read().decode("utf-8") 
        except urllib2.URLError, e:
