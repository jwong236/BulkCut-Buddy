from flask import Flask
import argparse
import os
from server.api.endpoints import initialize_api
from server.weight_projection_model import WeightProjectionModel
import atexit
from utils.db_utils import Database
from database import db_config

app = Flask(__name__)

weekly_model_path = "weekly_model.joblib"
monthly_model_path = "monthly_model.joblib"


def get_models(wnew, mnew):
    """
    Instantiates both weekly and monthly models. Uses already existing serialized one unless --wnew for weekly and/or --mnew for monthly is true, 
    or if serialized model doesn't already exist. Models are trained upon instantiation
    """
    if wnew or not os.path.exists(weekly_model_path):
        weekly_training_dataframe = query_weekly_training_dataframe() # TODO: Implement query_weekly_training_dataframe() which retrieves dataframe containing all training data
        weekly_model = WeightProjectionModel(mode="weekly")
        print("New weekly model created")
        weekly_model.train(weekly_training_dataframe)
        print("New weekly model trained")
    else:
        weekly_model = WeightProjectionModel(mode="weekly")
        weekly_model.deserialize(weekly_model_path)
        print("Weekly model deserialized.")

    if mnew or not os.path.exists(monthly_model_path):
        monthly_training_dataframe = query_monthly_training_dataframe() # TODO: Implement query_monthly_training_dataframe() which retrieves dataframe containing all training data
        monthly_model = WeightProjectionModel(mode="monthly")
        print("New monthly model created")
        monthly_model.train(monthly_training_dataframe)
        print("New monthly model trained")
    else:
        monthly_model = WeightProjectionModel(mode="monthly")
        monthly_model.deserialize(monthly_model_path)
        print("Monthly model deserialized.")

    return weekly_model, monthly_model

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
    weekly_model, monthly_model = get_models(args.wnew, args.mnew)

    # 3.
    atexit.register(serialize_models_on_exit, weekly_model, monthly_model, weekly_model_path, monthly_model_path) # Serialize models on server close
    initialize_api(app) # Set resource endpoitns to flask app
    app.db = Database(db_config)
    app.config['WEEKLY_MODEL'] = weekly_model
    app.config['MONTHLY_MODEL'] = monthly_model
    app.run(debug=True) # run server

if __name__ == '__main__':
    main()
