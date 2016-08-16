#   coding=UTF_8
#
#   problem_041.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from ppe_permutation import num_of_permutations, get_permutation
from ppe_math import number_from_list, is_prime

class Problem_041(Problem):
    
    def __init__(self):
        self.problem_nr = 41
        self.description_str = '''We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''
    
    def calculate(self, unused):
        
        largest = 2
        mag = 1
        
        for ds in range(9, 0, -1):
            #print(str(ds))
            Ds = range(1, ds + 1)
            nop = num_of_permutations(Ds)
            n = number_from_list(Ds)
            i = 0
            while i < nop and not is_prime(n):
                i += 1
                n = number_from_list(get_permutation(nop - i, Ds))
                #print(str(n) + " " + str(is_prime(n)))
            if is_prime(n):
                largest = n
                mag = ds
                break
        
        self.last_result = largest
        self.last_result_details = mag
        
    def details(self):
        return dye_result_var(self.last_result) + " is a " + dye_highlight(self.last_result_details) + "-digit pandigital prime."
        
register_problem(Problem_041())
