import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def main():
    # Example dataframe, we would get this data from a SQL server with however we make queries
    # TODO: Fabricate more data
    df = pd.DataFrame({
        # Physiological Factors
        'initial_weight': [165.0],
        'body_fat_percentage': [.2],
        'height': [172.72],
        'gender': [0], # 0 for male

        # Activity Factors
        'weight_change_metric': [30],
        'active_calories_burned': [358],
        'resting_calories_burned':  [1723]
        'steps': [8659]
        'hours_of_sleep': [8],
        
        # Diet
        'daily_calorie_intake': [2000],
        'daily_protein_intake': [100],

        # Temporal Variable
        'week_count': [1],

        # Target
        'future_weight': [164.0]
    })




    # Define predictors and outcome
    X = df[['initial_weight', 'daily_calorie_intake', 'calorie_expenditure', 'hours_of_sleep', 'body_fat_percentage', 'height', 'gender', 'weight_change_metric', 'week_count']]
    y = df['future_weight']

    # Splitting dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Creating and training the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Making predictions
    y_pred = model.predict(X_test)

    # Model evaluation metrics
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"Mean Squared Error (MSE): {mse}")
    print(f"R-squared: {r2}")




    # Example of using the model: collect this data from the user upon account creation
    predict_data = pd.DataFrame({
        'initial_weight': [163.0],
        'daily_calorie_intake': [2030],
        'calorie_expenditure': [190],
        'hours_of_sleep': [7],
        'body_fat_percentage': [.3],
        'height': [182.72],
        'gender': [0],
        'weight_change_metric': [20],
        'week_count': [3]
    })

    # Making a prediction
    future_weight_prediction = model.predict(predict_data)
    print("Predicted future weight:", future_weight_prediction[0])

if __name__ == "__main__":
    main()