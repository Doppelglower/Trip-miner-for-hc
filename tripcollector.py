import json
import websocket
import os
import threading
import time
import requests
res = dict()
room = "testttt"
def cremin():
    while True:
        os.chdir(r"C:\Python310\mine")
        os.popen(r"python .\tripminer.py "+room)
        time.sleep(30.0)
def getw(text,sender):
	return str(text[len(sender)+12:])
def on_open(ws):
    ws.send(json.dumps({"cmd": "join", "channel": room, "nick": "trip_collector"}))
    cre = threading.Thread(target=cremin)
    cre.start()

    #socks4_list1 = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all').text.split('\n')
    #socks4_list2 = requests.get('https://www.proxyscan.io/download?type=socks4').text.split('\n')
    #socks4_list3 = requests.get('https://www.proxy-list.download/api/v1/get?type=socks4').text.split('\n')
    return 
    socks4_list4 = requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt').text.split()     
    socks4_list5 = requests.get('https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt').text.split()
    socks4_list6 = requests.get('https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt').text.split()
    socks4_list7 = requests.get('https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt').text.split()
    socks4_list8 = requests.get('https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt').text.split()
    socks4_list9 = requests.get('https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt').text.split()
    socks4_list10 = requests.get('https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt').text.split()
    socks4_list11 = requests.get('https://raw.githubusercontent.com/RX4096/proxy-list/main/online/socks4.txt').text.split()
    socks4_list = list(set(socks4_list4 + socks4_list5 + socks4_list6 + socks4_list7 + socks4_list8 + socks4_list9 + socks4_list10 + socks4_list11))
    #socks5_list1 = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all').text.split('\n')
    #socks5_list2 = requests.get('https://www.proxyscan.io/download?type=socks5').text.split('\n')
    #socks5_list3 = requests.get('https://www.proxy-list.download/api/v1/get?type=socks5').text.split('\n')
    socks5_list4 = requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt').text.split()
    socks5_list5 = requests.get('https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt').text.split()
    socks5_list6 = requests.get('https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt').text.split()
    socks5_list7 = requests.get('https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt').text.split()
    socks5_list8 = requests.get('https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt').text.split()
    socks5_list9 = requests.get('https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt').text.split()
    socks5_list10 = requests.get('https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt').text.split()
    socks5_list11 = requests.get('https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt').text.split()
    socks5_list12 = requests.get('https://raw.githubusercontent.com/ryanhaticus/superiorproxy.com/main/proxies.txt').text.split()
    socks5_list13 = requests.get('https://raw.githubusercontent.com/RX4096/proxy-list/main/online/socks5.txt').text.split()
    socks5_list = list(set(socks5_list4 + socks5_list5 + socks5_list6 + socks5_list7 + socks5_list8 + socks5_list9 + socks5_list10 + socks5_list11 + socks5_list12 + socks5_list13))
    proxy_dict = {'socks4':socks4_list,'socks5':socks5_list}#'https':https_list}
    proxy_list = socks4_list + socks5_list # + https_list
    bb = open(r"C:\Python310\files\proxy.txt",mode="w")
    bb.writelines(str(proxy_dict)+'\n')
    bb.writelines(str(proxy_list))
    bb.close()

def on_message(ws,message):
    global res
    dat = json.loads(message)
    if dat["cmd"] == "info" and dat["type"] == "whisper":
        nic = dat["from"]
        tex = getw(str(dat["text"]),nic)
        if str(nic).startswith("trip_miner_")  and dat["trip"] not in res:
            res.update({dat["trip"]:tex})
            aa = open(r"C:\Python310\files\trips.txt",mode="a")
            aa.write(str(res)+'\n')
            aa.close()
            res.clear()
if __name__ == "__main__":
    #websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://hack.chat/chat-ws",on_message=on_message)
    ws.on_open=on_open
    ws.run_forever()