from datetime import datetime

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