import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load data
df = pd.read_csv("iris.csv")
print(df.head())

# Prepare features (X) and target (y)
X = df.iloc[:, :-1]  # All columns except last
y = df.iloc[:, -1]   # Last column (species)

# Encode labels (e.g., "setosa" → 0, "versicolor" → 1)
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train logistic regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# User input for prediction
s_len = float(input("Sepal Length (cm): "))
s_wid = float(input("Sepal Width (cm): "))
p_len = float(input("Petal Length (cm): "))
p_wid = float(input("Petal Width (cm): "))

# Format input for prediction
sample = np.array([s_len, s_wid, p_len, p_wid]).reshape(1, -1)
sample_df = pd.DataFrame(sample, columns=X.columns)

# Predict species
prediction = model.predict(sample_df)
species = label_encoder.inverse_transform(prediction)
print(f"Predicted Species: {species[0]}")
