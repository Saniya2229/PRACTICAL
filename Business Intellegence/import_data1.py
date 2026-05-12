import pandas as pd

# Read CSV file
data = pd.read_csv("Business Intellegence\sales_data_sample.csv", encoding="latin1")

# Show first 5 rows
print("Imported Data:")
print(data.head())

# Load to target system
data.to_csv("output.csv", index=False)

print("\nData loaded successfully.")
print("Output file created: output.csv")