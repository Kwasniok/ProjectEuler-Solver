#   coding=UTF_8
#
#   problem_001.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from ppe_math import simplify_fraction_dec

class Problem_033(Problem):
    
    def __init__(self):
        self.problem_nr = 33
        self.description_str = '''The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''
    
    def calculate(self, unused):
        
        # result as fraction (N / D)
        N = 1
        D = 1
        counter = 0
        
        # digits
        Ds = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
        
        # for every possible digit to be canceled
        for dc in Ds:
            # first other digit (numerator)
            for d1 in Ds:
                # second other digit (denominator)
                for d2 in Ds:
                    # position left for canceled digit  in numerator
                    for p1 in [True, False]:
                        # position left for canceled digit in denominator
                        for p2 in [True, False]:
                            n = 1.0
                            d = 1.0
                            
                            if p1:
                                n = dc * 10.0 + d1
                            else:
                                n = dc + d1 * 10.0
                                
                            if p2:
                                d = dc * 10.0 + d2
                            else:
                                d = dc + d2 * 10.0
                            
                            # quotient
                            q = float(n) / float(d)
                            
                            # canceled quotient
                            qc = float(d1) / float(d2)
                            
                            if qc == q and q < 1.0:
                                N *= d1
                                D *= d2
                                counter += 1
                                #print("%d / %d = %d / %d = %f" % (int(n), int(d), int(d1), int(d2), qc))
                            
        
        #print(N)
        #print(D)
        
        if counter == 0:
            N = 0
        F = simplify_fraction_dec(int(N), int(D))
        self.last_result_details = [int(N), int(D), F]
        self.last_result = F[1]
        
    def details(self):
        return "The fraction " + str(self.last_result_details[0]) + "/" + str(self.last_result_details[1]) + " was simplified to " + str(self.last_result_details[2][0]) + "/" + dye_result_var(self.last_result_details[2][1]) + "."
        
        
register_problem(Problem_033())
    