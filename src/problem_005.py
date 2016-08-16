#   coding=UTF_8
#
#   problem_005.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *

class Problem_005(Problem):
    
    def __init__(self):
        self.problem_nr = 5
        self.input_format = (InputType.NUMBER_INT, 2, 25)
        self.default_input = 20
        self.description_str = '''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible (no reminder) by all of the numbers from 1 to ''' + dye_input_var(20) + "?"
    
    def is_divisible(self, number, divs):
        
        for i in divs:
            if number % i != 0:
                return False
        
        return True
    
    def calculate(self, N):
        
        finished = False
        divs = []
        
        i = N

        for i in range(2, N +1):
            if N % i != 0:
                divs.append(i)
        
        while finished == False:
            if self.is_divisible(i, divs):
                finished = True
                self.last_result = i
                self.last_result_details = divs
                break
            i += N

register_problem(Problem_005())
