import pytest
from src.decorators import timer, retry, cache2

def test_timer_returns_result():
    """Timer decorator should not affect return value."""
    # ARRANGE
    actual = 0
    expected = 5 + 5
    @timer
    def func(a, b):
        return a + b
    
    # ACT
    actual = func(5, 5)
    # ASSERT
    assert actual == expected

def test_retry_succeeds_eventually():
    """Retry should succeed if function works within attempts."""
    # ARRANGE
    actual = 0
    expected = 10
    expected2 = None
    
    @retry(1, 0.5)
    def func1(a, b):
        return a + b
    
    @retry(0, 0.5)
    def func2(a, b):
        return a + b
    # ACT
    actual = func1(5, 5)
    actual2 = func2(5, 5)

    # ASSERT
    assert actual == expected
    assert actual2 == expected2

def test_cache_returns_cached_value():
    """Cache should return same value without recomputing."""
    # ARRANGE
    expected = 1
    actual = 0

    # ACT
    @cache2(10)
    def func(a, b):
        return a + b
    
    for i in range(3):
        func(5, 5).cache_info()
        actual += 1
    # ASSERT
    assert actual == expected

def test_cache_info_tracks_hits():
    """Cache info should track hits and misses."""
    pass
