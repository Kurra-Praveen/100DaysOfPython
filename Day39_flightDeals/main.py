import requests

END_POINT = "https://api.sheety.co/7fb3c5689a468091190853d840f1c2c5/samples/sheets"
data = {
    "sheet": {
        "companyName": "Tesla",
        "age": "40",
        "salary": "$1238",
        "designation": "Developer"
    }
}

poet_request = requests.post(url=END_POINT, json=data)
print(poet_request.text)

# get=requests.get(url="https://api.sheety.co/7fb3c5689a468091190853d840f1c2c5/samples/sheets")
# dataa=get.json()
# print(dataa)