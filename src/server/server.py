from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, marshal_with

app = Flask(__name__)
api = Api(app)

resource_fields = {
    'accountID': fields.Integer(default=0),
    'name': fields.String(default=''),
    'height': fields.Float(default=0.0),
    'weight': fields.Float(default=0.0),
    'age': fields.Integer(default=0),
    'sex': fields.String(default=''),
    'message': fields.String,
}

class Home(Resource):
    def get(self):
        return {"message": "BulkCut Buddy Homepage"}

class Profile(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True, help="Username cannot be blank.")
        parser.add_argument('password', required=True, help="Password cannot be blank.")  # Note: Ensure secure handling
        args = parser.parse_args()
        
        #accountID = create_account(args['username'], args['password'])  # Create account in database
        accountID = 123
        return {'accountID': accountID, 'message': "Account created successfully"}, 200
    
    def put(self, accountID):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type = str)
        parser.add_argument('height', type=int)
        parser.add_argument('weight', type=float)
        parser.add_argument('age', type=int)
        parser.add_argument('sex', type=str)
        args = parser.parse_args()
        
        # Logic for updating account with new information
        return {'message': "Account updated successfully"}, 200

    @marshal_with(resource_fields)
    def get(self, accountID):
        # Get data from DB, here is some dummy data
        user_data = {
            'accountID': accountID,
            'height': 180.0,
            'weight': 150.0,
            'age': 25,
            'sex': 'M',
            'message': 'Profile data fetched successfully.'
        }   
        return user_data

api.add_resource(Home, '/')
api.add_resource(Profile, '/profile', '/profile/<int:accountID>')

if __name__ == '__main__':
    app.run(debug=True)
