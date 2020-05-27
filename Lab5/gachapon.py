#!/usr/bin/env python3

import random
import numpy
import sys


class GachaponSimulator:
    """
    A simulator of a gachapon machine
    """

    def __init__(self, n=1):
        """
        Initializing the gachapon
        :param n: The number of prizes.  Defaults to 1
        """
        self.pool = n
        self.results = []
        self.runs = 0

    def _simulate_once(self):
        """
        Simulating a gachapon
        :return: The number of pulls required to win all of the prizes
        """

        self.counter = 0
        self.prize_get = 0
        while not (self.prize_get >= self.pool):
            self.prize_get += random.randint(0, self.pool - 1)
            self.counter += 1
        return self.counter

    def reset(self):
        """
        Resets the results list to an empty list
        :return: An empty list
        """
        self.results = []
        return self.results

    def simulate(self, num_games):
        """
        A command which runs multiple loops of the simulation
        :param num_games: The number of games/ loops for the simulation to run
        :return: A list of the number iterations for each game within the "results" list.
        """
        # self.runs = num_games  #Initializes a tracker for the number of runs
        for _ in range(num_games):
            self.results.append(self._simulate_once())
        return self.results

    def get_summary_stats(self):
        """
        Returns a dictionary with a number of games that have been run (key of n)
        :return:
        """
        n = len(self.results)

        if n == 0:
            mean = None
            stdev = None

        elif n == 1:
            mean = numpy.mean(self.results)
            stdev = None

        else:
            mean = numpy.mean(self.results)
            stdev = numpy.std(self.results)

        sum_stats = {'n': n, 'mean': mean, 'stdev': stdev}

        return sum_stats


if __name__ == '__main__':

    # one = GachaponSimulator(10)
    # two = one.simulate(1000)
    # three = one.get_summary_stats()
    # print(three)
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    some = GachaponSimulator(x)
    thing = some.simulate(y)  # Use some to call the thing
    fun = some.get_summary_stats()
    print('Running {}-prize lottery simulator {} times... \nAverage number of iterations was {} with a '
          'standard deviation of {}'.format(x, y, fun['mean'], fun['stdev']))
