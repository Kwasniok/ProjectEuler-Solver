#   coding=UTF_8
#
#   problem_071.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 16.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from ppe_math import simplify_fraction_dec, highest_common_factor
from fraction import Fraction

class Problem_071(Problem):

    def __init__(self):
        self.problem_nr = 71
        self.input_format = (InputType.NUMBER_INT, 3, 10000000)
        self.default_input = 1000000
        self.description_str = '''Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, ''' + dye_highlight("2/5") + ', ' + dye_highlight("3/7") + ''', 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that ''' + dye_highlight("2/5") + ' is the fraction immediately to the left of ' + dye_highlight("3/7") + '''.

By listing the set of reduced proper fractions for d ≤ ''' + dye_input_var("1,000,000") + ''' in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.
'''

    def calculate(self, d_max):

        pivot = 3.0 / 7.0

        n_best = 1
        d_best = d_max

        d = 1
        while d <= d_max:
            n = int(pivot * d)
            if n >= 1 and float(n) / float(d) < pivot and float(n) / float(d) > float(n_best) / float(d_best) and highest_common_factor(n, d) == 1:
                n_best = n
                d_best = d
            d += 1

        self.last_result = n_best
        self.last_result_details = Fraction(n_best, d_best)

    def details(self):
        f = self.last_result_details
        return "complete fraction: " + dye_result_var(f.numerator) + "/" + dye_highlight(f.denominator) + " ≈ " + str(f.evaluate()) + " < " + str(3.0/7.0) + " ≈ " + "3/7"


register_problem(Problem_071())
