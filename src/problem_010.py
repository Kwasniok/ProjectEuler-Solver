#   coding=UTF_8
#
#   problem_010.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from ppe_math import is_prime

class Problem_010(Problem):

    def __init__(self):
        self.problem_nr = 10
        self.input_format = (InputType.NUMBER_INT, 3, 2000000)
        self.default_input = 2000000
        self.description_str = '''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below ''' +  dye_input_var("two million") + "."

    def calculate(self, N):

        res = 2

        i = 3
        while i < N:
            if is_prime(i):
                res += i
            i += 2

        self.last_result = res

register_problem(Problem_010())
