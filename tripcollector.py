import json
import websocket
import os
import threading
import time
import requests
import sys
room = ""
ini = 10.0
thr = False
rst = True
def restartttt():
    global rst,ini
    rst = False
    while ini>=0:
        ini-=0.1
        time.sleep(0.1)
        if thr:
            rst = True
            return
    restartt()
restarttt = threading.Thread(target=restartttt)
def restartt():
	py=sys.executable
	os.execl(py,py,*sys.argv)
def cremin():
    while thr:
        os.chdir(r"C:\Python310\mine")
        os.popen(r"python .\tripminer.py "+room)
        time.sleep(50.0)
    return
cre = threading.Thread(target=cremin)
def getw(text,sender):
	return str(text[len(sender)+12:])
def on_open(ws):
    ws.send(json.dumps({"cmd": "join", "channel": room, "nick": "trip_collector"}))
def clo():
    global ini,thr,rst
    while True:
        thr = False
        rst = False
        ini -= 0.1
        time.sleep(0.1)
        if ini <= 0.0:
            ws.send({})
            sys.exit()
cloo = threading.Thread(target=clo)
def on_message(ws,message):
    global ini,thr,rst
    dat = json.loads(message)
    if dat["cmd"] == "info" and dat["type"] == "whisper":
        nic = dat["from"]
        tex = getw(str(dat["text"]),nic)
        if str(nic).startswith("trip_miner_"):
            with open(r"C:\Python310\files\trips.txt",mode="a") as aa:aa.write("{'"+dat["trip"]+"': '"+tex+"'}\n")
            ini = 10.0
    elif dat["cmd"] == "chat" and dat["trip"] in ["VEbeHK","AAfFKK"] and dat["text"] == "STOP":
        thr = False
        rst = False
        cloo.start()
    elif dat["cmd"] == "chat" and dat["trip"] in ["VEbeHK","AAfFKK"] and str(dat["text"]).lower() == "stop":
        thr = False
        if rst:
            restarttt.start()
    elif dat["cmd"] == "chat" and dat["trip"] in ["VEbeHK","AAfFKK"] and str(dat["text"]).lower() == "start":
        thr = True
        cre.start()

if __name__ == "__main__":
    #websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://hack.chat/chat-ws",on_message=on_message)
    ws.on_open=on_open
    ws.run_forever()
