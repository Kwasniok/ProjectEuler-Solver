#   coding=UTF_8
#
#   problem_069.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from prime import next_prime
from sys import float_info

class Problem_069(Problem):
    
    def __init__(self):
        self.problem_nr = 69
        self.input_format = (InputType.NUMBER_INT, 2, None)
        self.default_input = 1000000
        self.description_str = '''Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

n    Relatively Prime  φ(n)  n/φ(n)
2    1                   1    2
3    1,2                 2    1.5
4    1,3                 2    2
5    1,2,3,4             4    1.25
6    1,5                 2    3
7    1,2,3,4,5,6         6    1.1666...
8    1,3,5,7             4    2
9    1,2,4,5,7,8         6    1.5
10   1,3,7,9             4    2.5

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ ''' + dye_input_var("1,000,000") + ''' for which n/φ(n) is a maximum.
'''
    
    def calculate(self, N):
        
        # numbers created by multiplying all primes starting with 2 have more proper/distinct dividers than every lower number
        
        pfs = []
        p = 2
        n = 1
        while n * p <= N:
            n *= p
            pfs.append(p)
            p = next_prime(p)
        
        self.last_result = n
        self.last_result_details = pfs
        
    def details(self):
        
        n = self.last_result
        pfs = self.last_result_details
        
        # φ(n) = n  (1 - 1/p1) (1 - 1/p2) ... (1 - 1/pk) , where p1, p2, ..., pk are distinct prime factors of n
        f = 1.0 # = n / φ(n) ; work around to avoid float convertion for very large numbers
        mult = 1
        div  = 1
        for pf in pfs:
            mult *= pf -1
            div  *= pf
            f /= (1.0 - 1.0 / pf)
        tc = n / div * mult # = φ(n) ; same here
        return "n = " + dye_result_var(n) + ", φ(n) = " + str(tc) + ", n/φ(n) = " + dye_highlight(f)
        
register_problem(Problem_069())
