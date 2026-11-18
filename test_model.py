
import joblib
import pandas as pd
from pathlib import Path

# Load trained model
model_path = Path("prediction/heart_model.pkl")

if not model_path.exists():
    print("Model file not found!")
    raise SystemExit

model = joblib.load(model_path)

# Sample test input using the 13 dataset features
sample = pd.DataFrame([{
    "age": 50,
    "sex": 1,
    "cp": 2,
    "trestbps": 130,
    "chol": 230,
    "fbs": 0,
    "restecg": 1,
    "thalach": 150,
    "exang": 0,
    "oldpeak": 1.0,
    "slope": 2,
    "ca": 0,
    "thal": 3
}])

# Make prediction
prediction = model.predict(sample)[0]

print("\nHEART DISEASE MODEL TEST")
print("-----------------------")

if prediction == 1:
    print("Model output: Higher estimated risk")
else:
    print("Model output: Lower estimated risk")

if hasattr(model, "predict_proba"):
    probability = model.predict_proba(sample)[0][1]
    print("Estimated model probability:", round(probability * 100, 2), "%")

print("\nModel test completed!")
