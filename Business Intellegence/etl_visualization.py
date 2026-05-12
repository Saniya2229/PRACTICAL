import pandas as pd
import matplotlib.pyplot as plt

# Extract
data = pd.read_csv(
    r"Business Intellegence\sales_data_sample.csv",
    encoding="latin1"
)

# Transform
data = data.dropna()

# Load / Show transformed data
print("Clean Data:")
print(data.head())

# Visualization
sales = data.groupby("YEAR_ID")["SALES"].sum()

sales.plot(kind="bar")

plt.title("Sales by Year")
plt.xlabel("Year")
plt.ylabel("Sales")

plt.show()