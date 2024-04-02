import requests
key="3f5640a1f87e9020247e996421b36f87"
url=f"https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={key}"
response=requests.get(url)
data=response.json()
print(data)