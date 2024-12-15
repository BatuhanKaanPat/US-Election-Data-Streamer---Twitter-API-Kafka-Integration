CREATE TABLE IF NOT EXISTS election_tweets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tweet_text TEXT,
    sentiment REAL
);