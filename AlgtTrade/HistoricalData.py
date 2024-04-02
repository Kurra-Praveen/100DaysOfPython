import requests
import pandas as pd
import time

url = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"


def get_marketInfo():
    try:
        start_time = time.time()
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data)
            end_time = time.time()
            total_time = end_time - start_time
            return df
        else:
            print("Request failed with status code:", response.status_code)
            return "invalid status code"

    except requests.RequestException as e:
        print("Error occurred during the request:", e)


