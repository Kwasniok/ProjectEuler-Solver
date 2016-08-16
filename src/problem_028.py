#   coding=UTF_8
#
#   problem_028.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *

class Problem_028(Problem):

    def __init__(self):
        self.problem_nr = 28
        self.input_format = (InputType.NUMBER_INT, 1, 1000000001)
        self.default_input = 1001
        self.description_str = '''Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a ''' + dye_input_var(1001) + " by 1001 spiral formed in the same way?"

    def calculate(self, N):
        res = 1
        i = 3
        while i < N+1:
            res += 4*(i*i)-6*(i-1)
            i += 2
        self.last_result = res

register_problem(Problem_028())
