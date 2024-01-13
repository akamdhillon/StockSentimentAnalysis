# Stock Sentiment Analysis
The Stock Sentiment Analysis Python script aims to contribute to predicting future stock prices by leveraging sentiment analysis on news articles related to a specific stock. Through the utilization of various libraries and APIs, the script facilitates the collection, analysis, and potential modeling of data to gain insights into stock sentiment.

# Purpose

The primary objectives of the script include:

Sentiment Analysis:
- Analyzing sentiment in news article titles related to a specified stock.
- Providing sentiment polarity and subjectivity scores for each article.

Historical Stock Price Visualization:
- Fetching historical stock price data using Yahoo Finance.
- Generating visualizations, such as line plots, to illustrate the historical stock prices.

User Interaction:
- Allowing users to input a stock ticker through the terminal or console.
- Console command 'exit' to break while loop of requesting analysis for stock.
- Customizing the analysis parameters, such as the date range and the number of articles to retrieve.

# Usage

To run the script:

1. Open the terminal or console.
2. Input a stock ticker when prompted (e.g., TSLA).
3. The script will output graphs illustrating sentiment analysis and historical stock prices.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<img width="1095" alt="Screen Shot 2024-01-12 at 11 36 34 PM" src="https://github.com/akamdhillon/StockSentimentAnalysis/assets/98356095/f99968e9-d0ce-42d9-aca6-d80208459922">
The stock price of Nvidia(NVDA) over 30-day period.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<img width="1287" alt="Screen Shot 2024-01-12 at 11 36 55 PM" src="https://github.com/akamdhillon/StockSentimentAnalysis/assets/98356095/64ff0b18-c310-44ff-adf9-c3560c62b462">
Sentiment analysis where polarity and subjectivity scores are plotted over time based on article dates.


# Libraries & APIs
Libraries:

yfinance:
- Used for fetching historical stock price data.
- Allows easy access to Yahoo Finance data.

pandas:
- Utilized for handling and manipulating tabular data structures (DataFrames).
- Simplifies the organization and analysis of fetched news articles and stock price data.

matplotlib:
- Creation of visualizations, such as line plots for sentiment analysis and stock prices.

TextBlob:
- Employs natural language processing capabilities for sentiment analysis.
- Provides sentiment polarity and subjectivity scores for news article titles.

APIs:

News API:
- Integrated to fetch news articles related to the entered stock symbol.
- Allows customization of parameters, such as the date range and number of articles.

# Potential Applications
This project serves as a stepping stone toward predicting future stock prices by leveraging news article sentiment. While not a definitive predictor, it provides valuable insights that may be considered alongside other financial indicators.

# Next Steps
Finding correlations between the sentiment analysis for each date an article was released, and the impact on the stock price will serve as an indicator for predicting the future of a stock price.
