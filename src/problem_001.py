#   coding=UTF_8
#
#   problem_001.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *

class Problem_001(Problem):

    def __init__(self):
        self.problem_nr = 1
        self.input_format = (InputType.NUMBER_INT, 0, 100000000)
        self.default_input = 1000
        self.description_str = '''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below ''' + dye_input_var(self.default_input) + '.'

    def calculate(self, N):

        i = 0
        res = 0
        while i < N:

            if i%3 == 0:
                res += i
            elif i%5 == 0:
                res += i

            i += 1

        self.last_result = res

register_problem(Problem_001())
