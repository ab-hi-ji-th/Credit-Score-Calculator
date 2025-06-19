import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

 
def linear_regression_and_plot():
    # Load the data
    df = pd.read_excel(r'C:\Users\Abhijith lappy\PycharmProjects\pythonProject\generated_data_with_updated_scores.xlsx')

    # Prepare the data
    X = df[['Temperature', 'Rainfall', 'Underground_Water', 'Neighbour_Success',
            'Bank_Statement_Balance', 'Livestock_Possession', 'Collateral',
            'Secondary_Income', 'Rental_Status', 'Utility_Bill', 'Government_Backed_Loan']]
    y = df['Score']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a linear regression model
    model = LinearRegression()

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error: {mse}')

    # Plot the best-fit line
    plt.scatter(y_test, y_pred, label='Scores')
    plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], linestyle='--', color='red', label='Ideal Line')
    plt.xlabel('Actual Scores')
    plt.ylabel('Predicted Scores')
    plt.title('Linear Regression Model - Best-Fit Line')
    plt.legend()
    plt.show()


linear_regression_and_plot()
