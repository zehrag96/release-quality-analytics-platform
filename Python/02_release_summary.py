import sqlite3
import pandas as pd

db_path = "../Database/release_quality.db"

conn = sqlite3.connect(db_path)

query = """
SELECT
    release_name,
    status,
    environment
FROM Releases;
"""

df = pd.read_sql_query(query, conn)

print("\nRelease Status Summary:")
print(df["status"].value_counts().to_string())

print("\nEnvironment Summary:")
print(df["environment"].value_counts().to_string())

print("\nTotal Release Count:", len(df))

conn.close()