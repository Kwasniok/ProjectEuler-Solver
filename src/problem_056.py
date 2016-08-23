#   coding=UTF_8
#
#   problem_056.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *

class Problem_056(Problem):

    def __init__(self):
        self.problem_nr = 56
        self.input_format = (InputType.NUMBER_INT, 1, 100)
        self.default_input = 100
        self.description_str = '''A googol (10^100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < ''' + dye_input_var(100) + ", what is the maximum digital sum?\n"

    def calculate(self, N):

        max_dsum = -1 # lowest result possible (a = b = 0)
        max_Details = None

        a = 0
        while a < N:

            b = 0
            while b < N:

                n = a ** b
                nStr = str(n)

                dsum = 0
                for d in nStr:
                    dsum += int(d)

                if dsum > max_dsum:
                    max_dsum = dsum
                    max_Details = [a, b]

                b += 1

            a += 1

        self.last_result = max_dsum
        self.last_result_details = max_Details

    def details(self):
        a = self.last_result_details[0]
        b = self.last_result_details[1]

        return "a = " + str(a) + ", b = " + str(b) + ", a^b = " + str(a**b)

register_problem(Problem_056())
