import requests
from datetime import datetime

APK_ID = "98a249eb"
APK_KEY = "267d94f754be0b3b0d0ec02f9da23fa3"
GENDER = "Male"
WEIGHT = "65",
HEIGHT = "168"
AGE = 22
END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = "https://api.sheety.co/7fb3c5689a468091190853d840f1c2c5/workouts/workouts"
headers = {
    "x-app-id": APK_ID,
    "x-app-key": APK_KEY
}

data = {
    "query": "ran 3 miles",
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}

post_request = requests.post(url=END_POINT, json=data, headers=headers)
excersie_data = post_request.json()

duration = excersie_data["exercises"][0]["duration_min"]
calories = excersie_data["exercises"][0]["nf_calories"]
excersice_name = excersie_data["exercises"][0]["name"].title()
current_date = datetime.now().strftime("%x")
current_time = datetime.now().strftime("%X")
sheet_data = {
    "workout": {
        "date": current_date,
        "time": current_time,
        "exercise": excersice_name,
        "duration": duration,
        "calories": calories,

    }

}
sheet_request = requests.post(url=SHEET_ENDPOINT, json=sheet_data)
print(sheet_request.text)

# get = requests.get(url="https://api.sheety.co/7fb3c5689a468091190853d840f1c2c5/workouts/workouts")
# print(get.json())
