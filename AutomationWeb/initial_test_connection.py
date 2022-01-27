from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(executable_path=r'C:\chromediver\chromedriver.exe')
# driver.get('http://python.org')
# driver.close()
# ************************************************************************************
# s = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=s)
# driver.maximize_window()
# driver.get('https://www.google.com')
# driver.find_element(By.NAME, 'q').send_keys('Yasser Khalil')
# ************************************************************************************


ser = Service(r'C:\chromediver\chromedriver.exe')
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
driver.maximize_window()
driver.get('https://www.google.com')

driver.close()
