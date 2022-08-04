import json
import time
import random
import threading
from websocket import create_connection
from websocket import WebSocketConnectionClosedException,WebSocketBadStatusException
from ssl import SSLCertVerificationError, SSLEOFError
from python_socks import ProxyConnectionError,ProxyError,ProxyTimeoutError
import sys
import ast

channel = str(sys.argv[1])
proxy_list = list()
proxy_dict = dict()
i = 0

def getDictKey_1(myDict, value):
    if value in myDict['socks4']:
        return 'socks4'
    if value in myDict['socks5']:
        return 'socks5'
    if value in myDict['https']:
        return 'https'

def fuck():
    def shit():
        global i
        try:
            ip = proxy_list.pop()
            ws=create_connection('wss://hack.chat/chat-ws',http_proxy_host=ip.split(':')[0], http_proxy_port=int(ip.split(':')[1]), proxy_type=getDictKey_1(proxy_dict,ip))
            nam = "trip_miner_"+str(random.randint(0,10000))
            pwd = ''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a','0','1','2','3','4','5','6','7','8','9','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M'], random.randint(18,36)))
            req = json.dumps({"cmd": "join", "channel": channel, "nick": nam + "#" + pwd})
            ws.send(req)
            time.sleep(0.1)
            ws.send(json.dumps({"cmd":"chat","text":"/w trip_collector "+pwd}))
            ws.close()
            i = 0
            return
        except (ProxyConnectionError,ProxyTimeoutError,ProxyError,SSLEOFError,SSLCertVerificationError,ValueError,WebSocketBadStatusException,WebSocketConnectionClosedException,ConnectionResetError,ConnectionRefusedError,TimeoutError):
            i = 0
            return
        except BrokenPipeError:
            i = 1
            return
    while True:
        shit()
        if i == 0:break
        time.sleep(3.0)
    return

def main():
    global proxy_list,proxy_dict
    thread_list = []
    aa = open(r"C:\Python310\files\proxy.txt",mode="r")
    bb = aa.readlines()
    aa.close()
    proxy_dict = ast.literal_eval(bb[0][:-1])
    proxy_list = ast.literal_eval(bb[1])


    for p in range(len(proxy_list)):
        t = threading.Thread(target=fuck)
        t.start()
        thread_list.append(t)
    for t in thread_list:
        t.join()

if __name__ == '__main__':
    #websocket.enableTrace(True)
    main()



    