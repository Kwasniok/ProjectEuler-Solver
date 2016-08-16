#   coding=UTF_8
#
#   problem_046.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from math import sqrt
from prime import is_prime, next_prime

class Problem_046(Problem):

    def __init__(self):
        self.problem_nr = 46
        self.description_str = '''It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

 9 =  7 + 2×1^2
15 =  7 + 2×2^2
21 =  3 + 2×3^2
25 =  7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''

    def calculate(self, unused):

        o = 9
        while True:

            p = 2
            isCG = False
            while p < o:
                r = sqrt((o - p) / 2.0)
                if r % 1.0 == 0.0:
                    isCG = True
                    break
                p = next_prime(p)

            if not isCG:
                    break

            o += 2
            while is_prime(o):
                o += 2

        self.last_result = o


register_problem(Problem_046())
