#   coding=UTF_8
#
#   problem_050.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from ppe_math import is_prime, next_prime

class Problem_050(Problem):
    
    def __init__(self):
        self.problem_nr = 50
        self.input_format = (InputType.NUMBER_INT, 3, 1000000)
        self.default_input = 1000000
        self.description_str = '''The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below ''' + dye_input_var("one-million") + ", can be written as the sum of the most consecutive primes?\n"
    
    def calculate(self, N):
        
        max_sum = 2
        max_sum_len = 1
        max_sum_start = 2
        
        ns = 2
        while ns < N:
            
            n = ns
            sum = n
            sum_len = 1
            
            while sum < N:
                
                if is_prime(sum) and sum_len > max_sum_len:
                    max_sum = sum
                    max_sum_len = sum_len
                    max_sum_start = ns
                    #print(" >> " + str(sum) + " : " + str(sum_len))
                    
                n = next_prime(n)
                sum += n
                sum_len += 1
                
            ns = next_prime(ns)
        
        self.last_result = max_sum
        self.last_result_details = [max_sum_start, max_sum_len]
        
    def details(self):
        ps = [self.last_result_details[0]]
        for i in range(self.last_result_details[1] - 1):
            ps.append(next_prime(ps[len(ps) - 1]))
        
        return list_to_fancy_str(ps, " + ") + " = " + dye_result_var(self.last_result)
        
register_problem(Problem_050())
