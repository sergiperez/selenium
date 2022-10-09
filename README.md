# install selenium
sudo apt install python3-pip

pip install selenium

pip3 install --upgrade requests

wget https://chromedriver.storage.googleapis.com/105.0.5195.52/chromedriver_linux64.zip

unzip chromedriver_linux64.zip

# Moodle selenium 
Bot que pujar un fitxer csv al moodle i fa la importació d'usuaris nous.
- config.json Fitxer configuració amb usuari / contrasenya i URL del Moodle.
- usuaris.csv Fitxer csv on hi ha l'alumnat a crear usuaris nous.
- moodleSelenium.py Fitxer Python que fa la creació.

# Renovar credencials 
Bot que renova les credencials d'un alumne/a: renova contrasenya i baixa el fitxer de les credencials. Pot fer més d'un alumne/a. Cada arxiu de credencials es renombra amb el nom i cognom de l'alumne/a.
- configIdi.json Fitxer configuració amb usuari i contrasenya per accedir al IDI.
- usuari.csv Fitxer csv on hi ha l'alumnat a renovar credencials. A ensenyament ha de ser un valor de : ESO, BATXLOE 2000, BATXLOE 3000 o CFPM .
- renovarCredencials.py Fitxer Python que fa la renovació i baixa l'arxiu pdf.

