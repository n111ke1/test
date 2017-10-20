import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import POfb
# from POfb import Feedback

class Begin (Ba):
    def setup (self):
        self.driver = webdriver.Chrome('D:\INSTALL\chromedriver_win32 (1)\chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("http://gutmoney.typical.dev.flustex.com/feedback")
        self.email = "a" + str(time.strftime('%H%M')) + "@asd.com"


    def test_1_timer(self):
        driver = self.driver
        feedback = Feedback(driver)

        feedback.NAME("Измаил")

        feedback.EMAIL(self.email)
        feedback.TEXT("some text")
        feedback.submit()
        WebDriverWait(self.driver, 10). \
            until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, "success__mail"), self.email))
        driver.refresh()
        feedback.NAME("Измаил")

        feedback.EMAIL(self.email)
        feedback.TEXT("some text")
        feedback.submit()
        WebDriverWait(self.driver, 10). \
            until(expected_conditions.visibility_of_element_located((By.ID, "success__timer")))
        driver.get_screenshot_as_file('D:/screen_test/timer.png')
    def teardown_module(module):

if __name__ == "__main__":
        pytest.main()