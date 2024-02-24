import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from joblib import dump, load

class WeightProjectionModel:
    def __init__(self, mode):
        self.model = LinearRegression()
        self.mse = 0.0
        self.r2 = 0.0
        if mode not in ["weekly", "monthly"]:
            raise ValueError("Mode must be 'weekly' or 'monthly'.")
        self.mode = mode

    def train_and_evaluate(self, df: pd.DataFrame, test_size = 0.2, random_state = 42):
        """
        Train and evaluate the model based on the dataframe provided.
        Parameters:
            df (pd.DataFrame): The input data frame containing training features and target.
            test_size (float): The proportion of the dataset to include in the test split.
            random_state (int): Controls the shuffling applied to the data before applying the split.
        Returns:
            None
        """
        # Extract features from dataframe
        features = ['initial_weight', 'body_fat_percentage', 'height', 'sex', 'weight_change_rate',
                           'active_calories_burned', 'resting_calories_burned', 'steps', 'hours_of_sleep',
                           'daily_calorie_intake',
                           'daily_protein_intake']
        if self.mode == "weekly":
            X = df[features + ['week_count']]
        else:
            X = df[features + ['month_count']]
        y = df['future_weight']

        # Split dataset into training and testing
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size, random_state)
        
        # Train model on training data
        self.model.fit(X_train, y_train)

        # Make prediction of test data
        y_pred = self.model.predict(X_test)  # Corrected to use X_test

        # Calculate metrics
        self.mse = mean_squared_error(y_test, y_pred)
        self.r2 = r2_score(y_test, y_pred)

    def get_metrics(self):
        """Retrieve the evaluation metrics from the last training and evaluation cycle."""
        return self.mse, self.r2

    def predict(self, user_data: pd.DataFrame) -> pd.Series:
        """Predict future weight based on user-provided data."""
        return self.model.predict(user_data)

    def serialize(self, path: str = 'model.joblib'):
        """Serialize the model to a file for future use."""
        # Prepend the mode to the filename
        full_path = f"{self.mode}_{path}"
        dump(self.model, full_path)


    def deserialize(self, path: str):
        """Deserialize the model from a file for use."""
        try:
            self.model = load(path)
        except FileNotFoundError:
            print(f"Model file {path} not found.")
        except Exception as e:
            print(f"Error loading model: {e}")
