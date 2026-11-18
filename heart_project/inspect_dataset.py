
import pandas as pd

# Load the dataset
file_path = "dataset/heart_disease.csv"

df = pd.read_csv(file_path, na_values=["NULL", "?"])

# Display dataset information
print("\n========== HEART DISEASE DATASET ==========")

print("\n1. Dataset size:")
print(df.shape)

print("\n2. Column names:")
print(df.columns.tolist())

print("\n3. First 5 records:")
print(df.head())

print("\n4. Dataset information:")
df.info()

print("\n5. Missing values:")
print(df.isnull().sum())

print("\n6. Target column distribution:")
print(df["target"].value_counts(dropna=False))

print("\n========== INSPECTION COMPLETE ==========")
