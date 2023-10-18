"""
This module is designed to solve the challenge of calculating the super digit of a given number.
The challenge is as follows:
Given an integer n, we need to find the super digit of the number obtained by concatenating n to itself k times.
The super digit of a number is obtained as follows:
- If the number has only one digit, then that number is the super digit.
- Otherwise, the super digit of the number is equal to the super digit of the sum of the digits of the number.

Example:
    Input: n = '148', k = 3
    The number obtained by concatenating '148' three times is '148148148'.
    The sum of the digits of '148148148' is 1 + 4 + 8 + 1 + 4 + 8 + 1 + 4 + 8 = 39.
    The sum of the digits of '39' is 3 + 9 = 12.
    The sum of the digits of '12' is 1 + 2 = 3.
    Since 3 has only one digit, the super digit of '148148148' is 3.

The module provides implementations of the super digit calculation using three different methods:
1. Recursive calculation with string concatenation and individual digit sum.
2. Iterative calculation with accumulated sum.
3. Recursive calculation with accumulated sum.

The module contains the following functions:
- super_digit_1: Computes the super digit using string concatenation and individual digit sum.
- super_digit_2: Computes the super digit using iterative calculation with accumulated sum.
- super_digit_3: Computes the super digit using recursive calculation with accumulated sum.
- simple_tests: Conducts basic tests to ensure the correctness of each super digit function.
- test_super_digit: Compares the execution times of the three super digit implementations.
- print_table: Displays the execution times of the three super digit implementations in a tabular format.

When executed as a script, it runs simple tests to verify the correctness of the super digit functions,
calculates the super digit for a specified input using each method, and displays the execution times in a sorted table.
"""
from utils import print_table
from utils import time_function


def super_digit_concatenation(n, k):
    """
    Calculates the super digit using string concatenation and individual digit sum.

    Parameters:
        n (str): The base number as a string.
        k (int): The repetition factor.

    Returns:
        str: The super digit.

    Complexity:
        Time: O(m * k) where m is the number of digits in n
        Space: O(m * k)
    """
    p = str(abs(int(n))) * k if k > 0 else str(abs(int(n)))
    count = sum(int(char) for char in p)
    while count >= 10:
        count = sum(int(char) for char in str(count))
    return str(count)


def super_digit_iteration(n, k):
    """
    Calculates the super digit using iterative calculation with accumulated sum.

    Parameters:
        n (str): The base number as a string.
        k (int): The repetition factor.

    Returns:
        str: The super digit.

    Complexity:
        Time: O(m + log(count)) where m is the number of digits in n
        Space: O(m)
    """
    d = str(k * sum(map(int, n)))
    while len(d) > 1:
        d = str(sum(map(int, d)))
    return d


def super_digit_recursive(n, k=1):
    """
    Calculates the super digit using recursive calculation with accumulated sum.

    Parameters:
        n (str): The base number as a string.
        k (int, optional): The repetition factor. Defaults to 1.

    Returns:
        str: The super digit.

    Complexity:
        Time: O(log(count)) in best case, O(m + log(count)) in worst case where m is the number of digits in n
        Space: O(log(count))
    """
    n = n * k
    if len(n) == 1:
        return n
    else:
        return super_digit_recursive(str(sum(int(char) for char in n)))


def simple_tests():
    """Performs simple tests to ensure each super digit function is working correctly."""
    for func in (super_digit_concatenation, super_digit_iteration, super_digit_recursive):
        assert func('148', 3) == '3'
        assert func('9875', 4) == '8'
        assert func('123', 3) == '9'
    print("All tests passed.")


def test_super_digit(n, k):
    """
    Tests and compares the execution time of three different implementations of the super digit calculation.

    Parameters:
        n (str): The base number as a string.
        k (int): The repetition factor.

    Returns:
        list: A list of tuples containing the method names and execution times (in seconds) of the three implementations.
    """
    timings = []
    for func in [super_digit_recursive, super_digit_iteration, super_digit_concatenation]:
        timings.append(time_function(func, n, k))

    # Sort the timings by execution time (from fastest to slowest)
    timings.sort(key=lambda x: x[1])

    return timings


if __name__ == '__main__':
    simple_tests()  # Run simple tests
    target_n = '740495400969422744624637574722784'
    target_k = 10000
    print(f"Calculating super digit of {target_n} repeated {target_k} times")
    table_timings = test_super_digit(target_n, target_k)
    print_table(table_timings)
