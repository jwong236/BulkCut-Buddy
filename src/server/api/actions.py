from utils import validate_password, encrypt_password
from flask import current_app

# PROFILERESOURCE METHODS

def create_profile(username: str, password: str) -> dict:
    """
    Creates an account entry in database using arguments, returns accountID of new account

    Args:
        username (str): The username of the new user.
        password (str): The password for the new user (not pre-hashed).

    Returns:
        dict: {'account_id': account_id, 'message': message, "status": status}
    """
    # Implement password validation
    if not validate_password(password):
        return {'message': 'Invalid password', 'status': 1}

    # Encrypt password using a secure algorithm
    password_hash = encrypt_password(password)
    

    data = [(username, password_hash)]
    query = """
        INSERT INTO profile (username, password_hash)
        VALUES (%s, %s);
    """

    try:
        response = current_app.db.execute_query(query, data)
        if response['status'] == 0:
            account_id = current_app.db.get_account_id(username)
            response['account_id'] = account_id
    except Exception as e:
        print(f"Error creating profile: {str(e)}")
        response = {'message': 'Failed to create profile', 'status': 1}

    return response

def get_profile(account_id: int) -> dict:
    """
    Retrieves basic profile data for a given account ID.

    Args:
        account_id (int): The ID of the account.

    Returns:
        dict: Profile data and status message.
    """
    query = """
        SELECT name, username, password_hash, height, age, sex
        FROM profile
        WHERE account_id = %s;
    """
    data = (account_id,)

    try:
        response = current_app.db.execute_query(query, data, fetch_one=True)
        if response['data']:
            profile_data = response['data']
            return {
                'data': {
                    'name': profile_data[0],
                    'username': profile_data[1],
                    'password_hash': profile_data[2],
                    'height': profile_data[3],
                    'age': profile_data[4],
                    'sex': profile_data[5]
                },
                'message': "Profile data retrieved successfully",
                'status': 200
            }
        else:
            return {'message': 'Profile not found', 'status': 404}
    except Exception as e:
        print(f"Error retrieving profile: {str(e)}")
        return {'message': 'Failed to retrieve profile', 'status': 500}

def upload_profile(account_id: int, name: str = None, height: float = None, age: int = None, sex: int = None) -> dict:
    """
    Finds the profile with the given account_id and updates it with the supplied data.

    Args:
        account_id (int): The ID of the account to update.
        name (str, optional): The new name of the user.
        height (float, optional): The new height of the user in cm.
        age (int, optional): The new age of the user.
        sex (int, optional): The new sex of the user (0 for female, 1 for male).

    Returns:
        dict: {'message': message, "status": status}
    """
    query_parts = []
    data = []

    if name is not None:
        query_parts.append("name = %s")
        data.append(name)
    if height is not None:
        query_parts.append("height = %s")
        data.append(height)
    if age is not None:
        query_parts.append("age = %s")
        data.append(age)
    if sex is not None:
        query_parts.append("sex = %s")
        data.append(sex)

    if not query_parts:
        return {'message': "No data provided to update", "status": 400}

    query = "UPDATE profile SET " + ", ".join(query_parts) + " WHERE account_id = %s;"
    data.append(account_id)

    try:
        response = current_app.db.execute_query(query, tuple(data))
        # Assuming the execute_query method returns a response with a status key
        if response['status'] == 0:  # Assuming 0 signifies success
            return {'message': "Profile updated successfully", "status": 200}
        else:
            return {'message': "Failed to update profile", "status": response['status']}
    except Exception as e:
        print(f"Error updating profile: {str(e)}")
        return {'message': 'Failed to update profile', 'status': 500}


def update_profile(account_id: int, username: str, password_hash: str, name: str = None, 
                   height: float = None, age: int = None, sex: int = None) -> dict:
    """
    Updates one or more basic profile data for a given account ID.

    Args:
        account_id (int): The ID of the account to update.
        username (str): The new username of the profile.
        password_hash (str): The new hashed password.
        name (str, optional): The new name of the user.
        height (float, optional): The new height of the user in cm.
        age (int, optional): The new age of the user.
        sex (int, optional): The new sex of the user (0 for women, 1 for men).

    Returns:
        dict: {'message': message, "status": status}
    """
    query_parts = ["username = %s", "password_hash = %s"]
    data = [username, password_hash]

    if name is not None:
        query_parts.append("name = %s")
        data.append(name)
    if height is not None:
        query_parts.append("height = %s")
        data.append(height)
    if age is not None:
        query_parts.append("age = %s")
        data.append(age)
    if sex is not None:
        query_parts.append("sex = %s")
        data.append(sex)

    query = "UPDATE profile SET " + ", ".join(query_parts) + " WHERE account_id = %s;"
    data.append(account_id)

    try:
        current_app.db.execute_query(query, tuple(data))
        return {'message': "Account data updated successfully", "status": 200}
    except Exception as e:
        return {'message': f"Failed to update profile: {e}", "status": 500}


def delete_profile(account_id: int) -> dict:
    """
    Deletes basic profile data for a given account ID.

    Args:
        account_id (int): The ID of the account for which the basic profile data is to be deleted.

    Returns:
        dict: {'message': message, "status": status}
    """
    query = "DELETE FROM profile WHERE account_id = %s;"

    try:
        current_app.db.execute_query(query, (account_id,))
        return {'message': "Account data deleted successfully", "status": 200}
    except Exception as e:
        return {'message': f"Failed to delete profile: {e}", "status": 500}





# PHASERESOURCES METHODS




def create_phase(account_id: int, phase_type: int, start_date: str, target_weight: float, target_date: str) -> dict:
    """
    Creates a new phase entry in the database with phase details.

    Args:
        account_id (int): The ID of the account to which the phase belongs.
        phase_type (int): The type of phase. 0 for bulk, 1 for cut.
        start_date (str): The start date of the phase.
        target_weight (float): The target weight to achieve by the end of the phase.
        target_date (str): The target date by which the target weight should be achieved.

    Returns:
        dict: {'message': message, "status": status}
    """
    return {'message': "Phase data uploaded successfully", "status": 201}

def get_phase(account_id: int, phase_id: int) -> dict:
    """
    Retrieves details of a specific phase entry from the database based on the given account ID and phase ID.

    Args:
        account_id (int): The ID of the account to which the phase belongs.
        phase_id (int): The ID of the phase to retrieve.

    Returns:
        dict: A dictionary containing the phase data (e.g., phase type, start date, target weight, target date)
         and a message indicating the success of the operation. 
         Example: {'data': {'phase_type': 0, 'start_date': "2023-01-01", 'target_weight': 75.0, 'target_date': "2023-06-01"},
         'message': "Phase data retrieved successfully", 'status': 200}
    """
    return {'data': {'phase_type': 0, 'start_date': "2023-01-01", 'target_weight': 75.0, 'target_date': "2023-06-01"}, 'message': "Phase data retrieved successfully", 'status': 200}

def update_phase(account_id: int, phase_id: int, phase_type: int = None, start_date: str = None, 
                      target_weight: float = None, target_date: str = None) -> dict:
    """
    Updates phase entry data for a given phase ID and account ID.

    Args: 
        account_id (int): The ID of the account.
        phase_id (int): The ID of the phase to update.
        phase_type (int, optional): The type of phase ("bulk" or "cut").
        start_date (str, optional): The start date of the phase.
        target_weight (float, optional): The target weight for the phase.
        target_date (str, optional): The target date to achieve the target weight.

    Returns:
        dict: {'message': "Phase data updated successfully", "status": 200}
    """
    return {'message': "Phase data updated successfully", "status": 200}

def delete_phase(account_id: int, phase_id: int) -> dict:
    """
    Deletes a specific phase entry from the database based on the provided account ID and phase ID.

    Args:
        account_id (int): The ID of the account from which the phase is to be deleted.
        phase_id (int): The ID of the phase to be deleted.

    Returns:
        dict: {'message': message, "status": status}
    """
    return {'message': "Phase data deleted successfully", "status": 200}




# DAILYENTRYRESOURCE METHODS



def create_daily_entry(account_id: int, phase_id: int, date: str, current_weight: float, 
                       active_calories_burned: int, resting_calories_burned: float, steps: int, 
                       hours_of_sleep: float, daily_calorie_intake: float, daily_protein_intake: int) -> dict:
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
        dict: {'message': message, "status": status}
    """
    return {'entry_id': 0, 'message': "Daily entry created successfully", "status": 201}

def get_daily_entry(account_id: int, phase_id: int, entry_id: int) -> dict:
    """
    Retrieves details of a specific daily entry from the database based on the given account ID, phase ID, and entry ID.

    Args:
        account_id (int): The ID of the account to which the daily entry belongs.
        phase_id (int): The ID of the phase during which the entry was made.
        entry_id (int): The ID of the daily entry to retrieve.

    Returns:
        dict: A dictionary containing the details of the daily entry (e.g., current weight, steps) 
        and a message indicating the success of the operation. Example: {'data': {'current_weight': 70.0, 'steps': 10000}, 'message': "Daily entry retrieved successfully", 'status': 200}
    """
    return {'data': {'current_weight': 70.0, 'steps': 10000}, 'message': "Daily entry retrieved successfully", 'status': 200}

def update_daily_entry(account_id: int, phase_id: int, entry_id: int, current_weight: float = None, 
                       active_calories_burned: int = None, resting_calories_burned: float = None, steps: int = None, 
                       hours_of_sleep: float = None, daily_calorie_intake: float = None, daily_protein_intake: int = None) -> dict:
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
        dict: {'message': message, "status": status}
    """
    return {'message': "Daily entry updated successfully", "status": 200}

def delete_daily_entry(account_id: int, phase_id: int, entry_id: int) -> dict:
    """
    Deletes a specific daily entry from the database based on the provided account ID, phase ID, and entry ID.

    Args:
        account_id (int): The ID of the account from which the daily entry is to be deleted.
        phase_id (int): The ID of the phase associated with the daily entry to be deleted.
        entry_id (int): The ID of the daily entry to be deleted.

    Returns:
        dict: {'message': message, "status": status}
    """
    return {'message': "Daily entry deleted successfully", "status": 200}



# PROJECTIONRESOURCE METHODS



def create_projection(account_id: int, phase_id: int, entry_id: int, projection_mode: str, initial_weight: float,
                      height: float, sex: int, weight_change_rate: float, active_calories_burned: int, resting_calories_burned: float, 
                      steps: int, hours_of_sleep: float, daily_calorie_intake: int, daily_protein_intake: int) -> dict:
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
        dict: {'message': message, "status": status}
    """
    projection_id = 1
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
        just do it in same way you implemented the other get functions
    """
    projection_data = {}
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
        dict: {'message': message, "status": status}
    """
    # Placeholder for database operation to delete projection data
    return {'message': "Projection data deleted successfully", "status": 200}
