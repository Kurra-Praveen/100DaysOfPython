import requests

key = "3f5640a1f87e9020247e996421b36f87"
url = f"https://restcountries.com/v3.1/name/India"
response = requests.get(url)
data = response.json()[1]['tld']
print(data)
print(isinstance(data, dict))
print(isinstance(data, list))
