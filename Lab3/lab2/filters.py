#!/usr/bin/env python3

from statistics import mean
from amp_filter import apply_amp_filter
from sensor import generate_sensor_data
import csv


def mean_filter(given_list, given_interval=3):
    """
    Find a list that returns the mean value of an array within the list
    :param given_list: List given by user
    :param given_interval: Spacing between mean values
    :return: A new list with the mean value between
    """
    new_list = []
    if given_interval < 1 or given_interval % 2 == 0:
        raise ValueError('The parameter must be positive and odd.')
    for i, e in enumerate(given_list):
        try:
            if i == 0:
                mean_val = mean(given_list[0:given_interval])
                new_list.append(mean_val)
            elif i + given_interval >= (len(given_list)+1):
                pass
            else:
                mean_val = mean(given_list[i: (i+given_interval)])
                new_list.append(mean_val)
        except IndexError:
            pass
    return new_list


if __name__ == '__main__':

    raw_data = generate_sensor_data(1000)
    filtered_data = apply_amp_filter(raw_data)
    mean_data = mean_filter(raw_data)
    rowd_e_boi = list(zip(raw_data, filtered_data, mean_data))

    with open('check_me_filters.csv', 'w', newline='') as boots:
        test_file = csv.writer(boots)
        for row in rowd_e_boi:
            test_file.writerow(row)

    test_check = mean_filter([1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1])
    check_list = [2, 2.333, 2, 1.667, 2, 2.333, 2, 1.667, 2, 2.333, 2]
    print(check_list)
    print(test_check)
