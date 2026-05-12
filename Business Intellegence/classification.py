import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load data
data = pd.read_csv(
    r"X:\MyNotes\SEM8\Practicals\Business Intellegence\sales_data_sample.csv",
    encoding="latin1"
)

# Create class
data["HIGH_SALES"] = (data["SALES"] > 5000).astype(int)

# Input features
X = data[["QUANTITYORDERED", "PRICEEACH"]]

# Output class
y = data["HIGH_SALES"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = DecisionTreeClassifier()

# Training
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))