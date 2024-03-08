from database import db_config
from utils import read_data_from_csv
from utils.db_utils import insert_data

# python -m scripts.insert_monthlytrainingdata

def main():
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
    if insert_data(data, query, db_config):
        print("Insert failed")

if __name__ == "__main__":
    main()
