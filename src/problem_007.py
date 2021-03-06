#   coding=UTF_8
#
#   problem_007.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from prime import next_prime

class Problem_007(Problem):

    def __init__(self):
        self.problem_nr = 7
        self.input_format = (InputType.NUMBER_INT, 1, 1000000)
        self.default_input = 10001
        self.description_str ='''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the ''' +  dye_input_var("10 001") + "st prime number?"

    def calculate(self, N):

        p = 2
        nr = 1
        while nr < N:
            p = next_prime(p)
            nr += 1

        self.last_result = p

register_problem(Problem_007())
