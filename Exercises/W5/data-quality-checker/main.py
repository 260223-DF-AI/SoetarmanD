# 1. Reads the CSV file
# 2. Runs all quality checks
# 3. Generates the report
# 4. Saves it to `output/report.md`
# 5. Prints a summary to the console

import pandas as pd
from quality_checks import check_nulls, check_duplicates, check_negative_values, check_future_dates, check_email_format
from report_generator import generate_report

# read the CSV file into a pandas DataFrame
df = pd.read_csv('sample_data.csv')

# generate a Markdown report with the results of all quality checks
report = generate_report(df)

# save the report to a file
with open('output/report.md', 'w') as f:
    f.write(report)

# print a summary to the console
print(report)
