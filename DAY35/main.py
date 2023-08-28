# weather api request - DAY 35

# packages
import requests
from dotenv import load_dotenv
import os

# getting secret keys from env file
load_dotenv()

# environment variables
API_KEY = os.getenv("API_KEY")

# ENDPOINT & PARAMETERS
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather?"

WEATHER_PARAMS = {
    "lat": 40.730610,
    "lon": -73.935242,
    "appid": API_KEY,
}

# request
response = requests.get(OWM_ENDPOINT, params=WEATHER_PARAMS)
response.raise_for_status()
weather_data = response.json()

# setting condition
will_rain_today = False

if weather_data['weather'][0]['id'] < 700:
    will_rain_today = True

# confirm if we should bring an umbrella
if will_rain_today:
    print('Bring an umbrella! =(')
else:
    print('Enjoy the weather!!')
