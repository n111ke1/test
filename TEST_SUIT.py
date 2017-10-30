import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from PO import Feedback
import PO
from selenium.webdriver.support import expected_conditions



class Feed(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('D:\INSTALL\chromedriver_win32 (1)\chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("http://n111ke1:12345@moneyteka.typical.dev.flustex.com/feedback")

    def test_1_button_disabled(self):
        helper_1 = Feedback(self.driver)
        helper_1.CLICK_BY_ID("feedback-submit")
        assert helper_1.ID("feedback-submit").get_attribute("disabled")
        helper_1.SEND_KEYS(PO.ID_NAME, "Антон")
        helper_1.CLICK_BY_ID(PO.ID_NAME)
        assert helper_1.ID("feedback-submit").get_attribute("disabled")
        helper_1.CLEAR_BY_ID(PO.ID_NAME)
        helper_1.SEND_KEYS(PO.ID_EMAIl, "asd@sds.com")
        assert helper_1.ID("feedback-submit").get_attribute("disabled")
        helper_1.CLEAR_BY_ID(PO.ID_EMAIl)
        helper_1.SEND_KEYS(PO.ID_TEXT, "Some text Some text Some text")
        assert helper_1.ID("feedback-submit").get_attribute("disabled")
        helper_1.CLICK_BY_ID("feedback-submit")
        helper_1.CLEAR_BY_ID(PO.ID_TEXT)



    def test_2_validation(self):
        helper_2 = Feedback(self.driver)
        helper_2.CLEAR_BY_ID(PO.ID_NAME)
        helper_2.CLICK_BY_ID(PO.ID_NAME)
        helper_2.CLEAR_BY_ID(PO.ID_EMAIl)
        helper_2.CLICK_BY_ID(PO.ID_EMAIl)
        WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element
                                             ((By.CSS_SELECTOR, "#NAME ~ .error-block"),
                                              "Пожалуйста, укажите ваше Имя"))
        helper_2.CLEAR_BY_ID(PO.ID_TEXT)
        helper_2.CLICK_BY_ID(PO.ID_TEXT)
        WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element
                                             ((By.CSS_SELECTOR, "#EMAIL ~ .error-block"), "Почта указана неверно"))
        helper_2.CLICK_BY_ID(PO.ID_NAME)
        WebDriverWait(self.driver, 10). \
            until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, "#TEXT ~ .error-block"),
                                                                    "Пожалуйста, введите текст сообщения"))
        helper_2.SEND_KEYS(PO.ID_NAME, "qwerty")
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".error-block img")))
        helper_2.CLEAR_BY_ID(PO.ID_NAME)
        helper_2.SEND_KEYS(PO.ID_NAME, "Иван")
        helper_2.CLEAR_BY_ID(PO.ID_EMAIl)
        helper_2.SEND_KEYS(PO.ID_EMAIl, "смит@mail.ru")
        helper_2.SEND_KEYS(PO.ID_TEXT, "text text text text text")
        helper_2.CLICK_BY_ID("feedback-submit")
        WebDriverWait(self.driver, 10). \
            until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, "#EMAIL ~ .error-block"),
                                                                    "Почта указана неверно"))

    def test_3_timer(self):

        helper_3 = Feedback(self.driver)
        helper_3.CHECK_TIMER()
        WebDriverWait(self.driver, 10). \
            until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, 'success__mail'), PO.email))
        self.driver.refresh()
        helper_3.CHECK_TIMER()
        WebDriverWait(self.driver, 10). \
            until(expected_conditions.visibility_of_element_located((By.ID, "success__timer")))

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
