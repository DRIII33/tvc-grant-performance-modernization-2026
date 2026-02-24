#INSTALL PACKAGES
!pip install pandas numpy


import pandas as pd
import numpy as np
import os

np.random.seed(42)

grantee_count = 50
programs = ["Mental Health", "Financial Assistance", "Transportation"]
counties = ["Harris", "Dallas", "Bexar", "Tarrant", "Travis"]

grantees = pd.DataFrame({
    "grantee_id": [f"G{i:03}" for i in range(1, grantee_count+1)],
    "county": np.random.choice(counties, grantee_count),
    "program_type": np.random.choice(programs, grantee_count)
})

dates = pd.date_range("2025-01-01", "2025-12-01", freq="MS")

records = []

for _, row in grantees.iterrows():
    for date in dates:
        veterans = np.random.poisson(lam=80)
        benchmark = 75
        funds = veterans * np.random.uniform(150, 400)

        records.append([
            row["grantee_id"],
            row["county"],
            row["program_type"],
            date,
            veterans,
            benchmark,
            round(funds, 2)
        ])

performance = pd.DataFrame(records, columns=[
    "grantee_id",
    "county",
    "program_type",
    "reporting_month",
    "veterans_served",
    "benchmark_target",
    "funds_expended"
])

# Create the 'raw' directory if it doesn't exist
os.makedirs('../raw', exist_ok=True)

performance.to_csv("../raw/performance_reports.csv", index=False)
