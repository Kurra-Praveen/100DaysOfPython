import http.client
import json

import EndPoints


class HistoricalCandleData:
    def __init__(self, exchange, symboltoken):
        self.exchange = exchange
        self.symboltoken = symboltoken

    def getHistoricalData(self, interval, fromDate, toDate):
        conn = http.client.HTTPSConnection(EndPoints.BASE_URL)
        payload = self.getBody(interval=interval, fromDate=fromDate, toDate=toDate)
        conn.request("POST", EndPoints.HISTORICAL_ENDPOINT, payload, EndPoints.getHeaders())
        res = conn.getresponse()
        var = res.status
        print(var)
        data = res.read()
        return data.decode("utf-8")

    def getBody(self, interval, fromDate, toDate):
        data = {
            "exchange": self.exchange,
            "symboltoken": self.symboltoken,
            "interval": interval,
            "fromdate": fromDate,
            "todate": toDate
        }
        return json.dumps(data)
