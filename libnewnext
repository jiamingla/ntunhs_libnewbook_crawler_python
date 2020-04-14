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
import re
import math
class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        
        chrome_options = Options()
        chrome_options.add_argument("--headless")       # define headless
        #self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver = webdriver.Chrome()

        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("http://140.131.94.8/")
        driver.find_element_by_link_text(u"新書通告").click()
        driver.find_element_by_link_text(u"新書通告 - 總館").click()
        driver.find_element_by_link_text(u"新書-2020年").click()
        driver.find_element_by_link_text(u"新書-2020年 4月份").click()
        driver.find_element_by_link_text(u"新書-2020年 4月份中文書").click()
        html = driver.page_source
        soup = BeautifulSoup(html, features='lxml')
        searchnum = soup.find('div', {"class": 'searchsummary'})
        em = searchnum.find_all('em')              # use searchnum as a parent
        for d in em:
            print('共{:s}筆資料'.format(d.get_text()))
        pagenum = math.ceil(int(d.get_text()) / 20)
        
        list = []

        for i in range(pagenum) :
            print('第{:d}頁'.format(i+1))
            html = driver.page_source
            soup = BeautifulSoup(html, features='lxml')
            hit_list = soup.find_all('li','hit_list_item_info')
            for list in hit_list:
                print([s for s in list.stripped_strings])
                #print(list.a.text.strip())

            """
            course_links = soup.find_all('a', {'href': re.compile('(callnum)')})
            for link in course_links:
                str = link['href'][53:].split('&')
                #list.append(str)
                print(str)
            """
            driver.find_element_by_link_text(">>").click()
            
        #print(list)
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
    unittest.main()
