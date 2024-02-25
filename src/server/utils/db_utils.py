def upload_new_account(username: str, encrypted_password: str) -> int:
    """
    Uploads account data to database, returns accountID of newly created account
    """
    return 0

def validate_new_account(username: str) -> bool:
    """"
    Checks if username exists in database. Return True if it does, False if it doesnt
    """
    return False

def update_account_data(accountID, name=None, height=None, age=None, sex=None) -> dict:
    """
    Uploads account data to database profile that contains accountID. Returns response ex. {'message': "Message here", 'status': 200}
    """
    return {}

def get_user_profile_data(accountID: int) -> dict:
    """
    Returns a dict of ALL data regarding accountID in the database. 
    Returns response ex. {'data1': data1, 'data2': data2, 'message': "Message here", 'status': 200} OR
    {'user_data': {user_data_here}, 'message': "Message here", 'status': 200} whichever ones easier
    """
    return {}

def upload_phase_data(phase_type: str, start_date: str, target_weight: float, target_date: str) -> dict:
    """
    Uploads phase data to database and returns response ex. {'message': "Message here", 'status': 200}
    """
    return {}

def edit_phase_data(phase_id, phase_type=None, start_date=None, target_weight=None, target_date=None) -> dict:
    """
    Edits the specified fields of a phase entry. Fields not provided are not updated. returns response ex. {'message': "Message here", 'status': 200}
    """
    return {}

def delete_current_phase() -> dict:
    """
    Deletes most recent phase data and returns response ex. {'message': "Message here", 'status': 200}
    """
    return {}

def get_phase_data(accountID: str) -> dict:
    """
    Returns all phase data, as well as a message ex. {'phase_data': {all data here}, 'message': "Message here", 'status': 200} or 
    {'data1': data1, 'data2': data2, 'message': "Message here", 'status': 200} whatevers easier
    """
    return {}

def upload_daily_entry(accountID, date, current_weight=None, active_calories_burned=None, resting_calories_burned=None,
                       steps=None, hours_of_sleep=None, daily_calorie_intake=None, daily_protein_intake=None) -> dict:
    """
    Processes and uploads daily data entry. Returns response ex. {'message': "Message here", 'status': 200}
    """
    #date must be in format "%Y-%m-%d"
    return {}

def edit_daily_entry(accountID, date, current_weight=None, active_calories_burned=None, resting_calories_burned=None,
                       steps=None, hours_of_sleep=None, daily_calorie_intake=None, daily_protein_intake=None) -> dict:
    """
    Edit fields to value in arguments. If argument is None, do nothing. Return response  ex. {'message': "Message here", 'status': 200}
    """