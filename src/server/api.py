from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask import current_app
import pandas as pd
from utils import *
from utils.db_utils import *


"""TODO: Implement marshal_with decorators to ensure consistent data passing
@marshal_with(resource_fields)
resource_fields = {
    'accountID': fields.Integer(default=0),
    'name': fields.String(default=''),
    'height': fields.Float(default=0.0),
    'weight': fields.Float(default=0.0),
    'age': fields.Integer(default=0),
    'sex': fields.String(default=''),
    'message': fields.String,
}"""

def initialize_api(app):
    """
    Initialize 
    """
    api = Api(app)
    api.add_resource(ProfileResource, '/api/profile')
    api.add_resource(DailyEntryResource, '/api/dailyentry')


# Note: frontend sends data to backend in the form of a "request" object
# The request object's data can be parsed with RequestParser() and the contents will be stored in args
# Ex: args['username'] = jacobw, args['password'] = ewoigjaie
class ProfileResource(Resource):
    def post(self):
        """
        Receive account data from frontend to create new account
        1. Validates if password meets requirements
        2. Validates if username already exists
        3. Encrypts password
        4. Uploads encrypted password to database
        Returns accountID of new account
        """
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True, help="Username cannot be blank.")
        parser.add_argument('password', required=True, help="Password cannot be blank.")
        args = parser.parse_args()

        if not validate_password(args['password']):
            return {'message': "Password does not meet requirements", "status": 400}
        if not validate_new_account(args['username']):
            return {'message': "Account with that username already exists", "status": 409}
        
        encrypted_password = encrypt_password(args['password'])
        new_accountID = upload_new_account(args['username'], encrypted_password)
        return {'accountID': new_accountID, 'message': "Account created successfully", "status": 201}
    
    def put(self):
        """
        Updates basic profile data
        """
        parser = reqparse.RequestParser()
        parser.add_argument('accountID', type=int, required=True)
        parser.add_argument('name', type=str)
        parser.add_argument('height', type=int)
        parser.add_argument('age', type=int)
        parser.add_argument('sex', type=str)
        args = parser.parse_args()

        return update_account_data(**args)

    def get(self):
        """
        Returns account data
        """
        parser = reqparse.RequestParser()
        parser.add_argument('accountID', type=int, required=True)
        args = parser.parse_args()
        return get_user_profile_data(args['accountID'])

class PhaseResources(Resource):
    def post(self):
        """
        Uploads phase data
        """
        parser = reqparse.RequestParser()
        parser.add_argument('phase_type')
        parser.add_argument('start_date')
        parser.add_argument('target_weight')
        parser.add_argument('target_date')
        args = parser.parse_args()

        return upload_phase_data(**args)

    def patch(self):
        """
        Edits phase data
        """
        parser = reqparse.RequestParser()
        parser.add_argument('phase_id', required=True, help="Phase ID is required")  # Assuming an identifier is needed to find the phase
        parser.add_argument('phase_type', store_missing=False)
        parser.add_argument('start_date', store_missing=False)
        parser.add_argument('target_weight', store_missing=False)
        parser.add_argument('target_date', store_missing=False)
        args = parser.parse_args()

        # Assuming edit_phase_data function exists and handles the logic to update the phase data
        return edit_phase_data(**args)

    def delete(self):
        """
        Deletes current phase data
        """
        return delete_current_phase()

    def get(self):
        """
        Returns account data
        """
        parser = reqparse.RequestParser()
        parser.add_argument('accountID', type=int, required=True)
        args = parser.parse_args()
        return get_phase_data(args['accountID'])

class DailyEntryResource(Resource):
    def post(self):
        """
        Uploads daily data entry
        """
        parser = reqparse.RequestParser()
        parser.add_argument('accountID', type=int, required=True)
        parser.add_argument('date', type=str, required=True)
        parser.add_argument('current_weight', type=str)
        parser.add_argument('active_calories_burned', type=int)
        parser.add_argument('resting_calories_burned', type=float)
        parser.add_argument('steps', type=int)
        parser.add_argument('hours_of_sleep', type=str)
        parser.add_argument('daily_calorie_intake', type=float)
        parser.add_argument('daily_protein_intake', type=int)
        args = parser.parse_args()
        
        return upload_daily_entry(**args)
    
    def patch(self):
        """
        Edits a daily entry
        """
        parser = reqparse.RequestParser()
        parser.add_argument('accountID', type=int, required=True)
        parser.add_argument('date', type=str, required=True)

        parser.add_argument('current_weight', type=str, store_missing=False)
        parser.add_argument('active_calories_burned', type=int, store_missing=False)
        parser.add_argument('resting_calories_burned', type=float, store_missing=False)
        parser.add_argument('steps', type=int, store_missing=False)
        parser.add_argument('hours_of_sleep', type=str, store_missing=False)
        parser.add_argument('daily_calorie_intake', type=float, store_missing=False)
        parser.add_argument('daily_protein_intake', type=int, store_missing=False)
        
        args = parser.parse_args()
        return edit_daily_entry(**args)
    
class WeightModelResource(Resource):
    def get(self):
        """

        """