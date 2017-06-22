#   coding=UTF_8
#
#   problem_080.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on XX.XX.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from fraction import Fraction
from math import sqrt

class Problem_080(Problem):

    def __init__(self):
        self.problem_nr = 80
        self.input_format = (InputType.NUMBER_INT, 1, 100000)
        self.default_input = 100
        self.description_str = '''It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first ''' + dye_input_var("one hundred") + ''' natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.'''

    def calculate(self, lim):

        res = 0

        def approx_root_first_100_digits(n, a_0):
            A = n
            a = int(a_0)
            c = 0
            while c < 102:
                if c < 102:
                    a *= 10
                    A *= 100
                a = (a + A/a) / 2
                c += 1
            while a > 10**100:
                a /= 10
            return a

        def digital_sum(n):
            s = 0
            while n != 0:
                s += n % 10
                n /= 10
            return s

        i = 1
        while i <= lim:
            sqr = int(sqrt(i))
            if i != (sqr**2):
                res += digital_sum(approx_root_first_100_digits(i, sqr))
            i += 1

        self.last_result = res

register_problem(Problem_080())
