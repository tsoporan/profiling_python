"""
Profiling by measuring time

- Using Python3 monotonic timers, perf_counter, (a clock with the highest level
of resolution, inludes time elapsed during sleep and system-wide)
- Using timeit, which runs multiple iterations and averages the result

"""

import math
from time import perf_counter
from timeit import timeit


def square_sums_basic(number):
    """Add up the squares with basic loop approach"""

    sumsq = 0
    for i in range(1, number):
        sumsq += math.sqrt(i)

    return sumsq


def square_sums_fn(number):
    """ Using builtins """
    return sum(map(math.sqrt, range(1, number)))

if __name__ == '__main__':
    start = perf_counter()
    sum1 = square_sums_basic(1000000)
    duration = perf_counter() - start  # Seconds

    print("square_sums_basic using perf_counter: {}".format(duration))

    start = perf_counter()
    sum2 = square_sums_fn(1000000)
    duration = perf_counter() - start

    assert sum1 == sum2

    print("square_sums_fn using perf_counter: {}".format(duration))

    print('square_sums_basic using timeit', timeit('square_sums_basic(10)', 'from __main__ import \
                                      square_sums_basic'))
    print('square_sums_fn using timeit', timeit('square_sums_fn(10)', 'from __main__ import \
                                   square_sums_fn'))
