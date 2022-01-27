import time
import pandas
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

df = pandas.read_excel('canciones.xlsx', sheet_name='lista_canciones')

url = 'https://www.youtube.com/'

# Xpath
path_busqueda = '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input'
boton_busqueda = '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button'
boton_ad = '/div/div[3]/div/div[2]/span/button'
path_cancion = '/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]'

# Abrir Navegador:
ser = Service(r'C:\chromediver\chromedriver.exe')
driver = webdriver.Chrome(service=ser)
driver.maximize_window()
driver.get(url)

for i in df.index:
    cancion = str(df['canción'][i])
    # tipear canción
    driver.find_element(By.XPATH, path_busqueda).send_keys(cancion)
    time.sleep(1)
    driver.find_element(By.XPATH, boton_busqueda).click()
    # Esperar que aparezcan las canciones
    wait = WebDriverWait(driver, 50)
    wait.until(ec.visibility_of_element_located((By.XPATH, path_cancion)))
    # Entrar a la canción
    driver.find_element(By.XPATH, path_cancion).click()
    # Disfrutar la canción
    time.sleep(10)
    # Borre la busqueda actual
    driver.find_element(By.XPATH, path_busqueda).clear()
driver.quit()


