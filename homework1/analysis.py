#!/usr/bin/env python3

import csv
import math


def load_data_from_file(filename):
    """
    Load that data, my dude(tte)
    :param filename: The file from which you want to load data
    :return: Time and position data of the file
    """
    time = []
    position = []
    with open(filename, 'r') as original:
        time_position = list(csv.reader(original))  # list()
        for row in range(1, len(time_position)):
            time.append(float(time_position[row][0]))
            position.append(float(time_position[row][1]))

    return time, position


def greater_than_index(numlist, singnum):
    """
    Function takes in a list of ints, compares them to a single int and returns the index value at which the
    list encounters a value greater than, or equal to, the value of interest.
    :param numlist: The list of ints
    :param singnum: The int to compare the list to
    :return: The index value of the position >= value of interest
    """
    try:
        for elem in numlist:
            if elem >= singnum:
                e_val = numlist.index(elem)
                return e_val
    except ValueError:
        return 'None. Try a value contained within the list.'


def less_than_index(numlist, singnum):
    """
    Function takes in a list of ints, compares them to a single int and returns the index value at which the
    list encounters a value greater than, or equal to, the value of interest.
    :param numlist: The list of ints
    :param singnum: The int to compare the list to
    :return: The index value of the position >= value of interest
    """
    try:
        for elem in numlist:
            if elem <= singnum:
                e_val = numlist.index(elem)
                return e_val
    except ValueError:
        return 'None. Try a value contained within the list.'


def ini_max_fin(pos1):
    c_initial = pos1[0]
    c_max = max(pos1)
    c_final = pos1[-1]
    return c_initial, c_max, c_final


def char_ests(time_c, pos_c, c_initial, c_max, c_final):
    """
    This function estimates the characteristics of the waveform we're analyzing
    :param time_c: A list of time values to determine the time it takes for certain things to occur
    :param pos_c: A list of position values to determine the position at certain values of time
    :param c_initial: The initial position value of our waveform
    :param c_max: The maximum position value of our waveform
    :param c_final: The final value of our waveform
    :return: Rise time (t_r), Peak time(t_p), % Overshoot(p_os_fix), Settling time (t_s).
    """
    # Index values for time statements
    maxdex = pos_c.index(c_max)
    ten_perc = (c_final + c_initial) * 0.1
    tr_10 = greater_than_index(pos_c, ten_perc)
    ninety_p = (c_final + c_initial) * 0.9
    tr_90 = greater_than_index(pos_c, ninety_p)

    # Calculations
    t_r = time_c[tr_10] - time_c[tr_90]  # Rise time
    t_p = time_c[maxdex]  # Peak time

    # Adjusted %OS eq
    p_os_fix = ((c_max - c_final) / (c_final-c_initial)) * 100  # %OS

    # two percent calcs
    two_perc = (c_final - c_initial) * 0.02
    c_thresh_low = c_final - two_perc
    c_thresh_high = c_final + two_perc
    mcfly = list(reversed(time_c))
    beckett = list(reversed(pos_c))
    minlist = [less_than_index(beckett, c_thresh_low), greater_than_index(beckett, c_thresh_high)]

    t_s = mcfly[min(minlist)]  # Settling time

    return t_r, t_p, p_os_fix, t_s


def get_system_params(perc_os, settle_t):
    """
    :param perc_os: The Overshoot Percentage value from which to calculate things 
    :param settle_t: The settling time from which to calculate things
    :return: The mass (m_spr), spring (k_spr), and damping constants(c_spr)
    """

    num_zet = -math.log(perc_os/100)
    den_zet = math.sqrt(math.pi**2 + math.log(perc_os/100)**2)
    zeta = num_zet/den_zet
    omega = 4 / (zeta*settle_t)
    m_spr = 1  # Told to assume mass is always 1 (unit)
    k_spr = omega**2
    c_spr = 2*zeta*omega
    return m_spr, k_spr, c_spr


def analyze_data(filename):
    """
    :param filename: A name for the csv file to run the resulting operations 
    :return: A dictionary with some gucci values
    """
    backtime, backpos = load_data_from_file(filename)
    c_i, c_m, c_f = ini_max_fin(backpos)
    t_rise, t_peak, percos, t_set = char_ests(backtime, backpos, c_i, c_m, c_f)
    m, k, c = get_system_params(percos, t_set)

    dict_party = {'c_initial': c_i, 'c_max': c_m, 'c_final': c_f, 'rise_time': t_rise, 'peak_time': t_peak,
                  'perc_overshoot': percos, 'settling_time': t_set, 'system_mass': m, 'system_spring': k,
                  'system_damping': c}
    true_dict = {}
    for key in sorted(dict_party):
        true_dict.update({key: dict_party[key]})

    return true_dict


if __name__ == '__main__':

    print(analyze_data('data1.csv'))
    # print(analyze_data('data2.csv'))
    # print(analyze_data('data3.csv'))
    # print(analyze_data('data4.csv'))
