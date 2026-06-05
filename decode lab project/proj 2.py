import pandas as pd

# Load dataset
df = pd.read_excel("data.xlsx")

# Basic information
print("Dataset Shape:", df.shape)
print("\nColumns:")
print(df.columns)

# Statistics
print("\nSummary Statistics:")
print(df.describe())

# Mean, Median, Count
print("\nQuantity")
print("Mean:", df["Quantity"].mean())
print("Median:", df["Quantity"].median())
print("Count:", df["Quantity"].count())

print("\nTotal Price")
print("Mean:", df["TotalPrice"].mean())
print("Median:", df["TotalPrice"].median())
print("Count:", df["TotalPrice"].count())

# Product-wise sales
print("\nTotal Sales by Product:")
print(df.groupby("Product")["TotalPrice"].sum().sort_values(ascending=False))

# Order Status
print("\nOrder Status Count:")
print(df["OrderStatus"].value_counts())

# Payment Method
print("\nPayment Method Count:")
print(df["PaymentMethod"].value_counts())