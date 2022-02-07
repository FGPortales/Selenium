from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\chromediver\chromedriver.exe')
driver.get('http://python.org')
driver.close()
