#   coding=UTF_8
#
#   problem_064.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from math import sqrt, floor

class Problem_064(Problem):
    
    def __init__(self):
        self.problem_nr = 64
        self.input_format = (InputType.NUMBER_INT, 2, 10000)
        self.default_input = 10000
        self.description_str = '''All square roots are periodic when written as continued fractions and can be written in the form:

√N = a0 +        1
         --------------------
          a1 +       1
              ---------------
               a2 +    1
                   ----------
                     a3 + ...
                     
For example, let us consider √23:

√23 = 4 + √23 — 4 = 4 +    1     = 4 +      1
                       ---------      -------------
                           1           1 + √23 + 4
                       ---------           -------
                        √23 - 4               7

If we continue we would get the following expansion:

√23 = 4 +          1
         ---------------------
          1 +        1
             -----------------
              3 +      1
                 -------------
                  1 +    1
                      --------
                       8 + ...

The process can be summarised as follows:

            1         √23 + 4           √23 - 3
a0 = ''' + dye_highlight(4) + ''', --------- =  ---------   = 1 + ---------
         √23 — 4         7                 7

            7        7(√23 + 3)         √23 - 3
a1 = ''' + dye_highlight(1) + ''', --------- = ------------ = 3 + ---------
         √23 — 3         14                2
         
            2        2(√23 + 3)         √23 - 4
a2 = ''' + dye_highlight(3) + ''', --------- = ------------ = 1 + ---------
         √23 — 3         14                7
    
            7        7(√23 + 4)         √23 - 4
a3 = ''' + dye_highlight(1) + ''', --------- = ------------ = 8 + ---------
         √23 — 4         7                 1   

            1          √23 + 4         √23 - 3
a4 = ''' + dye_highlight(8) + ''', --------- = ------------ = 1 + ---------
         √23 — 4         7                 7

            7        7(√23 + 3)        √23 - 3
a5 = ''' + dye_highlight(1) + ''', --------- = ------------ = 3 + ---------
         √23 — 3         14                2
         
            2        2(√23 + 3)         √23 - 4
a6 = ''' + dye_highlight(3) + ''', --------- = ------------ = 1 + ---------
         √23 — 3         14                7
         
            7        7(√23 + 4)         √23 - 4
a7 = ''' + dye_highlight(1) + ''', --------- = ------------ = 8 + ---------
         √23 — 4         7                 1
         
                        ...
                        
It can be seen that the sequence is repeating. For conciseness, we use the notation √23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats indefinitely.

The first ten continued fraction representations of (irrational) square roots are:

√2  = [1;(2)],         period=1
√3  = [1;(1,2)],       period=2
√5  = [2;(4)],         period=1
√6  = [2;(2,4)],       period=2
√7  = [2;(1,1,1,4)],   period=4
√8  = [2;(1,4)],       period=2
√10 = [3;(6)],         period=1
√11 = [3;(3,6)],       period=2
√12 = [3;(2,6)],       period=2
√13 = [3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N ≤ 13, have an odd period.

How many continued fractions for N ≤ ''' + dye_input_var(10000) + ''' have an odd period?
'''
    
    def calculate(self, N):
        
        sum = 0
        details = []
        
        # returns list of integer value pairs representing the continues fraction
        # format (an, (nsn, dn)) where nsn is the nth numerator summand and dn is the nth denominator as part of the intermediate fraction
        # first pair represents digit before point
        def getContinuedFraction(s, ns = 0.0, d = 1.0, cfivps = None): # s := square, nf := numerator factor, ns := numerator summand, d := denominator, cfivps := continued fraction integer values pairs
            
            if cfivps == None: # is first iteration
                cfivps = []
                ipi = floor(sqrt(s)) # integer part
                nsi = -ipi
                di = 1.0
            else:
                nsi = - ns
                di =  (s - (ns ** 2)) / d
                
                ipi = floor((sqrt(s) + nsi) / di)
                
                nsi -= ipi * di
            
            cfivpi = (ipi, (nsi, di))
            
            if not cfivpi in cfivps:
                cfivps.append(cfivpi)
                return getContinuedFraction(s, nsi, di, cfivps)
            else:
                return cfivps
        
        
        n = 2
        while n <= N:
            
            if not sqrt(n) % 1.0 == 0.0:
            
                cfivps = getContinuedFraction(n)
                #print(cfivps)
                
                if len(cfivps) % 2 == 0: # 
                    sum += 1
                    
                details.append(cfivps)
            
            n += 1
        
        self.last_result = sum
        self.last_result_details = details
        
    def details(self):
        desc_str = "List of all continued fractions:"
        for cfivps in self.last_result_details:
            desc_str += "\n[" + str(int(cfivps[0][0])) + ";("
            i = 1
            while i < len(cfivps):
                desc_str += str(int(cfivps[i][0]))
                if i < len(cfivps) - 1:
                    desc_str += ','
                i += 1
            desc_str += ")], period="
            if len(cfivps) % 2 == 0:
                desc_str += dye_highlight(str(i - 1))
            else:
                desc_str += str(i - 1)
        return desc_str
        
register_problem(Problem_064())
