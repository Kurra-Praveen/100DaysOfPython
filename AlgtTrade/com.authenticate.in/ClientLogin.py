import http.client
import json

import pyotp
from SmartApi import SmartConnect

import EndPoints
import MyUtils


class Login:
    def __init__(self):
        self.api_key: str = MyUtils.getValue("api_key")
        self.clientId: str = MyUtils.getValue("clientId")
        self.token: str = MyUtils.getValue("token")
        self.pwd: str = MyUtils.getValue("pwd")
        self.connection = http.client.HTTPSConnection(EndPoints.BASE_URL)

    def generateSession(self):
        MyUtils.client_info()
        smartApi = SmartConnect(self.api_key)
        var = smartApi.clientLocalIP
        totp = pyotp.TOTP(self.token).now()
        data = smartApi.generateSession(self.clientId, self.pwd, totp)
        print(data)
        authToken = data['data']['jwtToken']
        refreshToken = data['data']['refreshToken']
        feedToken = smartApi.getfeedToken()
        MyUtils.setValue(key="AUTHORIZATION_TOKEN", value=authToken)
        MyUtils.setValue(key="Refresh_Token", value=refreshToken)
        MyUtils.setValue(key="Feed_Token", value=feedToken)

        return {"authToken": authToken, "refreshToken": refreshToken, "feedToken": feedToken}

    def logout(self):
        payload = {'clientcode': f'{self.clientId}'}
        # conn = http.client.HTTPSConnection(EndPoints.BASE_URL)
        conn = self.connection
        conn.request("POST", EndPoints.LOGOUT_ENDPOINT, json.dumps(payload), EndPoints.getHeaders())
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))

    def getProfileInfo(self):
        conn = self.connection
        payload = ''
        conn.request("GET", EndPoints.PROFILE_ENDPOINT, payload, EndPoints.getHeaders())
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))
        return data.decode("utf-8")
