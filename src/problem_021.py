#   coding=UTF_8
#
#   problem_021.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from ppe_math import sum_of_all_proper_divisors_of

class Problem_021(Problem):
    
    def __init__(self):
        self.problem_nr = 21
        self.input_format = (InputType.NUMBER_INT, 2, 100000)
        self.default_input = 10000
        self.description_str = '''Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under ''' + dye_input_var(self.default_input) + ".\n"
    
    def calculate(self, N):
        
        ami = 0
        self_ami = 0
        
        i = 2
        while i < N:
            spdi = sum_of_all_proper_divisors_of(i)
            if sum_of_all_proper_divisors_of(spdi) == i:
                ami += i
            if spdi == i:
                self_ami += i
            
            i += 1
                    
        self.last_result = ami - self_ami
        self.last_result_details = self_ami
        
    
    def details(self):
        return "The sum of all self-amicabled numbers under " + dye_input_var(self.last_input) + " is: " + dye_highlight(self.last_result_details) + "."

register_problem(Problem_021())
