import copy
import math
import random

import numpy as np


class Complex:
    def __init__(self, t):
        if isinstance(t, Complex):
            self.__pair = copy.deepcopy(t.__pair)
        else:
            assert (type(t[0]) is float or type(t[0]) is int) and (type(t[1]) is int or type(t[1]) is float)
            self.__pair = copy.deepcopy(t)

    def __str__(self):
        if self.__pair[0] == 0 and self.__pair[1] == 0:
            return 0
        elif self.__pair[0] == 0 and self.__pair[1] != 1 and self.__pair[1] != -1:
            return f"{self.__pair[1]}i"
        elif self.__pair[0] == 0 and self.__pair[1] != -1:
            return 'i'
        elif self.__pair[0] == 0:
            return '-i'
        elif self.__pair[1] == 0:
            return str(self.__pair[0])
        elif self.__pair[1] == 1:
            return f'{self.__pair[0]} + i'
        elif self.__pair[1] == -1:
            return f'{self.__pair[0]} - i'
        elif self.__pair[1] < 0:
            return f'{self.__pair[0]} - {-self.__pair[1]}i'
        return f'{self.__pair[0]} + {self.__pair[1]}i'

    def conjugate(self):
        return Complex((self.__pair[0], -self.__pair[1]))

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex((self.__pair[0] + other.__pair[0], self.__pair[1] + other.__pair[1]))
        else:
            return Complex((self.__pair[0] + other, self.__pair[1]))

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex((self.__pair[0] - other.__pair[0], self.__pair[1] - other.__pair[1]))
        else:
            return self + -other

    def __rsub__(self, other):
        if isinstance(other, Complex):
            return Complex((other.__pair[0] - self.__pair[0], other.__pair[1] - self.__pair[1]))
        return Complex((other - self.__pair[0], -self.__pair[1]))

    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex((self.__pair[0] * other.__pair[0] - self.__pair[1] * other.__pair[1],
                            (self.__pair[0] * other.__pair[1] + self.__pair[1] * other.__pair[0])))
        else:
            return Complex((self.__pair[0] * other, self.__pair[1] * other))

    def __rmul__(self, other):
        return other * self

    def __truediv__(self, other):
        if isinstance(other, Complex):
            assert other.__pair != (0, 0)
            return self * other.conjugate() * ((other.__pair[0] ** 2 + other.__pair[1] ** 2) ** (-1))
        else:
            assert other != 0
            return self * (other ** (-1))

    def __pow__(self, power):
        assert type(power) is int or type(power) is float
        r = (self.__pair[0] ** 2 + self.__pair[1] ** 2) ** 0.5
        phi = math.atan2(self.__pair[1], self.__pair[0])
        r_to_power = r ** power
        phi_to_power = phi * power
        x = r_to_power * math.cos(phi_to_power)
        y = r_to_power * math.sin(phi_to_power)
        return Complex((round(x, 3), round(y, 3)))

    @staticmethod
    def solve_quadratic_equation(coefficients):
        a = coefficients[0]
        b = coefficients[1]
        c = coefficients[2]
        if a != 0:
            sqrt_d = Complex((b ** 2 - 4 * a * c, 0)) ** 0.5
            t = -b - sqrt_d
            x1, x2 = (-b + sqrt_d) / (2 * a), (-b - sqrt_d) / (2 * a)
            return x1.__str__(), x2.__str__()


if __name__ == '__main__':
    cp = Complex((0, 1))
    print(Complex.solve_quadratic_equation((1, 4, 5)))
    random_coefficients = [[random.randint(-10, 10) for i in range(3)] for j in range(3)]
    print(random_coefficients)
    for i in range(len(random_coefficients)):
        print(Complex.solve_quadratic_equation(random_coefficients[i]), "complex", i)
        print(np.roots(random_coefficients[i]), 'np', i)
