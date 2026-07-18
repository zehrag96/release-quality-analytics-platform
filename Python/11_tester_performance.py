import pandas as pd
from pathlib import Path

# -----------------------------------
# File Paths
# -----------------------------------
BASE_DIR = Path(__file__).resolve().parent
POWERBI_DIR = BASE_DIR.parent / "PowerBI"
OUTPUT_DIR = BASE_DIR / "Python_Outputs"

OUTPUT_DIR.mkdir(exist_ok=True)

# -----------------------------------
# Read CSV Files
# -----------------------------------
testcases = pd.read_csv(POWERBI_DIR / "TestCases.csv")
users = pd.read_csv(POWERBI_DIR / "Users.csv")

# -----------------------------------
# Merge Test Cases with Users
# -----------------------------------
df = testcases.merge(
    users,
    left_on="executed_by",
    right_on="user_id",
    how="left"
)

# -----------------------------------
# Tester Performance
# -----------------------------------
tester_summary = (
    df.groupby(["full_name", "role"])
      .size()
      .reset_index(name="Executed Tests")
      .sort_values("Executed Tests", ascending=False)
)

# Percentage of total executions
total_tests = tester_summary["Executed Tests"].sum()

tester_summary["Share (%)"] = (
    tester_summary["Executed Tests"] / total_tests * 100
).round(1)

# Rename columns
tester_summary.rename(
    columns={
        "full_name": "Tester",
        "role": "Role"
    },
    inplace=True
)

# -----------------------------------
# Export CSV
# -----------------------------------
tester_summary.to_csv(
    OUTPUT_DIR / "tester_performance.csv",
    index=False
)

# -----------------------------------
# Console Output
# -----------------------------------
print("\n=== Tester Performance Summary ===\n")
print(tester_summary)

print("\nCSV file created successfully!")