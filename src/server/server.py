from flask import Flask
import argparse
import os
from api import initialize_api
from server.weight_projection_model import WeightProjectionModel

"""
Upon server start:
1. Load and deserialize model
OPTIONAL: (Do this only if you want to train the model)
1. Fetch training data from database
2. Train model

Upon frontend using POST endpoint to backend:
1. Accept data from APi endpoints
2. Upload user data to database

Upon frontend using PUT endpoint to backend:
1. Accept data from API endpoints
2. Upload user data to database

Upon frontend using GET endpoint from backend
1. Fetch user data from database
2. Clean data
3. Feed data into model
4. receive predicttion from model
5. Send prediction to frontend

Upon server close:
1. Deserialize model
"""
def main():
    parser = argparse.ArgumentParser(description="Start the Flask server with optional model initialization.")
    parser.add_argument("--new", action="store_true", help="Force the creation of a new model regardless of existing serialized models.")
    args = parser.parse_args()
    
    weekly_model_file_path = "weekly_model.joblib"
    monthly_model_file_path = "monthly_model.joblib"

    app = Flask(__name__)
    
    if args.new or not os.path.exists(model_file_path):
        model = WeightProjectionModel(mode="weekly")
        print("Initialized a new model.")
    else:
        model = WeightProjectionModel(mode="weekly")
        model.deserialize(model_file_path)
        print(f"Deserialized model from {model_file_path}.")


    initialize_api(app)
    app.run(debug=True)

if __name__ == '__main__':
    main()
