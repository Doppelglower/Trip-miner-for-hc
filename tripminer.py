import json
import time
import random
import threading
import websocket
from websocket import create_connection
from websocket import WebSocketConnectionClosedException,WebSocketBadStatusException
from ssl import SSLCertVerificationError, SSLEOFError
from python_socks import ProxyConnectionError,ProxyError,ProxyTimeoutError
import sys
import ast
# headers = {
#     'authority': 'public.freeproxyapi.com',
#     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
#     'accept': 'application/octet-stream',
#     'dnt': '1',
#     'content-type': 'application/json',
#     'sec-ch-ua-mobile': '?0',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62',
#     'sec-ch-ua-platform': '"Windows"',
#     'origin': 'https://freeproxyapi.com',
#     'sec-fetch-site': 'same-site',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-dest': 'empty',
#     'referer': 'https://freeproxyapi.com/',
#     'accept-language': 'zh-CN,zh;q=0.9',
# }

# data = '{"types":[],"levels":[],"countries":[],"type":"json","resultModel":"Mini"}'

# response = requests.post('https://public.freeproxyapi.com/api/Download/Json', headers=headers, data=data)

channel = str(sys.argv[1])

def getDictKey_1(myDict, value):
    if value in myDict['socks4']:
        return 'socks4'
    if value in myDict['socks5']:
        return 'socks5'
    # if value in myDict['https']:
    #     return 'https'

def fuck():
    global api,channel
    def shit():
        global proxy_dict,i
        try:
            ip = proxy_list.pop()
            ws=create_connection('wss://hack.chat/chat-ws',http_proxy_host=ip.split(':')[0], http_proxy_port=int(ip.split(':')[1]), proxy_type=getDictKey_1(proxy_dict,ip))
            nam = "trip_miner_"+str(random.randint(0,10000))
            pwd = ''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a','0','1','2','3','4','5','6','7','8','9','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M'], random.randint(18,36)))
            req = json.dumps({"cmd": "join", "channel": channel, "nick": nam + "#" + pwd})
            ws.send(req)
            time.sleep(0.2)
            ws.send(json.dumps({"cmd":"chat","text":"/w trip_collector "+pwd}))
            time.sleep(0.2)
            ws.close()
        except (ProxyConnectionError,ProxyTimeoutError,ProxyError,SSLEOFError,SSLCertVerificationError,ValueError,WebSocketBadStatusException,WebSocketConnectionClosedException,ConnectionResetError,ConnectionRefusedError):
            i = 0
            return
        except BrokenPipeError:
            i = 1
            return
    while True:
        shit()
        if i == 0:break
        time.sleep(0.5)

# def get_zuan():
#     url = random.choice(['https://api.shadiao.app/nmsl?level=min','https://api.shadiao.app/nmsl?level=max'])
#     text = requests.get(url,timeout=5).text
#     return json.loads(text)["data"]["text"]

    # def getproxy():
    #     d = {'Socks4':[],'Socks5':[],'Https':[]}
    #     response = json.loads(requests.post('https://public.freeproxyapi.com/api/Download/Json', headers=headers, data=data).text)
    #     for w in response:
    #         if w['Type'] in ['Socks4','Socks5','Https']:
    #             proxyip = w['Host'] + ':' + str(w['Port'])
    #             d[w['Type']].append(proxyip)
    #     return d
        
    # m = getproxy()
def main():
    global proxy_list,proxy_dict,thread_count,success_count
    thread_list = []
    thread_count = 0
    success_count = 0
    proxy_lst = []
    lst = []
#     https_list1 = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=10000&country=all&ssl=all&anonymity=all').text.split('\r\n')
#     https_list2 = requests.get('https://www.proxyscan.io/download?type=https').text.split('\n')
#     https_list3 = requests.get('https://www.proxy-list.download/api/v1/get?type=https').text.split('\r\n')
# #    https_list4 = requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt').text.split('\n')
#     https_list5 = requests.get('https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt').text.split('\n')
#     https_list6 = requests.get('https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt').text.split('\n')
#     https_list7 = requests.get('https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/https.txt').text.split('\n')
#     https_list8 = m['Https']
#     https_list = list(set(https_list1 + https_list2 + https_list3 + https_list5 + https_list6 + https_list7 + https_list8))
#     print(len(https_list))
    aa = open(r"C:\Python310\files\proxy.txt",mode="r")
    bb = aa.readlines()
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



    