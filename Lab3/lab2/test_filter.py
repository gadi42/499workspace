#!/usr/bin/env python3

from amp_filter import apply_amp_filter
from sensor import generate_sensor_data
import csv


if __name__ == '__main__':

    raw_data = generate_sensor_data(1000)
    filtered_data = apply_amp_filter(raw_data)
    row_d_boi = list(zip(raw_data, filtered_data))

    with open('check_me.csv', 'w', newline='') as toots:
        test_file = csv.writer(toots)
        for row in row_d_boi:
            test_file.writerow(row)
