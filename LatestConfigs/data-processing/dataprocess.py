from kafka import KafkaConsumer
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Kafka consumer
consumer = KafkaConsumer('tweets', bootstrap_servers=['kafka:9092'])

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Consume messages from Kafka topic
for message in consumer:
    tweet_text = message.value.decode('utf-8')
    sentiment = sia.polarity_scores(tweet_text)
    # Produce processed message to another Kafka topic
    producer = KafkaProducer(bootstrap_servers=['kafka:9092'])
    producer.send('processed_tweets', value=str(sentiment).encode('utf-8'))