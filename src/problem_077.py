#   coding=UTF_8
#
#   problem_077.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 27.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from partition import num_of_prime_partitions
from prime import is_prime

class Problem_077(Problem):

    def __init__(self):
        self.problem_nr = 77
        self.input_format = (InputType.NUMBER_INT, 0, 10000000000000000000000000)
        self.default_input = 5000
        self.description_str = '''It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over ''' + dye_input_var("five thousand") + ''' different ways?'''

    def calculate(self, N):

        res = 0

        n = 0
        while True:
            nopps = num_of_prime_partitions(n)
            if nopps > N + 1 or (nopps == N + 1 and not is_prime(n)):
                res = n
                break
            n += 1

        self.last_result = res

register_problem(Problem_077())
