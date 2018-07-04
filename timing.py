"""
Measuring time with Python3 monotonic timers (a clock with the highest level
of resolution)

Inludes time elapsed during sleep and system-wide.
"""

import math
from time import perf_counter


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

    print("Duration: {}".format(duration))

    start = perf_counter()
    sum2 = square_sums_fn(1000000)
    duration = perf_counter() - start

    assert sum1 == sum2

    print("Duration: {}".format(duration))
