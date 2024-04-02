import random
import time
from timeit import timeit
import concurrent.futures
import requests
import pandas as pd
import datetime
import numpy as np

url = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"


def get_FandO_stocks():
    try:
        df = pd.read_json("sample.json")
        var = df[(df['instrumenttype'] == "FUTSTK") & (df['expiry'] == getLastFriday())]
        fAndoStrocks = var["name"].values.tolist()
        # np.save("output.npy", np.array(fAndoStrocks))
        new_list = [item + "-EQ" for item in fAndoStrocks]
        validatingF_OData = df[df["symbol"].isin(new_list)]
        return validatingF_OData[["token", "symbol"]].to_dict(orient="records")
    except Exception as e:
        print(e)


def getLastFriday():
    today = datetime.date.today()
    month = today.strftime("%b").upper()
    lastDayOfMonth = datetime.date(today.year, today.month, 1) + datetime.timedelta(days=32)
    lastDayOfMonth -= datetime.timedelta(days=lastDayOfMonth.day)
    while lastDayOfMonth.weekday() != 3:
        lastDayOfMonth -= datetime.timedelta(days=1)
    return str(lastDayOfMonth).split("-")[2] + month + today.year.__str__()


def getPriceData(data):
    data["increase"] = random.randint(-5, 5)
    random.randbytes(5)
    time.sleep(1)
    return data


if __name__ == "__main__":
    get_stocks = get_FandO_stocks()
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        output = list(executor.map(getPriceData, get_stocks))
    # output = [getPriceData(item) for item in get_stocks]
    end = time.time()
    print(output)
    print(end - start)
