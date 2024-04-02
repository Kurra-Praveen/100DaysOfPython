import requests
import pandas as pd
import datetime

url = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"


def get_marketInfo():
    try:
        # columns = ['token', 'symbol', 'name', 'expiry', 'strike', 'lotsize', 'instrumenttype', 'exch_seg',
        # 'tick_size']
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data)
            # var = df[(df['strike'] == getLastFriday()) & (df['instrumenttype'] == "FUTSTK")]
            var = df[(df['instrumenttype'] == "FUTSTK") & (df['expiry'] == getLastFriday())]
            print(var.head(1))
            return ""
        else:
            print("Request failed with status code:", response.status_code)
            return "invalid status code"

    except requests.RequestException as e:
        print("Error occurred during the request:", e)


def getLastFriday():
    today = datetime.date.today()
    month = today.strftime("%b").upper()
    lastDayOfMonth = datetime.date(today.year, today.month, 1) + datetime.timedelta(days=32)
    lastDayOfMonth -= datetime.timedelta(days=lastDayOfMonth.day)
    while lastDayOfMonth.weekday() != 3:
        lastDayOfMonth -= datetime.timedelta(days=1)
    return str(lastDayOfMonth).split("-")[2] + month + today.year.__str__()


if __name__ == '__main__':
    # print("praveen" == "praveen")
    print(getLastFriday())
    get_marketInfo()
