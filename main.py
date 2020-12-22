import keyboard, random, time, requests
from bs4 import BeautifulSoup

def salmo():
    soup = BeautifulSoup(requests.get("https://dailyverses.net/pt/versiculo-aleatorio-da-biblia").text, 'html.parser')
    salmo = soup.find("span", {"class":"v1"})
    referencia = soup.find("a", {"class":"vc"})
    return [salmo.text.split(".")[0], referencia]

def evangeliza():
    [v, referencia] = salmo()
    # P/ pegar sempre salmos pequenos, para não cortar no chat
    while len(v) + len(referencia.text) >= 140:
        [v, referencia] = salmo()
    
    keyboard.write("/all "+v+" - "+referencia.text, delay=0.001)
    keyboard.press_and_release('enter')

keyboard.add_hotkey('enter', lambda: evangeliza())
keyboard.wait('esc')

