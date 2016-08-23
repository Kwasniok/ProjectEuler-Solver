#   coding=UTF_8
#
#   problem_073.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 19.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from ppe_math import highest_common_factor

class Problem_073(Problem):

    def __init__(self):
        self.problem_nr = 73
        self.input_format = (InputType.NUMBER_INT, 2, 12000)
        self.default_input = 12000
        self.description_str = '''Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ ''' + dye_input_var("12,000") + "?"

    def calculate(self, d_max):

        pivot_low = 1.0 / 3.0
        pivot_high = 1.0 / 2.0

        res = 0

        d = 2.0
        while d <= d_max:
            n = int(pivot_low * d) + 1.0
            while n / d < pivot_high:
                if highest_common_factor(n, d) == 1:
                    res += 1
                n += 1.0
            d += 1.0

        self.last_result = res

register_problem(Problem_073())
