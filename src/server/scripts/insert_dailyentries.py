from utils import get_db_config, read_data_from_csv
from utils.db_utils import Database

# python -m scripts.insert_dailyentries

def main():
    db_config = get_db_config()
    db = Database(db_config)
    file_path = r'..\..\data\dummy_dailyentries_data_1.csv'
    query = """
            INSERT INTO 
                dailyentries (daily_entry_id, phase_id, date, current_weight, active_calories_burned,
                resting_calories_burned, steps, hours_of_sleep, daily_calorie_intake, daily_protein_intake)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    data = read_data_from_csv(file_path)
    print(f"Read data from file: {data}")
    response = db.execute_query(query, data, db_config)
    if response['status'] != 0:
        print(f"Insert failed: {response['message']}")
    else:
        print("Insert successful")

if __name__ == "__main__":
    main()
