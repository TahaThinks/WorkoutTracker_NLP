import api_data
import requests

APP_ID = api_data.NUTRITION_APPID
APP_KEY = api_data.NUTRITION_APPKEY

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "x-remote-user-id": "0"
}

