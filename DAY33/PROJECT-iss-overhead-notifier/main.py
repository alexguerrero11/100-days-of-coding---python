import requests
from datetime import datetime
import smtplib
import time
# getting email and secret keys from env file
from dotenv import load_dotenv
import os

# NYC Location
MY_LAT = 40.7127837
MY_LON = -74.0059413


load_dotenv()
# environment variables
TEST_EMAIL = os.getenv("GMAIL_TEST")
PASSWORD = os.getenv("GMAIL_TEST_PASS")


# Checking if ISS is overhead
def iss_overhead(degree=5):
    # ISS Location API Request
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()  # incase we don't get a 200 code

    # ISS Data
    data = response.json()
    print(f"ISS Data:\n{data}")

    # Fields
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["latitude"])

    # Check if ISS location is near 5 degree of us
    if MY_LAT - degree < iss_latitude < MY_LAT + degree and MY_LON - degree < iss_longitude < MY_LON + degree:
        return True


# Function to determine if its night time
def is_night():
    # Setting NYC Location field into correct format for API Request
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LON,
        "formatted": 0
    }

    # Sunset times with the Current Time API
    response = requests.get("http://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()  # incase we don't get a 200 code

    # Sunset/Sunrise Data
    data = response.json()
    print(f"Sunset/Sunrise Data: {data}")

    # Fields
    sunrise = int(data["results"]["sunrise"].split('T')[1].split(':')[0])
    sunset = int(data["results"]["sunset"].split('T')[1].split(':')[0])

    time_now = datetime.now().hour

    if time_now > sunset or time_now <= sunrise:
        return True  # It's Dark


# ISS Overhead
print(iss_overhead())

# It's Night?
print(is_night())

while True:
    time.sleep(60)  # Run code every 60 seconds
    # Send email to gmail if ISS is overhead and it' night time
    if iss_overhead() and is_night():
        # Connect and Send email
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            # a way of securing our connection
            connection.starttls()
            # login
            connection.login(user=TEST_EMAIL, password=PASSWORD)

            # Send email to
            SEND_TO_EMAIL = "test_email@gmail.com"

            # Body of message
            body = f"Subject: Look Up! \n\n The ISS is above you!"

            # Sending message
            connection.sendmail(
                from_addr=TEST_EMAIL,
                to_addrs=SEND_TO_EMAIL,
                msg=body)
