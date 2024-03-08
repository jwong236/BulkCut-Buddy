import mysql.connector

def insert_training_data(data, query, db_config):
    """
    Inserts data specified by a query into a database.

    Args:
        data (list of tuple): Data to be inserted into database.
        query (str): Query that specifies how to insert data into database.
        db_config (dict): Database connection info.

    Returns:
        int: Status code.
    """
    status = 0
    try:
        cnx = mysql.connector.connect(**db_config)
        if cnx.is_connected():
            print("Successfully connected to the database.")
        cursor = cnx.cursor()
        cursor.executemany(query, data)
        cnx.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        status = 1
    finally:
        if cnx.is_connected():
            cursor.close()
            cnx.close()
    return status
