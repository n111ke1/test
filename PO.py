
import time
email = "a" + str(time.strftime('%H%M')) + "@asd.com"
ID_NAME = "NAME"
ID_EMAIl = "EMAIL"
ID_TEXT = "TEXT"


class Feedback(object):

    def __init__(self, driver):
        self.driver = driver

    def ID(self, id):
        return self.driver.find_element_by_id(id)

    def CLEAR_BY_ID(self, id):
        self.driver.find_element_by_id(id).clear()

    def SEND_KEYS(self, id, key,):
        self.driver.find_element_by_id(id).send_keys(key)

    def CLICK_BY_ID(self,id):
        self.driver.find_element_by_id(id).click()

    def CLICK_BY_CLASS(self,id):
        self.driver.find_element_by_class_name(id).click()

    def CLASS_NAME(self, class_name):
        self.driver.find_element_by_class_name(class_name)

    def SEND_TIME_EMAIL(self, id, email):
        self.driver.find_element_by_id(id).send_keys(email)

    def CHECK_TIMER(self):
        self.CLEAR_BY_ID("NAME")
        self.SEND_KEYS("NAME", "Измаил")
        self.CLEAR_BY_ID("EMAIL")
        self.SEND_TIME_EMAIL("EMAIL", email)
        self.SEND_KEYS("TEXT", "some text")
        self.CLICK_BY_ID("feedback-submit")