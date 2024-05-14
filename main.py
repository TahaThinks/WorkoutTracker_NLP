import api_data
import requests
import datetime

current_day = datetime.datetime.now().strftime("%d/%m/%Y")
current_time = datetime.datetime.now().strftime("%H:%M:%S")

APP_ID = api_data.NUTRITION_APPID
APP_KEY = api_data.NUTRITION_APPKEY
SHEET_ENDPOINT = api_data.SHEET_ENDPOINT
SHEET_AUTH = api_data.SHEET_AUTH

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "x-remote-user-id": "0"
}

NLP_URL = "https://trackapi.nutritionix.com"
NLP_ENDPOINT = "/v2/natural/exercise"

workout_text = {
    "query": input("Please Enter today's Exercise: ")
}

response = requests.post(url=f"{NLP_URL}{NLP_ENDPOINT}", headers=headers, json=workout_text)
print(response.text)

for exercise in response.json()["exercises"]:
    exercise_data = {
        "workout": {
            "date": current_day,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    # print(exercise_data)
    response = requests.post(url=SHEET_ENDPOINT, json=exercise_data, headers=SHEET_AUTH)
    print(response.text)