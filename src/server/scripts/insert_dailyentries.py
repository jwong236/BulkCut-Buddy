from database import db_config
from utils import read_data_from_csv
from utils.db_utils import Database
from flask import current_app

# python -m scripts.insert_dailyentries

def main():
    db = current_app.db
    file_path = r'..\..\data\dummy_dailyentries_data_1.csv'
    query = """
            INSERT INTO 
                dailyentries (daily_entry_id, phase_id, date, current_weight, active_calories_burned,
                resting_calories_burned, steps, hours_of_sleep, daily_calorie_intake, daily_protein_intake)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
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
