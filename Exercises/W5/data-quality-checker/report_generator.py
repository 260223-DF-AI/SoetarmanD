"""
1. Takes the results from all quality checks
2. Generates a Markdown report with:
   - Header with timestamp
   - Summary statistics (total rows, total issues found)
   - Detailed results for each check
   - A severity rating (PASS / WARNING / FAIL)
   - Recommendations for each issue found
   """

import datetime
import pandas as pd
import numpy as np

from quality_checks import check_nulls, check_duplicates, check_negative_values, check_future_dates, check_email_format

def generate_report(results):
    # call all quality checks and store the results in a dictionary
    quality_checks = check_nulls(results)
    quality_checks += check_duplicates(results, 'order_id')
    quality_checks += check_negative_values(results, 'amount')
    quality_checks += check_future_dates(results, 'order_date')
    quality_checks += check_email_format(results, 'email')

    # generate a Markdown report listed out in table format in the markdown file
    report = f"# Data Quality Report\n\n"
    report += f"**Generated**: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    report += f"## Summary\n\n"
    report += f"**Total Rows**: {results.shape[0]}\n"
    # sum all of the issues found in each quality check
    report += f"**Total Issues**: {quality_checks}\n\n"
    # generate a table with the results of each quality check
    report += f"## Quality Checks\n\n"
    report += f"| Check | Total Issues | Severity |\n"
    report += f"| --- | --- | --- |\n"
    # for check, issues in quality_checks.items():
    #     severity = 'PASS' if issues == 0 else 'WARNING' if issues < results.shape[0] else 'FAIL'
    #     report += f"| {check} | {sum(issues)} | {severity} |\n"
    report += f"## Details\n\n"
    # generate recommendations for each quality check
    recommendations = {
        'check_nulls': 'Remove rows with null values.',
        'check_duplicates': 'Remove duplicate rows.',
        'check_negative_values': 'Remove rows with negative values.',
        'check_future_dates': 'Remove rows with future dates.',
        'check_email_format': 'Fix email format.'
    }
    # for check, issues in quality_checks.items():
        # report += f"### {check}\n\n"
        # report += f"**Total Issues**: {sum(issues)}\n\n"
        # report += f"**Issues Found**: {issues}\n\n"
        # report += f"**Recommendations**: {recommendations[check]}\n\n"
    return report