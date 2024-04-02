import json
import requests

# import json

MY_LAN = 81.138481
MY_LAT = 16.506323
parameters = {
    "lat": MY_LAT,
    "lan": MY_LAN
}
response = requests.get(f"https://api.sunrise-sunset.org/json", params=parameters)

response.raise_for_status()
data = response.json()
with open("myfile.json", "w") as file:
    json.dump(data, file, indent=4)
print(data)
