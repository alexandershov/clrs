import math

import decimal

import itertools


def print_run_times_table():
    hour = 3600
    day = hour * 24
    month = day * 30
    year = day * 365
    century = year * 100
    times_in_seconds = [
        1,
        60,
        hour,
        day,
        month,
        year,
        century,
    ]
    times_in_microseconds = [t * 10 ** 6 for t in times_in_seconds]
    functions = [
        # str, direct, reverse
        # 2 ** x is too large for microseconds, that's why it's commented
        # ('lg(n)', lambda n: math.log(n, 2), lambda x: 2 ** x),
        ('sqrt(n)', math.sqrt, lambda x: x ** 2),
        ('n', lambda n: n, lambda n: n),
        # too long with simple count
        # ('n*lg(n)', lambda n: n * math.log(n, 2), lambda x: get_max_n(lambda n: n * math.log(n, 2), x)),
        ('n^2', lambda n: n ** 2, lambda x: x ** (1 / 2)),
        ('n^3', lambda n: n ** 3, lambda x: x ** (1 / 3)),
        ('2^n', lambda n: 2 ** n, lambda x: math.log(x, 2)),
        ('n!', math.factorial, lambda x: get_max_n(math.factorial, x)),
    ]
    for fn_info in functions:
        name, direct_fn, reverse_fn = fn_info
        print(name, end=': ')
        for time in times_in_microseconds:
            max_n = int(math.floor(reverse_fn(time)))
            print(format_n(max_n), end=' ')
        print()


def get_max_n(direct_fn, time):
    result = 0
    for i in itertools.count(1):
        if direct_fn(i) > time:
            return result
        else:
            result = i
    return result


def format_n(x):
    if x < 10000:
        return str(x)
    return format(decimal.Decimal(x), '.2g')


if __name__ == '__main__':
    print_run_times_table()
