#   coding=UTF_8
#
#   problem_043.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from copy import copy

class Problem_043(Problem):

    def __init__(self):
        self.problem_nr = 43
        self.description_str = '''The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
'''

    def calculate(self, unused):

        sum = 0
        details = []

        Ds1 = range(10)
        for d1 in Ds1:
            Ds2 = copy(Ds1)
            Ds2.remove(d1)

            for d2 in Ds2:
                Ds3 = copy(Ds2)
                Ds3.remove(d2)

                for d3 in Ds3:
                    Ds4 = copy(Ds3)
                    Ds4.remove(d3)

                    for d4 in Ds4:
                        if (d2 * 100 + d3 * 10 + d4) % 2 != 0:
                            continue
                        Ds5 = copy(Ds4)
                        Ds5.remove(d4)

                        for d5 in Ds5:
                            if (d3 * 100 + d4 * 10 + d5) % 3 != 0:
                                continue
                            Ds6 = copy(Ds5)
                            Ds6.remove(d5)

                            for d6 in Ds6:
                                if (d4 * 100 + d5 * 10 + d6) % 5 != 0:
                                    continue
                                Ds7 = copy(Ds6)
                                Ds7.remove(d6)

                                for d7 in Ds7:
                                    if (d5 * 100 + d6 * 10 + d7) % 7 != 0:
                                        continue
                                    Ds8 = copy(Ds7)
                                    Ds8.remove(d7)

                                    for d8 in Ds8:
                                        if (d6 * 100 + d7 * 10 + d8) % 11 != 0:
                                            continue
                                        Ds9 = copy(Ds8)
                                        Ds9.remove(d8)

                                        for d9 in Ds9:
                                            if (d7 * 100 + d8 * 10 + d9) % 13 != 0:
                                                continue
                                            Ds10 = copy(Ds9)
                                            Ds10.remove(d9)

                                            d10 = Ds10[0]

                                            if (d8 * 100 + d9 * 10 + d10) % 17 == 0:
                                                n = d1*10**9 + d2*10**8 + d3*10**7 + d4*10**6 + d5*10**5 + d6*10**4 + d7*10**3 + d8*10**2 + d9*10**1 + d10*10**0
                                                sum += n
                                                details.append(n)


        self.last_result = sum
        self.last_result_details = details

    def details(self):
        return "List of all numbers:\n" + list_to_fancy_str(self.last_result_details, ", ")

register_problem(Problem_043())
