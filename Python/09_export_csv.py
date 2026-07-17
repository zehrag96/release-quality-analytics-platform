import sqlite3
import pandas as pd
import os

db_path = "../Database/release_quality.db"

conn = sqlite3.connect(db_path)

output_folder = "../PowerBI"

os.makedirs(output_folder, exist_ok=True)

tables = [
    "Projects",
    "Releases",
    "Users",
    "Bugs",
    "TestCases"
]

for table in tables:
    df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
    df.to_csv(f"{output_folder}/{table}.csv", index=False)
    print(f"✅ {table}.csv exported")

conn.close()

print("\n🎉 All CSV files exported successfully!")