import mysql.connector
from mysql.connector import pooling

class Database:
    def __init__(self, db_config):
        self.db_pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=5, **db_config)

    def execute_query(self, query, data=None, fetch_one=True):
        response = {
            'message': 'Operation completed successfully.',
            'status': 0,
            'data': None
        }
        try:
            cnx = self.db_pool.get_connection()
            cursor = cnx.cursor()
            if data:
                if isinstance(data[0], tuple):
                    cursor.executemany(query, data) # If data is a list of tuples, method will execute query for each tuple in the list
                else:
                    cursor.execute(query, data) # If data is a single tuple it will execute query on it
            else:
                cursor.execute(query)

            if query.strip().upper().startswith("SELECT"):
                if fetch_one:
                    response['data'] = cursor.fetchone() # If a query returns hundreds of rows, fetchone would return1
                else:
                    response['data'] = cursor.fetchall() # If a query returns hudnreds of rows, fetchall would return all

            cnx.commit()
        except mysql.connector.Error as err:
            response['message'] = f"Error: {err}"
            response['status'] = 1
        finally:
            if cnx.is_connected():
                cursor.close()
                cnx.close()
        return response

    def get_account_id(self, username):
        query = "SELECT account_id FROM profile WHERE username = %s;"
        result = self.execute_query(query, (username,), fetch_one=True)
        if result['status'] == 0 and result['data']:
            return result['data'][0]
        else:
            return None
