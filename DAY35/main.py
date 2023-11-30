# DAY 35 - Rain Alert (weather api request)

# import packages
import requests
from dotenv import load_dotenv
import os
import smtplib

# getting secret keys from env file
load_dotenv()

# environment variables
API_KEY = os.getenv("API_KEY")
TEST_EMAIL = os.getenv("GMAIL_TEST")
PASSWORD = os.getenv("GMAIL_TEST_PASS")
TO_EMAIL = os.getenv("TO_EMAIL")

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
    body = 'Looking at the weather today: bring an umbrella! =('
else:
    body = 'Looking at the weather today: Enjoy the weather'


# Connect and Send Quote
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # a way of securing our connection
        connection.starttls()
        # login
        connection.login(user=TEST_EMAIL, password=PASSWORD)

        # Body of message
        body = f"Subject: Today's Weather Forecast \n\n This is your daily reminder! {body}."

        # Sending message
        connection.sendmail(
            from_addr=TEST_EMAIL,
            to_addrs=TO_EMAIL,
            msg=body)
