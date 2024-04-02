import pandas
import requests
import json

request = requests.get("https://opentdb.com/api.php?amount=40&type=boolean")
request.raise_for_status()
data = request.json()
entire_data = data["results"]

with open("quiz.json", "w") as file:
    json.dump(entire_data, file,indent=4)
