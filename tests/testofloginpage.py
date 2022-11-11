import time
import pytest
from selenium.webdriver.common.by import By
from homepagelocator import *


# from loginpageLocators import email_field,continue_button
class TestLoginPage:

    @pytest.mark.usefixtures("initiate_driver")
    def test_email_enter(self, initiate_driver):
        driver = initiate_driver

        driver.find_element(By.CSS_SELECTOR, enter_email).send_keys("7827986689")
        time.sleep(2)

    def test_password(self, initiate_driver):
        driver = initiate_driver
        self.test_email_enter(driver)

        driver.find_element(By.CSS_SELECTOR, password).send_keys("")
        time.sleep(5)

    def test_login_button(self, initiate_driver):
        driver = initiate_driver
        self.test_password(driver)
        driver.find_element(By.CSS_SELECTOR, loginbutton).click()
        time.sleep(5)

    def test_search_button(self, initiate_driver):
        driver = initiate_driver
        self. test_login_button(driver)
        driver.find_element(By.CSS_SELECTOR,cart).click()
        time.sleep(8)

    def test_searchbutton(self,initiate_driver):
        driver=initiate_driver
        self.test_login_button(driver)
        driver.find_element(By.CSS_SELECTOR,value="input._3704LK").send_keys("Pen")
        time.sleep(10)
    def test_exploreplus(self,initiate_driver):
        driver=initiate_driver
        self.test_login_button(driver)
        # driver.find_element(driver)
        driver.find_element(By.CSS_SELECTOR,value=exploreplus).click()
        time.sleep(6)

    def test_searchbutton2(self, initiate_driver):
        driver = initiate_driver
        self.test_login_button(driver)
        driver.find_element(By.CSS_SELECTOR, value="input._3704LK").send_keys("Pen")
        time.sleep(10)
        driver.find_element(By.CSS_SELECTOR, value=search_button).click()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, value=flipkart_logo).click()
        time.sleep(10)
        driver.find_element(By.CSS_SELECTOR, value="input._3704LK").send_keys("Notebook")
        time.sleep(10)
        driver.find_element(By.CSS_SELECTOR, value=search_button).click()
        time.sleep(3)