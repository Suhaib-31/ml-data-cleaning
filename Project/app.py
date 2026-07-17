import pandas as pd

print("===== Data Cleaning Project =====\n")

# Load Dataset
df = pd.read_csv("dirty_data.csv")

print("Original Dataset:")
print(df)

# -----------------------------
# Missing Values
# -----------------------------

print("\nMissing Values:")
print(df.isnull().sum())

# Fill Missing Age

df["Age"] = df["Age"].fillna(
    df["Age"].mean()
)

# Fill Missing Salary

df["Salary"] = df["Salary"].fillna(
    df["Salary"].mean()
)

# Fill Missing City

df["City"] = df["City"].fillna(
    "Unknown"
)

# -----------------------------
# Remove Duplicates
# -----------------------------

df = df.drop_duplicates()

# -----------------------------
# Fix Data Types
# -----------------------------

df["Age"] = df["Age"].astype(int)

df["Salary"] = df["Salary"].astype(int)

# -----------------------------
# Save Clean Dataset
# -----------------------------

df.to_csv(
    "cleaned_data.csv",
    index=False
)

print("\nCleaned Dataset:")
print(df)

print("\nData Cleaning Completed!")