import pandas as pd
import pyodbc
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER lexicon for sentiment analysis if not already present.
nltk.download('vader_lexicon')

# Function to fetch data from a SQL database using a SQL Query.
def fetch_data_from_sql():
    # Defining Connection String with parameters for the database connection
    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=DESKTOP-G3BBETR\\SQLEXPRESS;"
        "DATABASE=PortfolioProject_MarketingAnalytics;"
        # "UID=DESKTOP-IU9C2BO\\ommeh;"
        "Trusted_Connection=yes;"
        "PWD="
    )
    # Establish the connection to the database
    conn = pyodbc.connect(conn_str)
    
    # SQL Query to fetch customer reviews data
    query = "SELECT ReviewID, CustomerID, ProductID, ReviewDate, Rating, ReviewText FROM customer_reviews"
    
    # Executing the query and fatch the data into a dataframe
    df = pd.read_sql(query, conn)
    
    # Closing the connection
    conn.close()
    
    # Return the fetch data as dataframe
    return df

# Fetching the customer reviews data from the SQL database
customer_reviews_df = fetch_data_from_sql()

# Initialize the VADER sentiment intensity analyzer for analyzing the sentiment of text data
sia = SentimentIntensityAnalyzer()

# Function to calculate sentiment score using VADER
def calculate_sentiment(review):
    # Get the sentiment score for the review text
    sentiment = sia.polarity_scores(review)
    # Return the compound score, which is a normalized score between -1 (most negative) and 1 (most positive)
    return sentiment['compound']

# Function to categorize sentiment using both the sentiment score and review rating
def categorize_sentiment(score, rating):
    # Using both the sentiment score and the numerical rating to determine sentiment category
    if score > 0.05: # Positive Sentiment Score
        if rating >= 4:
            return 'Positive' # High Rating and Positive Sentiment
        elif rating == 3:
            return 'Mixed Positive' # Neutral Rating and Positive Sentiment
        else:
            return 'Mixed Negative' # Low rating but positive sentiment
    elif score < -0.05: # Negative Sentiment Score
        if rating <= 2:
            return 'Negative' # Low rating and negative sentiment
        elif rating == 3:
            return 'Mixed Negative' # Neutral rating and negative sentiment
        else:
            return 'Mixed Positive' # High rating but negative sentiment
    else: # Neutral Sentiment Score
        if rating >= 4:
            return 'Positive' # High Rating with neutral sentiment
        elif rating <= 2:
            return 'Negative' # Low Rating with neutral sentiment
        else:
            return 'Neutral' # Neutral rating and neutral sentiment

# Function to bucket sentiment scores into text ranges
def sentiment_bucket(score):
    if score >= 0.5:
        return '0.5 to 1.0' # Strongly positive sentiment
    elif 0.0 <= score < 0.5:
        return '0.0 to 0.49' # Mildy positive sentiment
    elif -0.5 <= score < 0.0:
        return '0.-49 to 0.0' # Mildy negative sentiment
    else:
        return '-1.0 to -0.5' # Strongly negative sentiment

# Sentiment analysis to calculate sentiment score for each review
customer_reviews_df['SentimentScore'] = customer_reviews_df['ReviewText'].apply(calculate_sentiment)

# Sentiment categorization using both text and rating
customer_reviews_df['Sentiment Category'] = customer_reviews_df.apply(
    lambda row: categorize_sentiment(row['SentimentScore'], row['Rating']), axis=1)

# Sentiment bucketing to categorize scores into defined ranges
customer_reviews_df['SentimentBucket'] = customer_reviews_df['SentimentScore'].apply(sentiment_bucket)

# Displaying first few rows of the dataframe after sentiment analysis
print(customer_reviews_df.head())

# Save the dataframe as a CSV file
customer_reviews_df.to_csv('Fact_Customer_Sentiment_Analysis.csv', index=False)