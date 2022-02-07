from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from getpass import getpass
import time

'''Login Gmail (corporate mail)'''
user_login = ''
password = ''

try:
    user_login = input('Login: ')
    password = getpass('Password: ')
except Exception as err:
    print('ERROR:', err)

acceder = '/html/body/header/div/div/div/a[2]'
button = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button'
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get('https://www.google.com/intl/es-419/gmail/about/')
driver.find_element(By.XPATH, acceder).click()
user = driver.find_element(By.ID, 'identifierId')
user.send_keys(user_login)
driver.find_element(By.XPATH, button).click()
time.sleep(3)

clave = driver.find_element(By.NAME, 'password')
clave.send_keys(password)
clave.send_keys(Keys.ENTER)
