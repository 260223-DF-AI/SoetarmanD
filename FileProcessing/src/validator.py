"""Validate csv file for accurate records"""

from src.exceptions import InvalidDataError, MissingFieldError
from src.logger import setup_logger

def validate_sales_record(record, line_number):
    """
    Validate a single sales record.
    
    Required fields: date, store_id, product, quantity, price
    Validation rules:
    - date must be in YYYY-MM-DD format
    - quantity must be a positive integer
    - price must be a positive number
    
    Returns: Validated record with converted types
    Raises: InvalidDataError or MissingFieldError
    """
    logger = setup_logger(__name__)
    logger.info("validate_sales_record started")

    logger.info("validate_sales_record ended")
    return record
    pass

def validate_all_records(records):
    """
    Validate all records, collecting errors instead of stopping.
    
    Returns: Tuple of (valid_records, error_list)
    """
    pass
