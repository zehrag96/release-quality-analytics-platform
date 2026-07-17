import sqlite3
import pandas as pd

db_path = "../Database/release_quality.db"

conn = sqlite3.connect(db_path)


query = """
SELECT *
FROM Users;
"""
df = pd.read_sql_query(query, conn)

print(df.columns)
print(df)

print("\n=== User Statistics ===\n")

print(df)

print("\nTotal User Count:", len(df))

print("\nRole Summary:")
print(df["role"].value_counts())



conn.close()