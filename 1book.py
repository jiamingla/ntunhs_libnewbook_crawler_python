# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.options import Options
import unittest, time, re
from bs4 import BeautifulSoup
from urllib.request import urlopen
import math
import json
import sys

Link_to_page_URL = sys.argv[1:] #直接在run .py時加入"網址"就可以使用了

if (Link_to_page_URL == ""):
    print("未輸入網址")
class NTUNHSLibCrawler(object):
    def __init__(self,cmdline = None):
        chrome_options = Options()
        chrome_options.add_argument("--headless") 

        #----------#
        #self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver = webdriver.Chrome()
        #----------#
        self.driver.implicitly_wait(30)#先等等
        self.base_url = "https://www.google.com/"#起始URL
        self.verificationErrors = []
        self.accept_next_alert = True
        #我還不懂這兩行能幹嘛
        
        """
        這邊放整個爬蟲流程，去呼叫下面的函數
        """
        #爬資料
        
        self.parse_bookinfo(Link_to_page_URL[0])
        #存進去資料庫
        #
    def parse_bookinfo(self,Link_to_page_URL):
        #Keywword = 'python'
        #filename = Keyword +'.json'
        driver = self.driver
        driver.get(Link_to_page_URL)
        
        html = driver.page_source
        #得到當前發好session的網址
        soup = BeautifulSoup(html, features='html.parser')
        #丟到解析庫

        #只有一本書的時候
    
        bookdata = soup.find('ul', {"class": 'tab_panels pct70 detail_page'})
        list = [s for s in bookdata.stripped_strings]
        driver.implicitly_wait(1)
        try:
            driver.find_element_by_link_text("預約")
            print("可預約")
            driver.implicitly_wait(0)
        except NoSuchElementException as e:
            print("無預約")
        bookinfo = list[1:13]
        bookstatus = list[19:28]
        print(bookinfo)
        print(bookstatus)
        self.driver.close()#關閉瀏覽器
        return 0
    
            
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    c = NTUNHSLibCrawler()