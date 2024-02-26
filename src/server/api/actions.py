from utils import validate_password, encrypt_password

# PROFILERESOURCE METHODS

def create_new_profile(username: str, password_hash: str) -> dict:
    """
    1. Validates if password meets requirements
    2. Validates if username already exists
    3. Encrypts password
    4. Uploads encrypted password to database
    Returns accountID of new account

    Args:
        username (str): The username of the new user.
        password_hash (str): The hashed password for the new user.

    Returns:
        dict: {'account_id': account_id, 'message': message, "status": status}
    """
    # Example implementation, but do whatever you want
    # if not validate_password(password):
    #     return {'message': "Password does not meet requirements", "status": 400}
    # if not validate_new_account(username):
    #     return {'message': "Account with that username already exists", "status": 409}
        
    # encrypted_password = encrypt_password(password)
    # new_accountID = upload_new_account(username, encrypted_password)
    return {'account_id': 0, 'message': "Account created successfully", "status": 201}

def get_user_profile_data(account_id: int) -> dict:
    """
    Retrieves basic profile data for a given account ID.
    Return dict should be {'data1': data1, 'data2': data2, 'message': "Profile data retrieved successfully", 'status': 200}
    OR
    {'data': {'name': "John Doe", 'height': 180.0, 'age': 30, 'sex': 1}}
    whatevers easier, i dont really care, i am leaning more towards this^ one though

    Args:
        account_id (int): The ID of the account to update.

    Returns:
        dict: {'account_id': account_id, 'message': message, "status": status}
    """
    # Database operation to retrieve user profile data
    return {'data': {'name': "John Doe", 'height': 180.0, 'age': 30, 'sex': 1}, 'message': "Profile data retrieved successfully", 'status': 200}

def upload_profile_data(account_id: int, name: str = None, height: float = None, age: int = None, sex: int = None) -> dict:
    """
    Updates the profile with specified basic profile data for a given account ID.

    Args:
        account_id (int): The ID of the account to update.
        name (str): The new name of the user.
        height (float): The new height of the user in cm.
        age (int): The new age of the user.
        sex (int): The new sex of the user (0 for female, 1 for male).

    Returns:
        dict: A dictionary with the message and status code indicating success. Example: {'message': "Profile updated successfully", "status": 200}
    """
    # Database operation to update profile data
    return {'message': "Profile updated successfully", "status": 200}

def update_profile_data(account_id: int, name: str = None, height: float = None, age: int = None, sex: int = None) -> dict:
    """
    Updates individual or a few basic profile data for a given account ID.

    Args:
        account_id (int): The ID of the account to update.
        name (str, optional): The new name of the user.
        height (float, optional): The new height of the user in cm.
        age (int, optional): The new age of the user.
        sex (int, optional): The new sex of the user (0 for women, 1 for men).

    Returns:
        dict: {'message': "Account data updated successfully", "status": 200}
    """
    # Database operation to update specific account data fields
    return {'message': "Account data updated successfully", "status": 200}

def delete_account_data(account_id: int) -> dict:
    """
    Deletes basic profile data for a given account ID. This action is irreversible and should be used cautiously.

    Args:
        account_id (int): The ID of the account for which the basic profile data is to be deleted.

    Returns:
        dict: A dictionary with a message indicating the success of the operation and a status code. Example: {'message': "Account data deleted successfully", "status": 200}
    """
    # Database operation to delete account data
    return {'message': "Account data deleted successfully", "status": 200}




# PHASERESOURCES METHODS




def upload_phase_data(account_id: int, phase_type: str, start_date: str, target_weight: float, target_date: str) -> dict:
    """
    Creates a new phase entry in the database with the specified details.

    Args:
        account_id (int): The ID of the account to which the phase belongs.
        phase_type (str): The type of phase, e.g., "bulk" or "cut".
        start_date (str): The start date of the phase.
        target_weight (float): The target weight to achieve by the end of the phase.
        target_date (str): The target date by which the target weight should be achieved.

    Returns:
        dict: A dictionary containing a message indicating the success of the operation and a status code. Example: {'message': "Phase data uploaded successfully", "status": 201}
    """
    # Database operation to create a new phase entry
    return {'message': "Phase data uploaded successfully", "status": 201}

def get_phase_data(account_id: int, phase_id: int) -> dict:
    """
    Retrieves details of a specific phase entry from the database based on the given account ID and phase ID.

    Args:
        account_id (int): The ID of the account to which the phase belongs.
        phase_id (int): The ID of the phase to retrieve.

    Returns:
        dict: A dictionary containing the phase data (e.g., phase type, start date, target weight, target date) and a message indicating the success of the operation. Example: {'data': {'phase_type': "bulk", 'start_date': "2023-01-01", 'target_weight': 75.0, 'target_date': "2023-06-01"}, 'message': "Phase data retrieved successfully", 'status': 200}
    """
    # Database operation to retrieve phase data
    return {'data': {'phase_type': "bulk", 'start_date': "2023-01-01", 'target_weight': 75.0, 'target_date': "2023-06-01"}, 'message': "Phase data retrieved successfully", 'status': 200}

def edit_phase_data(account_id: int, phase_id: int, phase_type: str = None, start_date: str = None, target_weight: float = None, target_date: str = None) -> dict:
    """
    Updates phase entry data for a given phase ID and account ID.

    Args:
        account_id (int): The ID of the account.
        phase_id (int): The ID of the phase to update.
        phase_type (str, optional): The type of phase ("bulk" or "cut").
        start_date (str, optional): The start date of the phase.
        target_weight (float, optional): The target weight for the phase.
        target_date (str, optional): The target date to achieve the target weight.

    Returns:
        dict: {'message': "Phase data updated successfully", "status": 200}
    """
    # Database operation to update phase data
    return {'message': "Phase data updated successfully", "status": 200}

def delete_current_phase(account_id: int, phase_id: int) -> dict:
    """
    Deletes a specific phase entry from the database based on the provided account ID and phase ID.

    Args:
        account_id (int): The ID of the account from which the phase is to be deleted.
        phase_id (int): The ID of the phase to be deleted.

    Returns:
        dict: A dictionary with a message indicating the success of the deletion operation and a status code. Example: {'message': "Phase data deleted successfully", "status": 200}
    """
    # Database operation to delete phase data
    return {'message': "Phase data deleted successfully", "status": 200}




# DAILYENTRYRESOURCE METHODS



def create_daily_entry(account_id: int, phase_id: int, date: str, current_weight: float, active_calories_burned: int, resting_calories_burned: float, steps: int, hours_of_sleep: float, daily_calorie_intake: float, daily_protein_intake: int) -> dict:
    """
    Creates a new daily data entry in the database with the provided details.

    Args:
        account_id (int): The ID of the account to which the daily entry belongs.
        phase_id (int): The ID of the phase during which the entry is made.
        date (str): The date of the entry.
        current_weight (float): The current weight of the user.
        active_calories_burned (int): The number of active calories burned.
        resting_calories_burned (float): The number of resting calories burned.
        steps (int): The number of steps taken.
        hours_of_sleep (float): The hours of sleep.
        daily_calorie_intake (float): The daily calorie intake.
        daily_protein_intake (int): The daily protein intake.

    Returns:
        dict: A dictionary containing the entry ID of the new daily entry and a message indicating the success of the operation. Example: {'entry_id': entry_id, 'message': "Daily entry created successfully", "status": 201}
    """
    # Database operation to create a daily entry
    return {'entry_id': 0, 'message': "Daily entry created successfully", "status": 201}

def get_daily_entry(account_id: int, phase_id: int, entry_id: int) -> dict:
    """
    Retrieves details of a specific daily entry from the database based on the given account ID, phase ID, and entry ID.

    Args:
        account_id (int): The ID of the account to which the daily entry belongs.
        phase_id (int): The ID of the phase during which the entry was made.
        entry_id (int): The ID of the daily entry to retrieve.

    Returns:
        dict: A dictionary containing the details of the daily entry (e.g., current weight, steps) and a message indicating the success of the operation. Example: {'data': {'current_weight': 70.0, 'steps': 10000}, 'message': "Daily entry retrieved successfully", 'status': 200}
    """
    # Database operation to retrieve daily entry
    return {'data': {'current_weight': 70.0, 'steps': 10000}, 'message': "Daily entry retrieved successfully", 'status': 200}

def edit_daily_entry(account_id: int, phase_id: int, entry_id: int, current_weight: float = None, active_calories_burned: int = None, resting_calories_burned: float = None, steps: int = None, hours_of_sleep: float = None, daily_calorie_intake: float = None, daily_protein_intake: int = None) -> dict:
    """
    Updates a specific daily entry for a user.

    Args:
        account_id (int): The ID of the user's account.
        phase_id (int): The ID of the phase associated with the daily entry.
        entry_id (int): The ID of the daily entry to be updated.
        current_weight (float, optional): The user's current weight.
        active_calories_burned (int, optional): The number of active calories burned.
        resting_calories_burned (float, optional): The number of resting calories burned.
        steps (int, optional): The number of steps taken.
        hours_of_sleep (float, optional): The number of hours slept.
        daily_calorie_intake (float, optional): The total daily calorie intake.
        daily_protein_intake (int, optional): The total daily protein intake.

    Returns:
        dict: {'message': "Daily entry updated successfully", "status": 200}
    """
    # Database operation to update a daily entry
    return {'message': "Daily entry updated successfully", "status": 200}

def delete_daily_entry(account_id: int, phase_id: int, entry_id: int) -> dict:
    """
    Deletes a specific daily entry from the database based on the provided account ID, phase ID, and entry ID.

    Args:
        account_id (int): The ID of the account from which the daily entry is to be deleted.
        phase_id (int): The ID of the phase associated with the daily entry to be deleted.
        entry_id (int): The ID of the daily entry to be deleted.

    Returns:
        dict: A dictionary with a message indicating the success of the deletion operation and a status code. Example: {'message': "Daily entry deleted successfully", "status": 200}
    """
    # Database operation to delete a daily entry
    return {'message': "Daily entry deleted successfully", "status": 200}



# PROJECTIONRESOURCE METHODS



def create_projection(account_id: int, phase_id: int, entry_id: int, projection_mode: str, initial_weight: float, height: float, sex: int, weight_change_rate: float, active_calories_burned: int, resting_calories_burned: float, steps: int, hours_of_sleep: float, daily_calorie_intake: int, daily_protein_intake: int) -> dict:
    """
    Creates a new projection based on provided data and model calculation.
    
    Args:
        account_id (int): The user's account ID.
        phase_id (int): The phase ID the projection is associated with.
        entry_id (int): The daily entry ID the projection is based on.
        projection_mode (str): "weekly" or "monthly" projection mode.
        initial_weight (float): The user's initial weight.
        height (float): The user's height.
        sex (int): The user's sex, 0 for female and 1 for male.
        weight_change_rate (float): The rate of weight change.
        active_calories_burned (int): Active calories burned.
        resting_calories_burned (float): Resting calories burned.
        steps (int): Number of steps taken.
        hours_of_sleep (float): Hours of sleep.
        daily_calorie_intake (int): Daily calorie intake.
        daily_protein_intake (int): Daily protein intake.
    
    Returns:
        dict: Return dict should be {'projection_id': projection_id, 'message': "Projection created successfully", "status": 201}
    """
    # Placeholder for database operation to create a projection
    projection_id = 1  # Example placeholder value
    return {'projection_id': projection_id, 'message': "Projection created successfully", "status": 201}

def get_projection(account_id: int, phase_id: int, entry_id: int, projection_mode: str, projection_id: int) -> dict:
    """
    Reads projection data based on provided identifiers.
    
    Args:
        account_id (int): The user's account ID.
        phase_id (int): The phase ID the projection is associated with.
        entry_id (int): The daily entry ID the projection is based on.
        projection_mode (str): "weekly" or "monthly" projection mode.
        projection_id (int): The specific projection ID to retrieve.
    
    Returns:
        dict: Return dict should be {'data': projection_data, 'message': "Projection data retrieved successfully", 'status': 200}
    """
    # Placeholder for database operation to retrieve projection data
    projection_data = {}  # Example placeholder value
    return {'data': projection_data, 'message': "Projection data retrieved successfully", 'status': 200}

def delete_projection(account_id: int, phase_id: int, entry_id: int, projection_mode: str, projection_id: int) -> dict:
    """
    Deletes a specific projection data entry.
    
    Args:
        account_id (int): The user's account ID.
        phase_id (int): The phase ID associated with the projection.
        entry_id (int): The daily entry ID associated with the projection.
        projection_mode (str): "weekly" or "monthly" projection mode.
        projection_id (int): The specific projection ID to delete.
    
    Returns:
        dict: Return dict should be {'message': "Projection data deleted successfully", "status": 200}
    """
    # Placeholder for database operation to delete projection data
    return {'message': "Projection data deleted successfully", "status": 200}
