from functools import wraps, cache
import time
import logging

logger = logging.getLogger(__name__)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('app.log')

fomatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

console_handler.setFormatter(fomatter)
file_handler.setFormatter(fomatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


def timer(func):
    """
    Measure and print function execution time.
    
    Usage:
        @timer
        def slow_function():
            time.sleep(1)
    
    Output: "slow_function took 1.0023 seconds"
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

def logger(func):
    """
    Log function calls with arguments and return value.
    
    Usage:
        @logger
        def add(a, b):
            return a + b
        
        add(2, 3)
    
    Output:
        "Calling add(2, 3)"
        "add returned 5"
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.warning(f"Calling {func.__name__}({func.args})")
        result = func(*args, **kwargs)
        logger.warning(f"{func.__name__} returned {result}")
        return result
    return wrapper

def retry(max_attempts=3, delay=1, exceptions=(Exception,)):
    """
    Retry a function on failure.
    
    Args:
        max_attempts: Maximum number of retry attempts
        delay: Seconds to wait between retries
        exceptions: Tuple of exceptions to catch
    
    Usage:
        @retry(max_attempts=3, delay=0.5)
        def flaky_api_call():
            # might fail sometimes
            pass
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed, retrying...")
                    time.sleep(delay)
        return wrapper
    return decorator

def cache2(max_size=128):
    """
    Cache function results.
    Similar to lru_cache but with visible cache inspection.
    
    Usage:
        @cache(max_size=100)
        def expensive_computation(x):
            return x ** 2
        
        expensive_computation(5)  # Computes
        expensive_computation(5)  # Returns cached
        
        # Inspect cache
        expensive_computation.cache_info()
        expensive_computation.cache_clear()
    """
    @cache
    def decorator(func):
        cached_results = {}
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args in cached_results:
                return cached_results[args]
            result = func(*args)
            cached_results[args] = result
            return result
        return wrapper
    return decorator