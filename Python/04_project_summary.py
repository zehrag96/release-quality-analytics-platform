import sqlite3
import pandas as pd
db_path = "../Database/release_quality.db"

conn = sqlite3.connect(db_path)
query = """
SELECT
    project_name,
    owner,
    status
FROM Projects;
"""
df = pd.read_sql_query(query, conn)
print("\n=== Project Summary ===\n")

print(df)
print("\nTotal Project Count:", len(df))
print("\nProject Status Summary:")

print(df["status"].value_counts())
print("\nProject Owner Summary:")

print(df["owner"].value_counts())
conn.close()