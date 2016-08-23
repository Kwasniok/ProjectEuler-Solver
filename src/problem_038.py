#   coding=UTF_8
#
#   problem_038.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from math import log10
from ppe_math import is_pandigital

class Problem_038(Problem):

    def __init__(self):
        self.problem_nr = 38
        self.description_str = '''Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''


    def calculate(self, unused):

        largest = 0

        l = 0
        # length of concatenated product must be 9 (to be pandigital)
        # at least 1 and 2 must be used as factors
        # every number starts with 9
        # l is appended to 9, leading to a minimal c.p. length of 1 + len(l) * 2
        # thus all l greater than 10^4 can be left out
        while l < 10E+4:

            if l % 1000 == 0:
                #self.setCounter(l, 10E+4)
                pass

            if l == 0:
                i = 9
            else:
                i = 9 * 10 ** int(log10(l) + 1.0) + l

            #print(i)

            cp = 0 # concatenated product
            f = 1 # factor
            cpl = 0 # cp length
            while cpl < 9:

                # calculate next product
                p = i * f
                pl = int (log10(p) + 1.0) # product length

                # shift and append
                cp *= 10 ** pl
                cp += p
                cpl += pl

                f += 1

            if cpl == 9 and is_pandigital(cp) and cp > largest:
                largest = cp
                self.last_result_details = [i, f - 1]

            l += 1

        self.last_result = largest

    def details(self):
        return dye_result_var(self.last_result) + " is obtained by multiplying " + dye_highlight(self.last_result_details[0]) + " with all factors from 1 to " + dye_highlight(self.last_result_details[1]) + " and appending the digits."

register_problem(Problem_038())
