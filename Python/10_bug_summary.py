import pandas as pd
from pathlib import Path

# -----------------------------
# File Paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent
POWERBI_DIR = BASE_DIR.parent / "PowerBI"
OUTPUT_DIR = BASE_DIR/ "Python_Outputs"

OUTPUT_DIR.mkdir(exist_ok=True)
print(OUTPUT_DIR)

# -----------------------------
# Read CSV
# -----------------------------
bugs = pd.read_csv(POWERBI_DIR / "Bugs.csv")

# -----------------------------
# Bug Status Summary
# -----------------------------
bug_status_summary = (
    bugs.groupby("status")
        .size()
        .reset_index(name="Bug Count")
)

# -----------------------------
# Bug Severity Summary
# -----------------------------
bug_severity_summary = (
    bugs.groupby("severity")
        .size()
        .reset_index(name="Bug Count")
)

# -----------------------------
# Export CSV Files
# -----------------------------
bug_status_summary.to_csv(
    OUTPUT_DIR / "bug_status_summary.csv",
    index=False
)

bug_severity_summary.to_csv(
    OUTPUT_DIR / "bug_severity_summary.csv",
    index=False
)

print("Bug summary files created successfully!")
print()
print(bug_status_summary)
print()
print(bug_severity_summary)