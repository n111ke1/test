import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from POfb import Feedback
import POfb
from selenium.webdriver.support import expected_conditions
import time
import xmlrunner


class Feed(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('D:\INSTALL\chromedriver_win32 (1)\chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("http://gutfin2.typical.dev.flustex.com/feedback")

    def test_2_button_disabled(self):
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.ID, "feedback-submit")))
        button = driver.find_element_by_id("feedback-submit")
        assert button.get_attribute("disabled")
        driver.find_element_by_id("NAME").send_keys("Итан")
        driver.find_element_by_id("feedback-submit")
        assert button.get_attribute("disabled")
        driver.find_element_by_id("NAME").clear()
        driver.find_element_by_id("EMAIL").send_keys("qwe@dfg.com")
        assert button.get_attribute("disabled")
        driver.find_element_by_id("EMAIL").clear()
        driver.find_element_by_id("TEXT").send_keys("rgdrgdrgdrgdrgdrgdgd")
        assert button.get_attribute("disabled")