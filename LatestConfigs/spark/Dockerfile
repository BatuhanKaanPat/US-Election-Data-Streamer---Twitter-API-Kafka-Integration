FROM bitnami/spark:3.0.1

# Set working directory
WORKDIR /opt/spark-apps

# Install dependencies for Python
USER root
RUN apt-get update && apt-get install -y python3-pip

# Install Python dependencies
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the Spark application
COPY spark.py spark.py

# Set the default command to run the Spark job
CMD ["/opt/bitnami/spark/bin/spark-submit", "--master", "spark://spark:7077", "spark.py"]