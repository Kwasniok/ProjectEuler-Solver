#   coding=UTF_8
#
#   problem_034.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from ppe_math import faculty, get_digits_as_list

class Problem_034(Problem):

    def __init__(self):
        self.problem_nr = 34
        self.description_str = '''145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

    def calculate(self, N):

        res = 0

        N = 100000
        i = 9
        while i < N:
            i += 1

            Ds = get_digits_as_list(i)

            sum = 0
            for d in Ds:
                sum += faculty(d)

            if sum == i:
                res += i
                #print(sum)

        self.last_result = res

register_problem(Problem_034())
