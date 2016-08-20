#   coding=UTF_8
#
#   problem_049.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from prime import is_prime
from ppe_permutation import Symmetric_Group

class Problem_049(Problem):

    def __init__(self):
        self.problem_nr = 49
        self.description_str = '''The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

    def calculate(self, unused):

        res = ""
        all = []

        ds = 4
        addValue = 3330

        n = 10 ** (ds - 1)
        max = 10 ** ds
        while n < max:

            ni = n
            nStr = str(n)
            nps = Symmetric_Group.get_all_of_list(nStr)
            i = 0
            while i < 3:

                if not is_prime(ni):
                    break

                niStr = str(ni)

                if len(niStr) != ds:
                    break

                if not (niStr in nps):
                    break

                i += 1
                ni += addValue

            if i == 3:
                all.append([n, n + addValue, n + 2 * addValue])

            n += 1

        # print (all)

        for t in all:
            if t[0] != 1487:
                for ni in t:
                    res += str(ni)

        self.last_result = res
        self.last_result_details = all

    def details(self):
        desc_str = ""
        all = self.last_result_details

        i = 0
        while i < len(all):
            if all[i][0] != 1487:
                desc_str += list_to_fancy_str(all[i], " <=> ", Colours.RESULTVAR)
            else:
                desc_str += list_to_fancy_str(all[i], " <=> ")
            if i < len(all) - 1:
                desc_str += '\n'
            i += 1

        return desc_str

register_problem(Problem_049())
