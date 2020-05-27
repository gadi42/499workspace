#!/usr/bin/env python3

import msd
import matplotlib.pyplot as plt
import numpy as np
from utils import simulate_gachapon as gach_sim
from collections import Counter
from counter import get_element_counts
from random import randint
import time


def prob1(m=1.0, k=5.0, c=2.5):
    spring_sys = msd.MassSpringDamper(m, k, c)
    state, tim = spring_sys.simulate(1, -1, 40.0, 0.01)
    x_pos = [i[0] for i in state]
    return tim, x_pos


def random_list(n):
    rand_list = []
    for _ in range(n):
        rand_list.append(randint(0, n-1))
    return rand_list


if __name__ == '__main__':

    t, space = prob1()
    plt.plot(t, space, color='teal')
    plt.xlabel('Time')
    plt.ylabel('Position')
    plt.savefig('problem1.png')
    plt.show()

    prize_count = 15
    numb = 1000
    x = Counter()
    for _ in range(numb):
        x[(gach_sim(prize_count))] += 1

    for i in x.keys():
        x[i] /= numb

    data = []
    for key in sorted(x.keys()):
        data.append([key, x[key]*100])

    plt.bar(*zip(*data))

    plt.title('Simulated Gachapon attempts')
    plt.xlabel('Casts to win all 15 prizes')
    plt.ylabel('Chance of winning with those casts (%)')
    plt.xlim(xmin=0)
    plt.savefig('problem2.png')
    plt.show()

    time_list = list(range(50, 2550, 50))
    english_patient = []
    for i in time_list:
        sack_lunch = random_list(i)
        start = time.time()
        get_element_counts(sack_lunch)
        end = time.time()
        english_patient.append(end-start)

    plt.scatter(time_list, english_patient)
    plt.title('Scatter plot')
    plt.xlabel('Length of list')
    plt.ylabel('Run time (seconds)')
    plt.savefig('problem3.png')
    plt.show()
