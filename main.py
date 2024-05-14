import api_data
import requests
import datetime

current_day = datetime.datetime.now().strftime("%d/%m/%Y")
current_time = datetime.datetime.now().strftime("%H:%M:%S")

APP_ID = api_data.NUTRITION_APPID
APP_KEY = api_data.NUTRITION_APPKEY
SHEET_ENDPOINT = api_data.SHEET_ENDPOINT

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "x-remote-user-id": "0"
}

NLP_URL = "https://trackapi.nutritionix.com"
NLP_ENDPOINT = "/v2/natural/exercise"

workout_text = {
    "query": "I swam for 1 hour and went cycling for 30 minutes"
}

response = requests.post(url=f"{NLP_URL}{NLP_ENDPOINT}", headers=headers, json=workout_text)
print(response.text)

for exercise in response.json()["exercises"]:
    exercise_data = {
        "Date": current_day,
        "Time": current_time,
        "Exercise": exercise["name"],
        "Duration": exercise["duration_min"],
        "Calories": exercise["nf_calories"]
    }
    print(exercise_data)
