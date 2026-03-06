"""Validate csv file for accurate records"""

from src.file_reader import read_csv_file
from src.exceptions import InvalidDataError, MissingFieldError
from src.logger import setup_logger
from datetime import datetime

def validate_date(date_string, logger, date_format='%Y-%m-%d'):
    """helper function to validate date"""
    try:
        datetime.strptime(date_string, date_format)
        return True
    except ValueError as e:
        logger.error("Invalid date")
        raise InvalidDataError("Invalid date format/date")

def validate_quantity(quantity, logger):
    """helper function to validate quantity"""
    if type(quantity) is not int:   # failed, unsupported data type
        logger.error("Not an integer", InvalidDataError)
        raise InvalidDataError("Quantity must be integer")
    if quantity <= 0:   # failed, given negative integer
        logger.error("Negative integer given")
        raise InvalidDataError("Quantity must be a positive integer")
    return quantity     # valid quantity

def validate_price(price, logger):
    """helper function to validate price"""
    if not isinstance(price, (int, float)):     # failed, unsupported data type
        logger.error("Not an integer or float", InvalidDataError)
        raise InvalidDataError("Price must be float or integer")
    if price <= 0:      # failed, given a negative number
        logger.error("Negative number given", InvalidDataError)
        raise InvalidDataError("Price must be positive number")
    return price

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
    logger.info(f"validate_sales_record started at line {line_number}")
    errors = []
    required_fields = ['date', 'store_id', 'product', 'quantity', 'price']      # check has all fields
    missing = [field for field in required_fields if field not in record or record[field] is None or str(record[field]).strip() == '']  # checks records for missing required fields
    if missing:
        errors.append(f"missing field: {missing}")
        logger.error(f"Line {line_number}: missing field {missing}")
        raise MissingFieldError(f"Line {line_number}: Missing required field")
    try:    # validate date
        validate_date(record['date'], logger)
    except InvalidDataError as e:
        errors.append(f"date: {e}")
    try:    # validate quantity
        record['quantity'] = int(record['quantity'])
        validate_quantity(record['quantity'], logger)
    except (ValueError, TypeError):
        errors.append("Quantity must be an integer")
    except InvalidDataError as e:
        errors.append(f"Quantity: {e}")
    try:    # validate price
        record['price'] = float(record['price'])
        validate_price(record['price'], logger)
    except (ValueError, TypeError):
        errors.append("Price must be a number")
    except InvalidDataError as e:
        errors.append(f"Price: {e}")
    if errors:  # errors found in data, raise
        error_summary = f"Line {line_number}: Validation failed - ".join(errors)
        logger.error(error_summary)
        raise InvalidDataError(error_summary)
    logger.info(f"Line {line_number}: record validated")
    return record

def validate_all_records(records):
    """
    Validate all records, collecting errors instead of stopping.
    
    Returns: Tuple of (valid_records, error_list)
    """
    logger = setup_logger(__name__)
    logger.info("Starting validate_all_records")

    valid_records = []
    error_list = []

    for line_number, record in enumerate(records):
        try:
            validated = validate_sales_record(record, line_number)
            valid_records.append(validated)
        except (InvalidDataError, MissingFieldError) as e:
            error_list.append({
                'line_number' : line_number,
                'record' : record,
                'error' : str(e)
            })
    logger.info("Ending validate_all_records")
    return valid_records, error_list

list = read_csv_file("data/sample_sales.csv")
print(validate_all_records(list))