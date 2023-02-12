import pandas as pd
from datetime import datetime
import random
import smtplib

# 1. Update the birthdays.csv with your friends & family's details.
birthday_data = pd.read_csv("birthdays.csv")
# print(birthday_data)

# 2. Check if today matches a birthday in the birthdays.csv
today = datetime.now()  # gives me the full date + time datestamp
today_tuple = (today.month, today.day)

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthday_data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name
# from birthdays.csv
    print(birthdays_dict[today_tuple][3])

    letter_file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(letter_file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", birthday_person["name"])
        print(content)

# 4. Send the letter generated in step 3 to that person's email address.
    birthday_person_email = birthday_person["email"]
    birthday_person_year = birthday_person["year"]

    # getting email and secret keys from env file
    from dotenv import load_dotenv
    import os

    load_dotenv()
    # environment variables

    TEST_EMAIL = os.getenv("GMAIL_TEST")
    PASSWORD = os.getenv("GMAIL_TEST_PASS")

    # Connect and Send Quote
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # a way of securing our connection
        connection.login(user=TEST_EMAIL, password=PASSWORD)  # login

        # Send email to
        SEND_TO_EMAIL = birthday_person_email
        # Body of message
        body = f"Subject: Happy Birthday!\n\n {content}."

        # Sending message
        connection.sendmail(
            from_addr=TEST_EMAIL,
            to_addrs=SEND_TO_EMAIL,
            msg=body)
