
import pandas as pd
from pathlib import Path

# 1. Load original dataset
file_path = Path("dataset/heart_disease.csv")

if not file_path.exists():
    print("ERROR: Dataset file not found!")
    print("Check whether dataset/heart_disease.csv exists.")
    raise SystemExit

df = pd.read_csv(file_path, na_values=["?", "NULL", ""])

print("ORIGINAL DATASET")
print("Shape:", df.shape)

# 2. Check required columns
required_columns = [
    "age", "sex", "cp", "trestbps", "chol",
    "fbs", "restecg", "thalach", "exang",
    "oldpeak", "slope", "ca", "thal", "target"
]

missing_columns = [
    col for col in required_columns if col not in df.columns
]

if missing_columns:
    print("Missing expected columns:", missing_columns)
    print("Actual columns:", df.columns.tolist())
    raise SystemExit

# 3. Keep the required columns
df = df[required_columns].copy()

# 4. Convert columns to numeric values
for column in required_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# 5. Remove duplicate records
duplicates = df.duplicated().sum()
print("\nDuplicate records:", duplicates)

df = df.drop_duplicates()

# 6. Remove rows with missing target values
df = df.dropna(subset=["target"])

# 7. Fill missing values
continuous_columns = [
    "age", "trestbps", "chol", "thalach", "oldpeak"
]

categorical_columns = [
    "sex", "cp", "fbs", "restecg",
    "exang", "slope", "ca", "thal"
]

for column in continuous_columns:
    df[column] = df[column].fillna(df[column].median())

for column in categorical_columns:
    if df[column].notna().any():
        df[column] = df[column].fillna(df[column].mode()[0])

# 8. Check missing values after cleaning
print("\nMISSING VALUES AFTER CLEANING:")
print(df.isnull().sum())

# 9. Save cleaned dataset
output_path = Path("dataset/heart_disease_cleaned.csv")
df.to_csv(output_path, index=False)

print("\nCLEANED DATASET")
print("Shape:", df.shape)
print("Target distribution:")
print(df["target"].value_counts().sort_index())

print("\nDataset saved successfully!")
print("Location:", output_path)
