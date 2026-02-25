# budget_calculator.py - Personal Finance Calculator
# Starter code for e002-exercise-python-intro

"""
Personal Finance Calculator
---------------------------
This program helps users understand their monthly budget by collecting
income and expense information and displaying a formatted summary.

Complete the TODO sections below to finish the program.
"""

# print("=" * 44)
# print("       PERSONAL FINANCE CALCULATOR")
# print("=" * 44)
# print()

# =============================================================================
# DONE: Task 1 - Collect User Information
# =============================================================================
# Get the user's name
# Example: name = input("Enter your name: ")
name = input("Enter your name: ")


# Get monthly income (as a float)
# Remember to convert the input to a float!
income = float(input("Enter your monthly income: "))
while income <= 0:
    print("Error, invalid income (cannot be negative)")
    income = float(input("Please enter monthly income again: "))

# Get expenses for at least 4 categories:
# - rent: Rent/Housing
# - utilities: Utilities (electric, water, internet)
# - food: Food/Groceries
# - transportation: Transportation (gas, public transit)
rent = float(input("Enter your monthly rent amount: "))
utilities = float(input("Enter your monthly utilities expenses: "))
food = float(input("Enter your monthly food expenses: "))
transportation = float(input("Enter your monthly transportation expenses: "))

if rent < 0:
    rent = 0
if utilities < 0:
    utilities = 0
if food < 0:
    food = 0
if transportation < 0:
    transportation = 0

# =============================================================================
# DONE: Task 2 - Perform Calculations
# =============================================================================
# Calculate total expenses
expenses = rent + utilities + food + transportation

# Calculate remaining balance (income - expenses)
balance = income - expenses

# Calculate savings rate as a percentage
# Formula: (balance / income) * 100
savings = (balance / income) * 100

# Determine financial status
# - If balance > 0: status = "in the green"
# - If balance < 0: status = "in the red"
# - If balance == 0: status = "breaking even"
status = ""
if balance > 0:
    status = "in the green"
elif balance < 0:
    status = "in the red"
else:
    status = "breaking even"

# =============================================================================
# TODO: Task 3 - Display Results
# =============================================================================
# Create a formatted budget report
# Use f-strings for formatting
# Dollar amounts should show 2 decimal places: f"${amount:.2f}"
# Percentages should show 1 decimal place: f"{rate:.1f}%"

# Example structure:
print("=" * 44)
print("       MONTHLY BUDGET REPORT")
print("=" * 44)
if name == "":
    name = "Anonymous"
    print(f"Name: {name}")
else:
    print(f"Name: {name}")
# ... continue building the report ...
print(f"Monthly Income: ${income:.2f}")
print(f"EXPENSES:")
print(f"  - Rent/Housing: ${(rent/income) * 100:.1f}% of income")
print(f"  - Utilities: ${(utilities/income) * 100:.1f}% of income")
print(f"  - Food: ${(food/income) * 100:.1f}% of income")
print(f"  - Transportation: ${(transportation/income) * 100:.1f}% of income")
print("-" * 44)
print(f"Total Expenses: ${expenses:.2f}")
print(f"Remaining Balance: ${balance:.2f}")
print(f"Savings Rate: {savings:.1f}%")
print()
print(f"Status: {status}")
print("=" * 44)
# =============================================================================
# DONE: Task 4 - Add Validation (Optional Enhancement)
# =============================================================================
# Add these validations before calculations:
# - If name is empty, use "Anonymous"
# - If income is <= 0, print error and exit
# - If any expense is negative, treat as 0


# =============================================================================
# STRETCH GOAL: Category Percentages
# =============================================================================
# Add a section showing what percentage each expense is of total income
# Example: print(f"  - Rent/Housing:    {(rent/income)*100:.1f}% of income")
