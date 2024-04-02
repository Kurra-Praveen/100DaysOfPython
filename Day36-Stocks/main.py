import requests
import html
import json
import pandas

STOCKS_API_KEY = "Z0YZM1A7WDRXP3N9"
NEWS_API_KEY = "7177b7b63cf243e49da5bcbc863605f4"
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "interval": "15min",
    "apikey": STOCKS_API_KEY
}
news_parameters = {
    "apiKey": NEWS_API_KEY,
    "q": "TESLA",
}
stocks_request = requests.get("https://www.alphavantage.co/query", params=stock_parameters)
stocks_request.raise_for_status()
stocks_data = stocks_request.json()["Time Series (Daily)"]

news_request = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
news_request.raise_for_status()
news_articles = news_request.json()["articles"]

extracted_data = [value for (key, value) in stocks_data.items()]
yesterday_closing_price = float(extracted_data[0]['4. close'])
oneday_before_closing_price = float(extracted_data[1]['4. close'])
difference = abs(yesterday_closing_price - oneday_before_closing_price)
percentage = (difference / yesterday_closing_price) * 100

latest_articles = [article for article in news_articles[:3]]
each_news = [f"Headline:{html.unescape(item['title'])} .\n Breif: {html.unescape(item['description'])}" for item in
             latest_articles]
for news in each_news:
    print(news)
