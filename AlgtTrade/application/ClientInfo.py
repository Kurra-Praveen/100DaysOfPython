from SmartApi import SmartConnect
import pyotp


class Client:
    def __init__(self):
        self.api_key: str = "5I424SoO"
        self.totp = pyotp.TOTP("ZUYSVDBEJAI54HAPLTBE44OTWI").now()
        self.clientId: str = "K136197"
        self.pwd: str = "8530"
        self.smartAPI = self.__generateSession()

    def __generateSession(self) -> SmartConnect:
        smartApi = SmartConnect(self.api_key)
        smartApi.generateSession(self.clientId, self.pwd, self.totp)
        return smartApi

    def getFundsInfo(self):
        data = self.smartAPI.holding()
        print(data)

    def getProfileInfo(self):
        smartApi = self.smartAPI
        return smartApi.getProfile(smartApi.refresh_token)

    def logOut(self):
        smartAPI = self.smartAPI
        return smartAPI.terminateSession(self.clientId)

    def getHistoricData(self, historicData):
        smartAPI = self.smartAPI
        return smartAPI.getCandleData(historicData)
