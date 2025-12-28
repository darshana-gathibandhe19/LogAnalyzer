import random
import time
from datetime import datetime, timedelta

# Configurations
LOG_FILE = "server_logs.txt"
ERROR_LEVELS = ["INFO", "WARNING", "ERROR", "CRITICAL"]
MESSAGES = [
    "User login successful",
    "Database connection timeout",
    "File not found exception",
    "Payment gateway latency high",
    "Disk space usage at 90%",
    "Cache miss for user_id_123"
]

def generate_log_line():
    """Creates a realistic looking log line."""
    timestamp = datetime.now() - timedelta(minutes=random.randint(0, 10000))
    timestamp_str = timestamp.strftime("%Y-%m-%d %H:%M:%S")
    level = random.choices(ERROR_LEVELS, weights=[50, 30, 15, 5])[0] # Mostly INFO
    msg = random.choice(MESSAGES)
    
    # The "Messy" Text Format
    return f"[{timestamp_str}] - SERVER-01 - {level} : {msg}\n"

if __name__ == "__main__":
    print(f"Generating 10,000 log lines into {LOG_FILE}...")
    with open(LOG_FILE, "w") as f:
        for _ in range(10000):
            f.write(generate_log_line())
    print("✅ Done! You now have a messy log file.")