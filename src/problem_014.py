#   coding=UTF_8
#
#   problem_001.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from sequences import collatz_depth, collatz_chain

class Problem_014(Problem):

    def __init__(self):
        self.problem_nr = 14
        self.input_format = (InputType.NUMBER_INT, 1, 10000000)
        self.default_input = 1000000
        self.description_str = '''The following iterative sequence is defined for the set of positive integers:

    n --> n/2 (n is even)
    n --> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

    13 --> 40 --> 20 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under ''' + dye_input_var("one million") + ''', produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

    def calculate(self, N):

        res = 0
        max = 0

        i = 1
        while i < N:
            d = collatz_depth(i)
            if d > max:
                res = i
                max = d

            i += 1

        self.last_result = res

    def details(self):
        desc_str = ""

        i = 0
        chain = collatz_chain(self.last_result)
        while i < len(chain):
            desc_str += str(chain[i])
            if i < len(chain) - 1:
                desc_str += ' --> '
            i += 1

        return desc_str

register_problem(Problem_014())
