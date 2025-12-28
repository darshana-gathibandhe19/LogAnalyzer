import re
import sqlite3
import pandas as pd

# 1. Configuration
INPUT_LOG = "server_logs.txt"
DB_NAME = "logs_warehouse.db"

# 2. The Regex Pattern (The "Magic")
# Matches: [2025-12-26 10:00:00] - SERVER-01 - ERROR : Message
log_pattern = re.compile(r"\[(.*?)\] - (.*?) - (.*?) : (.*)")

print("--- 🚀 Starting ETL Process ---")

# 3. Extract (Read & Parse)
clean_data = []
with open(INPUT_LOG, "r") as file:
    for line in file:
        match = log_pattern.match(line)
        if match:
            clean_data.append({
                "timestamp": match.group(1),
                "server_id": match.group(2),
                "error_level": match.group(3),
                "message": match.group(4)
            })

print(f"✅ Extracted {len(clean_data)} lines using Regex.")

# 4. Transform (Convert to DataFrame)
df = pd.DataFrame(clean_data) # Quick trick to convert list of dicts
df['timestamp'] = pd.to_datetime(df['timestamp']) # Convert string to actual Time

# 5. Load (Save to SQL)
conn = sqlite3.connect(DB_NAME)
df.to_sql("server_logs", conn, if_exists="replace", index=False)
conn.close()

print(f"✅ Loaded data into SQL Database: {DB_NAME}")
print("--- ETL Complete ---")