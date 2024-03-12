from flask import Flask
import argparse
import os
from server.api.endpoints import initialize_api
from server.weight_projection_model import WeightProjectionModel
import atexit
from utils.db_utils import Database
from utils import get_db_config

app = Flask(__name__)

weekly_model_path = "weekly_model.joblib"
monthly_model_path = "monthly_model.joblib"




def serialize_models_on_exit(weekly_model, monthly_model, weekly_path, monthly_path):
    """
    Serializes both monthly and weekly models
    """
    weekly_model.serialize(weekly_path)
    monthly_model.serialize(monthly_path)
    print("Models serialized on server exit.")
    
def main():
    """
    1. Set up command-line arguments
    - Run server by running 'python src/server/server.py'
    - Include --wnew flag to train a new weekly model, --mnew flag to train a new monthly model
    2. Instantiates models
    - If flags arent included, attempt to deserialized an already existing model for either. If one doesnt exist, train a new model
    3. Initializes app
    - Registers on_server_close action
    - Initializes API endpoints for flask app
    - Sets models as a config for the app
    - Runs server
    """
    # 1.
    parser = argparse.ArgumentParser()
    parser.add_argument("--wnew", action="store_true", help="Train a new weekly model.")
    parser.add_argument("--mnew", action="store_true", help="Train a new monthly model.")
    args = parser.parse_args()
    
    # 2.
    #weekly_model, monthly_model = get_models(args.wnew, args.mnew)

    # 3.
    #atexit.register(serialize_models_on_exit, weekly_model, monthly_model, weekly_model_path, monthly_model_path) # Serialize models on server close
    initialize_api(app) # Set resource endpoitns to flask app
    db_config = get_db_config()
    app.db = Database(db_config)
    #app.config['WEEKLY_MODEL'] = weekly_model
    #app.config['MONTHLY_MODEL'] = monthly_model
    app.run(debug=True) # run server

if __name__ == '__main__':
    main()
