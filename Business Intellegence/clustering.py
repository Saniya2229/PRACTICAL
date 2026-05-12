import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load data
data = pd.read_csv(
    r"Business Intellegence\sales_data_sample.csv",
    encoding="latin1"
)

# Features
X = data[["QUANTITYORDERED", "SALES"]]

# K-Means
model = KMeans(n_clusters=3, random_state=42)
data["Cluster"] = model.fit_predict(X)

# Output
print(data[["QUANTITYORDERED", "SALES", "Cluster"]].head())

# Graph
plt.scatter(data["QUANTITYORDERED"], data["SALES"])
plt.title("K-Means Clustering")
plt.xlabel("Quantity")
plt.ylabel("Sales")
plt.show()