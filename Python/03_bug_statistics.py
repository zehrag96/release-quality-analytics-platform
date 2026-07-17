import sqlite3
import pandas as pd

db_path = "../Database/release_quality.db"

conn = sqlite3.connect(db_path)

query = """
SELECT
    severity,
    status
FROM Bugs;
"""

df = pd.read_sql_query(query, conn)

print("\n=== Bug Statistics ===\n")

print(f"📊 Total Bug Count: {len(df)}")

print("\n=== Severity Summary ===")
print(df["severity"].value_counts().to_string())

print("\n=== Status Summary ===")
print(df["status"].value_counts().to_string())

closed_bugs = (df["status"] == "Closed").sum()
closure_rate = (closed_bugs / len(df)) * 100

print(f"\nBug Closure Rate: {closure_rate:.1f}%")
conn.close()