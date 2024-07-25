import mechanicalsoup
import time

# Erstelle eine Browserinstanz
browser = mechanicalsoup.StatefulBrowser()

# HTTPS-Webseite öffnen
browser.open("https://www.knuddels.de/")

# Versuche, das Cookie-Overlay zu finden und zu akzeptieren
try:
    accept_button = browser.get_current_page().find("a", {"class": "cmpboxbtn cmpboxbtnyes"})
    if accept_button:
        accept_button.click()
except Exception as e:
    print("Cookie overlay not found:", e)

# Einloggen-Link finden und darauf klicken
login_link = browser.get_current_page().find("a", {"href": "/login"})
if login_link:
    # Überprüfen, ob der Einloggen-Link gefunden wurde
    if login_link.has_attr('href'):
        browser.follow_link(login_link)
    else:
        print("Login link found, but not clickable")
else:
    print("Login link not found")

# Warte auf das Laden der neuen Seite
browser.select_form('astro-island')

# Benutzerdaten
username = "Wilder Willie" #username in knuddels
password = "p4ssw0rt" #passwort in knuddels

# Finde das Eingabefeld mit dem aria-label-Attribut "Dein Nickname"
nickname_input = browser.get_current_page().find("input", {"aria-label": "Dein Nickname"})

# Überprüfe, ob das Eingabefeld gefunden wurde
if nickname_input:
    # Setze den Wert des Eingabefelds
    nickname_input["value"] = username
    print("Nickname eingetragen")
else:
    print("Nickname input field not found")

# Finde das Passwort-Eingabefeld mit dem aria-label-Attribut "Passwort"
password_input = browser.get_current_page().find("input", {"aria-label": "Passwort"})

# Überprüfe, ob das Passwort-Eingabefeld gefunden wurde
if password_input:
    # Setze den Wert des Passwort-Eingabefelds
    password_input["value"] = password
    print("Passwort eingetragen")
else:
    print("Password input field not found")

# Führe das JavaScript aus, um das Formular zu senden
script = """
document.querySelector('.primary.svelte-1ca3sg7.dark-content').click();
"""
browser.execute_script(script)

# Warte kurz, um sicherzustellen, dass die Seite geladen wurde
time.sleep(3)

# Ausgabe des aktuellen DOM-Baums in der Konsole
print("Aktueller DOM-Baum:")
print(browser.get_current_page())

# Browser für 60 Sekunden offen halten
time.sleep(60)

# Browser schließen
browser.close()
