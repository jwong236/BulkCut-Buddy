from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask import current_app
import pandas as pd
resource_fields = {
    'accountID': fields.Integer(default=0),
    'name': fields.String(default=''),
    'height': fields.Float(default=0.0),
    'weight': fields.Float(default=0.0),
    'age': fields.Integer(default=0),
    'sex': fields.String(default=''),
    'message': fields.String,
}

# Note: frontend sends data to backend in the form of a "request" object
# The request object's data can be parsed with RequestParser() and the contents will be stored in args
# Ex: args['username'] = jacobw, args['password'] = ewoigjaie
class ProfileResource(Resource):
    def post(self):
        """
        Receive account data from frontend to create new account
        """
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True, help="Username cannot be blank.")
        parser.add_argument('password', required=True, help="Password cannot be blank.")
        args = parser.parse_args()
        
        # Check if the username already exists
        # Hash password using bcrypt or werkzeug.security
        # Create a new Account instance with the provided username and password hash and a generated accountID
        # Commit the new account to the database
        # Return the account ID of the newly created account
        create_account() # TODO

        return {'accountID': new_account.accountID, 'message': "Account created successfully"}, 201

    
    def put(self, accountID):
        """
        Receive account data from frontend to update account
        """
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('height', type=int)
        parser.add_argument('weight', type=float)
        parser.add_argument('age', type=int)
        parser.add_argument('sex', type=str)
        args = parser.parse_args()
        
        update_account_data() # TODO
        # Load data into database with accountID

        return {'message': "Account updated successfully"}, 200

    @marshal_with(resource_fields)
    def get(self, accountID):
        """
        Send account data to frontend
        """
        user_data = get_user_profile_data() # TODO
        return user_data
    
class WeightModelResource(Resource):
        
    def post(self, current_weight, active_calories_burned, resting_calories_burned, steps, hours_of_sleep, daily_calorie_intake, daily_protein_intake, mode):
        user_body_data = get_user_body_data()
        features = {'initial_weight': current_weight, 'height': user_body_data['height'], 'sex': user_body_data['sex'], 'weight_change_rate': user_body_data['weight_change_rate'],
            'active_calories_burned': active_calories_burned, 'resting_calories_burned' : resting_calories_burned, 'steps': steps, 'hours_of_sleep': hours_of_sleep,
            'daily_calorie_intake': daily_calorie_intake, 'daily_protein_intake': daily_protein_intake}
        if(mode == "weekly"):
            model = current_app.config['WEEKLY_MODEL']
            features['week_count'] = get_week_count()
        elif(mode == "monthly"):
            model = current_app.config['MONTHLY_MODEL']
            features['month_count'] = get_month_count()
        else:
            return None
        pd.DataFrame(features)

        
        return model.predict(features)
    
def initialize_api(app):
    """
    Initialize 
    """
    api = Api(app)
    api.add_resource(ProfileResource, '/api/profile')
    api.add_resource(WeightModelResource, '/api/weightmodel')