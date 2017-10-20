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


    def test_1_open(self):
        driver = self.driver
        feedback = Feedback(driver)
        feedback.NAME("Антон")

        email = "a" + str(time.strftime('%H%M%S')) + "@asd.com"
        feedback.EMAIL(email)
        feedback.TEXT("some text")
        feedback.submit()
        WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, "success__mail"), email))
        # driver.get_screenshot_as_file('D:/screen_test/1.png')

    def test_2_button_disabled(self):
        driver = self.driver
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.ID, "feedback-submit")))
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


    def test_3_validation(self):
        driver = self.driver
        driver.implicitly_wait(10)
        name = driver.find_element_by_id("NAME")
        name.clear()
        name.click()
        email = driver.find_element_by_id("EMAIL")
        email.clear()
        email.click()
        WebDriverWait(self.driver, 10).\
            until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, "#NAME ~ .error-block"), "Пожалуйста, укажите ваше Имя"))
        # WebDriverWait(self.driver, 10). \
        #     until(expected_conditions.visibility_of_element_loc
        # ated((By.CLASS_NAME, "input-wrap has-error")))
        text = driver.find_element_by_id("TEXT")
        text.clear()
        text.click()
        WebDriverWait(self.driver, 10).\
            until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, "#EMAIL ~ .error-block"), "Почта указана неверно"))
        name = driver.find_element_by_id("NAME")
        name.clear()
        name.click()
        name.send_keys("qwerty")
        WebDriverWait(self.driver, 10).\
            until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#NAME ~ .error-block")))
        WebDriverWait(self.driver, 10).\
            until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, "#TEXT ~ .error-block"), "Пожалуйста, введите текст сообщения"))
        name.clear()
        name.send_keys("Иван")
        email.clear()
        email.send_keys("смит@mail.ru")
        text.send_keys("текст текст текст")
        feedback = Feedback(driver)
        feedback.submit()
        WebDriverWait(self.driver, 10).\
            until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, "#EMAIL ~ .error-block"), "Почта указана неверно"))


    def test_4_timer(self):
        driver = self.driver
        feedback = Feedback(driver)
        feedback.NAME("Измаил")

        # email = "a" + str(time.strftime('%H%M')) + "@asd.com"
        feedback.EMAIL(POfb.email)
        feedback.TEXT("some text")
        feedback.submit()
        WebDriverWait(self.driver, 10).\
            until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, "success__mail"), POfb.email))
        driver.refresh()
        feedback.NAME("Измаил")

        feedback.EMAIL(POfb.email)
        feedback.TEXT("some text")
        feedback.submit()
        WebDriverWait(self.driver, 10).\
            until(expected_conditions.visibility_of_element_located((By.ID, "success__timer")))
        # driver.get_screenshot_as_file('D:/screen_test/timer.png')


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    with open('/D:/screen_test/results.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)



