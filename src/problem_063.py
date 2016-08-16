#   coding=UTF_8
#
#   problem_063.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from math import log10

class Problem_063(Problem):

    def __init__(self):
        self.problem_nr = 63
        self.description_str = '''The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
'''

    def calculate(self, unused):

        Ns = []

        # x^n for x >= 10 always produces a number with more digits than x

        for x in range (1, 10):

            n = 1
            while True:

                N = x ** n
                ds = int(log10(N) + 1)

                if n > ds:
                    break

                if ds == n:
                    #print("x=" + str(x) + ", n=" + str(n) + ", ds=" + str(ds))
                    if not N in Ns: # this line does not change anything
                        Ns.append(N)

                n += 1

        Ns.sort()

        self.last_result = len(Ns)
        self.last_result_details = Ns

    def details(self):
        return list_to_fancy_str(self.last_result_details, ", ", Colours.HIGHLIGHT)

register_problem(Problem_063())
