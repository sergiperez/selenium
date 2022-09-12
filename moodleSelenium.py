from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
import json

file = open('config.json')
params = json.load(file)

driver = webdriver.Chrome(params["pathDriver"])
driver.implicitly_wait(30)
driver.maximize_window()

# Acceder a la aplicación web
driver.get(params["baseUrlMoodle"]+"login/index.php")
main_page = driver.current_window_handle

# Localizar cuadro de texto
search_field = driver.find_element("id","username")
search_field.send_keys(params["user"])
search_field = driver.find_element("id","password")
search_field.send_keys(params["password"])
search_field = driver.find_element("id","loginbtn")
search_field.submit()


#Pasar por todos los elementos y reproducir el texto individual

driver.get(params["baseUrlMoodle"]+"admin/tool/uploaduser/index.php")
delimiter_field = driver.find_element("id","id_delimiter_name")
for option in delimiter_field.find_elements("tag name",'option'):
    if option.text == ',':
        option.click() # select() in earlier versions of webdriver
        break
f = driver.find_element("name","userfilechoose")
f.click()

f2 = driver.find_element("name","repo_upload_file")
f2.send_keys(params["pathCsv"])
button = driver.find_element("class name","fp-upload-btn")
button.click()
sleep(2)
submit = driver.find_element("id","id_submitbutton")
submit.click()
#uupasswordnew
field = Select(driver.find_element("name","uupasswordnew"))
field.select_by_index(0)
submit = driver.find_element("id","id_submitbutton")
submit.click()
sleep(5)

# Cerrar la ventana del navegador
driver.quit()
file.close()
