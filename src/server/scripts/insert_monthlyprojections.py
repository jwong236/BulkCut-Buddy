from utils import get_db_config, read_data_from_csv
from utils.db_utils import Database

# python -m scripts.insert_monthlyprojections

def main():
    db_config = get_db_config()
    db = Database(db_config)
    file_path = r'..\..\data\dummy_monthlyprojections_data_1.csv'
    query = """
            INSERT INTO 
                monthlyprojections(monthly_projection_id, daily_entry_id, projected_weight, month_count)
            VALUES (%s, %s, %s, %s)
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
