import mysql.connector
seed = __import__('seed')

def stream_users_in_batches(batch_size):
    """Generator that fetches rows from the user_data table in batches."""
    connection = seed.connect_to_prodev()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM user_data")
            while True:
                batch = cursor.fetchmany(batch_size)
                if not batch:
                    break
                yield batch
            cursor.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            connection.close()

def batch_processing(batch_size):
    """Processes each batch to filter and print users over the age of 25."""
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)
