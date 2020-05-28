#!/usr/bin/env python3
from math import pi, pow


def cylinder_volume(radius, height):
    """
    This function calculates the volume of a cylinder.

    :param radius: The radius of the cylinder.
    :param height: The height of the cylinder.
    :return: The volume  of the cylinder.
    """
    if radius < 0:
        raise ValueError("I'm sorry Dave, I can't do that.")
    if height < 0:
        raise ValueError("Just what do you think you're doing, Dave?")
    return height * pow(radius, 2) * pi


def torus_volume(inner_radius, outer_radius):
    """
    This function calculates the volume of a taurus.
    :param inner_radius: Inner radius of the donut.
    :param outer_radius: Outer radius of the donut.
    :return: The total volume of the cylinder.
    """
    if inner_radius < 0:
        raise ValueError("C'mon dogg.")
    if outer_radius < 0:
        raise ValueError("That's not how this works.")
    if outer_radius < inner_radius:
        raise ValueError("I think you have your radii backwards.")

    return pow(pi, 2) * (inner_radius + outer_radius) * pow((outer_radius - inner_radius), 2) / 4


if __name__ == '__main__':  # Use this for test code after defining your functions

    test_radius = 3
    test_height = 5
    test_volume = cylinder_volume(test_radius, test_height)
    print(test_volume)

    test_radii = [(3, 4), (5, -3), (-4, 3), (10, -3)]
    for i in test_radii:
        torryborealis = torus_volume(i[0], i[1])
        print(torryborealis)
