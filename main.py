import keyboard, random, threading, requests
from bs4 import BeautifulSoup

class SalmoGenerator():
    AVAILABLE_APIS = {
        "dailyverse":"https://dailyverses.net/pt/versiculo-aleatorio-da-biblia"
    }

    def __init__(self, api="dailyverse"):
        self.endpoint = self.AVAILABLE_APIS[api]
        self._lock = threading.Lock()
        self.servo = threading.Thread(target=self.auto_salmo)
        self._ready = []
        self._stop_flag = False

    def get_salmo(self):
        soup = BeautifulSoup(requests.get(self.endpoint).text, 'html.parser')
        salmo = soup.find("span", {"class":"v1"})
        referencia = soup.find("a", {"class":"vc"})
        return [salmo.text.split(".")[0], referencia.text]

    def auto_salmo(self):
        conds = True
        print("[i] Loading salmos....")
        while(conds):
            if self._stop_flag:
                conds = False

            [v, ref] = self.get_salmo()
            if len(v) + len(ref) < 140:
                self._lock.acquire()
                self._ready.append("/all %s - %s" % (v,ref))
                self._lock.release()

    def evangeliza(self):
        if len(self._ready) > 0:
            txt = self._ready.pop()
            keyboard.write(txt)
            keyboard.press_and_release('enter')
    
    def blasfemia(self):
        self._stop_flag = True

def main():
    print("[i] Starting... \n Coded by GuilhermeC")
    client = SalmoGenerator()
    client.servo.start()
    keyboard.add_hotkey('enter', lambda: client.evangeliza())
    keyboard.wait('esc')
    print("[!] Got exit arg")
    client.blasfemia()

if __name__ == '__main__':
    main()