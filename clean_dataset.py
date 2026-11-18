
import pandas as pd
from pathlib import Path

# Dataset file location
file_path = Path("dataset/heart_disease.csv")

if not file_path.exists():
    print("ERROR: Dataset file not found!")
    print("Please check the dataset folder.")
    raise SystemExit

# Read dataset
df = pd.read_csv(file_path, na_values=["?", "NULL", ""])

print("ORIGINAL DATASET")
print("Dataset shape:", df.shape)

# Required columns
required_columns = [
    "age", "sex", "cp", "trestbps", "chol",
    "fbs", "restecg", "thalach", "exang",
    "oldpeak", "slope", "ca", "thal", "target"
]

# Check columns
missing_columns = [
    col for col in required_columns if col not in df.columns
]

if missing_columns:
    print("Missing columns:", missing_columns)
    print("Available columns:", df.columns.tolist())
    raise SystemExit

# Keep required columns
df = df[required_columns].copy()

# Convert columns to numeric
for column in required_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# Remove duplicate records
print("\nDuplicate records:", df.duplicated().sum())
df = df.drop_duplicates()

# Remove rows without target values
df = df.dropna(subset=["target"])

# Fill missing numerical values
continuous_columns = [
    "age", "trestbps", "chol", "thalach", "oldpeak"
]

for column in continuous_columns:
    if df[column].notna().any():
        df[column] = df[column].fillna(df[column].median())

# Fill missing categorical values
categorical_columns = [
    "sex", "cp", "fbs", "restecg",
    "exang", "slope", "ca", "thal"
]

for column in categorical_columns:
    if df[column].notna().any():
        df[column] = df[column].fillna(df[column].mode()[0])

# Check missing values
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Check target values
print("\nTarget distribution:")
print(df["target"].value_counts().sort_index())

# Save cleaned dataset
output_path = Path("dataset/heart_disease_cleaned.csv")
df.to_csv(output_path, index=False)

print("\nCleaned dataset shape:", df.shape)
print("Dataset saved successfully!")
print("Saved location:", output_path)
