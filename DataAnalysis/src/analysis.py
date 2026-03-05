# Task 1: Data loading and data exploration (load_data and explore_data)

import pandas as pd

def load_data(filepath):
    """
    Load the orders dataset.
    - Parse dates correctly
    - Handle missing values
    - Return a clean DataFrame
    """
    data: pd.DataFrame = pd.read_csv(filepath)
    return data

df = load_data("data/sample_data.csv")

def explore_data(df):
    """
    Print basic statistics about the dataset:
    - Shape (rows, columns)
    - Data types
    - Missing value counts
    - Basic statistics for numeric columns
    - Date range covered
    """
    print(f"Number of rows: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}")
    print(f"Number of missing values: {df.isna().sum().sum()}") # will take the sum of every missing value of every column
    print(f"Total Unit Prices: {df['unit_price'].sum()}")
    print(f"Average price of products: {df['unit_price'].mean()}")
    print(f"Date Range: {df['order_date'].min()} to {df['order_date'].max()}")

explore_data(df)

# Task 2 Data cleaning and data transformation (clean_data and add_time_features)
def clean_data(df):
    """
    Clean the dataset:
    - Remove duplicates
    - Fill or drop missing values (document your strategy)
    - Standardize text columns (strip whitespace, consistent case)
    - Add calculated columns: 'total_amount' = quantity * unit_price
    """
    df_cleaned = df.drop_duplicates()      # drop duplicates
    df_cleaned = df_cleaned.dropna(how='all')        # drop all rows with all missing values
    df_cleaned['order_id'] = df['order_id'].fillna("N/A")   # fill missing values with default of NA
    df_cleaned['customer_id'] = df['customer_id'].fillna("N/A")
    df_cleaned['product_name'] = df['product_name'].fillna("N/A")
    df_cleaned['category'] = df['category'].fillna("N/A")
    df_cleaned['quantity'] = df['quantity'].fillna(0)           # fill missing values with default of 0
    df_cleaned['unit_price'] = df['unit_price'].fillna(0)
    df_cleaned['region'] = df['region'].fillna("N/A")
    df_cleaned = df_cleaned.dropna()                            # drop rows if any missing values were not filled
    return df_cleaned

cleaned = clean_data(df)
print()
explore_data(cleaned)
print()
print(cleaned)

def add_time_features(df):
    """
    Add time-based features:
    - day_of_week (0=Monday, 6=Sunday)
    - month
    - quarter
    - is_weekend (boolean)
    """
    df['order_date'] = df.DataFrame({'order_date': pd.to_datetime([df['order_date']])})
    df['day_name'] = df['order_date'].dt.day_name()
    return df

print()
time = add_time_features(cleaned)
print(time)

def sales_by_category(df):
    """
    Calculate total sales and order count by category.
    Returns: DataFrame with columns [category, total_sales, order_count, avg_order_value]
    Sorted by total_sales descending.
    """
    pass

def sales_by_region(df):
    """
    Calculate total sales by region.
    Returns: DataFrame with columns [region, total_sales, percentage_of_total]
    """
    pass

def top_products(df, n=10):
    """
    Find top N products by total sales.
    Returns: DataFrame with columns [product_name, category, total_sales, units_sold]
    """
    pass

def daily_sales_trend(df):
    """
    Calculate daily sales totals.
    Returns: DataFrame with columns [date, total_sales, order_count]
    """
    pass

def customer_analysis(df):
    """
    Analyze customer purchasing behavior.
    Returns: DataFrame with columns [customer_id, total_spent, order_count, 
             avg_order_value, favorite_category]
    """
    pass

def weekend_vs_weekday(df):
    """
    Compare weekend vs weekday sales.
    Returns: Dict with weekend and weekday total sales and percentages.
    """
    pass
