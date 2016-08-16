#   coding=UTF_8
#
#   problem_058.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from ppe_math import is_prime

class Problem_058(Problem):
    
    def __init__(self):
        self.problem_nr = 58
        self.input_format = (InputType.NUMBER_INT, 0, 100)
        self.default_input = 10
        self.description_str = '''Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

          37 36 35 34 33 32 31
          38 17 16 15 14 13 30
          39 18  5  4  3 12 29
          40 19  6  1  2 11 28
          41 20  7  8  9 10 27
          42 21 22 23 24 25 26
          43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
'''
    
    def calculate(self, R):
        
        R /= 100.0
        
        l = 1 # spiral length
        n = 1 # current number
        
        primes = 0.0
        total = 1.0
        
        while primes / total >= R or l == 1:
            
            for i in range(4):
                
                n += 2 * l
                
                if is_prime(n):
                    primes += 1.0
            
            total += 4
            l += 1
            
			#print("l = " + str(l)  + ", p/t = " + str(primes / total))
        
        self.last_result = 2 * l -1
        
register_problem(Problem_058())
