#   coding=UTF_8
#
#   problem_065.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from ppe_math import simplify_fraction_dec as simplify_fraction

class Problem_065(Problem):
    
    def __init__(self):
        self.problem_nr = 65
        self.input_format = (InputType.NUMBER_INT, 1, 50000)
        self.default_input = 100
        self.description_str = '''The square root of 2 can be written as an infinite continued fraction.

√2 = 1 +         1
        --------------------
         2 +       1
            ----------------
             2 +     1
                ------------
                 2 +   1
                    --------
                     2 + ...
                     
The infinite continued fraction can be written, √2 = [1;(2)], (2) indicates that 2 repeats ad infinitum. In a similar way, √23 = [4;(1,3,1,8)].

It turns out that the sequence of partial values of continued fractions for square roots provide the best rational approximations. Let us consider the convergents for √2.

    1
1 + - = 3 / 2
    2
    
        1
1 + ------- = 7 / 5
     1 + 1
         -
         2
    
        1
1 + ------------ = 17 / 12
    1 +   1
        -------
         1 + 1
             -
             2
    
             1
1 + ------------------ = 41 / 29
    1 +       1
        -------------
         1 +    1
             -------
              1 + 1
                  -
                  2

Hence the sequence of the first ten convergents for √2 are:

1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...

What is most surprising is that the important mathematical constant,
e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

The first ten terms in the sequence of convergents for e are:

2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the ''' + dye_input_var(100) + '''th convergent of the continued fraction for e.
'''
    
    def calculate(self, L):
        
        sum = 0
        
        if L > 1:
            F = [1, 0]
            
            i = L
            while i > 1:
                
                if i % 3 == 0:
                    ni = 2 * (i + 1) / 3
                else:
                    ni = 1
                    
                F = [ni * F[0] + F[1], F[0]]
                #print(F)
                
                i -= 1
            
            # add 2
            F = [2 * F[0] + F[1], F[0]]
        
        else:
            F = [2, 1]
            
        Ncpy = F[0]
        while Ncpy != 0:
            sum += Ncpy % 10
            Ncpy /= 10
        
        self.last_result = sum
        self.last_result_details = F
        
    def details(self):
        F = self.last_result_details
        desc_str = "e ≈ " +  dye_highlight(F[0]) + " / " + str(F[1])
        try:
            desc_str += " ≈ " + str(float(F[0]) / float(F[1]))
        except (OverflowError):
            pass
        return desc_str
            
        
register_problem(Problem_065())
