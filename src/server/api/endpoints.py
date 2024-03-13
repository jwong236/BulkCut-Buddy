from flask_restful import Api, Resource, reqparse, fields, marshal_with
from utils import *
from api.actions import *


#   RESOURCE FIELDS

standard_resource_fields = {
    'message': fields.String,
    'status': fields.Integer
}

post_response_resource_fields = {
    'id': fields.Integer,
    'message': fields.String,
    'status': fields.Integer
}

basic_resource_fields = {
    'username': fields.String,
    'password_hash': fields.String,
    'name': fields.String,
    'height': fields.Float,
    'age': fields.Integer,
    'sex': fields.Integer,
    'message': fields.String,
    'status': fields.Integer
}

phase_resource_fields = {
    'phase_type': fields.Integer,
    'start_date': fields.String, 
    'target_weight': fields.Float,
    'target_date': fields.String,
    'message': fields.String,
    'status': fields.Integer
}

daily_entry_resource_fields = {
    'current_weight': fields.Float,
    'active_calories_burned': fields.Integer,
    'resting_calories_burned': fields.Float,
    'steps': fields.Integer,
    'hours_of_sleep': fields.Float,
    'daily_calorie_intake': fields.Float,
    'daily_protein_intake': fields.Integer,
    'message': fields.String,
    'status': fields.Integer
}

projection_resource_fields = {
    'projection_mode': fields.Integer,
    'initial_weight': fields.Float,
    'height': fields.Float,
    'sex': fields.Integer,
    'weight_change_rate': fields.Float,
    'active_calories_burned': fields.Integer,
    'resting_calories_burned': fields.Float,
    'steps': fields.Integer,
    'hours_of_sleep': fields.Float,
    'daily_calorie_intake': fields.Integer,
    'daily_protein_intake': fields.Integer,
    'message': fields.String,
    'status': fields.Integer
}

#  INITIALIZATION METHOD

def initialize_api(app):
    """
    Initialize API and add resources to it
    """
    api = Api(app)
    api.add_resource(ProfileResource, '/api/profile')
    api.add_resource(DailyEntryResource, '/api/dailyentry')
    api.add_resource(PhaseResources, '/api/phase')
    api.add_resource(ProjectionResource, '/api/projection')
    print("Initialize success")

#  RESOURCE CLASSES

class ProfileResource(Resource):
    @marshal_with(post_response_resource_fields)
    def post(self):
        """
        CREATES new profile entry
        """
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help="Username cannot be blank.")
        parser.add_argument('password_hash', type=str, required=True, help="Password cannot be blank.")
        args = parser.parse_args()
        return create_profile(**args)
    
    @marshal_with(basic_resource_fields)
    def get(self):
        """
        READS basic profile data
        """
        parser = reqparse.RequestParser()
        parser.add_argument('account_id', type=int, required=True, help="Account ID cannot be blank.")
        args = parser.parse_args()
        return get_profile(**args)

    @marshal_with(standard_resource_fields)
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
        return upload_profile(**args)

    @marshal_with(standard_resource_fields)
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
        return update_profile(**args)
    
    @marshal_with(standard_resource_fields)
    def delete(self):
        """
        DELETES basic profile data
        """
        parser = reqparse.RequestParser()
        parser.add_argument('account_id', type=int, required=True, help="Account ID cannot be blank.")
        args = parser.parse_args()
        return delete_profile(**args)

class PhaseResources(Resource):
    @marshal_with(post_response_resource_fields)
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
        return create_phase(**args)
    
    @marshal_with(phase_resource_fields)
    def get(self):
        """
        READS phase entry in database
        """
        parser = reqparse.RequestParser()
        parser.add_argument('account_id', type=int, required=True, help="Account ID cannot be blank.")
        parser.add_argument('phase_id', type=int, required=True, help="Phase ID cannot be blank.")
        args = parser.parse_args()
        return get_phase(**args)

    @marshal_with(standard_resource_fields)
    def patch(self):
        """
        UPDATES phase entry data
        """
        parser = reqparse.RequestParser()
        parser.add_argument('account_id', type=int, required=True, help="Account ID cannot be blank.")
        parser.add_argument('phase_id', type=int, required=True, help="Phase ID cannot be blank.")
        parser.add_argument('phase_type', type=int, choices=[0, 1], help="Projection mode must be 0 for bulk or 1 for cut.")
        parser.add_argument('start_date', store_missing=False)
        parser.add_argument('target_weight', store_missing=False)
        parser.add_argument('target_date', store_missing=False)
        args = parser.parse_args()
        return update_phase(**args)

    @marshal_with(standard_resource_fields)
    def delete(self):
        """
        DELETES phase entry data
        """
        parser = reqparse.RequestParser()
        parser.add_argument('account_id', type=int, required=True, help="Account ID cannot be blank.")
        parser.add_argument('phase_id', type=int, required=True, help="Phase ID cannot be blank.")
        args = parser.parse_args()
        return delete_phase(**args)



class DailyEntryResource(Resource):
    @marshal_with(post_response_resource_fields)
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
    
    @marshal_with(daily_entry_resource_fields)
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

    @marshal_with(standard_resource_fields)
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
    
    @marshal_with(standard_resource_fields)
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
    @marshal_with(post_response_resource_fields)
    def post(self):
        """
        CREATES new projection based on provided data and model calculation.
        """
        parser = reqparse.RequestParser()
        parser.add_argument('account_id', type=int, required=True, help="Account ID cannot be blank.")
        parser.add_argument('phase_id', type=int, required=True, help="Phase ID cannot be blank.")
        parser.add_argument('entry_id', type=int, required=True, help="Entry ID cannot be blank.")
        parser.add_argument('projection_mode', type=int, required=True, choices=[0, 1], help="Projection mode must be 0 for weekly or 1 for monthly.")
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

    @marshal_with(projection_resource_fields)
    def get(self):
        """
        READS projection data
        """
        parser = reqparse.RequestParser()
        parser.add_argument('account_id', type=int, required=True, help="Account ID cannot be blank.")
        parser.add_argument('phase_id', type=int, required=True, help="Phase ID cannot be blank.")
        parser.add_argument('entry_id', type=int, required=True, help="Entry ID cannot be blank.")
        parser.add_argument('projection_mode', type=int, required=True, choices=[0, 1], help="Projection mode must be 0 for weekly or 1 for monthly.")
        parser.add_argument('projection_id', type=int, required=True, help="Projection ID cannot be blank.")
        args = parser.parse_args()
        return get_projection(**args)
    
    @marshal_with(standard_resource_fields)
    def delete(self):
        """
        DELETES projection data
        """
        parser = reqparse.RequestParser()
        parser.add_argument('account_id', type=int, required=True, help="Account ID cannot be blank.")
        parser.add_argument('phase_id', type=int, required=True, help="Phase ID cannot be blank.")
        parser.add_argument('entry_id', type=int, required=True, help="Entry ID cannot be blank.")
        parser.add_argument('projection_mode', type=int, required=True, choices=[0, 1], help="Projection mode must be 0 for weekly or 1 for monthly.")
        parser.add_argument('projection_id', type=int, required=True, help="Projection ID cannot be blank.")
        args = parser.parse_args()
        return delete_projection(**args)