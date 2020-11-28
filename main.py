import keyboard, random, time, requests
from bs4 import BeautifulSoup

def evangeliza():
    soup = BeautifulSoup(requests.get("https://dailyverses.net/pt/versiculo-aleatorio-da-biblia").text, 'html.parser')
    salmo = soup.find("span", {"class":"v1"})
    referencia = soup.find("a", {"class":"vc"})
    keyboard.write("/all "+salmo.text.split(".")[0]+" - "+referencia.text, delay=0.01)
    keyboard.press_and_release('enter')

keyboard.add_hotkey('enter', lambda: evangeliza())
keyboard.wait('esc')
