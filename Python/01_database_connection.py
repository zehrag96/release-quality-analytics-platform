import sqlite3
import pandas as pd

db_path = "../Database/release_quality.db"

conn = sqlite3.connect(db_path)

query = """
SELECT *
FROM Releases;
"""

df = pd.read_sql_query(query, conn)

print("\n=== Releases Table ===\n")
print(df)

print("\nToplam Release Sayısı:", len(df))

conn.close()