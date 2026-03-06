def read_lines(filepath, encoding='utf-8'):
    """
    Yield lines from a file one at a time.
    - Strip whitespace from each line
    - Skip empty lines
    - Handle encoding errors gracefully
    
    Usage:
        for line in read_lines('large_file.txt'):
            process(line)
    """
    try:
        with open(filepath, "r", encoding) as f:
            for line in f:
                if line.strip():
                    continue
                yield line.strip(" ")
    except UnicodeDecodeError as e:
        print(f"File not utf-8")

def chunk(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

def batch(iterable, size):
    """
    Yield items in batches of the specified size.
    
    Usage:
        list(batch([1,2,3,4,5,6,7], 3))
        # [[1,2,3], [4,5,6], [7]]
    """
    for group in chunk(iterable, size):
        yield group
    

print(list(batch([1,2,3,4,5,6,7], 3)))

def filter_by(iterable, predicate):
    """
    Yield items that match the predicate.
    
    Usage:
        evens = filter_by(range(10), lambda x: x % 2 == 0)
        list(evens)  # [0, 2, 4, 6, 8]
    """
    pass
