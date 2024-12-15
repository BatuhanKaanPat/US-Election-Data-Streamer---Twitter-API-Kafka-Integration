FROM mysql:latest

# Set environment variables
ENV MYSQL_ROOT_PASSWORD=mysqlroot_password
ENV MYSQL_DATABASE=twitter_data
ENV MYSQL_USER=mysqluser
ENV MYSQL_PASSWORD=mysqlpassword

# Copy database initialization script
COPY initdb/database_init.sql /docker-entrypoint-initdb.d/

# Copy additional initialization script to create database and user
COPY create_database.sql /docker-entrypoint-initdb.d/

# Expose port
EXPOSE 3306
