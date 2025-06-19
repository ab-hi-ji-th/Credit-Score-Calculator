import pandas as pd

# Specify the path to your Excel file
excel_file_path = "C:\\Users\\Abhijith lappy\\PycharmProjects\\pythonProject\\generated_data_with_updated_scores.xlsx"

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)

# Copy the existing DataFrame
df_copy = df.copy()

# Create a new column 'Mean Score' and initialize it with NaN 
df_copy['Mean Score'] = float('nan')

# Group by 'Farmer_Id' and calculate the mean of 'Score' for each farmer
mean_scores_by_farmer = df.groupby('Farmer_Id')['Score'].mean().reset_index()

# Iterate over unique Farmer_Id values
for farmer_id in df_copy['Farmer_Id'].unique():
    # Get the mean score for the farmer_id
    mean_score = mean_scores_by_farmer.loc[mean_scores_by_farmer['Farmer_Id'] == farmer_id, 'Score'].values[0]

    # Update 'Mean Score' only for the rows where year is 2010 and for the respective farmer_id
    df_copy.loc[(df_copy['Year'] == 2010) & (df_copy['Farmer_Id'] == farmer_id), 'Mean Score'] = mean_score

# Save the updated data to a new Excel file
df_copy.to_excel('generated_data_with_mean_scores.xlsx', index=False)
