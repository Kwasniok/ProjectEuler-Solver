#   coding=UTF_8
#
#   problem_001.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from ppe_math import is_triangle_number, is_square_number, is_pentagonal_number, is_hexagonal_number, is_heptagonal_number, is_octagonal_number
from ppe_math import triangle_number, square_number, pentagonal_number, hexagonal_number, heptagonal_number, octagonal_number

class Problem_061(Problem):
    
    def __init__(self):
        self.problem_nr = 61
        self.input_format = (InputType.NUMBER_INT, 4, 8)
        self.default_input = 8
        self.description_str = '''Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate (polygonal) numbers and are generated by the following formulae:

        Triangle       P3,n=n(n+1)/2     1, 3,  6, 10, 15, ...
        Square         P4,n=n2           1, 4,  9, 16, 25, ...
        Pentagonal     P5,n=n(3n−1)/2    1, 5, 12, 22, 35, ...
        Hexagonal      P6,n=n(2n−1)      1, 6, 15, 28, 45, ...
        Heptagonal     P7,n=n(5n−3)/2    1, 7, 18, 34, 55, ...
        Octagonal      P8,n=n(3n−2)      1, 8, 21, 40, 65, ...

The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties.

The set is cyclic, in that the last two digits of each number is the first two digits of the next number (including the last number with the first).
Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and pentagonal (P5,44=2882), is represented by a different number in the set.
This is the only set of 4-digit numbers with this property.
Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.
'''
    
    def calculate(self, N):
        
        sum = 0
        
        ds = 4 # must be divisible by 2
        
        # All functions have only two point in common Q1(0|0) and Q2(1|1).
        # Thus each number n despite 1 creates different values for each polygonal number.
        # BUT different n for different polygonal numbers CAN create the same number!
        
        # all possible combinations of 6 4-digit numbers with the following pattern are created:
        # A1 A2 B1 B2,  B1 B2 C1 C2, C1 C2 D1 D2, ..., F1 F2 A1 A2
        # A1 to F1 must not be 0
        
        def isPologonalNumber(n, p):
            if p == 3:
                return is_triangle_number(n)
            if p == 4:
                return is_square_number(n)
            if p == 5:
                return is_pentagonal_number(n)
            if p == 6:
                return is_hexagonal_number(n)
            if p == 7:
                return is_heptagonal_number(n)
            if p == 8:
                return is_octagonal_number(n)
        
        def test(ld1, ld2, fd1, fd2, rpts): # n := remaining steps, upts := remaining polygonal types
            n = ld1 * 1000 + ld2 * 100
            
            if len(rpts) == 1: # last step ? --> use very first digits as last digits
                n += fd1 * 10 + fd2
                
                if isPologonalNumber(n, rpts[0]): # --> last number matches!
                    return [(n, rpts[0])]
                else:
                    return None
                
            else: # --> use new combination of digits as last digits
                for d1 in range (1, 10): # d1 must not be 0
                    for d2 in range(0, 10): # d2 can be 0
                        ni = n + d1 * 10 + d2
                        
                        for pt in rpts:
                            
                            if isPologonalNumber(ni, pt):
                                rptsi = list(rpts)
                                rptsi.remove(pt)
                                
                                npps = test(d1, d2, fd1, fd2, rptsi)
                                
                                if npps != None:
                                    npps[0:0] = [(ni, pt)]
                                    return npps
                        
            return None
        
        def test_start(N):
            
            for fd1 in range (1, 10): # d1 must not be 0
                for fd2 in range(0, 10): # d2 can be 0
                    for ld1 in range (1, 10): # d1 must not be 0
                        for ld2 in range(0, 10): # d2 can be 0
                            
                            ni = fd1 * 1000 + fd2 * 100 + ld1 *10 + ld2
                            
                            rpts = range(3, N + 1)
                            
                            for pt in rpts:
                                        
                                if isPologonalNumber(ni, pt):
                                    rptsi = list(rpts)
                                    rptsi.remove(pt)
                                    
                                    npps = test(ld1, ld2, fd1, fd2, rptsi)
                                    
                                    if npps != None:
                                        npps[0:0] = [(ni, pt)]
                                        return npps
                
            
            return None
        
        
        npps = test_start(N) # number polygon type pairs
        
        for p in npps:
            sum += p[0]
        
        self.last_result = sum
        self.last_result_details = npps
        
    def details(self):
        npps = self.last_result_details
        desc_str = "number | polygonal type"
        for npp  in npps:
            desc_str += "\n " + dye_highlight(npp[0]) + "    " + str(npp[1])
        desc_str += "\nThe algorithm can find " + dye_warning("at most one solution") + "."
        return desc_str
        
register_problem(Problem_061())