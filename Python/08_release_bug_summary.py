import sqlite3
import pandas as pd

db_path = "../Database/release_quality.db"

conn = sqlite3.connect(db_path)

query = """
SELECT
    r.release_name,
    COUNT(b.bug_id) AS total_bugs
FROM Releases r
LEFT JOIN Bugs b
ON r.release_id = b.release_id
GROUP BY r.release_id, r.release_name
ORDER BY total_bugs DESC;
"""

df = pd.read_sql_query(query, conn)

print("\n=== Release Bug Summary ===\n")
print(df)

print("\nTotal Releases:", len(df))

conn.close()