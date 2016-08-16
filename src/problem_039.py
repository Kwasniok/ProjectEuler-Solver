#   coding=UTF_8
#
#   problem_039.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from math import sqrt

class Problem_039(Problem):
    
    def __init__(self):
        self.problem_nr = 39
        self.input_format = (InputType.NUMBER_INT, 2, 10000)
        self.default_input = 1000
        self.description_str = '''If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ ''' + dye_input_var(1000) + ", is the number of solutions maximised?\n"
    
    def calculate(self, N):
        
        ps = []
        p = 0
        while p < N + 1:
            ps.append(0)
            p += 1
        
        # p = a + b + c = a + b + √(a^2 + b^2)
        # c(a, b) = √(a^2 + b^2)
        # --> p(a, b)
        
        # for each a = 1, 2, 3, ...
        a = 1.0
        while a < N:
            
            #for each b >= a
            b = a
            while a + b < N:
                c = sqrt(a**2 + b**2)
                
                # is c an integer?
                if c % 1.0 == 0.0:
                    p = a + b + c
                    
                    # is perimeter limit not exceeded?
                    if p <= N:
                        ps[int(p)] += 1
                
                b += 1.0
                
            a += 1.0
            
        #print(ps)
        
        max_i = 0
        max = ps[max_i]
        for i in range(0, N + 1):
            if ps[i] > max:
                max_i = i
                max = ps[i]
                
        self.last_result = max_i
        
register_problem(Problem_039())
