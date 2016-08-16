#   coding=UTF_8
#
#   problem_030.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *


class Problem_030(Problem):
    
    def __init__(self):
        self.problem_nr = 30
        self.input_format = (InputType.NUMBER_INT, 2, 7)
        self.default_input = 5
        self.description_str = '''Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of ''' + dye_input_var("fifth") + " powers of their digits.\n"
    
    def calculate(self, pow):
        sum = 0
        i = 2
        while i < 10**pow*10:
            n = i
            k = 0
            while n > 0:
                l = (n % 10)
                k += l ** pow
                n -= l
                n /= 10
            if i == k:
                sum += i
            i += 1
            
        self.last_result = sum
        
register_problem(Problem_030())
