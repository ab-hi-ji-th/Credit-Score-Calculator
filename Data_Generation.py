import os
import pandas as pd
import numpy as np

# Define parameters for data generation
num_samples = 500  # Set to the desired number of farmers 
num_years = 5  # Number of years for each farmer
min_temperature = 15
max_temperature = 45
min_rainfall = 120
max_rainfall = 350
min_underground_water = 1400
max_underground_water = 2100
min_utility = 800
max_utility = 2000

# Additional criteria parameters
bank_statement_balance_mean = 5800
bank_statement_balance_std_dev = 2900
livestock_possession_probability = 0.5  # Probability of possessing livestock
secondary_income_probability = 0.6  # Probability of having secondary income
rental_status_probability = 0.6  # Probability of owning a property
government_backed_loan_probability = 0.2  # Probability of having a government-backed loan

# Generate synthetic data
np.random.seed(42)  # For reproducibility

data = {
    'Farmer_Id': [],
    'Year': [],
    'Temperature': [],
    'Rainfall': [],
    'Underground_Water': [],
    'Neighbour_Success': [],
    'Bank_Statement_Balance': [],
    'Livestock_Possession': [],
    'Collateral': [],
    'Secondary_Income': [],
    'Rental_Status': [],
    'Utility_Bill': [],
    'Government_Backed_Loan': [],
}

# Generate data for each farmer and year
for farmer_id in range(1, num_samples + 1):
    for year in range(2010, 2010 + num_years):
        data['Farmer_Id'].append(farmer_id)
        data['Year'].append(year)
        data['Temperature'].append(np.round(np.random.uniform(min_temperature, max_temperature), 2))
        data['Rainfall'].append(np.round(np.random.uniform(min_rainfall, max_rainfall), 2))
        data['Underground_Water'].append(np.round(np.random.uniform(min_underground_water, max_underground_water), 2))
        data['Neighbour_Success'].append(np.round(np.random.uniform(10, 100), 2))
        data['Bank_Statement_Balance'].append(
            np.round(np.random.normal(bank_statement_balance_mean, bank_statement_balance_std_dev), 2))
        data['Livestock_Possession'].append(
            np.random.choice([0, 1], p=[1 - livestock_possession_probability, livestock_possession_probability]))
        data['Collateral'].append(1 if data['Livestock_Possession'][-1] == 1 else np.random.choice([0, 1], p=[
            1 - livestock_possession_probability, livestock_possession_probability]))
        data['Secondary_Income'].append(
            np.random.choice([0, 1], p=[1 - secondary_income_probability, secondary_income_probability]))
        data['Rental_Status'].append(
            np.random.choice([0, 1], p=[1 - rental_status_probability, rental_status_probability]))
        data['Utility_Bill'].append(np.round(np.random.uniform(min_utility, max_utility), 2))
        data['Government_Backed_Loan'].append(
            np.random.choice([0, 1], p=[1 - government_backed_loan_probability, government_backed_loan_probability]))

# Create a DataFrame
df = pd.DataFrame(data)

# Function to calculate the credit score
weights = {
    'Temperature': 0.1,
    'Rainfall': 0.2,
    'Underground_Water': 0.1,
    'Neighbour_Success': 0.1,
    'Bank_Statement_Balance': 0.05,
    'Livestock_Possession': 0.1,
    'Collateral': 0.1,
    'Secondary_Income': 0.1,
    'Rental_Status': 0.1,
    'Utility_Bill': 0.05,
    'Government_Backed_Loan': 0.1,
}


# Scoring function based on the new criteria
def credit_score_function(row):
    score = 0

    # Temperature
    score += 12 if 21 <= row['Temperature'] <= 37 else 0

    # Rainfall
    score += 12 if 175 <= row['Rainfall'] <= 300 else 0

    # Underground Water
    score += 12 if row['Underground_Water'] > 2000 else 0

    # Neighbours Success
    score += 12 if row['Neighbour_Success'] > 60 else 0

    # Bank Statement Balance
    score += 8 if row['Bank_Statement_Balance'] > 5000 else 0

    # Livestock Possession
    score += 7 if row['Livestock_Possession'] == 1 else 0

    # Collateral
    score += 7 if row['Collateral'] == 1 else 0

    # Secondary Income
    score += 7 if row['Secondary_Income'] == 1 else 0

    # Rental Status
    score += 8 if row['Rental_Status'] == 1 else 0

    # Utility Bills
    score += 8 if row['Utility_Bill'] > 1300 else 0

    # Government Backed Loan
    score += 6 if row['Government_Backed_Loan'] == 1 else 0

    return score


# Apply the credit_score_function to calculate scores for each row
df['Score'] = df.apply(credit_score_function, axis=1)

# Print the current working directory
print("Current working directory:", os.getcwd())

# Save the generated data to an Excel file
df.to_excel('generated_data_with_updated_scores.xlsx', index=False)
