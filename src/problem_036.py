#   coding=UTF_8
#
#   problem_036.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from ppe_math import inBase, is_palindrome

class Problem_036(Problem):
    
    def __init__(self):
        self.problem_nr = 36
        self.input_format = (InputType.NUMBER_INT, 1, 10000000)
        self.default_input = 1000000
        self.description_str = '''The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
        
Find the sum of all numbers, less than ''' + dye_input_var("one million") + ''', which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''
    
    def calculate(self, N):
        
        sum = 0
        
        for i in range(1, N):
            
            # get representations as strings
            d = inBase(i, 10)
            b = inBase(i,  2)
            
            if is_palindrome(d) and is_palindrome(b):
                sum += i
                #print("%s <--> %s" % (d, b))
        
        self.last_result = sum
        
register_problem(Problem_036())
