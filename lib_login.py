# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("http://140.131.94.8/uhtbin/cgisirsi/x/x/0/49/")
        driver.find_element_by_id("user_id").click()
        driver.find_element_by_id("user_id").clear()
        driver.find_element_by_id("user_id").send_keys("072214130")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("CHANGEME")
        driver.find_element_by_xpath(u"//input[@value='登入']").click()
        driver.find_element_by_link_text(u"新書通告").click()
        driver.find_element_by_link_text(u"新書通告 - 總館").click()
        driver.find_element_by_link_text(u"新書-2020年").click()
        driver.find_element_by_link_text(u"新書-2020年 4月份").click()
        driver.find_element_by_link_text(u"新書-2020年 4月份中文書").click()
    
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
