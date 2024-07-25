from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Pfad zum Chrome Webdriver
chrome_driver_path = "chromedriver.exe"

# Chrome-Optionen festlegen
chrome_options = Options()
chrome_options.add_argument("--disable-infobars")  # Benachrichtigungen deaktivieren

# Chrome-Service initialisieren
service = Service(chrome_driver_path)
service.start()

# Chrome-Browser starten
driver = webdriver.Chrome(service=service, options=chrome_options)

# Webseite öffnen
driver.get("https://www.knuddels.de/")

# Warte auf das Laden der Seite
time.sleep(3)

# Cookie-Overlay akzeptieren, falls vorhanden
try:
    accept_button = driver.find_element(By.CSS_SELECTOR, ".cmpboxbtn.cmpboxbtnyes")
    accept_button.click()
except Exception as e:
    print("Cookie overlay not found:", e)

# Einloggen-Link finden und darauf klicken
login_link = driver.find_element(By.CSS_SELECTOR, "a[href='/login']")
login_link.click()

# Warte auf das Laden der Seite
time.sleep(3)

# Benutzerdaten eingeben
username = "Wilder Bob30"
password = "359700"

nickname_input = driver.find_element(By.CSS_SELECTOR, "input[aria-label='Dein Nickname']")
nickname_input.send_keys(username)

password_input = driver.find_element(By.CSS_SELECTOR, "input[aria-label='Passwort']")
password_input.send_keys(password)

# Einloggen-Button klicken
submit_button = driver.find_element(By.CSS_SELECTOR, ".primary.svelte-1ca3sg7.dark-content")
submit_button.click()

# Warte kurz, um sicherzustellen, dass die Seite geladen wurde
time.sleep(3)

# Aktuellen DOM-Baum ausgeben
print("Aktueller DOM-Baum:")
print(driver.page_source)

# Browser für 60 Sekunden offen halten
time.sleep(60)

# Browser schließen
driver.quit()
