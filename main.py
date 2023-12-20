import requests
from datetime import datetime as dt
import os

GENDER = "male"
WEIGHT_KG = "72"
HEIGHT_CM = "164"
AGE = "24"

APP_ID = os.environ.get("API_ID")
API_KEY = os.environ["API_KEY"]

domain = "https://trackapi.nutritionix.com"

exercise_endpoint = f"{domain}/v2/natural/exercise"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
exercise_text = input("Tell me which exercises you did: ")
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, params=parameters, headers=headers)
result = response.json()

today_date = dt.now().strftime("%d/%m/%Y")
time_now = dt.now().strftime("%X")
sheet_endpoint = os.environ.get("SHEET_ENDPOINT")
auth_token = os.environ.get("TOKEN")
sheet_header = {
    "Authorization": auth_token
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=sheet_header)





