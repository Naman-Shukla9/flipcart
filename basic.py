from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.find_element(By.CSS_SELECTOR,"a._1_3w1N").click()
time.sleep(2)