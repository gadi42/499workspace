#!/usr/bin/env python3

import random


def simulate_gachapon(n):
    """
    Simulating a gachapon
    :param n: The number of prizes in the gachapon
    :return: The number of pulls required to win all the prizes in the gachapon
    """

    counter = 0
    prize_get = 0
    while not(prize_get == n):
        prize_get += random.randint(0, n-1)
        counter += 1
    return counter


if __name__ == '__main__':
    f = simulate_gachapon(3)
    print(f)
