# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.options import Options
import unittest, time, re
from bs4 import BeautifulSoup
import urllib.request
import re
import math
import json
import datetime
datetime_dt = datetime.datetime.today().date()
class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        
        chrome_options = Options()
        chrome_options.add_argument("--headless")       # define headless
        chrome_options.add_argument('log-level=2') #減少不必要的警告訊息
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        #self.driver = webdriver.Chrome()
        
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("http://140.131.94.8/")
        driver.find_element_by_link_text(u"新書通告").click()
        sp_or_xm = "總館"
        driver.find_element_by_link_text(u"新書通告 - "+sp_or_xm).click()
        year = datetime_dt.year
        month = datetime_dt.month
        driver.find_element_by_link_text(u"新書-"+str(year)+"年").click()
        driver.find_element_by_link_text(u"新書-"+str(year)+"年 "+str(month)+"月份").click()
        booklist = []
        language_name = ["中文書","西文書","視聽"] #有三種書籍類型
        for name in language_name: #三種都來一次
            try : #你先試試看
                language = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT,u"新書-"+str(year)+"年 "+str(month)+"月份"+name)))
                #driver在這找值，預設是最多隱性等待10秒
                language.click()    
            except NoSuchElementException: 
                print(str(year)+"年 "+str(month)+"月"+name+"沒有館藏")
            except TimeoutException: #多半是等到沒耐心了才拋出例外
                print(str(year)+"年 "+str(month)+"月"+name+"沒有館藏")
            else :
                html = driver.page_source
                soup = BeautifulSoup(html, features='html.parser')
                
                if soup.find('strong').text == "沒有館藏":
                    print(str(year)+"年 "+str(month)+"月"+name+"沒有館藏")
                    driver.find_element(By.CSS_SELECTOR, ".button").click()
                else:
                    searchnum = soup.find('div', {"class": 'searchsummary'})
                    em = searchnum.find_all('em')              # use searchnum as a parent
                    for d in em:
                        print(name +'共{:s}筆資料'.format(d.get_text()))
                    pagenum = math.ceil(int(d.get_text()) / 20)
                    
                    for i in range(pagenum) :
                        print('第{:d}頁'.format(i+1))
                        html = driver.page_source
                        soup = BeautifulSoup(html, features='html.parser')
                        hit_list = soup.find_all('li','hit_list_item_info')
                        for list in hit_list:
                            #print([s for s in list.stripped_strings])#這是有全部資料的
                            booklist.append([s for s in list.stripped_strings])
                            #print([s for s in list.stripped_strings][1])#這是只有書名的
                            #print(list.a.text.strip())
                        if(i == pagenum-1):break
                        if(driver.find_element_by_link_text(">>")):
                            driver.find_element_by_link_text(">>").click()
                    driver.find_element_by_link_text(u"返回").click() #點返回回到書籍類型
        
        driver.close() #關閉瀏覽器
        with open(str(year)+str(month)+".json", 'w+', encoding='utf-8') as f:
                json.dump(booklist, f, indent=2, sort_keys=True, ensure_ascii=False)   
                print("已寫入資料到"+str(year)+str(month)+".json，88") 
    #下面是當你遇到錯誤時該如何處理的預設事件            
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
