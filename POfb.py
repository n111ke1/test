from  selenium import webdriver
import time



email = "a" + str(time.strftime('%H%M')) + "@asd.com"

class Feedback(object):
    def __init__(self, driver):
        self.driver = driver

    def NAME(self, name):
        self.driver.find_element_by_id("NAME").clear()
        self.driver.find_element_by_id("NAME").send_keys(name)

    def EMAIL(self, email):
        self.driver.find_element_by_id("EMAIL").clear()
        self.driver.find_element_by_id("EMAIL").send_keys(email)

    def TEXT(self, text):
        self.driver.find_element_by_id("TEXT").clear()
        self.driver.find_element_by_id("TEXT").send_keys(text)

    def submit(self):
        self.driver.find_element_by_id("feedback-submit").click()
    def button(self):
        self.driver.find_element_by_id("feedback-submit")
    def EMAIL1(self, name):
        self.driver.find_element_by_id("")


    # def EMAIL_ADMIN(self, email):
    #     email = "a" + str(time.strftime('%H%M')) + "@asd.com"