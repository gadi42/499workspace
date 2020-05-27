#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# Look up argmin, argsort, isclose


def numpy_close(array_a, array_b, tol=1e-8):
    """
    Takes two arrays, a and b, and checks if they have the same shape (mxn) -and-
    the "absolute difference" < tol. If both are true, it returns "True"
    :param array_a: An array of m x n dimensions and values
    :param array_b: An array of m x n dimensions and values
    :param tol: The tolerance to check for truth within the inquiry
    :return: True or False statements
    """

    if array_a.shape == array_b.shape and abs(array_a - array_b) < tol:
        # Should I be using isclose here..?
        return True
    else:
        return False


def simple_minimizer(func, start, end, num=100):
    """
    Evaluate func at num evenly-spaced points between start -and- end (inclusive) and return two values:
    The x corresponding to the *minimum* value of func, followed by the actual minimum.
    ex: f(0.5) = 2.4 returns (0.5, 2.4)
    :param func: A 1 dimensional function ( f(x) = x^2 )
    :param start: The float beginning the search
    :param end: The float ending the search
    :param num: The number of evenly spaced points between "start" and "end".
    :return: The index and value of the minimum point within that range of the function.
    """
    if start > end:
        return ValueError('Oops. Start value cannot be bigger than End value.')
    else:
        func_eval = np.linspace(start, end, num)  # Creates an array of values to run through the function
        solved_func = func(func_eval)  # Evaluates the function with func_eval
        min_func, ind_func = solved_func[np.argmin(solved_func)], func_eval[np.argmin(solved_func)]
        return ind_func, min_func


def simulate_dice_rolls(num_rolls, iterations):
    """
    It should return a 1-D Numpy array of length iterations, where each item is the sum
    of throwing a fair 6-sided die num_rolls times.
    :param num_rolls: The number of rolls for a d6
    :param iterations: The amount of times to roll the d6 (num_rolls) times.
    :return: a histogram of that bizzz and some other stuff if you're feeling spicy.
    """
    firecheck = np.random.randint(1, 7, size=(iterations, num_rolls))  # randint is straight dumb.
    fireball = np.sum(firecheck, axis=1)
    # firesmall = fireball.min()
    # firebig = fireball.max()
    # firebad = fireball.mean()
    # print(firesmall, firebig, firebad)
    plt.hist(fireball)
    plt.savefig(f'dice_{num_rolls}_rolls_{iterations}.png')
    return fireball


def is_transformation_matrix(fourxfour):
    # Checking bottom row
    check_transf = np.in1d(fourxfour, np.array([0., 0., 0., 1.]))
    is_transf = np.all(check_transf[12:])
    # Checking 3x3 for Identity
    roto_mat = np.array(fourxfour[0:3, 0:3])
    cooked_buns = np.allclose(roto_mat.T @ roto_mat, np.identity(3))
    if cooked_buns and is_transf:
        return True
    else:
        return False


def nearest_neighbors(user_array, point, dist):
    """
    Should return an n x d numpy array of all points in the array within euclidian
    distance of the point sorted by distance from the corresponding point.
    :param user_array: The user's array
    :param point: A 1D array of length D
    :param dist: A distance threshold
    :return: An M X D array of all points within dist and point
    Take user array, compare it to the point value and see if it's within the distance required
    duplicate point vector to have same rows as user_array, compare distances row by row
    """

    euc_dist = np.linalg.norm(user_array-point, axis=1)  # Check euclidean distance between vectors
    sorting_index = np.argsort(euc_dist)  # Sort indexes of euclidian distance array
    test_dist = euc_dist[sorting_index]  # Make new euclidian distance array that's beens sorted
    new_user = user_array[sorting_index]  # Make new sorted user array
    check_dist = test_dist < dist  # See if distances are within tolerance
    near_array = new_user[check_dist]  # Make new array of nearest neighbors
    return near_array


if __name__ == '__main__':
    print('butts')
    # my_func = lambda x: x ** 2
    # check= simple_minimizer(my_func, 3, 2.25, num=5)
    # # Should return (0.25, 0.0625)
    # print(check)
    # toots = simulate_dice_rolls(5, 2000)
    # print(toots)
    # tf_valid = np.array([
    #     [0, 0, -1, 4],
    #     [0, 1, 0, 2.4],
    #     [1, 0, 0, 3],
    #     [0, 0, 0, 1]
    # ])
    #
    # tf_invalid = np.array([
    #     [1, 2, 3, 1],
    #     [0, 1, -3, 4],
    #     [0, 1, 1, 1],
    #     [-0.5, 4, 0, 2]
    # ])
    # print(is_transformation_matrix(np.eye(4)))
    # print(is_transformation_matrix(tf_valid))  # True
    # print(is_transformation_matrix(tf_invalid))  # False
    array = np.array([[1, 1, 1], [2, 3, 5], [0, 1, 1], [1.5, 1, 1], [10, 9, 9]])
    target_pt = np.array([0, 1, 1])
    print(nearest_neighbors(array, target_pt, 3))
    # Should return [[0, 1, 1], [1, 1, 1], [1.5, 1, 1]]
