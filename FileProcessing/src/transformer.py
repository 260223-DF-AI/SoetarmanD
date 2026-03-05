def calculate_totals(records):
    """
    Calculate line totals (quantity * price) for each record.
    Returns: Records with added 'total' field
    """
    for record in records:      # assumes already valid records
        total = record['quantity'] * record['price']
        record['total_sales'] = total
    return records

def aggregate_by_store(records):
    """
    Aggregate sales by store_id.
    Returns: Dict mapping store_id to total sales
    """
    sales = {}
    for record in records:      # assumes already valid records
        sales[record['store_id']] = record['total_sales']
    return sales

def aggregate_by_product(records):
    """
    Aggregate sales by product.
    Returns: Dict mapping product to total quantity sold
    """
    pass
