from datetime import datetime
import csv
import bcrypt
import re
import configparser
import os

def str_to_datetime(value: str) -> datetime:
    """
    Attempts to parse a datetime string into a datetime object.
    """
    datetime_format = "%Y-%m-%d"
    try:
        return datetime.strptime(value, datetime_format)
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format")

    
def read_data_from_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        data = [tuple(row) for row in csv_reader]
    return data

def validate_password(password: str) -> bool:
    """
    Checks if the password fulfills password requirements. 
    Returns True if it does, False otherwise.
    """
    if len(password) < 8:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True

def encrypt_password(password: str) -> str:
    """
    Encrypts (hashes) a password using bcrypt.
    """
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed.decode()

def get_db_config():
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'config.ini')
    config_path = os.path.normpath(config_path)
    config.read(config_path)
    db_config = {
        'host': config['DATABASE']['host'],
        'database': config['DATABASE']['database'],
        'user': config['DATABASE']['user'],
        'password': config['DATABASE']['password'],
        'port': int(config['DATABASE']['port'])
    }
    return db_config