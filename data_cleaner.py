import pandas as pd

# Load dataset
df = pd.read_csv("raw_data.csv")

print("Original Data:")
print(df)

# Remove missing values
df = df.dropna()

# Remove duplicate rows
df = df.drop_duplicates()

# Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

print("Cleaned data saved as cleaned_data.csv")
