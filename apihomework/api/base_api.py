import requests


class BaseApi:
    _CORPID = 'ww7a7ffdd981b9b6b7'
    _CORPSECRET = 'OzAfOCueDHDzt3pLOlZQHMNvanuzLp-tcPKT-4omlcU'
    _URL = f"https://qyapi.weixin.qq.com/cgi-bin"

    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        url = self._URL + f"/gettoken?corpid={self._CORPID}&corpsecret={self._CORPSECRET}"
        r = requests.get(url)
        # 用.get('access_token') 比用 ['access_token'] 要好：因为.get找不到时不会报错
        return r.json().get('access_token')
