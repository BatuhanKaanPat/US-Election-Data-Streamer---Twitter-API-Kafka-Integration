from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Connect to the MySQL database
cnx = mysql.connector.connect(
    user='mysqluser',
    password='mysqlpassword',
    host='mysql',
    database='twitter_data'
)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/tweets')
def get_tweets():
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM tweets')
    tweets = cursor.fetchall()
    return jsonify([{'id': tweet[0], 'text': tweet[1]} for tweet in tweets])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')