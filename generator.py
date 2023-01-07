"""This module provide access to generator functions"""

def geom_sequence(n: int, m: int):
    """
    Return an object that produces a sequence of integers of geometric sequence.
    geom_sequence(n, m) produces 1 * m, (1 + 1) * m, (2 + 1) * m, ..., (n - 1) * m, n * m.
    geom_sequence(3, 2) produces 2, 4, 6.

    Parameters:
        n (int): Max limit of multiplicand integers.
        m (int): Multiplier.
    """

    if not isinstance(n and m, int):
        raise TypeError("The arguments must be an integer")

    number = 1
    while number <= n:
        value = yield number * m
        if value:
            n = value
        number += 1


def range_gen(*args):
    """
    range(stop) -> range object
    range(start, stop[, step]) -> range object

    Return an object that produces a sequence of integers from start (inclusive)
    to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
    start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
    These are exactly the valid indices for a list of 4 elements.
    When step is given, it specifies the increment (or decrement).
    """

    if not len(args):
        raise TypeError("Expected at least 1 argument")

    elif len(args) == 1:
        start = 0
        args = (*args,)
        stop = args[0]
        step = 1

        if not isinstance(stop, int):
            raise TypeError("The arguments must be an integer")

        while start < stop:
            yield start
            start += step

    elif len(args) == 2:
        start, stop = (*args,)
        step = 1

        if not isinstance(start and stop, int):
            raise TypeError("The arguments must be an integer")

        while start < stop:
            yield start
            start += step

    elif len(args) == 3:
        start, stop, step = (*args,)

        if not isinstance(start and stop and step, int):
            raise TypeError("The arguments must be an integer")
        if not step:
            raise ValueError("The step argument must not be zero")

        if step > 0:
            while start < stop:
                yield start
                start += step
        if step < 0:
            while start > stop:
                yield start
                start += step

    else:
        raise TypeError("Expected at most 3 arguments")


def prime_number(number: int):
    """
    Return an object that produces a sequence of prime numbers from 1 (inclusive) to number (exclusive).

    Parameters:
        number (int): Max limit of prime numbers range.
    """

    if isinstance(number, int):
        for num in range(1, number):
            for i in range(2, num):
                if not num % i:
                    break
            else:
                yield num
    else:
        raise TypeError("The number must be an integer")


