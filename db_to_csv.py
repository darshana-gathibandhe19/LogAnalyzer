import sqlite3
import pandas as pd

# Connect to your database
conn = sqlite3.connect("logs_warehouse.db")

# Read table
df = pd.read_sql_query("SELECT * FROM server_logs", conn)

# Save as CSV (Power BI loves CSVs)
df.to_csv("server_logs_clean.csv", index=False)

print("✅ Converted Database to server_logs_clean.csv")
conn.close()