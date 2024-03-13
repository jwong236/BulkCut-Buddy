from flask import Flask
import argparse
from api.endpoints import initialize_api
from utils.db_utils import Database
from utils import get_db_config

app = Flask(__name__)

weekly_model_path = "weekly_model.joblib"
monthly_model_path = "monthly_model.joblib"
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--wnew", action="store_true", help="Train a new weekly model.")
    parser.add_argument("--mnew", action="store_true", help="Train a new monthly model.")
    args = parser.parse_args()


    initialize_api(app) # Set resource endpoitns to flask app
    db_config = get_db_config()
    app.db = Database(db_config)
    #app.config['WEEKLY_MODEL'] = weekly_model
    #app.config['MONTHLY_MODEL'] = monthly_model
    app.run(debug=True) # run server

if __name__ == '__main__':
    main()
