#   coding=UTF_8
#
#   problem_076.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 26.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from partition import partition_P

class Problem_076(Problem):

    def __init__(self):
        self.problem_nr = 76
        self.input_format = (InputType.NUMBER_INT, 0, 2000)
        self.default_input = 100
        self.description_str = '''It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can ''' + dye_input_var("one hundred") + ''' be written as a sum of at least two positive integers?'''

    def calculate(self, n):

        self.last_result = partition_P(n) - 1

register_problem(Problem_076())
