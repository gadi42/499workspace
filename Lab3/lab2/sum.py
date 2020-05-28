#!/usr/bin/env python3


def sum_i(given_list):
    addition = 0
    if isinstance(given_list, list) is False:
        return given_list
    else:
        for i in given_list:
            addition += i
        return addition


def sum_r(given_list):

    if isinstance(given_list, list) is False:
        return given_list
    else:
        if len(given_list) == 1 or len(given_list) == 0:
            return given_list[-1]
        else:
            return given_list[-1] + sum_r(given_list[:-1])

#    for i in rec_list:
#       rec_add = rec_add + rec_list[-1]
#      rec_list = rec_list[:-1]
# return rec_add


if __name__ == '__main__':

    test_list = [1, 3, 5, 7, 9, 11, 13, 1]

    s = sum_i(test_list)
    true_s = sum(test_list)
    sr = sum_r(test_list)

    print(true_s)
    print(s)
    print(sr)

    s1 = sum_r(1)
    s2 = sum_i(13)
    print(s1, s2)
