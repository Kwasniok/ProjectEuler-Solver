#   coding=UTF_8
#
#   problem_012.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from ppe_math import number_of_divisors, list_of_divisors

class Problem_012(Problem):

    def __init__(self):
        self.problem_nr = 12
        self.input_format = (InputType.NUMBER_INT, 1, None)
        self.default_input = 500
        self.description_str = '''The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over ''' + dye_input_var('five hundred') + " divisors?"

    def calculate(self, N):

        finnished = False
        i = 0
        j = 0
        res = 1

        while not finnished:
            if number_of_divisors(j) > N:
                res = j
                finnished = True
            i += 1
            j += i

        self.last_result = res

    def details(self):
        desc_str = ""

        desc_str += dye_input_var(self.last_result) + ' : '

        divs = list_of_divisors(self.last_result)

        i = 0
        while i < len(divs):
            desc_str += str(divs[i])

            if i < len(divs) - 1:
                desc_str += ', '

            i += 1

        return desc_str

register_problem(Problem_012())
