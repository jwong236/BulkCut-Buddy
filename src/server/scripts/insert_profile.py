from database import db_config
from utils import read_training_data_from_csv
from utils.db_utils import insert_training_data

# python -m scripts.insert_profile

def main():
    file_path = r'..\..\data\dummy_profile_data_1.csv'
    query = """
            INSERT INTO 
                profile (name, username, password_hash, height, age, sex)
            VALUES (%s, %s, %s, %s, %s, %s)
    """
    data = read_training_data_from_csv(file_path)
    print(f"Read data from file: {data}")
    if insert_training_data(data, query, db_config):
        print("Insert failed")

if __name__ == "__main__":
    main()
