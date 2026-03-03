from src.exceptions import FileProcessingError
from src.logger import setup_logger

def read_csv_file(filepath):
    """
    Read a CSV file and return a list of dictionaries.
    
    Should handle:
    - FileNotFoundError
    - UnicodeDecodeError (try utf-8, then latin-1)
    - Empty files
    
    Returns: List of dictionaries (one per row)
    Raises: FileProcessingError with descriptive message
    """
    logger = setup_logger(__name__)
    logger.info("read_csv_file started")
    try:
        list = []
        with open(filepath, "r", encoding='utf-8') as f:      # attempt to open file
            for i, line in enumerate(f):
                if i == 0:
                    stripped_line = line.rstrip('\n')
                    column_names = stripped_line.split(",")      # first line of csv file contains column names
                    date = column_names[0]
                    store_id = column_names[1]
                    product = column_names[2]
                    quantity = column_names[3]
                    price = column_names[4]
                else:
                    stripped_line = line.rstrip('\n')
                    entry = stripped_line.split(",")
                    try: list.append({
                        date : entry[0],
                        store_id : entry[1],
                        product : entry[2],
                        quantity : entry[3],
                        price : entry[4],
                    })
                    except IndexError as e:
                        logger.error("Index Error", e)
                        print(e)
    except UnicodeDecodeError as e:         # unicode error
        logger.error("Unicode Error", e)
        try:                                # try with latin-1
            with open(filepath, "r", encoding='latin-1') as f:      # attempt to open file
                for i, line in enumerate(f):
                    if i == 0:
                        stripped_line = line.rstrip('\n')
                        column_names = stripped_line.split(",")      # first line of csv file contains column names
                        date = column_names[0]
                        store_id = column_names[1]
                        product = column_names[2]
                        quantity = column_names[3]
                        price = column_names[4]
                    else:
                        stripped_line = line.rstrip('\n')
                        entry = stripped_line.split(",")
                        try: list.append({
                            date : entry[0],
                            store_id : entry[1],
                            product : entry[2],
                            quantity : entry[3],
                            price : entry[4],
                        })
                        except IndexError as e:
                            logger.error("Index Error", e)
                            print(e)
        except FileNotFoundError as e:          # file not found after attempting to open
            print(FileProcessingError)
    except FileNotFoundError as e:          # file not found after attempting to open
        print(FileProcessingError)
    logger.info("read_csv_file finished")
    return list

# Requirements:
# - Use context managers (`with` statement)
# - Log errors before re-raising
# - Return empty list for empty files (not an error)

print(read_csv_file("data/sample_sales.csv"))