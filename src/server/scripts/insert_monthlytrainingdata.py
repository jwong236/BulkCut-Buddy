from utils import get_db_config, read_data_from_csv
from utils.db_utils import Database

# python -m scripts.insert_monthlytrainingdata

def main():
    db_config = get_db_config()
    db = Database(db_config)
    file_path = r'..\..\data\month_training_data_1.csv'
    query = """
            INSERT INTO
                monthlytrainingdata (height, age, sex, phase_type, initial_weight,
                active_calories_burned, resting_calories_burned, steps, hours_of_sleep,
                weight_change_rate, daily_calorie_intake, daily_protein_intake, month_count, future_weight)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
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
