#   coding=UTF_8
#
#   problem_070.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from prime import next_prime
from ppe_math import totient_from_distinct_prime_factors
from ppe_permutation import is_permutation_of_number
from math import sqrt

class Problem_070(Problem):

    def __init__(self):
        self.problem_nr = 70
        self.input_format = (InputType.NUMBER_INT, 21, None)
        self.default_input = 10000000
        self.description_str = '''Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < ''' + dye_input_var("10^7") + ''', for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
'''

    def calculate(self, N):

        # if n is a prime, than φ(n) = n - 1
        # n can never be a permutation of n - 1
        # therefore n can not be a prime

        # stores the current minimum
        min_r = float("inf")
        min_n = None
        min_ds = None

        # create list of all primes used
        PS = [2]
        supp = 3.0 * sqrt(N) # 3 is somewhat random
        while True:
            np = next_prime(PS[len(PS) - 1])
            if np > supp:
                break
            PS.append(np)
        PS.sort(reverse=True)

        # check all possible combinations of subsets of two primes
        # (numbers with three prime factors have a higher ratio, but not guaranteed!)
        # try combinations with highest prime factors first
        for i in range(len(PS)):
            for j in range (len(PS)):

                # choose the primes for the current number
                ps = [PS[i], PS[j]]

                # create a number from distinct primes
                n = 1
                for p in ps:
                    n *= p

                if n > N:
                    continue

                # calculate totient and ratio
                t = totient_from_distinct_prime_factors(n, ps)
                f = float(n) / float(t)

                # check for minimum
                if f < min_r and is_permutation_of_number(t, n):
                    min_r = f
                    min_n = n
                    min_ds = ps
                    #print("HIT: " + str(n) + ", " + str(ps) + ", " + str(t) + ", " + str(f))

        print(min_r)

        self.last_result = min_n
        self.last_result_details = min_ds

        ''' for complete search (takes too much time!)
        # stores the current minimum
        min_r = float("inf")
        min_n = None

        # create list of all primes used
        PS = [2]
        supp = N / 2
        while True:
            np = next_prime(PS[len(PS) - 1])
            if np > supp:
                break
            PS.append(np)
        PS.sort(reverse=True)


        # check all possible combinations of subsets of two or more primes
        # try combinations with less prime factors and highest prime factors first
        num_of_ps = 2
        while num_of_ps <= len(PS):

            # remove primes from list which are too large
            while num_of_ps < len(PS):
                max_possible = 1.0
                for i in range(num_of_ps):
                    max_possible *= PS[i]
                if max_possible > N:
                    PS.remove(PS[0])
                    continue
                else:
                    break

            print(num_of_ps)
            print(PS)

            if num_of_ps > len(PS):
                break

            #ps_i_chosen = range(num_of_ps) # no overlap
            ps_i_chosen = []
            for i in range(num_of_ps):
                ps_i_chosen.append(0)
            #ps_i_chosen.append(len(PS)) # no overlap
            while True: # != len(PS) - num_of_ps: for no overlap

                # choose the primes for the current number
                ps = []
                for i in range(num_of_ps):
                    ps.append(PS[ps_i_chosen[i]])

                # create a number from distinct primes
                n = 1
                for p in ps:
                    n *= p

                # calculate totient and ratio
                t = totient_from_distinct_prime_factors(n, ps)
                f = float(n) / float(t)

                # check for minimum
                if n < N and f < min_r and is_permutation_of_number(t, n):
                    min_r = f
                    min_n = n
                    print("HIT: " + str(n) + ", " + str(ps) + ", " + str(t) + ", " + str(f))

                if (ps_i_chosen[0] == len(PS)-1): # remove for no overlap
                    break

                # increment indices
                for i in range(num_of_ps-1, -1, -1):
                    if ps_i_chosen[i] + 1 != len(PS): # != ps_i_chosen[i+1] for no overlap
                        pos = ps_i_chosen[i] + 1 # (no +1 for no overlap
                        for j in range(i, num_of_ps):
                            #pos += 1 # no overlap
                            ps_i_chosen[j] = pos
                        break

            num_of_ps += 1

        print(min_r)
        '''

    def details(self):
        n = self.last_result
        ps = self.last_result_details
        t = totient_from_distinct_prime_factors(n, ps)
        f = float(n) / float(t)
        desc_str = "φ(" + dye_result_var(n) + ") = " + dye_highlight(t)  + "\n" + dye_result_var(n) + " / " + str(t) + " = " + dye_highlight(f)

        return desc_str

register_problem(Problem_070())
