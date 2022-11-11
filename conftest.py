import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


@pytest.fixture()
def initiate_driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.flipkart.com")
    time.sleep(5)
    driver.maximize_window()
    yield driver

    driver.quit()