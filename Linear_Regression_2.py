import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load your data
df = pd.read_excel("C:\\Users\\Abhijith lappy\\PycharmProjects\\pythonProject\\generated_data_with_mean_scores.xlsx")

# Specify the column you want to use for linear regression (e.g., 'Mean Score')
target_column = 'Mean Score'

# Drop rows with NaN values in the target column
df_regression = df.dropna(subset=[target_column])

# Create a linear regression model
model = LinearRegression()

# Fit the model using the specified column for prediction
X = df_regression[['Farmer_Id']]  # Replace 'Your_Column1', 'Your_Column2', ... with the actual column names
y = df_regression['Mean Score']
model.fit(X, y)

# Make predictions
predictions = model.predict(X)

# Plot the data and the linear regression line
plt.scatter(df_regression['Farmer_Id'], y, color='blue', label='Actual')
plt.plot(df_regression['Farmer_Id'], predictions, color='red', linewidth=2, label='Linear Regression')
plt.xlabel('Farmer_Id')
plt.ylabel(target_column)
plt.title('Linear Regression')
plt.legend()
plt.show()
