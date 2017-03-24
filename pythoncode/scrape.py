# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 10:48:08 2017

@author: zcao
"""

import json
import requests
from bs4 import BeautifulSoup

url = "http://www.unionpayintl.com/upiweb-card/serviceCenter/rate/search"


class currencyScraper(object):
    def __init__(self):
        self.search_request = {
            "curDate":"2017-03-25",
            "baseCurrency":"AUD",
            "transactionCurrency":"USD"
        }        

    def scrape(self):
        currencys = self.scrape_cur()
        for currency in currencys:
            print(currency)
    
    def scrape_cur(self, max_pages=3):
        currs = []
        payload = { 
            '$.ajax': json.dumps(self.search_request)
        }    
        r = requests.post(
            url     = 'http://www.unionpayintl.com/upiweb-card/serviceCenter/rate/search HTTP/1.1',
            data    = payload,
            headers = {
                'X-Requested-With': 'XMLHttpRequest'
            }
        )
     
        s = BeautifulSoup(r.text)
        #if not s.requisition:
        #   break
     
        for r in s.findAll('requisition'):
           curr = {}
           curr['baseCurrency'] = r.baseCurrency.text
           curr['exchangeRate'] = r.exchangeRate
           curr['transactionCurrency'] = r.transactionCurrency.text
           currs.append(curr)
           print(curr)
        return(r)



if __name__ == '__main__':
    scraper = currencyScraper()
    scraper.scrape()