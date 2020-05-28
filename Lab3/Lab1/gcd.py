#!/usr/bin/env python3

import random
import math


def gcd(a, b):
    """

    :param a: Ideally an integer value greater than 0
    :param b: Ideally an integer value greater than 0
    :return: The greatest common divisor of a and b
    """

    a_true = abs(round(a))
    b_true = abs(round(b))
    d_count = 0
    while a_true % 2 == 0 and b_true % 2 == 0:
        a_true = a_true/2
        b_true = b_true/2
        d_count = d_count + 1

    while a_true != b_true:
        if a_true < math.pow(10, -8) or b_true < math.pow(10, -8):
            a_true = 1
            break
        if a_true % 2 == 0:
            a_true = a_true/2
        elif b_true % 2 == 0:
            b_true = b_true/2
        elif a_true > b_true:
            a_true = (a_true-b_true) / 2
        else:
            b_true = (b_true-a_true) / 2

    waen = a_true

    return math.ceil(waen * math.pow(2, d_count))


if __name__ == '__main__':  # Use this for test code after defining your functions

    from math import gcd as gcd_true

    for check_please in range(1, 1001):
        test_a = random.randint(-math.pow(10, 8), math.pow(10, 8))
        test_b = random.randint(-math.pow(10, 8), math.pow(10, 8))
        check_right = gcd_true(test_a, test_b)
        check_mine = gcd(test_a, test_b)
        print("Python's nested gcd is", check_right)
        print("My written gcd is", check_mine)
