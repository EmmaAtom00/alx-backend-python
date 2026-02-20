import mysql.connector
seed = __import__('seed')

def stream_users():
    """Generator that yields rows from the user_data table one by one."""
    connection = seed.connect_to_prodev()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM user_data")
            for row in cursor:
                yield row
            cursor.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            connection.close()
