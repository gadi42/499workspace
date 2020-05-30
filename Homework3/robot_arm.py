import numpy as np
import matplotlib.pyplot as plt
from itertools import product

class RobotArm:

    def __init__(self, *arm_lengths, obstacles=None):
        """
        Represents an N-link arm with the arm lengths given.
        Example of initializing a 3-link robot with a single obstacle:

        my_arm = RobotArm(0.58, 0.14, 0.43, obstacles=[VerticalWall(0.45)])

        :param arm_lengths: Float values representing arm lengths of the robot.
        :param obstacles:
        """
        self.arm_lengths = np.array(arm_lengths)
        if np.any(self.arm_lengths < 0):
            raise ValueError("Cannot have negative arm length!")
        self.obstacles = []
        if obstacles is not None:
            self.obstacles = obstacles

    def __repr__(self):
        msg = '<RobotArm with {} links\nArm lengths: '.format(len(self.arm_lengths))
        msg += ', '.join(['{:.2f}'.format(length) for length in self.arm_lengths])
        msg += '\nObstacles: '
        if not len(self.obstacles):
            msg += 'None'
        else:
            msg += '\n\t' + '\n\t'.join(str(obstacle) for obstacle in self.obstacles)
        msg += '\n>'
        return msg

    def __str__(self):
        return self.__repr__()

    def get_links(self, thetas):
        """
        Returns all of the link locations of the robot as Link objects.
        :param thetas: A list or array of scalars matching the number of arms.
        :return: A list of Link objects.
        """

        cum_theta = np.cumsum(thetas)

        results = np.zeros((self.arm_lengths.shape[0] + 1, 2))

        results[1:, 0] = np.cumsum(self.arm_lengths * np.cos(cum_theta))
        results[1:, 1] = np.cumsum(self.arm_lengths * np.sin(cum_theta))
        links = [Link(start, end) for start, end in zip(results[:-1], results[1:])]

        return links

    def get_ee_location(self, thetas):
        """
        Returns the location of the end effector as a length 2 Numpy array.
        :param thetas: A list or array of scalars matching the number of arms.
        :return: A length 2 Numpy array of the x,y coordinate.
        """
        return self.get_links(thetas)[-1].end

    def ik_grid_search(self, target, intervals):
        """
        Uses stuff to do things
        :param target: The point that the arm should try to reach
        :param intervals: Splits the interval into the specified number of endpoints
        :return:
        """
        initial_int = np.linspace(0, 2*np.pi, num=intervals, endpoint=False)  # , endpoint=True
        # num=intervals,
        # num=intervals**len(self.arm_lengths),
        # good_hits = list(product(initial_int, repeat=len(self.arm_lengths)))
        good_hits = np.array(list(product(initial_int, repeat=len(self.arm_lengths))))
        my_goodlinks = []
        Probable_links = []
        for i in range(len(good_hits)):
            test = self.get_ee_location(good_hits[i])
            if self.get_ee_location(good_hits[i]) is target:
                my_goodlinks.append(self.get_links(good_hits[i]))
            # if self.get_links((good_hits[i]))[-1].end == target:
        #     my_goodlinks.append(self.get_links(good_hits[i]))
        # for i in range(len(my_goodlinks)):
        #     if self.get_ee_location()


        return print(my_goodlinks)


    def ik_fmin_search(self, target, thetas_guess, max_calls=100):
        raise NotImplementedError

    def get_collision_score(self, thetas):
        count = 0
        hit_links = self.get_links(thetas)
        if self.obstacles is not None:
            for j in range(len(self.obstacles)):
                for i in range(len(hit_links)):
                    if hit_links[i].check_wall_collision((self.obstacles[j])) is True:
                        count -= 1
        return count

    def ik_constrained_search(self, target, thetas_guess, max_iters=100):
        raise NotImplementedError

    def plot_robot_state(self, thetas, target=None, filename='robot_arm_state.png'):
        """

        :param thetas: The joint angles
        :param target: A target point in the environment
        :param filename: The filename to output
        :return: Visualization of all vertical walls, an arbitrary target point,
                 The links of the robot, as well as coloring connected areas differently
                 and plotting that link as a dashed line which connect with walls, marked
                 joints.
                 x and y bounds that show the elongated arm
                 Don't worry about titles or axis'
        """
        plt.ylim(-sum(self.arm_lengths), sum(self.arm_lengths))
        plt.xlim(-sum(self.arm_lengths), sum(self.arm_lengths))
        # plt.axis('square')
        my_linkshake = self.get_links(thetas)
        if self.obstacles is not None:
            for k in self.obstacles:
                plt.axvline(k.loc, color='m')
                # Shift origin to end location once loop starts over.
                for l in range(len(my_linkshake)):
                    xval = [my_linkshake[l].start[0], my_linkshake[l].end[0]]
                    yval = [my_linkshake[l].start[1], my_linkshake[l].end[1]]
                    # thisval = [xval, yval]
                    plt.plot(my_linkshake[l].end[0], my_linkshake[l].end[1], 'bo' )
                    if my_linkshake[l].check_wall_collision(k) is True:
                        # plt.setp(thisval, '-', color='r')
                        plt.plot(xval, yval, '--', color='r')
                    else:
                        plt.plot(xval, yval, color='k')

        if target is not None:
            plt.plot(target[0], target[1], 'co')

        plt.show()

        return plt.savefig(filename)

        # raise NotImplementedError


class Link:

    def __init__(self, start, end):
        """
        Represents a finite line segment in the XY plane, with start and ends given as 2-vectors
        :param start: A length 2 Numpy array
        :param end: A length 2 Numpy array
        """
        self.start = start
        self.end = end

    def __repr__(self):
        return '<Link: ({:.3f}, {:.3f}) to ({:.3f}, {:.3f})>'.format(self.start[0], self.start[1],
                                                                     self.end[0], self.end[1])

    def __str__(self):
        return self.__repr__()

    def check_wall_collision(self, wall):
        """
        A function to check for wall collision with each link
        I tried a bunch of stuff here but decided to just go with the end of the link
        :param wall: The wall's values to check for distances
        :return: True if the link is longer than the wall
        """
        # link_length = np.linalg.norm(self.end) - np.linalg.norm(self.start)
        if not isinstance(wall, VerticalWall):
            raise ValueError('Please input a valid Wall object to check for collision.')

        if self.start[0] < wall.loc < self.end[0]:
            return True
        elif self.end[0] < wall.loc < self.start[0]:
            return True
        else:
            return False
        # raise NotImplementedError


class VerticalWall:

    def __init__(self, loc):
        """
        A VerticalWall represents a vertical line in space in the XY plane, of the form x = loc.
        :param loc: A scalar value
        """
        self.loc = loc

    def __repr__(self):
        return '<VerticalWall at x={:.3f}>'.format(self.loc)


if __name__ == '__main__':
    # # Example of initializing a 3-link robot arm
    # arm = RobotArm(1.2, 0.8, 0.5, obstacles=[VerticalWall(1.2)])
    # print(arm)
    #
    # # Get the end-effector position of the arm for a given configuration
    # thetas = [np.pi / 4, np.pi / 2, -np.pi / 4]
    # pos = arm.get_ee_location(thetas)
    # print('End effector is at: ({:.3f}, {:.3f})'.format(*pos))
    #
    # # Get each of the links for the robot arm, and print their start and end points
    # links = arm.get_links(thetas)
    #
    # for i, link in enumerate(links):
    #     print('Link {}:'.format(i))
    #     print('\tStart: ({:.3f}, {:.3f})'.format(*link.start))
    #     print('\tEnd: ({:.3f}, {:.3f})'.format(*link.end))
    # # Test 1.1
    # my_link = Link((1.1, 5.0), (3.0, 3.3))
    # toot = my_link.check_wall_collision(VerticalWall(2.1))  # True
    # butt = my_link.check_wall_collision(VerticalWall(-0.3))  # False
    # print(toot, butt)
    # # Test 1.2
    # my_arm = RobotArm(1, 1, 1, obstacles=[VerticalWall(1.5)])
    #
    # # Arm is vertical, should be 0
    # arm1 = my_arm.get_collision_score([np.pi / 2, 0, 0])
    #
    # # Arm is horizontal but then folds back, should be -2
    # arm2 = my_arm.get_collision_score([0, 0, np.pi])
    # print(arm1, arm2)
    mybot = RobotArm(2, 1, 2, obstacles=[VerticalWall(3.2)])
    # plotbot= mybot.plot_robot_state([0.2, 0.4, 0.6], target=[1.5, 1.5])
    print(mybot.ik_grid_search([1, 2], 4))