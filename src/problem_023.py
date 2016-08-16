#   coding=UTF_8
#
#   problem_023.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from ppe_math import is_abundant

class Problem_023(Problem):
    
    def __init__(self):
        self.problem_nr = 23
        self.description_str = '''A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''
    
    def calculate(self, unused):
        
        def all_abundant_numbers_in_range(Range):
            abundants = []
            
            for i in Range:
                if is_abundant(i):
                    abundants.append(i)
            
            return abundants
        
        sum = 0
        
        max = 20162
        abundants = all_abundant_numbers_in_range(range(1, max))
        i = 1
        while i < max:
            j = 0
            while True:
                if abundants[j] > i/2:
                    sum += i
                    break
                
                if is_abundant(i-abundants[j]):
                    break
                j += 1
                
            if i > 48:
                i += 2
            else:
                i += 1
                
        self.last_result = sum
        
register_problem(Problem_023())
    