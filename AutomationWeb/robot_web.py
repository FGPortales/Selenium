from getpass import getpass
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

user = 'fportalesar@gmail.com'
password = getpass('Password: ')
url = 'https://www.hackerrank.com/'

# Selectores:

boton_access_account = '#menu-item-2887 > a'
boton_inicio_sesion = '#post-175 > div > div > div.fl-row.fl-row-full-width.fl-row-bg-none.fl-node-5bd106f71c93d.hr__header-form-section.hr__header-form-section--sign-up > div > div > div.fl-col-group.fl-node-5bd106f71c9ec.fl-col-group-custom-width > div.fl-col.fl-node-5bd106f71cd43 > div > div.fl-module.fl-module-button.fl-node-5bd106f71cbed.hr__builder-button.hr__builder-button--primary.hr__builder-button--primary--halo.hr__builder-button--lg > div > div > a'
selector_user = '#input-1'
selector_password = '#input-2'
boton_login = '#tab-1-content-1 > div.login-form.auth-form.theme-m > form > div.form-item.clearfix > button'

# Abrir Navegador:
ser = Service(r'C:\chromediver\chromedriver.exe')
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
driver.maximize_window()
driver.get(url)

# Acciones en la página:
driver.find_element(By.CSS_SELECTOR, boton_access_account).click()
driver.find_element(By.CSS_SELECTOR, boton_inicio_sesion).click()
driver.find_element(By.CSS_SELECTOR, selector_user).send_keys(user)
driver.find_element(By.CSS_SELECTOR, selector_password).send_keys(password)
driver.find_element(By.CSS_SELECTOR, boton_login).click()

time.sleep(7)
driver.quit()
