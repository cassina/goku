# Practice a fibonacci sequence and recursion
import time


def fibonacci_with_memo(n, memo={}):
    if n < 2:
        return n
    elif n not in memo:
        memo[n] = fibonacci_with_memo(n - 2) + fibonacci_with_memo(n - 1)
    return memo[n]


# O(2^n) time | O(n) space
def fibonacci_no_memo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_no_memo(n - 2) + fibonacci_no_memo(n - 1)


# O(n) time | O(n) space
def test_fibonacci(n=40):
    start_time = time.time()
    fibonacci_no_memo(n)  # The 30th Fibonacci number
    end_time = time.time()
    no_memo_time = end_time - start_time

    start_time = time.time()
    fibonacci_with_memo(n)  # The 30th Fibonacci number
    end_time = time.time()
    with_memo_time = end_time - start_time

    return no_memo_time, with_memo_time


if __name__ == '__main__':
    assert fibonacci_with_memo(1) == 1, 'Error testing fib(1)'
    assert fibonacci_with_memo(2) == 1, 'Error testing fib(2)'
    assert fibonacci_with_memo(3) == 2, 'Error testing fib(3)'
    assert fibonacci_with_memo(4) == 3, 'Error testing fib(4)'
    assert fibonacci_with_memo(5) == 5, 'Error testing fib(5)'
    assert fibonacci_with_memo(6) == 8, 'Error testing fib(6)'
    assert fibonacci_with_memo(10) == 55, 'Error testing fib(10)'
    assert fibonacci_with_memo(15) == 610, 'Error testing fib(15)'
    print(f'All tests passed for the {fibonacci_with_memo.__name__} function!')

    times = test_fibonacci()
    print(f'Fibonacci without memoization took {times[0]} seconds')
    print(f'Fibonacci with memoization took {times[1]} seconds')
