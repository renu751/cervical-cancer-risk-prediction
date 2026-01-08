import pandas as pd

# Load dataset
df = pd.read_csv("risk_factors_cervical_cancer.csv")

# Basic information
print("Dataset shape:", df.shape)
print("\nColumn names:\n", df.columns)

# Check missing values
print("\nMissing values per column:\n")
print(df.isnull().sum())

# Display first few rows
print("\nSample data:\n")
print(df.head())
