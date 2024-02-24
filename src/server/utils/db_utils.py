import mysql.connector
def fetch_user_data():
    """
    Establishes a connection with the MySql server and fetches user data
    """
    config = {
        'user': 'database username',
        'password': 'database password',
        'host': 'localhost',
        'database': 'our database name',
        'raise_on_warnings': True
    }
    try:
        # Establishing a connection to the database
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor(dictionary=True)

        query = """
        SELECT 
            initial_weight, body_fat_percentage, height, gender,
            weight_change_metric, active_calories_burned, resting_calories_burned, steps, hours_of_sleep,
            daily_calorie_intake, daily_protein_intake,
            week_count,
            future_weight
        FROM
            our_table_name
        """

        # Execute the query
        cursor.execute(query)

        # Fetch all rows from the query result
        result = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        cnx.close()

        # If nothing was fetched into result then return an empty dict
        if result:
            return result[0]  # Return the first row as a dictionary
        else:
            return {}

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return {}