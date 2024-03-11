from database import db_config
from utils import read_data_from_csv
from utils.db_utils import Database

# python -m scripts.insert_phases

def main():
    db = Database(db_config)
    file_path = r'..\..\data\dummy_phases_data_1.csv'
    query = """
            INSERT INTO 
                phases (phase_id, account_id, phase_type, start_date, target_weight, target_date)
            VALUES (%s, %s, %s, %s, %s, %s)
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
