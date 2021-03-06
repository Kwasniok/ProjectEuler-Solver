#   coding=UTF_8
#
#   problem_044.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from sequences import pentagonal_number, is_pentagonal_number
from math import sqrt

class Problem_044(Problem):

    def __init__(self):
        self.problem_nr = 44
        self.description_str = '''Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?
'''

    def calculate(self, unused):

        # P(n) = 1/2n(3n - 1) = 3/2n^2 - 1/2n

        # ∆P(n1, n2) = P(n2) - P(n1)
        # ∆P(n, n+1) = ... = 3n + 1
        # --> gap size between two consecutive pantagonal numbers increases linearly

        # D = ∆P(n1, n2) for n2 > n1

        # ∑P(n1, n2) = P(n1) + P(n2)
        # ∑P(n, n+1) = ... = 3n^2 + 2n + 1

        # smallest n for ∆P(n, n+1), ∑P(n, n+1) ∈ P is greater than 10^8
        # P(10^8) ≈ 10^16

        ''' to find smallest n for ∆P(n, n+1), ∑P(n, n+1) ∈ P
        j = 1
        while not (is_pentagonal_number(3 * j + 1) and is_pentagonal_number(3 * (j**2) + 2 * j + 1)):
            if j % 100000 == 0:
                print(j)
            j += 1

        k = j + 1
        '''

        j = 1
        k = 2
        while True:

            pj = pentagonal_number(j)
            pk = pentagonal_number(k)

            if is_pentagonal_number(pk - pj) and is_pentagonal_number(pj + pk):
                break

            if j == 1:
                k += 1
                j = k - 1
            else:
                j -= 1

        self.last_result = pk - pj
        self.last_result_details = [j, k]

    def details(self):
        j = self.last_result_details[0]
        k = self.last_result_details[1]
        pj = pentagonal_number(j)
        pk = pentagonal_number(k)

        return "j = " + dye_highlight(j) + ", k = " + dye_highlight(k) + "\nPj = " + dye_highlight(pj) + ", Pk = " + dye_highlight(pk)

register_problem(Problem_044())
