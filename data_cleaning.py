import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("risk_factors_cervical_cancer.csv")

# Replace '?' with NaN
df.replace("?", np.nan, inplace=True)

# Convert all columns to numeric
df = df.apply(pd.to_numeric)

print("Missing values after replacing '?':\n")
print(df.isnull().sum())

# Fill missing values with median (safe for medical data)
df_filled = df.fillna(df.median())

print("\nMissing values after imputation:\n")
print(df_filled.isnull().sum())

# Save cleaned dataset
df_filled.to_csv("cleaned_cervical_cancer_data.csv", index=False)

print("\nCleaned dataset saved as cleaned_cervical_cancer_data.csv")
