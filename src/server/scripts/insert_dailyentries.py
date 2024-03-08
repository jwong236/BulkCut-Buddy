from database import db_config
from utils import read_data_from_csv
from utils.db_utils import insert_data

# python -m scripts.insert_dailyentries

def main():
    file_path = r'..\..\data\dummy_dailyentries_data_1.csv'
    query = """
            INSERT INTO 
                dailyentries (daily_entry_id, phase_id, date, current_weight, active_calories_burned,
                resting_calories_burned, steps, hours_of_sleep, daily_calorie_intake, daily_protein_intake)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    data = read_data_from_csv(file_path)
    print(f"Read data from file: {data}")
    if insert_data(data, query, db_config):
        print("Insert failed")

if __name__ == "__main__":
    main()
