#!/usr/bin/env python3


from math import pi, pow, fabs


def close(first, second, third):
    # that takes three numbers as arguments.  It returns True if the absolute
    # difference between the first two numbers is less than the third number.
    """

    :param first: The first value to compare.
    :param second: The second value to compare.
    :param third: The third value to compare.
    :return: Determines if the absolute difference between the first two numbers
    is less than the third number.
    """
    if fabs(second-first) < third:
        return True
    if fabs(second-first) >= third:
        return False


if __name__ == '__main__':  # Use this for test code after defining your functions

    test_close = [(1, 2, 3), (1, 0.5, 0.5), (pi, pow(pi, 4), 3.15), (2, 5, 6)]

    for i in test_close:
        test = close(i[0], i[1], i[2])
        print(test)
