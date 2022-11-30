from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import json
import csv

# JA NO ES POT OBRIR DRIVER DES DE PATH :-(
#https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python
#driver = webdriver.Chrome("/home/super/")

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(30)
driver.maximize_window()

# Acceder a la aplicación web
#URL IMPRESSORA
driver.get("http://10.241.181.214:9191/admin")
main_page = driver.current_window_handle

# Localizar cuadro de texto
search_field = driver.find_element("id","inputUsername")
search_field.send_keys("direccio")
search_field = driver.find_element("id","inputPassword")
search_field.send_keys("7553305")
search_field = driver.find_element("name","$Submit$0")
search_field.submit()

#Crear usuari
sleep(1)
search_field = driver.find_element("id","pageactions").click()
search_field = driver.find_element("xpath","//a[@href='/app?service=page/CreateInternalUser']").click()

#csv file
csvFile = open("usuari.csv",mode='r')
users = csv.DictReader(csvFile)
for user in users:
    search_field = driver.find_element("id","chosen-username")
    search_field.clear()
    search_field.send_keys(user["nom"])
    search_field = driver.find_element("name","adminInputFullName")
    search_field.clear()
    search_field.send_keys(user["nom"]+user["cognoms"])
    search_field = driver.find_element("name","adminInputEmail")
    search_field.clear()
    search_field.send_keys(user["email"])
    search_field = driver.find_element("name","adminInputPassword")
    search_field.clear()
    search_field.send_keys(user["contrasenya"])
    search_field = driver.find_element("name","adminInputPasswordVerify")
    search_field.clear()
    search_field.send_keys(user["contrasenya"])
    search_field = driver.find_element("name","adminInputUserID")
    search_field.clear()
    search_field.send_keys(user["ID"])
    search_field = driver.find_element("name","adminInputIDPIN")
    search_field.clear()
    search_field.send_keys(user["PIN"])
    search_field = driver.find_element("name","adminInputIDPINVerify")
    search_field.clear()
    search_field.send_keys(user["PIN"])
    search_field = driver.find_element("name","adminInputEmailConfirmation").click()
    #Enviar    
    search_field = driver.find_element("name","$Submit$1").click()
    #Modificar usuari
    search_field = driver.find_element("xpath","//a[@href='/app?service=page/UserList']").click()
    search_field = driver.find_element("id","quickFindAuto")
    search_field.clear()
    search_field.send_keys(user["buscar"])
    sleep(1)
    search_field = driver.find_element("name","$Submit").click() 
    search_field = driver.find_element("xpath","//a[@href='/app?service=direct/1/UserDetails/$DirectLink&sp=1']").click()
    search_field = driver.find_element("id","adjustmentValue")
    search_field.clear()
    search_field.send_keys("1000,00")
    search_field = driver.find_element("name","$Submit").click()
    search_field = driver.find_element("xpath","//a[@href='/app?service=page/UserList']").click()
    search_field = driver.find_element("id","pageactions").click()
    search_field = driver.find_element("xpath","//a[@href='/app?service=page/CreateInternalUser']").click()   
# Cerrar la ventana del navegador
driver.quit()
csvFile.close()
