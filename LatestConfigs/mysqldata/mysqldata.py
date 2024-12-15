import mysql.connector

# Database connection string
connection_string = 'mysql://mysqluser:mysqlpassword@mysql:3306/twitter_data'

# Create database connection
cnx = mysql.connector.connect(user='mysqluser', password='mysqlpassword',
                              host='mysql',
                              database='twitter_data')

# Create table if it doesn't exist
cursor = cnx.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS election_tweets (
        id INT AUTO_INCREMENT PRIMARY KEY,
        tweet_text TEXT,
        sentiment REAL
    );
''')

# Insert processed tweet data into table
for tweet in tweets:
    cursor.execute('''
        INSERT INTO election_tweets (tweet_text, sentiment)
        VALUES (%s, %s);
    ''', (tweet, sentiment))
    cnx.commit()

cursor.close()
cnx.close()