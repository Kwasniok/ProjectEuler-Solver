#   coding=UTF_8
#
#   problem_037.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from math import log10
from prime import is_prime

class Problem_037(Problem):
    
    def __init__(self):
        self.problem_nr = 37
        self.input_format = (InputType.NUMBER_INT, 1, 11)
        self.default_input = 11
        self.description_str = '''The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only ''' + dye_input_var("eleven") + ''' primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''
    
    def calculate(self, N):
        
        tps = 0 # amount of found truncated primes
        sum = 0
        
        i = 10
        while True:
            
            if is_prime(i):
                
                add = True
                
                # n backwards
                nb = i
                while nb != 0:
                    if not is_prime(nb):
                        add = False
                        break
                    nb /= 10
                    
                # n forwards
                if add: # (for speed)
                    nf = i
                    nf = nf % (10 ** int(log10(nf))) # (for speed)
                    while nf != 0:
                        if not is_prime(nf):
                            add = False
                            break
                        nf = nf % (10 ** int(log10(nf)))
                
                if add:
                    #print("HIT : %d" % i)
                    tps += 1
                    sum += i
                    if tps == N:
                        run = False
                        break
                
            i += 1
            
        self.last_result = sum
        
register_problem(Problem_037())
    