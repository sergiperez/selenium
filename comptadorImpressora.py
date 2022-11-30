from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import json
file = open('config.json')
params = json.load(file)
#driver = webdriver.Chrome("/home/super/")

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(30)
driver.maximize_window()

# Acceder a la aplicación web
#URL IMPRESSORA
driver.get(params["baseUrlMoodle"])
main_page = driver.current_window_handle

# Localizar cuadro de texto
search_field = driver.find_element("id","inputUsername")
search_field.send_keys(params["user"])
search_field = driver.find_element("id","inputPassword")
search_field.send_keys(params["password"])
search_field = driver.find_element("name","$Submit$0")
search_field.submit()

#Revisar saldo
search_field = driver.find_element("xpath","//a[@href='/app?service=direct/1/UserList/filter.toggle']").click()
search_field = driver.find_element("id","maxBalance")
search_field.send_keys("60")
search_field = driver.find_element("name","apply")
search_field.click()
sleep(1)

search_field = driver.find_elements("xpath","//a[starts-with(@href,'/app?service=direct/1/UserList/user.link')]")

#definir
enllacos = []

#recorrer search_field i omplier array enllacos
for s in search_field:
    #afegir a l'array ennlacos el s.get_attribute("href")
    enllacos.append(s.get_attribute("href"))
for h in enllacos:
    driver.get(h)
    sleep(1)
    #actualitzes sumbmit
    search_field = driver.find_element("xpath","//a[@href='/app?service=direct/1/UserDetails/$DirectLink&sp=1']").click()
    search_field = driver.find_element("id","adjustmentValue")
    search_field.clear()
    search_field.send_keys("1000,00")
    search_field = driver.find_element("name","$Submit").click()
    #search_field = driver.find_element("xpath","//a[@href='/app?service=page/UserList']").click()
    sleep(2)
