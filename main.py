import yfinance as yf
import numpy as np
import pandas as pd
import requests
import matplotlib.pyplot as plt
from textblob import TextBlob
from datetime import datetime, timedelta

# Function to analyze sentiment for a list of texts
def analyze_sentiment(text_list):
    polarities = []
    subjectivities = []

    for text in text_list:
        blob = TextBlob(text)
        sentiment_polarity = blob.sentiment.polarity
        sentiment_subjectivity = blob.sentiment.subjectivity
        polarities.append(sentiment_polarity)
        subjectivities.append(sentiment_subjectivity)

    return np.array(polarities), np.array(subjectivities)

api_key = '2537c63164734b82bb0741c0bd2200c9'

# Function to search for news articles and return a DataFrame
def search_articles(api_key, keyword, from_date, to_date, page_size=20):
    url = f'https://newsapi.org/v2/everything?q={keyword}&apiKey={api_key}&from={from_date}&to={to_date}&pageSize={page_size}'

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        articles_list = [{'title': article['title'], 'date': article['publishedAt'].split('T')[0]} for article in data['articles']]
        articles_df = pd.DataFrame(articles_list)
        return articles_df
    else:
        print(f"Error: {data['message']}")
        return None

while True:
    symbol = input("Enter the stock symbol, or type 'exit' to end: ").upper()

    if symbol.lower() == 'exit':
        break

    # Define the date range for the last 30 days
    to_date = datetime.now().strftime('%Y-%m-%d')
    from_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')

    # Search for news articles related to the stock symbol
    articles_df = search_articles(api_key, symbol, from_date, to_date, page_size=5)  # Adjust page_size as needed

    if articles_df is not None:

        # Sort by date
        articles_df = articles_df.sort_values(by='date')

        # Extract titles and dates from the DataFrame
        article_titles = articles_df['title']

        # Analyze sentiment for the list of article titles
        polarities, subjectivities = analyze_sentiment(article_titles)

        # Print sentiment analysis results
        for i in range(len(polarities)):
            print(f"Article: {article_titles.iloc[i]}")
            print(f"Date: {articles_df['date'].iloc[i]}")
            print(f"Sentiment Polarity: {polarities[i]}")
            print(f"Sentiment Subjectivity: {subjectivities[i]}")
            print("---")

        # Plot sentiment polarities and subjectivities over time
        plt.figure(figsize=(12, 6))

        # Plot sentiment polarities
        plt.subplot(2, 1, 1)
        plt.plot(articles_df['date'], polarities, marker='o', linestyle='-', label='Sentiment Polarity')
        plt.title('Sentiment Analysis Over Time')
        plt.ylabel('Sentiment Polarity')
        plt.xticks(articles_df['date'])
        plt.legend()
        plt.grid(True)

        # Plot sentiment subjectivities
        plt.subplot(2, 1, 2)
        plt.plot(articles_df['date'], subjectivities, marker='o', linestyle='-', color='orange', label='Sentiment Subjectivity')
        plt.xlabel('Date')
        plt.ylabel('Sentiment Subjectivity')
        plt.xticks(articles_df['date'])
        plt.legend()
        plt.grid(True)

        plt.tight_layout()
        plt.show()

        # Plot stock prices over time
        data = yf.Ticker(symbol)
        historical_data = data.history(period='1mo')

        dates = historical_data.index
        open_prices = historical_data['Open']

        plt.figure(figsize=(12, 6))
        plt.plot(dates, open_prices, label='Prices', color='blue')
        plt.title(f'{symbol} Prices - Year To Date')
        plt.xlabel('Date')
        plt.ylabel(f'{symbol} Price')
        plt.legend()
        plt.grid(True)
        plt.show()
