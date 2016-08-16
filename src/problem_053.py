#   coding=UTF_8
#
#   problem_053.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from ppe_math import binomial_coefficient as nCr

class Problem_053(Problem):
    
    def __init__(self):
        self.problem_nr = 53
        self.input_format = (InputType.TUPLE_HETEROGENE, 2, (InputType.NUMBER_INT, 1, 500), (InputType.NUMBER_INT, 1, None))
        self.default_input = (100, 1000000)
        self.description_str = '''There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, nCr(5, 3) = 10.

In general, 
nCr = n! / r!(n−r)!, 
where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ ''' + dye_input_var(100) + ''', are greater than ''' + dye_input_var("one-million") + "?\n"
    
    def calculate(self, Ns):
        
        N1 = Ns[0]
        N2 = Ns[1]
        
        count = 0
        
        n = 1
        while n <= N1:
            
            r = 0
            while r <= n:
                
                if nCr(n, r) > N2:
                    count += 1
                    
                r += 1
            
            n += 1
        
        self.last_result = count
        
register_problem(Problem_053())
