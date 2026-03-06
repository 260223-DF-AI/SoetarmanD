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
    - Add calculated columns: 'total_sales' = quantity * unit_price
    """
    df_cleaned = df.copy()  # copy data to not overwrite starting data

    df_cleaned = df_cleaned.drop_duplicates()      # drop duplicates
    df_cleaned = df_cleaned.dropna(how='all')        # drop rows with all missing values
    df_cleaned['order_id'] = df_cleaned['order_id'].fillna("N/A")   # fill missing values with default of NA
    df_cleaned['customer_id'] = df_cleaned['customer_id'].fillna("N/A")
    df_cleaned['product_name'] = df_cleaned['product_name'].fillna("N/A")
    df_cleaned['category'] = df_cleaned['category'].fillna("N/A")
    df_cleaned['quantity'] = df_cleaned['quantity'].fillna(0)           # fill missing values with default of 0
    df_cleaned['unit_price'] = df_cleaned['unit_price'].fillna(0)
    df_cleaned['region'] = df_cleaned['region'].fillna("N/A")
    df_cleaned = df_cleaned.dropna()                            # drop rows if any missing values were not filled

    text_cols = ['order_id', 'customer_id', 'product_name', 'category', 'region']   # standardize text columns: strip whitespace, all lowercase
    for col in text_cols:
        df_cleaned[col] = df_cleaned[col].astype(str).str.strip().str.lower()

    df_cleaned['order_date'] = pd.to_datetime(df_cleaned['order_date']) # standardize date
    df_cleaned['quantity'] = df_cleaned['quantity'].astype(int)         # standardize quantity
    df_cleaned['unit_price'] = df_cleaned['unit_price'].astype(float)   # standardize unit price
    
    df_cleaned['total_sales'] = df_cleaned['quantity'] * df_cleaned['unit_price']  # create total_sales column

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
    new_df = df.copy()
    new_df['day_of week'] = new_df['order_date'].dt.dayofweek
    new_df['month'] = new_df['order_date'].dt.month
    new_df['quarter'] = new_df['order_date'].dt.quarter
    new_df['is_weekend'] = (new_df['order_date'].dt.dayofweek >= 5)
    return new_df

print()
time = add_time_features(cleaned)
print(time)

def sales_by_category(df):
    """
    Calculate total sales and order count by category.
    Returns: DataFrame with columns [category, total_sales, order_count, avg_order_value]
    Sorted by total_sales descending.
    """
    df_sales_by_category = df.groupby("category")
    return df_sales_by_category

print(sales_by_category(cleaned))

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
