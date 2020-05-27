#!/usr/bin/env python3


class Complex:
    """
    A class that redefines complex numbers for learning purposes
    """
    def __init__(self, real=0.0, imag=0.0):
        """
        Initializes Complex
        :param real: The real number
        :param imag: The imaginary number
        """
        self.re = real
        self.im = imag

    def __repr__(self):
        """
        Representation of the self for the author
        :return: you know ;)
        """
        # base = '({} + {}i)'.format(round(self.re, 2), round(self.im, 2))
        if self.im < 0.0:
            return '({} - {}i)'.format(round(self.re, 1), abs(round(self.im, 1)))
        else:
            return '({} + {}i)'.format(round(self.re, 1), abs(round(self.im, 1)))

    def __str__(self):
        """
        Representation of self for the user.
        :return: you know (;
        """
        return self.__repr__()

    def __add__(self, other):
        """
        Mathematical addition of the imaginary numbers
        :param other: The right side of addition
        :return: The sum of all that jazz
        """
        try:
            return Complex(real=self.re + other.re, imag=self.im + other.im)
        except AttributeError:
            return self + Complex(other)

    def __radd__(self, other):
        """
        Mathematical right addition
        :param other: The right hand side of the addition
        :return: The sum of literally all that jazz
        """

        return self + other

    def __mul__(self, other):
        """
        Imaginary multiplication
        :param other: Part of that jazz
        :return: All of that jazz multiplied
        """
        try:
            return Complex(real=self.re * other.re + self.re * other.im,
                           imag=(-self.im * other.im) + self.im * other.re)
        except AttributeError:
            return self * Complex(other)

    def __rmul__(self, other):
        """
        Now mult to the left
        :param other: jazz fingers
        :return: Full body jazz
        """
        return self * other


if __name__ == '__main__':

    # print(Complex(-3,2))
    # print(Complex())
    # print(Complex(3.45, -2.13))

    # a = Complex(2.0, 3.0)
    #
    # print(a + Complex(-1.5, 2))  # (0.5 + 5.0i)
    # print(a + 8)  # (10.0 + 3.0i)
    # print(3.5 + a)  # (5.5 + 3.0i)

    a = Complex(1.0, -3.0)
    print(a)
    # b = complex(4.0, 5.5)
    # print(b)
    # print(a * b)
    print(a * Complex(4.0, 5.5))  # (20.5 - 6.5i)
    print(a * 3.5)  # (3.5 - 10.5i)
    print(-2 * a)  # (-2.0 + 6.0i)
