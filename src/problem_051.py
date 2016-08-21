#   coding=UTF_8
#
#   problem_051.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from prime import is_prime, next_prime
from ppe_math import binomial_coefficient as nCr
from choose import choose_from_range

class Problem_051(Problem):

    def __init__(self):
        self.problem_nr = 51
        self.input_format = (InputType.NUMBER_INT, 0, 8)
        self.default_input = 8
        self.description_str = '''By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
'''

    def calculate(self, N):

        res = 0
        res_details = []

        smallest = None
        ds = 2
        while smallest == None:

            cds = 1 # number of changing digits
            while cds < ds:

                ncds = ds - cds

                nncds = 0 # raw number for non changing digits
                nncds_max = 10 ** ncds
                while nncds < nncds_max:

                    i = 1
                    nocv = nCr(ds, cds) # number of choose variations
                    while i <= nocv:

                        ps = 0
                        PS = []

                        nis = choose_from_range(i, cds, ds, reverse=True)

						#print(" >> " + str(nncds))

                        d = 0
                        while d < 10:

                            n = 0
                            nncds_str = ("0" * (ncds - len(str(nncds))))+ str(nncds)
                            l = 0
                            nncdsi = 0
                            while l < ds:
                                n *= 10
                                if l in nis:
                                    n += d
                                else:
                                    n += int(nncds_str[nncdsi])
                                    nncdsi += 1
                                l += 1
                            #print('\t' +" >-> " + niStr + " -> " + str(is_prime(int(niStr))))
                            #print(n)

                            if len(str(n)) == ds and is_prime(n):
                                ps += 1
                                PS.append(n)

                            d += 1

                        #print(nStr + " >ps> " + str(ps))

                        if ps == N:
                            if smallest == None or PS[0] < smallest:
                                smallest = PS[0]
                                res_details = PS

                        i += 1

                    nncds += 1

                cds += 1

            ds += 1

        res = smallest

        self.last_result = res
        self.last_result_details = res_details

    def details(self):
        return list_to_fancy_str(self.last_result_details, ", ")

register_problem(Problem_051())
