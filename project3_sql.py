import pandas as pd
import sqlite3

# Load Excel dataset
df = pd.read_excel("data.xlsx")

# Create SQLite database
conn = sqlite3.connect("analytics.db")
df.to_sql("orders", conn, if_exists="replace", index=False)

# SELECT
print("\nAll Products:")
print(pd.read_sql("SELECT Product FROM orders LIMIT 10", conn))

# WHERE
print("\nDelivered Orders:")
print(pd.read_sql(
    "SELECT * FROM orders WHERE OrderStatus='Delivered' LIMIT 5",
    conn
))

# ORDER BY
print("\nTop Orders by Total Price:")
print(pd.read_sql(
    "SELECT Product, TotalPrice FROM orders ORDER BY TotalPrice DESC LIMIT 10",
    conn
))

# GROUP BY + SUM
print("\nSales by Product:")
print(pd.read_sql(
    "SELECT Product, SUM(TotalPrice) AS TotalSales "
    "FROM orders GROUP BY Product ORDER BY TotalSales DESC",
    conn
))

# COUNT
print("\nOrders by Status:")
print(pd.read_sql(
    "SELECT OrderStatus, COUNT(*) AS TotalOrders "
    "FROM orders GROUP BY OrderStatus",
    conn
))

# AVG
print("\nAverage Price by Product:")
print(pd.read_sql(
    "SELECT Product, AVG(TotalPrice) AS AvgPrice "
    "FROM orders GROUP BY Product",
    conn
))

conn.close()