#   coding=UTF_8
#
#   problem_001.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *

class Problem_016(Problem):

    def __init__(self):
        self.problem_nr = 16
        self.input_format = (InputType.NUMBER_INT, 0, 750000)
        self.default_input = 1000
        self.description_str = '''2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number ''' + dye_input_var("2^1000") + "?"

    def calculate(self, N):

        res = 0
        res_str = str(2**N)
        for c in res_str:
            res += int(c)

        self.last_result = res

register_problem(Problem_016())
