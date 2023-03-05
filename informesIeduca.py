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

file = open('configIeduca.json')
params = json.load(file)

driver = webdriver.Chrome(params["pathDriver"])
driver.maximize_window()


driver.get(params["baseUrl"])
search_field = driver.find_element("name","username_email")
search_field.send_keys(params["user"])
search_field = driver.find_element("name","password")
search_field.send_keys(params["password"])
search_field = driver.find_element("xpath","//a[@id='btn-login']").click()

enllacos = []
for num in range(0,4):
	driver.get("https://perealsius.ieduca.com/index.php?pageNum_persones="+str(num)+"&seccio=186")
	table_id = driver.find_element("xpath","//table[@class='taula']")
	rows = table_id.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table
	for row in rows:
		cols = row.find_elements(By.TAG_NAME, "td") #note: index start from 0, 1 is col 2
		if (len(cols)>0):
			if ("recerca" in cols[0].text):
				enllacos.append(cols[4].find_elements(By.TAG_NAME,"a")[0].get_attribute('href'))

os.chdir('..')
for e in enllacos:
	driver.get(e)
	#S'ha de cerca últim.Problema dos profes.
	alumnes = driver.find_elements("xpath","//span[@class='contacte_msg']")
	alumne = alumnes[len(alumnes)-1].text
	id_alumne = e[e.index("id=")+3:e.index("&",e.index("id"))]
	banderes_verdes = driver.find_elements("xpath",'//div[@class="inline tooltip icon icon-ribbon green"]')
	if (len(banderes_verdes)>0):
		driver.get("https://perealsius.ieduca.com/pop/informe_imprimir_grup.php?id_sol="+id_alumne)
		while not os.path.exists(os.getcwd()+"/"+params["password"]+".doc"):
			sleep(1)
		if os.path.isfile(os.getcwd()+"/"+params["password"]+".doc"):
			os.rename(os.getcwd()+"/"+params["password"]+".doc", os.getcwd()+"/tr/"+alumne.replace(" ","")+".doc")
			os.system("libreoffice --headless --convert-to pdf "+os.getcwd()+"/tr/"+alumne.replace(" ","")+".doc --outdir  "+os.getcwd()+"/tr/")	
			os.system("rm "+os.getcwd()+"/tr/"+alumne.replace(" ","")+".doc")	
	else:
		print(alumne+" no s'ha fet encara informe")
			
	
	
