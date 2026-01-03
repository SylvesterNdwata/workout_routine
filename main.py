import requests
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
SHEETY_AUTH_KEY = os.environ.get("SHEETY_AUTH_KEY")

base_url = "https://app.100daysofpython.dev"

query = input("What exercise/s did you do today? ")
""" Supported activities:
**Character Limit: 50 Characters
Running/Jogging - "ran for 30 minutes", "jogged 2 miles"
Swimming - "swam for 1 hour", "swimming laps"
Walking - "walked 3 miles", "brisk walk 45 min"
Cycling - "biked for 1 hour", "rode bike 10 miles"
Weightlifting - "lifted weights 45 min", "weight training\""""

parameters = {
    "query": query,
    "weight_kg": 85,
    "height_cm": 184,
    "age": 21,
    "gender": "male"
}

auth_headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

response = requests.post(url=f"{base_url}/v1/nutrition/natural/exercise", json=parameters, headers=auth_headers)
data = response.json()
# print(data["exercises"])

exercise = data["exercises"][0]["name"].title()
today = dt.datetime.now()
date = today.strftime("%d/%m/%Y")
now_time = today.strftime("%X")
duration = data["exercises"][0]["duration_min"]
calories = data["exercises"][0]["nf_calories"]





sheety_url = "https://api.sheety.co/5045b2d0c914791f25027f99d5619b22/workoutRotine/workouts"

sheety_params = {
    "workout": {
        "date": date,
        "time": now_time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}

sheety_auth = {
    "Authorization": SHEETY_AUTH_KEY
}

sheety_response = requests.post(url=sheety_url, json=sheety_params, headers=sheety_auth)
sheety_data = sheety_response.json()
print(sheety_data)