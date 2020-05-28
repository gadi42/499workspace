#!/usr/bin/env python3
from itertools import chain


def reverse_i(given_list):

    check = list(chain(given_list))
    backtrack = []
    for i in check:
        backtrack.append(check[-1])
        check = check[:-1]
        i += i
    return backtrack


def reverse_r(given_list):

    #  if isinstance(given_list, list) is False:
    #  raise ValueError("Please try with a list next time")
    #  else:
    if len(given_list) == 0:
        return given_list[-1:]
    else:
        lst = given_list[-1:] + reverse_r(given_list[:-1])
        # lst calls the last element of the given_list, followed by the rest of the list.
        # Then it returns the function of the given list
        return lst


if __name__ == '__main__':

    t1 = reverse_i(['h', 'e', 'l', 'l', 'o'])  # ['o', 'l', 'l', 'e', 'h']
    t2 = reverse_r(['h', 'e', 'l', 'l', 'o'])  # ['o', 'l', 'l', 'e', 'h']
    t3 = reverse_i([1, 2, 3, 4, 5])  # [5, 4, 3, 2, 1]
    t4 = reverse_r([['e', 'y', 'b', '-', 'd', 'o', 'o', 'g']])  # Goodbye
    t5 = reverse_r([1, 2, 3, 4, 5])
    print(t1), print(t2), print(t3), print(t4), print(t5)
