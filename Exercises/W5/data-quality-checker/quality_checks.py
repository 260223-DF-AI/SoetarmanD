import pandas as pd

def check_nulls(df: pd.DataFrame) -> int:
    """Check for null values in each column."""
    # add edge case checks (ie: empty dataframe, missing columns)
    if df.empty:
        pass

    if not all(col in df.columns for col in ['order_id', 'customer_id', 'order_date', 'product_name', 'category', 'quantity', 'unit_price', 'region']):
        pass

    # check for null values in each column of the given dataframe
    null_counts = df.isnull().sum()
    return null_counts


def check_duplicates(df: pd.DataFrame, key_column: str) -> int:
    """Find duplicate rows based on a key column."""
    # add edge case checks (ie: empty dataframe, missing columns)
    if df.empty:
        raise ValueError("DataFrame is empty.")
    
    # check for duplicate rows in the given dataframe based on the key column
    duplicates = df.duplicated(subset=[key_column], keep=False).sum()
    return duplicates

def check_negative_values(df: pd.DataFrame, key_column: str) -> int:
    """Flag negative values in specified numeric columns."""
    # add edge case checks (ie: empty dataframe, missing columns)
    if df.empty:
        raise ValueError("DataFrame is empty.")
    if not all(col in df.columns for col in ['order_id', 'customer_id', 'order_date', 'product_name', 'category', 'quantity', 'unit_price', 'region']):
        pass
    # check for negative values in the specified numeric columns of the given dataframe
    negative_values = (df[key_column] < 0).sum()
    return negative_values

def check_future_dates(df: pd.DataFrame, date_column: str) -> int:
    """Check for dates in the future."""
    # add edge case checks (ie: empty dataframe, missing columns)
    if df.empty:
        raise ValueError("DataFrame is empty.")

    if not all(col in df.columns for col in ['order_id', 'customer_id', 'order_date', 'product_name', 'category', 'quantity', 'unit_price', 'region']):
        pass
    
    # check for future dates in the specified date column of the given dataframe
    future_dates = (pd.to_datetime(df[date_column]) > pd.Timestamp.now()).sum()
    return future_dates

def check_email_format(df: pd.DataFrame, email_column: str) -> int:
    """Validate email format in the specified column."""
    # add edge case checks (ie: empty dataframe, missing columns)
    if df.empty:
        raise ValueError("DataFrame is empty.")

    if not all(col in df.columns for col in ['order_id', 'customer_id', 'order_date', 'product_name', 'category', 'quantity', 'unit_price', 'region']):
        pass
    
    # check for valid emails and return the amount of invalid emails
    invalid_emails = (df[email_column].str.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$') == False).sum()
    return invalid_emails
