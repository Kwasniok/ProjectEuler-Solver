#   coding=UTF_8
#
#   problem_060.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from prime import is_prime, next_prime
from ppe_math import binomial_coefficient as nCr
from math import log10

class Problem_060(Problem):

    def __init__(self):
        self.problem_nr = 60
        self.input_format = (InputType.NUMBER_INT, 2, 5)
        self.default_input = 5
        self.description_str = '''The numbers 3, 7, 109, and 673, are quite remarkable. By taking any two numbers and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four numbers, 792, represents the lowest sum for a set of four numbers with this property.

Find the lowest sum for a set of five numbers for which any two numbers concatenate to produce another prime.
'''

    def should_warn_long_execution_time(self):
        return True

    def calculate(self, N):

        resS = None

        # a and b must be integers
        def concats_to_prime(a, b):
            return is_prime(a * 10 ** int(log10(b) + 1) + b)

        def set_sum(S):
            sum = 0
            for e in S:
                sum += e
            return sum

        def comp_sets_by_sum(s1, s2):
            return set_sum(s1) - set_sum(s2)


        Ss = []
        p = 2
        cont = True
        while cont:

            p = next_prime(p)

            #print(p)

            new_sets = [[p]]
            for s in Ss:

                append = True
                for e in s:

                    if not concats_to_prime(p, e) or not concats_to_prime(e, p):
                        append = False
                        break

                if append:
                    extended_set = list(s)
                    extended_set.append(p)

                    if len(extended_set) == N:
                        resS = extended_set
                        cont = False
                        break

                    new_sets.append(extended_set)

            for s in new_sets:
                Ss.append(s)
                #if len(s) == 4:
                #    print(s)

            # sort all sets by sum in ascendent order
            Ss = sorted(Ss, cmp = comp_sets_by_sum) # TODO: use 'key = ConverterClassHere(comp_sets_by_sum)' for v. 3.X code

        self.last_result = set_sum(resS)
        self.last_result_details = resS

    def details(self):
        return list_to_fancy_str(self.last_result_details, ", ")

register_problem(Problem_060())
