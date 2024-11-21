import pandas as pd

# Load the CSV file
file_path = "worldwide_vaccine_data.csv"  # Replace with the path to your CSV file
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(data.head())

# Calculate the average of a specific column
column_name = "% of population vaccinated"  # Replace with the name of the column
if column_name in data.columns:
    average = data[column_name].mean()
    print(f"\nThe average of the '{column_name}' column is: {average}")
else:
    print(f"\nColumn '{column_name}' not found in the dataset.")

# Get a summary of the dataset
print("\nSummary of the dataset:")
print(data.describe())

# Check for missing values
missing_values = data.isnull().sum()
print("\nMissing values in each column:")
print(missing_values)
