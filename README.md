This project is designed to stream US Election-related data from the Twitter Search API to Kafka in real-time. The setup uses Docker Compose to manage multiple containers, including Kafka, Zookeeper, MySQL, and Spark, for efficient data processing and storage.

Features:
Streams data from Twitter's Search API based on election-related keywords.
Kafka integration for scalable and reliable data streaming.
Docker Compose setup for containerized services (Kafka, Spark, MySQL, Zookeeper).
Real-time data handling and storage for future analysis.

Installation:
Clone this repository.
Configure your Twitter API credentials.
Use Docker Compose to bring up the necessary containers (docker-compose up).
Monitor the data flow and processing through Kafka and Spark.

Usage:
The project streams real-time US Election data and pushes it to Kafka topics.
Use Spark for further processing and analysis of the data.

Requirements:
Docker and Docker Compose
Twitter API access (with the necessary keys)
