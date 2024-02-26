from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask import current_app
from utils import *
from server.api.actions import *


"""TODO: Implement marshal_with decorators to ensure consistent data passing
@marshal_with(resource_fields)
resource_fields = {
    'account_id': fields.Integer(default=0),
    'name': fields.String(default=''),
    'height': fields.Float(default=0.0),
    'weight': fields.Float(default=0.0),
    'age': fields.Integer(default=0),
    'sex': fields.String(default=''),
    'message': fields.String,
}"""

resource_fields = {
    'message': fields.String,
    'status': fields.Integer
}

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
        CREATES new profile entry
        """
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help="Username cannot be blank.")
        parser.add_argument('password_hash', type=str, required=True, help="Password cannot be blank.")
        args = parser.parse_args()
        return create_new_profile(**args)
    
    def get(self):
        """
        READS basic profile data
        """
        parser = reqparse.RequestParser()
        parser.add_argument('account_id', type=int, required=True, help="Account ID cannot be blank.")
        args = parser.parse_args()
        return get_user_profile_data(**args )

    def put(self):
        """
        UPDATES profile with all basic profile data
        """
        parser = reqparse.RequestParser()
        parser.add_argument('account_id', type=int, required=True, help="Account ID cannot be blank.")
        parser.add_argument('name', type=str)
        parser.add_argument('height', type=float)
        parser.add_argument('age', type=int)
        parser.add_argument('sex', type=int, choices=[0, 1], help="Projection mode must be 0 for women or 1 for man.")
        args = parser.parse_args()
        return upload_profile_data(**args)

    def patch(self):
        """
        UPDATES individual/few basic profile data
        """
        parser = reqparse.RequestParser()
        parser.add_argument('account_id', type=int, required=True, help="Account ID cannot be blank.")
        parser.add_argument('username' , type=str, store_missing=False)
        parser.add_argument('password_hash' , type=str, store_missing=False)
        parser.add_argument('name', type=str, store_missing=False)
        parser.add_argument('height', type=float, store_missing=False)
        parser.add_argument('age', type=int, store_missing=False)
        parser.add_argument('sex', type=int, choices=[0, 1], store_missing=False, help="Projection mode must be 0 for women or 1 for man.")
        args = parser.parse_args()
        return update_profile_data(**args)
    
    def delete(self):
        """
        DELETES basic profile data
        """
        parser = reqparse.RequestParser()
        parser.add_argument('account_id', type=int, required=True, help="Account ID cannot be blank.")
        args = parser.parse_args()
        return delete_account_data(**args)

class PhaseResources(Resource):
    def post(self):
        """
        CREATES phase entry in database
        """
        parser = reqparse.RequestParser()
        parser.add_argument('account_id', type=int, required=True, help="Account ID cannot be blank.")
        parser.add_argument('phase_type', type=int, required=True, choices=[0, 1], help="Projection mode must be 0 for bulk or 1 for cut.")
        parser.add_argument('start_date')
        parser.add_argument('target_weight')
        parser.add_argument('target_date')
        args = parser.parse_args()
        return upload_phase_data(**args)
    
    def get(self):
        """
        READS phase entry in database
        """
        parser = reqparse.RequestParser()
        parser.add_argument('account_id', type=int, required=True, help="Account ID cannot be blank.")
        parser.add_argument('phase_id', type=int, required=True, help="Phase ID cannot be blank.")
        args = parser.parse_args()
        return get_phase_data(**args)

    def patch(self):
        """
        UPDATES phase entry data
        """
        parser = reqparse.RequestParser()
        parser.add_argument('account_id', type=int, required=True, help="Account ID cannot be blank.")
        parser.add_argument('phase_id', type=int, required=True, help="Phase ID cannot be blank.")
        parser.add_argument('phase_type', type=int, required=True, choices=[0, 1], help="Projection mode must be 0 for bulk or 1 for cut.")
        parser.add_argument('start_date', store_missing=False)
        parser.add_argument('target_weight', store_missing=False)
        parser.add_argument('target_date', store_missing=False)
        args = parser.parse_args()
        return update_phase_data(**args)

    def delete(self):
        """
        DELETES phase entry data
        """
        parser = reqparse.RequestParser()
        parser.add_argument('account_id', type=int, required=True, help="Account ID cannot be blank.")
        parser.add_argument('phase_id', type=int, required=True, help="Phase ID cannot be blank.")
        args = parser.parse_args()
        return delete_current_phase(**args)



class DailyEntryResource(Resource):
    def post(self):
        """
        CREATES daily data entry
        """
        parser = reqparse.RequestParser()
        parser.add_argument('account_id', type=int, required=True, help="Account ID cannot be blank.")
        parser.add_argument('phase_id', type=int, required=True, help="Phase ID cannot be blank.")
        parser.add_argument('current_weight', type=float)
        parser.add_argument('active_calories_burned', type=int)
        parser.add_argument('resting_calories_burned', type=float)
        parser.add_argument('steps', type=int)
        parser.add_argument('hours_of_sleep', type=float)
        parser.add_argument('daily_calorie_intake', type=float)
        parser.add_argument('daily_protein_intake', type=int)
        args = parser.parse_args()
        return create_daily_entry(**args)
    
    def get(self):
        """
        READS daily data entry
        """
        parser = reqparse.RequestParser()
        parser.add_argument('account_id', type=int, required=True, help="Account ID cannot be blank.")
        parser.add_argument('phase_id', type=int, required=True, help="Phase ID cannot be blank.")
        parser.add_argument('entry_id', type=int, required=True, help="Entry ID cannot be blank.")
        args = parser.parse_args()
        return get_daily_entry(**args)

    def patch(self):
        """
        UPDATES a daily entry
        """
        parser = reqparse.RequestParser()
        parser.add_argument('account_id', type=int, required=True, help="Account ID cannot be blank.")
        parser.add_argument('phase_id', type=int, required=True, help="Phase ID cannot be blank.")
        parser.add_argument('entry_id', type=int, required=True, help="Entry ID cannot be blank.")
        parser.add_argument('current_weight', type=float, store_missing=False)
        parser.add_argument('active_calories_burned', type=int, store_missing=False)
        parser.add_argument('resting_calories_burned', type=float, store_missing=False)
        parser.add_argument('steps', type=int, store_missing=False)
        parser.add_argument('hours_of_sleep', type=float, store_missing=False)
        parser.add_argument('daily_calorie_intake', type=float, store_missing=False)
        parser.add_argument('daily_protein_intake', type=int, store_missing=False)
        args = parser.parse_args()
        return update_daily_entry(**args)
    
    def delete(self):
        """
        DELETES a daily entry
        """
        parser = reqparse.RequestParser()
        parser.add_argument('account_id', type=int, required=True, help="Account ID cannot be blank.")
        parser.add_argument('phase_id', type=int, required=True, help="Phase ID cannot be blank.")
        parser.add_argument('entry_id', type=int, required=True, help="Entry ID cannot be blank.")
        args = parser.parse_args()
        return delete_daily_entry(**args)
    
class ProjectionResource(Resource):
    def post(self):
        """
        CREATES new projection based on provided data and model calculation.
        """
        parser = reqparse.RequestParser()
        parser.add_argument('account_id', type=int, required=True, help="Account ID cannot be blank.")
        parser.add_argument('phase_id', type=int, required=True, help="Phase ID cannot be blank.")
        parser.add_argument('entry_id', type=int, required=True, help="Entry ID cannot be blank.")
        parser.add_argument('projection_mode', type=str, required=True, choices=["weekly", "monthly"], help="Projection mode must be 'weekly' or 'monthly'.")
        parser.add_argument('initial_weight', type=float, required=True)
        parser.add_argument('height', type=float, required=True)
        parser.add_argument('sex', type=int, choices=[0, 1], required=True, help="Projection mode must be 0 for women or 1 for man.")
        parser.add_argument('weight_change_rate', type=float, required=True)
        parser.add_argument('active_calories_burned', type=int, required=True)
        parser.add_argument('resting_calories_burned', type=float, required=True)
        parser.add_argument('steps', type=int, required=True)
        parser.add_argument('hours_of_sleep', type=float, required=True)
        parser.add_argument('daily_calorie_intake', type=int, required=True)
        parser.add_argument('daily_protein_intake', type=int, required=True)
        args = parser.parse_args()
        return create_projection(**args)

    def get(self):
        """
        READS projection data
        """
        parser = reqparse.RequestParser()
        parser.add_argument('account_id', type=int, required=True, help="Account ID cannot be blank.")
        parser.add_argument('phase_id', type=int, required=True, help="Phase ID cannot be blank.")
        parser.add_argument('entry_id', type=int, required=True, help="Entry ID cannot be blank.")
        parser.add_argument('projection_mode', type=str, required=True, choices=["weekly", "monthly"], help="Projection mode must be 'weekly' or 'monthly'.")
        parser.add_argument('projection_id', type=int, required=True, help="Projection ID cannot be blank.")
        args = parser.parse_args()
        return get_projection(**args)
    
    def delete(self):
        """
        DELETES projection data
        """
        parser = reqparse.RequestParser()
        parser.add_argument('account_id', type=int, required=True, help="Account ID cannot be blank.")
        parser.add_argument('phase_id', type=int, required=True, help="Phase ID cannot be blank.")
        parser.add_argument('entry_id', type=int, required=True, help="Entry ID cannot be blank.")
        parser.add_argument('projection_mode', type=str, required=True, choices=["weekly", "monthly"], help="Projection mode must be 'weekly' or 'monthly'.")
        parser.add_argument('projection_id', type=int, required=True, help="Projection ID cannot be blank.")
        args = parser.parse_args()
        return delete_projection(**args)