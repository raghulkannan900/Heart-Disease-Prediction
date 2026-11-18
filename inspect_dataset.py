import pandas as pd

file_path = "dataset/heart_disease.csv"

df = pd.read_csv(file_path, na_values=["NULL", "?"])

print("\nDATASET SIZE:")
print(df.shape)

print("\nCOLUMN NAMES:")
print(df.columns.tolist())

print("\nFIRST 5 RECORDS:")
print(df.head())

print("\nMISSING VALUES:")
print(df.isnull().sum())

print("\nTARGET DISTRIBUTION:")
print(df["target"].value_counts(dropna=False))

print("\nDATASET INSPECTION COMPLETE!")
