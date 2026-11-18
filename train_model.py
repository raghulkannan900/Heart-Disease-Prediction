
import pandas as pd
import joblib
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load cleaned dataset
file_path = Path("dataset/heart_disease_cleaned.csv")

if not file_path.exists():
    print("ERROR: Cleaned dataset not found!")
    print("Run python clean_dataset.py first.")
    raise SystemExit

df = pd.read_csv(file_path)

# Separate input features and target
X = df.drop("target", axis=1)
y = (df["target"] > 0).astype(int)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Create and train model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)

print("\nMODEL TRAINING COMPLETED")
print("Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Save trained model
Path("prediction").mkdir(exist_ok=True)

joblib.dump(model, "prediction/heart_model.pkl")

print("\nModel saved successfully!")
print("Location: prediction/heart_model.pkl")
