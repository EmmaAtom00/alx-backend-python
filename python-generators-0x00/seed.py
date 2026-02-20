import mysql.connector
import csv
import uuid
import os

def connect_db():
    """Connects to the MySQL database server."""
    try:
        connection = mysql.connector.connect(
            host=os.getenv('ALX_MYSQL_HOST', 'localhost'),
            user=os.getenv('ALX_MYSQL_USER', 'root'),
            password=os.getenv('ALX_MYSQL_PWD', '')
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_database(connection):
    """Creates the database ALX_prodev if it does not exist."""
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def connect_to_prodev():
    """Connects to the ALX_prodev database in MySQL."""
    try:
        connection = mysql.connector.connect(
            host=os.getenv('ALX_MYSQL_HOST', 'localhost'),
            user=os.getenv('ALX_MYSQL_USER', 'root'),
            password=os.getenv('ALX_MYSQL_PWD', ''),
            database='ALX_prodev'
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_table(connection):
    """Creates a table user_data if it does not exists with the required fields."""
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id VARCHAR(128) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL(10, 0) NOT NULL,
                INDEX (user_id)
            )
        """)
        connection.commit()
        cursor.close()
        print("Table user_data created successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def insert_data(connection, data_file):
    """Inserts data in the database if it does not exist."""
    try:
        cursor = connection.cursor()
        with open(data_file, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Check if user already exists
                cursor.execute("SELECT 1 FROM user_data WHERE user_id = %s", (row['user_id'],))
                if cursor.fetchone() is None:
                    cursor.execute(
                        "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)",
                        (row['user_id'], row['name'], row['email'], row['age'])
                    )
        connection.commit()
        cursor.close()
    except (mysql.connector.Error, FileNotFoundError) as err:
        print(f"Error: {err}")
