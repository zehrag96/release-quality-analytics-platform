import sqlite3
import pandas as pd

db_path = "../Database/release_quality.db"

conn = sqlite3.connect(db_path)

query = """
SELECT
    tc.title,
    tc.test_type,
    tc.priority,
    tc.status,
    u.full_name
FROM TestCases tc
JOIN Users u
ON tc.executed_by = u.user_id;
"""

df = pd.read_sql_query(query, conn)

print("\n=== Test Execution Summary ===\n")


print("\nTotal Executed Test Cases:", len(df))

print("\nStatus Summary:")
print(df["status"].value_counts())

print("\nTester Performance:")
print(df["full_name"].value_counts())

conn.close()