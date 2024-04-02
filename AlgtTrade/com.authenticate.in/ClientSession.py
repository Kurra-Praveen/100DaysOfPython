import http.client
import json
import time

import requests

import EndPoints
import MyUtils
from ClientLogin import Login


def getPreciseData(clientIpAddress):
    data = {
        "exchange": "NSE",
        "symboltoken": "2885",
        "interval": "ONE_MINUTE",
        "fromdate": "2023-07-10 09:15",
        "todate": "2023-07-10 09:16"
    }
    if clientIpAddress is None:
        login = Login()
        login.generateSession()
    conn = http.client.HTTPSConnection(EndPoints.BASE_URL)
    payload = json.dumps(data)
    headers = {
        'X-PrivateKey': str(MyUtils.getValue("api_key")),
        'Accept': 'application/json',
        'X-ClientLocalIP': str(MyUtils.getValue("CLIENT_LOCAL_IP")),
        'X-MACAddress': str(MyUtils.getValue("MAC_ADDRESS")),
        'X-UserType': 'USER',
        'Authorization': str(MyUtils.getValue("AUTHORIZATION_TOKEN")),
        'X-SourceID': 'WEB',
        'Content-Type': 'application/json',
    }
    conn.request("POST", EndPoints.LOGIN_ENDPOINT, payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


def getData():
    start = time.time()
    headers = {
        'X-PrivateKey': str(MyUtils.getValue("api_key")),
        'Accept': 'application/json',
        'X-ClientLocalIP': str(MyUtils.getValue("CLIENT_LOCAL_IP")),
        'X-MACAddress': str(MyUtils.getValue("MAC_ADDRESS")),
        'X-ClientPublicIP': str(MyUtils.getValue("CLIENT_PUBLIC_IP")),
        'X-UserType': 'USER',
        'Authorization': str(MyUtils.getValue("AUTHORIZATION_TOKEN")),
        'X-SourceID': 'WEB',
        'Content-Type': 'application/json',
    }
    data = {
        "exchange": "NSE",
        "symboltoken": "2885",
        "interval": "ONE_MINUTE",
        "fromdate": "2023-07-10 09:15",
        "todate": "2023-07-10 09:16"
    }
    url = "https://apiconnect.angelbroking.com/rest/secure/angelbroking/historical/v1/getCandleData"
    response = requests.post(url, data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        print("Request successful!")
        print(response.json())  # If the response is also in JSON format
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response)

    end = time.time()
    print(end - start)


getData()
# getPreciseData(MyUtils.getValue("CLIENT_LOCAL_IP"))
