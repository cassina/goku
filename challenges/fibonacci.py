"""
This module provides implementations of the Fibonacci sequence calculation using three different methods:
1. Recursive calculation without memoization.
2. Recursive calculation with memoization.
3. Recursive calculation with Least Recently Used (LRU) cache for memoization.

The module contains the following functions:
- fibonacci_with_memo: Computes the nth Fibonacci number using memoization.
- fibonacci_no_memo: Computes the nth Fibonacci number without memoization.
- fibonacci_with_lru_cache: Computes the nth Fibonacci number using LRU cache for memoization.
- simple_tests: Conducts basic tests to ensure the correctness of each Fibonacci function.
- test_fibonacci: Compares the execution times of the three Fibonacci implementations.
- print_table: Displays the execution times of the three Fibonacci implementations in a tabular format.

The module is designed to analyze and compare the performance of different Fibonacci sequence calculation methods.
When executed as a script, it runs simple tests to verify the correctness of the Fibonacci functions,
calculates the 30th Fibonacci number using each method, and displays the execution times in a sorted table.
"""
import time
from functools import lru_cache
from utils import print_table, time_function


def fibonacci_with_memo(n, memo={}):
    """
    Calculates the nth Fibonacci number using memoization.

    Parameters:
        n (int): The index of the Fibonacci number to calculate.
        memo (dict, optional): A dictionary to store previously calculated Fibonacci numbers.
            Defaults to an empty dictionary.

    Returns:
        int: The nth Fibonacci number.

    Complexity:
        Time: O(n)
        Space: O(n)
    """
    if n < 2:
        return n
    elif n not in memo:
        memo[n] = fibonacci_with_memo(n - 2, memo) + fibonacci_with_memo(n - 1, memo)
    return memo[n]


def fibonacci_no_memo(n):
    """
    Calculates the nth Fibonacci number without memoization.

    Parameters:
        n (int): The index of the Fibonacci number to calculate.

    Returns:
        int: The nth Fibonacci number.

    Complexity:
        Time: O(2^n)
        Space: O(n)
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_no_memo(n - 2) + fibonacci_no_memo(n - 1)


@lru_cache(maxsize=None)
def fibonacci_with_lru_cache(n):
    """
    Calculates the nth Fibonacci number using the Least Recently Used (LRU) cache for memoization.

    Parameters:
        n (int): The index of the Fibonacci number to calculate.

    Returns:
        int: The nth Fibonacci number.

    Complexity:
        Time: O(n)
        Space: O(n)
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_with_lru_cache(n - 1) + fibonacci_with_lru_cache(n - 2)


def simple_tests():
    """Performs simple tests to ensure each Fibonacci function is working correctly."""
    for func in (fibonacci_with_memo, fibonacci_no_memo, fibonacci_with_lru_cache):
        assert func(0) == 0
        assert func(1) == 1
        assert func(2) == 1
        assert func(3) == 2
        assert func(10) == 55
    print("All tests passed.")


def test_fibonacci(n=30):
    """
    Tests and compares the execution time of three different implementations of the Fibonacci sequence.

    Parameters:
        n (int, optional): The index of the Fibonacci number to calculate.
            Defaults to 30.

    Returns:
        list: A list of tuples containing the method names and execution times (in seconds) of the three implementations.
    """
    timings = []
    for func in [fibonacci_no_memo, fibonacci_with_memo, fibonacci_with_lru_cache]:
        timings.append(time_function(func, n))

    # Sort the timings by execution time (from fastest to slowest)
    timings.sort(key=lambda x: x[1])

    return timings


if __name__ == '__main__':
    simple_tests()  # Run simple tests
    target = 30
    print(f"Calculating Fibonacci {target}")
    table_timings = test_fibonacci(target)
    print_table(table_timings)
