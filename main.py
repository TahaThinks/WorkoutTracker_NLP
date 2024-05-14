import api_data
import requests
import datetime

current_day = datetime.datetime.now().strftime("%d/%m/%Y")

APP_ID = api_data.NUTRITION_APPID
APP_KEY = api_data.NUTRITION_APPKEY

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "x-remote-user-id": "0"
}

NLP_URL = "https://trackapi.nutritionix.com"
NLP_ENDPOINT = "/v2/natural/exercise"

workout_text = {
    "query": "I swam for 1 hour"
}

response = requests.post(url=f"{NLP_URL}{NLP_ENDPOINT}", headers=headers, json=workout_text)
print(response.text)
