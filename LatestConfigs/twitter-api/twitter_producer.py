import tweepy
from kafka import KafkaProducer
import json

# Twitter API credentials
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Kafka producer
producer = KafkaProducer(bootstrap_servers=['kafka:9092'])

# Define search query
search_query = '2024USElection'

# Retrieve tweets
tweets = tweepy.Cursor(api.search_tweets, q=search_query).items(100)

# Produce messages to Kafka topic
for tweet in tweets:
    producer.send('tweets', value=tweet.text.encode('utf-8'))
