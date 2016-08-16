#   coding=UTF_8
#
#   problem_057.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from math import log10

class Problem_057(Problem):
    
    def __init__(self):
        self.problem_nr = 57
        self.input_format = (InputType.NUMBER_INT, 1, 500000)
        self.default_input = 1000
        self.description_str = '''It is possible to show that the square root of two can be expressed as an infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first ''' + dye_input_var("one-thousand")  + ''' expansions, how many fractions contain a numerator with more digits than denominator?
'''
    
    def calculate(self, L):
        
        res = 0
        
        N = 1 # final numerator
        D = 1 # final denominator 
        n = 1 # intermediate numerator
        d = 2 # intermediate denominator
        
        i = 0
        while i < L:
            
            N = n + d
            D = d
            
            Nds = int(log10(N))# + 1
            Dds = int(log10(D))# + 1
            
            if Nds > Dds:
                res += 1
            
            #print(str(N) + " / " + str(D) + " ==> " + str(Nds + 1) + " : " + str(Dds + 1))
            
            # next 
            n_ = d
            d_ = 2 * d + n
            
            n = n_
            d = d_
            
            i += 1
        
        self.last_result = res
        self.last_result_details = [N, D]
        
    def details(self):
        N = self.last_result_details[0]
        D = self.last_result_details[1]
        return "The algorithm reached an approximated value of √(2) ≈ " + dye_highlight(N) + " / " + dye_highlight(D)
        
register_problem(Problem_057())
