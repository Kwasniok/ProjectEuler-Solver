#   coding=UTF_8
#
#   problem_020.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from math import factorial

class Problem_020(Problem):

    def __init__(self):
        self.problem_nr = 20
        self.input_format = (InputType.NUMBER_INT, 0, 100000)
        self.default_input = 100
        self.description_str = '''n! means n  (n  1)  ...  3  2  1

For example, 10! = 10  9  ...  3  2  1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number ''' + dye_input_var(100) + "!\n"

    def calculate(self, N):

        res_str = str(factorial(N))

        res = 0
        for c in res_str:
            res += int(c)

        self.last_result = res

register_problem(Problem_020())
