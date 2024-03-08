from database import db_config
from utils import read_data_from_csv
from utils.db_utils import Database
from flask import current_app

# python -m scripts.insert_weeklyprojections

def main():
    db = current_app.db
    file_path =   r'..\..\data\dummy_weeklyprojections_data_1.csv'
    query = """
            INSERT INTO 
                weeklyprojections(weekly_projection_id, daily_entry_id, projected_weight, week_count)
            VALUES (%s, %s, %s, %s)
    """
    data = read_data_from_csv(file_path)
    print(f"Read data from file: {data}")
    response = db.execute_query(data, query, db_config)
    if response['status'] != 0:
        print(f"Insert failed: {response['message']}")
    else:
        print("Insert successful")

if __name__ == "__main__":
    main()
