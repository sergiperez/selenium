from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import json
import csv
file = open('configu.json')
params = json.load(file)
#driver = webdriver.Chrome("/home/super/")

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(30)
driver.maximize_window()

# Acceder a la aplicación web
#URL IMPRESSORA
driver.get(params["baseUrl"])
main_page = driver.current_window_handle

# Localizar cuadro de texto
search_field = driver.find_element("id","inputUsername")
search_field.send_keys(params["user"])
search_field = driver.find_element("id","inputPassword")
search_field.send_keys(params["password"])
search_field = driver.find_element("name","$Submit$0")
search_field.submit()

csvFile = open("usuari.csv",mode='r')
users = csv.DictReader(csvFile)
for user in users:
    search_field = driver.find_element("id","quickFindAuto")
    search_field.clear()
#S'ha de buscar per el nom d'usuari per evitar errors
    search_field.send_keys(user["buscar"])
    sleep(1)
    search_field = driver.find_element("name","$Submit").click()
    search_field = driver.find_element("id","pageactions").click()
    search_field = driver.find_element("xpath","//a[starts-with(@href,'/app?service=direct/1/UserDetails/deleteUser')]").click()
    sleep(1)
    driver.switch_to.alert.accept()

    search_field = driver.find_element("xpath","//a[@href='/app?service=page/UserList']").click()
    sleep(1)
    sleep(1)
# Cerrar la ventana del navegador
driver.quit()
csvFile.close()
