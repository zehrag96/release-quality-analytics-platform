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
bugs = pd.read_csv(POWERBI_DIR / "Bugs.csv")
testcases = pd.read_csv(POWERBI_DIR / "TestCases.csv")
releases = pd.read_csv(POWERBI_DIR / "Releases.csv")

# -----------------------------------
# Bug Count per Release
# -----------------------------------
bug_summary = (
    bugs.groupby("release_id")
        .size()
        .reset_index(name="Total Bugs")
)

# -----------------------------------
# Test Count per Release
# -----------------------------------
test_summary = (
    testcases.groupby("release_id")
             .size()
             .reset_index(name="Total Test Cases")
)

# -----------------------------------
# Merge
# -----------------------------------
summary = releases.merge(
    bug_summary,
    on="release_id",
    how="left"
)

summary = summary.merge(
    test_summary,
    on="release_id",
    how="left"
)

# Fill missing values
summary["Total Bugs"] = summary["Total Bugs"].fillna(0).astype(int)
summary["Total Test Cases"] = summary["Total Test Cases"].fillna(0).astype(int)

# -----------------------------------
# Bug/Test Ratio
# -----------------------------------
summary["Bug per Test"] = (
    summary["Total Bugs"] /
    summary["Total Test Cases"].replace(0, pd.NA)
)

summary["Bug per Test"] = (
    summary["Bug per Test"]
    .fillna(0)
    .astype(float)
    .round(2)
)

# -----------------------------------
# Final Output
# -----------------------------------
summary = summary[[
    "release_name",
    "Total Bugs",
    "Total Test Cases",
    "Bug per Test"
]]

summary.rename(columns={
    "release_name": "Release"
}, inplace=True)

summary.to_csv(
    OUTPUT_DIR / "release_health.csv",
    index=False,
    float_format="%.2f"
)

print(summary)
print("\nrelease_health.csv created successfully.")