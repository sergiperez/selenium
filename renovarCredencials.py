from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import os
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import csv
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException

file = open('configIdi.json')
params = json.load(file)

driver = webdriver.Chrome(params["pathDriver"])
driver.implicitly_wait(30)
driver.maximize_window()

# Accedir a la pàgina principal de l'indic'
driver.get(params["baseUrl"])
search_field = driver.find_element("id","L2AGLb").click()
sleep(1)
search_field = driver.find_element("name","q")
search_field.send_keys("idi ensenyament")
search_field = driver.find_element("name","btnI").submit()
search_field = driver.find_element("xpath","//a[@href='https://aplicacions.ensenyament.gencat.cat/pls/apex/f?p=idi']").click()

#Validar usuari
search_field = driver.find_element("name","USER")
search_field.send_keys(params["user"])
search_field = driver.find_element("name","PASSWORD")
search_field.send_keys(params["password"])
search_field = driver.find_element("xpath","//input[@type='submit']").submit()

sleep(1)
el = driver.find_element("xpath","//button[text()='Identitat digital']").click()
el = driver.find_element("xpath","//a[text()='Alumnes']").click()
sleep(3)

wait = WebDriverWait(driver,600)
csvFile = open(params["usuari"],mode='r')
users = csv.DictReader(csvFile)
for user in users:
    #Filtrar
    search_field = driver.find_element("name","P10_IDENTIFICADOR")   
    search_field.clear()
    search_field.send_keys(user["idalu"])
    search_field = driver.find_element("name","P10_NOM")   
    search_field.clear()
    search_field.send_keys(user["nom"])
    search_field = driver.find_element("name","P10_COGNOM1")   
    search_field.clear()
    search_field.send_keys(user["cognom1"])
    search_field = driver.find_element("name","P10_COGNOM2")   
    search_field.clear()
    search_field.send_keys(user["cognom2"]) 
    driver.find_element("xpath","//a[@class='a-Button a-Button--popupLOV']").click()
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element("xpath","//a[starts-with(text(),'"+user["ensenyament"]+"')]").click()
    driver.switch_to.window(driver.window_handles[0])
    sleep(2)
    search_field = driver.find_element("name","P10_NIVELL")   
    search_field.send_keys(user["nivell"])   
    driver.find_element("xpath","//button[@title='Cerca']").click()
    sleep(5)
    driver.find_element("xpath","//span[@class='fa fa-pencil edit-link-pencil']").click()
    #Renovem credencials
    driver.find_element("id","B161053013313277439").click()   
    sleep(5)
    driver.find_element("xpath","//span[@class='fa fa-pencil edit-link-pencil']").click()
    
    #Baixem credencials
    nom=driver.find_element("name","P13_NOM").get_attribute("value")
    cognom=driver.find_element("name","P13_COGNOM1").get_attribute("value")
    driver.find_element("id","B162306647501880342").click()   
    #canviem nom fitxer
    while not os.path.exists(os.getcwd()+"/IDI_CREDENCIALS_IDI_CREDENCIALS.pdf"):
	    sleep(1)
    if os.path.isfile(os.getcwd()+"/IDI_CREDENCIALS_IDI_CREDENCIALS.pdf"):
	    os.rename(os.getcwd()+"/IDI_CREDENCIALS_IDI_CREDENCIALS.pdf", os.getcwd()+"/"+nom+cognom+".pdf")		
    driver.find_element("id","B161869714135804447").click()   
csvFile.close()


# Cerrar la ventana del navegador
driver.quit()

