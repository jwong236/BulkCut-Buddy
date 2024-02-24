from flask import Flask
import argparse
import os
from api import initialize_api
from server.weight_projection_model import WeightProjectionModel
import atexit

app = Flask(__name__)

weekly_model_path = "weekly_model.joblib"
monthly_model_path = "monthly_model.joblib"


def get_models(wnew, mnew):
    # Define model file paths
    # Initialize model if flag is true or path doesnt exist. Otherwise use already existing one
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

    # Initialize model if flag is true or path doesnt exist. Otherwise use already existing one
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
    weekly_model.serialize(weekly_path)
    monthly_model.serialize(monthly_path)
    print("Models serialized on server exit.")
    
def main():

    # CREATE MODELS
    # Set up command-line arguments
    # Run server by running 'python src/server/server.py'
    # Include --wnew flag to train a new weekly model, --mnew flag to train a new monthly model
    # If flags arent included, attempt to deserialized an already existing model for either. If one doesnt exist, train a new model
    parser = argparse.ArgumentParser(description="Start the Flask server with optional model initialization.")
    parser = argparse.ArgumentParser(description="Manage weekly and monthly models.")
    parser.add_argument("--wnew", action="store_true", help="Train a new weekly model.")
    parser.add_argument("--mnew", action="store_true", help="Train a new monthly model.")
    args = parser.parse_args()
    
    # Call function for logic of training models depending on flag or existance.
    weekly_model, monthly_model = get_models(args.wnew, args.mnew)

    # INITIALIZE & START SERVER
    atexit.register(serialize_models_on_exit, weekly_model, monthly_model, weekly_model_path, monthly_model_path) # Serialize models on server close
    initialize_api(app) # Set resource endpoitns to flask app
    app.config['WEEKLY_MODEL'] = weekly_model
    app.config['MONTHLY_MODEL'] = monthly_model
    app.run(debug=True) # run server

    # Profile's POST
    # 1. Accept data from APi endpoints
    # 2. Upload user data to database

    # Profile's PUT
    # 1. Accept data from API endpoints
    # 2. Upload user data to database

    # Profile's GET
    # 1. Fetch user data from database
    # 2. Clean data
    # 3. Feed data into model
    # 4. receive predicttion from model
    # 5. Send prediction to frontend

if __name__ == '__main__':
    main()
