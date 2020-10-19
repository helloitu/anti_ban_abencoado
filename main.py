import keyboard, random, time, requests
from bs4 import BeautifulSoup

def evangeliza():
    soup = BeautifulSoup(requests.get("https://dailyverses.net/pt/versiculo-aleatorio-da-biblia").text, 'html.parser')
    referencia = soup.find("div", {"class":"reference"})
    salmo = soup.find("div", {"class":"bibleVerse"})
    keyboard.write("/all "+salmo.text.split(".")[0]+" - "+referencia.text, delay=0.01)
    keyboard.press_and_release('enter')

keyboard.add_hotkey('enter', lambda: evangeliza())
keyboard.wait('esc')
