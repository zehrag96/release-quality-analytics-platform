import sqlite3
import pandas as pd

db_path = "../Database/release_quality.db"

conn = sqlite3.connect(db_path)

query = """
SELECT
    title,
    test_type,
    priority,
    status,
    executed_by
FROM TestCases;
"""

df = pd.read_sql_query(query, conn)


print("\n=== Test Case Statistics ===\n")

print(df)

print("\nTotal Test Case Count:", len(df))

print("\nStatus Summary:")
print(df["status"].value_counts())
print("\nExecuted By Summary:")
print(df["executed_by"].value_counts())
conn.close()
