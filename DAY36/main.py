# DAY 36 - Stock Price

# Import packages
from dotenv import load_dotenv
import requests
import os
from datetime import datetime, timedelta

# Getting secrets
load_dotenv()

# Declaring variables
STOCK_API_KEY = os.getenv('STOCK_API_KEY')
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
TEST_EMAIL = os.getenv("GMAIL_TEST")
PASSWORD = os.getenv("GMAIL_TEST_PASS")
TO_EMAIL = os.getenv("TO_EMAIL")

# Stock Parameters
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

# API Endpoints
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g.
#  [new_value for (key, value) in dictionary.items()]
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key

# Import data
stock_url = f'{STOCK_ENDPOINT}?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey={STOCK_API_KEY}'
r = requests.get(stock_url)
data = r.json()
# HELPER - print out data
print(data)

# Get the current date and time
current_date_time = datetime.now()

# Calculate the difference
# Format the date as a string
yesterday = (current_date_time - timedelta(days=1)).strftime("%Y-%m-%d")
day_before_yesterday = (current_date_time - timedelta(days=2)).strftime("%Y-%m-%d")

# Extract yesterdays closing stock price
yesterday_closing = [value['4. close'] for date, value in data['Time Series (Daily)'].items() if date ==
                     yesterday][0]

# TODO 2. - Get the day before yesterday's closing stock price

# Extract day before yesterday closing stock price
day_before_yesterday_closing = [value['4. close'] for date, value in data['Time Series (Daily)'].items() if date ==
                     day_before_yesterday][0]

print("Today's date is:", day_before_yesterday)
print("Stock Closing Price:", float(day_before_yesterday_closing))
print("Today's date is:", yesterday)
print("Stock Closing Price:", float(yesterday_closing))

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
#  Hint: https://www.w3schools.com/python/ref_func_abs.asp
price_difference = abs(float(yesterday_closing) - float(day_before_yesterday_closing))
print(price_difference)

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before
#  yesterday.
percent_change = (price_difference / float(day_before_yesterday_closing)) * 100
print(f'{percent_change:.2f}%')


# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
trigger = 5
if percent_change > 5:
    print('Get News')
else:
    print('Dont get news')
## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
# Import data
news_url = f'{NEWS_ENDPOINT}?q={STOCK_NAME}&from={day_before_yesterday}&to={day_before_yesterday}&sortBy=popularity&apikey={NEWS_API_KEY}'
r = requests.get(news_url)
news_data = r.json()

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
number_of_articles = 3

sliced_news_data = news_data['articles'][0:number_of_articles]
print(len(sliced_news_data))

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

for article in sliced_news_data:
    print(article['title'])
    print(article['description'])

    for _ in article:
        print(_)

# TODO 9. - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""