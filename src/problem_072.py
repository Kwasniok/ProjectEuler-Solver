#   coding=UTF_8
#
#   problem_072.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 16.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from prime import distinct_prime_factors
from ppe_math import totient_from_distinct_prime_factors

class Problem_072(Problem):

    def __init__(self):
        self.problem_nr = 72
        self.input_format = (InputType.NUMBER_INT, 2, 1000000)
        self.default_input = 1000000
        self.description_str = '''Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are ''' + dye_highlight(21) + ''' elements in this set.

How many elements would be contained in the set of reduced proper fractions for d ≤ ''' + dye_input_var("1,000,000") + '''
'''

    def calculate(self, d_max):

        res = 0
        d = 2
        while d <= d_max:
            d_dpfs = distinct_prime_factors(d)
            res += totient_from_distinct_prime_factors(d, d_dpfs)
            d += 1

        self.last_result = res

register_problem(Problem_072())
