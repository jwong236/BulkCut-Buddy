import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from joblib import dump, load

class WeightProjectionModel:
    def __init__(self, mode):
        self.model = LinearRegression()
        self.mode = mode

        self.X_test = None
        self.y_test = None
        self.mse = 0.0
        self.r2 = 0.0

        if mode not in ["weekly", "monthly"]:
            raise ValueError("Mode must be 'weekly' or 'monthly'.")

    def train(self, df: pd.DataFrame, test_size=0.2, random_state=42):
        """
        Train the model based on the provided DataFrame.
        Parameters:
            df (pd.DataFrame): Input data frame containing training features and target.
            test_size (float): Proportion of the dataset to include in the test split.
            random_state (int): Controls the shuffling applied to the data before applying the split.
        """
        # Bodyfat percentage is not feasible
        features = ['initial_weight', 'height', 'sex', 'weight_change_rate',
                    'active_calories_burned', 'resting_calories_burned', 'steps', 'hours_of_sleep',  
                    'daily_calorie_intake', 'daily_protein_intake']
        if self.mode == "weekly":
            X = df[features + ['week_count']]
        else:
            X = df[features + ['month_count']]
        y = df['future_weight']

        X_train, self.X_test, y_train, self.y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
        
        self.model.fit(X_train, y_train)

    def evaluate(self):
        """
        Evaluate the model using the test data set aside during training.
        Requires train to be called first to set X_test and y_test.
        Returns:
            mse (float): Mean Squared Error of the model on the test data.
            r2 (float): R-squared value of the model on the test data.
        """
        if self.X_test is None or self.y_test is None:
            raise ValueError("Model has not been trained - X_test or y_test are not set.")
        
        y_pred = self.model.predict(self.X_test)
        self.mse = mean_squared_error(self.y_test, y_pred)
        self.r2 = r2_score(self.y_test, y_pred)
        return self.mse, self.r2
            

    def get_metrics(self):
        """Retrieve the evaluation metrics from the last training and evaluation cycle."""
        return self.mse, self.r2

    def predict(self, user_data: pd.DataFrame) -> pd.Series:
        """Predict future weight based on user-provided data."""
        return self.model.predict(user_data)

    def serialize(self, path: str):
        """Serialize the model to a file for future use."""
        dump(self.model, path)


    def deserialize(self, path: str):
        """Deserialize the model from a file for use."""
        try:
            self.model = load(path)
        except FileNotFoundError:
            print(f"Model file {path} not found.")
        except Exception as e:
            print(f"Error loading model: {e}")
