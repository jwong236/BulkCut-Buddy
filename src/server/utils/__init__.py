from datetime import datetime
import csv

def validate_password(password: str) -> bool:
    """
    Checks if password fulfills password requirements. Return True if it does, False if it doesnt
    """
    return False

def encrypt_password(password: str) -> str:
    """
    Encrypts password
    """
    # Hash password using bcrypt or werkzeug.security maybe
    return ""

def str_to_datatime(value):
    """
    Attempts to parse a datetime string into a datetime object.
    """
    # Define your datetime format
    datetime_format = "%Y-%m-%d"
    try:
        return datetime.strptime(value, datetime_format)
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format")
    
def read_training_data_from_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        data = [tuple(row) for row in csv_reader]
    return data