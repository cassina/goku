from prettytable import PrettyTable
import time


def print_table(timings):
    table = PrettyTable()
    table.field_names = ["Method", "Time (seconds)"]
    for timing in timings:
        table.add_row([timing[0], f"{timing[1]:.8f}"])
    print(table)


def time_function(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return func.__name__, end_time - start_time
