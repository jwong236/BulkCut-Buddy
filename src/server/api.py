from flask_restful import Api, Resource, reqparse, fields, marshal_with

resource_fields = {
    'accountID': fields.Integer(default=0),
    'name': fields.String(default=''),
    'height': fields.Float(default=0.0),
    'weight': fields.Float(default=0.0),
    'age': fields.Integer(default=0),
    'sex': fields.String(default=''),
    'message': fields.String,
}
# Account creation page --leads to--> Homepage with home tabs and a welcome message
# Hometabs: 1) Home 2) Workout 3) Input daily data 4) Weight projection Graph page
# Pages: 1) Account creation page 2) Homepage 3) Workout 3) Input daily data page 4) Projections page



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
        
        user_data = get_account_data() # TODO
        return user_data
    
class WeightModelResource(Resource):
    def get(self):
        """
        Send model predictions to frontend
        """
    
def initialize_api(app):
    """
    Initialize 
    """
    api = Api(app)
    api.add_resource(ProfileResource, '/api/profile')
    api.add_resource(WeightModelResource, '/api/weightmodel')