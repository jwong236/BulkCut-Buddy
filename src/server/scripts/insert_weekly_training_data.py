from database import db_config
from utils import read_training_data_from_csv
from utils.db_utils import insert_training_data

# python -m scripts.insert_training_data

def main():
    file_path = r'..\..\data\week_training_data_1.csv'
    query = """
            INSERT INTO weeklytrainingdata (height, age, sex, phase_type, initial_weight,
                active_calories_burned, resting_calories_burned, steps, hours_of_sleep,
                weight_change_rate, daily_calorie_intake, daily_protein_intake, week_count, future_weight)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    data = read_training_data_from_csv(file_path)
    insert_training_data(data, query, db_config)

if __name__ == "__main__":
    main()
